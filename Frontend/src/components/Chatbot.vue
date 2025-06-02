<template>
  <div class="main-layout">
    <!-- Sidebar -->
    <aside class="sidebar">
      <div class="sidebar-header">
        <img src="/uplogo.png" alt="UP Cebu Logo" class="sidebar-logo" />
        <span class="sidebar-title">UP Cebu Chatbot</span>
      </div>
      <nav class="sidebar-nav">
        <button class="sidebar-btn active">New Chat</button>
        <button class="sidebar-btn">Search Chat</button>
      </nav>
    </aside>

    <div class="chat-area">
      <header class="chat-header">
        <img src="/uplogo.png" alt="UP Cebu Logo" class="header-logo" />
        <span class="header-title">UP Cebu FAQ</span>
      </header>

      <div class="chat-body">
        <div class="message-row bot-row">
          <img src="/uplogo.png" class="avatar bot-avatar" />
          <div class="bubble bot-bubble">
            Hi, how may I help you?
          </div>
        </div>

        <div v-if="!userMessage" class="quick-options">
          <button @click="sendMessage('When do classes start?')">When do classes start?</button>
          <button @click="sendMessage('How do I enroll?')">How do I enroll?</button>
          <button @click="sendMessage('What is the dress code?')">What is the dress code?</button>
        </div>

        <div v-if="userMessage" class="message-row user-row">
          <div class="bubble user-bubble">{{ userMessage }}</div>
          <div class="avatar user-avatar">
            <span class="user-icon">👤</span>
          </div>
        </div>

        <div v-if="botReply" class="message-row bot-row">
          <img src="/uplogo.png" class="avatar bot-avatar" />
          <div class="bubble bot-bubble">{{ botReply }}</div>
        </div>
      </div>

      <div class="chat-input">
        <input v-model="input" @keyup.enter="sendMessage(input)" placeholder="Ask anything" />
        <button @click="sendMessage(input)">
          <svg width="24" height="24" fill="none" viewBox="0 0 24 24">
            <path d="M2 21L23 12L2 3V10L17 12L2 14V21Z" fill="#006400"/>
          </svg>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      input: '',
      userMessage: '',
      botReply: ''
    }
  },
  methods: {
    sendMessage(msg) {
      if (!msg.trim()) return;
      this.userMessage = msg
      this.input = ''
      // Simulated response
      if (msg.toLowerCase().includes("enroll")) {
        this.botReply = `According to the Academic Calendar for A.Y. 2025 - 2026, enrollment starts June 17 - June 21, 2025.

For enrolling students, you may refer to the following dates:

June 17, 2025 - Students from 2022
June 18, 2025 - Students from 2023
June 19, 2025 - Students from 2024
June 20, 2025 - Incoming first year students
June 21, 2025 - All year levels

Bring all necessary documents such as your School ID, Form 137, etc.`
      } else if (msg.toLowerCase().includes("classes start")) {
        this.botReply = "Classes for A.Y. 2025-2026 start on August 5, 2025."
      } else if (msg.toLowerCase().includes("dress code")) {
        this.botReply = "UP Cebu does not have a strict dress code, but students are expected to dress appropriately and respectfully on campus."
      } else {
        this.botReply = "I'm sorry, I can only help with enrollment, class schedules, and dress code for now."
      }
    }
  }
}
</script>

<style scoped>
/* Base Layout */
.main-layout {
  display: flex;
  height: 100vh;
  background: #1e1e1e;
  font-family: 'Inter', sans-serif;
  color: #e0e0e0;
}

/* Sidebar */
.sidebar {
  width: 260px;
  background: #2d2d2d;
  display: flex;
  flex-direction: column;
  padding: 20px;
  border-right: 1px solid #3a3a3a;
}

.sidebar-header {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 24px;
}

.sidebar-logo {
  width: 40px;
  height: 40px;
  border-radius: 8px;
}

.sidebar-title {
  font-size: 1rem;
  font-weight: 600;
  color: #fff;
}

.sidebar-nav {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.sidebar-btn {
  background: #3a3a3a;
  color: #fff;
  border: none;
  padding: 12px;
  border-radius: 10px;
  font-size: 0.95rem;
  cursor: pointer;
  text-align: left;
  transition: background 0.2s;
}

.sidebar-btn:hover,
.sidebar-btn.active {
  background: #4f4f4f;
}

/* Chat Area */
.chat-area {
  flex: 1;
  display: flex;
  flex-direction: column;
}

/* Header */
.chat-header {
  display: flex;
  align-items: center;
  padding: 16px 24px;
  background: #202020;
  border-bottom: 1px solid #333;
}

.header-logo {
  width: 36px;
  height: 36px;
  border-radius: 6px;
  margin-right: 12px;
}

.header-title {
  font-size: 1.1rem;
  font-weight: 500;
  color: #e0e0e0;
}

/* Chat Body */
.chat-body {
  flex: 1;
  padding: 32px 48px;
  overflow-y: auto;
}

.message-row {
  display: flex;
  gap: 12px;
  margin-bottom: 18px;
}

.bot-row {
  flex-direction: row;
  align-items: flex-start;
}

.user-row {
  flex-direction: row-reverse;
  align-items: flex-start;
}

.avatar {
  width: 36px;
  height: 36px;
  background: #444;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  font-size: 1.2rem;
}

.bot-avatar {
  background: #555;
}

.user-avatar {
  background: #7b1113;
}

.bubble {
  padding: 14px 18px;
  border-radius: 14px;
  font-size: 1rem;
  max-width: 70%;
  line-height: 1.5;
  word-break: break-word;
}

.bot-bubble {
  background: #2f2f2f;
  color: #eee;
}

.user-bubble {
  background: #7b1113;
  color: #fff;
}

/* Quick Options */
.quick-options {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin: 20px 0 0 48px;
}

.quick-options button {
  background: #3a3a3a;
  color: #fff;
  border: none;
  padding: 12px 20px;
  border-radius: 12px;
  font-size: 0.95rem;
  cursor: pointer;
  transition: background 0.2s;
  text-align: left;
}

.quick-options button:hover {
  background: #505050;
}

/* Chat Input */
.chat-input {
  display: flex;
  align-items: center;
  padding: 16px 24px;
  border-top: 1px solid #333;
  background: #1e1e1e;
}

.chat-input input {
  flex: 1;
  padding: 14px 16px;
  background: #2a2a2a;
  border: none;
  border-radius: 12px 0 0 12px;
  color: #fff;
  font-size: 1rem;
  outline: none;
}

.chat-input button {
  background: #7b1113;
  color: #fff;
  border: none;
  padding: 0 20px;
  border-radius: 0 12px 12px 0;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 0.2s;
}

.chat-input button:hover {
  background: #b71c1c;
}
</style>
