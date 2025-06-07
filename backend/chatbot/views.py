import json
import logging
from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from .services import send_message_to_together_ai
from .utils.handbookloader import load_and_chunk_handbook, find_relevant_chunks

logger = logging.getLogger(__name__)

HANDBOOK_CHUNKS = load_and_chunk_handbook()

@csrf_exempt
def chatbot_api(request: HttpRequest) -> JsonResponse:
    if request.method != "POST":
        return JsonResponse({"error": "Only POST requests are allowed."}, status=405)

    try:
        data = json.loads(request.body)
        user_input = data.get("user_input", "").strip()

        if not user_input:
            return JsonResponse({"error": "Missing or empty 'user_input' field."}, status=400)

        relevant_chunks = find_relevant_chunks(user_input, HANDBOOK_CHUNKS, top_k=3)
        context_text = "\n\n".join(relevant_chunks)

        messages = [
            {
                "role": "system",
                "content": "You are a helpful assistant answering questions about the university's student handbook and services."
            },
            {
                "role": "user",
                "content": f"Context:\n{context_text}\n\nQuestion:\n{user_input}"
            }
        ]

        ai_response = send_message_to_together_ai(messages)
        answer = ai_response.get("choices", [{}])[0].get("message", {}).get("content", "")

        return JsonResponse({"response": answer})

    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON in request body."}, status=400)

    except Exception as e:
        logger.exception("Unexpected error in chatbot_api")
        return JsonResponse({"error": str(e)}, status=500)
