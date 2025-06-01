<template>
  <div class="chat-container">
    <!-- Header -->
    <div class="flex items-center justify-between mb-6">
      <div class="flex items-center">
        <img src="@/assets/up-logo.svg" alt="UP Logo" class="w-10 h-10 mr-2" />
        <h1 class="text-white text-xl">UP Cebu FAQ</h1>
      </div>
      <router-link to="/" class="text-white hover:text-gray-300">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
        </svg>
      </router-link>
    </div>

    <!-- Chat Messages -->
    <div class="flex-1 overflow-y-auto mb-4" ref="chatContainer">
      <div v-for="(message, index) in messages" :key="index" 
           :class="['chat-message', message.isUser ? 'user-message' : 'bot-message']">
        {{ message.text }}
      </div>
    </div>

    <!-- Input Area -->
    <div class="bg-white rounded-lg p-2 flex items-center">
      <input 
        v-model="userInput"
        type="text"
        placeholder="Type your message..."
        class="flex-1 border-none focus:ring-0 focus:outline-none"
        @keyup.enter="sendMessage"
      />
      <button 
        @click="sendMessage"
        class="ml-2 p-2 rounded-full bg-up-red text-white hover:bg-red-900"
      >
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
          <path d="M10.894 2.553a1 1 0 00-1.788 0l-7 14a1 1 0 001.169 1.409l5-1.429A1 1 0 009 15.571V11a1 1 0 112 0v4.571a1 1 0 00.725.962l5 1.428a1 1 0 001.17-1.408l-7-14z" />
        </svg>
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'

const messages = ref([
  { text: 'Hello! How can I help you today?', isUser: false },
])
const userInput = ref('')
const chatContainer = ref<HTMLElement | null>(null)

const sendMessage = () => {
  if (!userInput.value.trim()) return

  // Add user message
  messages.value.push({
    text: userInput.value,
    isUser: true
  })

  // Simulate bot response (you'll need to implement actual chatbot logic)
  setTimeout(() => {
    messages.value.push({
      text: 'This is a sample response. You\'ll need to implement actual chatbot logic here.',
      isUser: false
    })
  }, 1000)

  userInput.value = ''
}

// Scroll to bottom when new messages arrive
const scrollToBottom = () => {
  if (chatContainer.value) {
    chatContainer.value.scrollTop = chatContainer.value.scrollHeight
  }
}

onMounted(() => {
  scrollToBottom()
})
</script> 