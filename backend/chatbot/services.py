import requests
from django.conf import settings

TOGETHER_API_KEY = getattr(settings, "TOGETHER_API_KEY", None)
TOGETHER_API_URL = "https://api.together.xyz/v1/chat/completions"

def send_message_to_together_ai(messages, model="meta-llama/Llama-3-8b-chat-hf"):
    """
    Sends a list of messages to the Together AI API and returns the response.
    :param messages: List of dicts, e.g. [{"role": "user", "content": "Hello"}]
    :param model: Model name to use.
    :return: Response JSON from Together AI.
    """
    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "messages": messages
    }
    response = requests.post(TOGETHER_API_URL, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()