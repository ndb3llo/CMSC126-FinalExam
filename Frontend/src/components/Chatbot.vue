<template>
  <div class="main-layout">
    <header class="main-header">
      <img src="/uplogo.png" alt="UP Cebu Logo" class="header-logo" />
      <span class="header-title">faqUP</span>
    </header>
    <aside class="sidebar">
      <div class="sidebar-header">
        <span class="sidebar-appname">Chat History</span>
      </div>
      <nav class="sidebar-nav">
        <button class="sidebar-btn active" @click="startNewChat">New Chat</button>
        <button class="sidebar-btn">Search Chat</button>
      </nav>
    </aside>
    <div class="chat-area">
      <div class="chat-body">
        <div class="message-container">
          <!-- Initial bot message -->
          <div class="message-row bot-row" v-if="messages.length === 0">
            <img src="/uplogo.png" class="avatar bot-avatar" />
            <div class="bubble bot-bubble">
              Hi, how may I help you?
            </div>
          </div>
          
          <!-- Quick options only show when no messages yet -->
          <div v-if="messages.length === 0" class="quick-options">
            <button @click="sendQuickMessage('When do classes start?')">When do classes start?</button>
            <button @click="sendQuickMessage('How do I enroll?')">How do I enroll?</button>
            <button @click="sendQuickMessage('What is the dress code?')">What is the dress code?</button>
          </div>
          
          <!-- Display all messages -->
          <div v-for="(message, index) in messages" :key="index" class="message-row" :class="message.sender === 'user' ? 'user-row' : 'bot-row'">
            <template v-if="message.sender === 'bot'">
              <img src="/uplogo.png" class="avatar bot-avatar" />
              <div class="bubble bot-bubble">{{ message.text }}</div>
            </template>
            <template v-else>
              <div class="bubble user-bubble">{{ message.text }}</div>
              <div class="avatar user-avatar">
                <span class="user-icon">👤</span>
              </div>
            </template>
          </div>
        </div>
      </div> 
      <div class="chat-input">
        <input v-model="input" @keyup.enter="sendMessage" placeholder="Ask anything" />
        <button @click="sendMessage">
          <svg width="32" height="32" fill="none" viewBox="0 0 24 24">
            <path d="M2 21L23 12L2 3V10L17 12L2 14V21Z" fill="#014421"/>
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
      messages: [],
      searchQuery: ''
    }
  },
  methods: {
    startNewChat() {
      this.messages = [];
    },
    sendQuickMessage(msg) {
      this.input = msg;
      this.sendMessage();
    },
    sendMessage() {
      const userMessage = this.input.trim();
      if (!userMessage) return;
      
      // Add user message to chat
      this.messages.push({
        sender: 'user',
        text: userMessage
      });
      
      // Clear input
      this.input = '';
      
      // Simulate bot thinking
      setTimeout(() => {
        this.getBotReply(userMessage);
      }, 500);
    },
    getBotReply(userMessage) {
      let botReply = '';
      
      if (userMessage.toLowerCase().includes("enroll")) {
        botReply = `According to the Academic Calendar for A.Y. 2025 - 2026, enrollment starts June 17 - June 21, 2025.

        For enrolling students, you may refer to the following dates:

        June 17, 2025 - Students from 2022
        June 18, 2025 - Students from 2023
        June 19, 2025 - Students from 2024
        June 20, 2025 - Incoming first year students
        June 21, 2025 - All year levels

        Bring all necessary documents such as your School ID, Form 137, etc.`;
      } else if (userMessage.toLowerCase().includes("classes start")) {
        botReply = "Classes for A.Y. 2025-2026 start on August 5, 2025.";
      } else if (userMessage.toLowerCase().includes("dress code")) {
        botReply = "UP Cebu does not have a strict dress code, but students are expected to dress appropriately and respectfully on campus.";
      } else {
        botReply = "I'm sorry, I can only help with enrollment, class schedules, and dress code for now.";
      }
      
      // Add bot reply to chat
      this.messages.push({
        sender: 'bot',
        text: botReply
      });
      
      // Scroll to bottom after new message
      this.$nextTick(() => {
        const chatBody = document.querySelector('.chat-body');
        chatBody.scrollTop = chatBody.scrollHeight;
      });
    }
  }
}
</script>

<style scoped>
.main-layout {
  display: flex;
  height: 100vh;
  background: linear-gradient(180deg, #014421 0%, #003319 100%);
  font-family: 'Inter', Arial, sans-serif;
}
.main-header {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 64px;
  background: linear-gradient(180deg, #7b1113 80%, #b71c1c 100%);
  color: #fff;
  display: flex;
  align-items: center;
  z-index: 10;
  padding-left: 24px;
  gap: 14px;
  box-sizing: border-box;
}
.header-logo {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background: #fff;
}
.header-title {
  font-size: 1.1rem;
  font-weight: bold;
  letter-spacing: 0.5px;
}
.sidebar {
  position: fixed;
  top: 64px;
  left: 0;
  width: 240px;
  height: calc(100vh - 64px);
  background: linear-gradient(180deg, #07351d 0%, #012d18 100%);
  color: #fff;
  display: flex;
  flex-direction: column;
  padding-top: 32px;
  z-index: 5;
}
.sidebar-header {
  display: flex;
  align-items: center;
  gap: 12px;
  padding-left: 24px;
  margin-bottom: 32px;
}
.sidebar-logo {
  width: 38px;
  height: 38px;
  border-radius: 50%;
  background: #fff;
}
.sidebar-appname {
  font-size: 1rem;
  font-weight: bold;
  letter-spacing: 0.5px;
}
.sidebar-nav {
  display: flex;
  flex-direction: column;
  gap: 12px;
  padding-left: 24px;
}
.sidebar-btn {
  background: none;
  border: none;
  color: #fff;
  font-size: 1rem;
  text-align: left;
  padding: 0;
  font-weight: 500;
  cursor: pointer;
  border-radius: 6px;
  transition: background 0.2s, color 0.2s;
}
.sidebar-btn.active,
.sidebar-btn:hover {
  text-decoration: underline;
  color: #ffe082;
}
.chat-area {
  margin-left: 240px;
  margin-top: 64px;
  flex: 1;
  display: flex;
  flex-direction: column;
  height: calc(100vh - 64px);
  background: none;
  position: relative;
}
.chat-body {
  flex: 1;
  overflow-y: auto;
  padding: 20px 0 20px 0;
  position: relative;
}
.message-container {
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  min-height: min-content;
  padding-bottom: 20px;
}
.message-row {
  display: flex;
  align-items: flex-end;
  margin-bottom: 24px;
  max-width: 70%;
}
.bot-row {
  flex-direction: row;
  margin-left: 80px;
}
.user-row {
  flex-direction: row;      
  align-self: flex-end;
  margin-right: 80px;
  align-items: center;
  gap: 18px;                
}
.avatar {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  margin: 0 12px;
  background: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
}
.bot-avatar {
  border: 2px solid #7b1113;
}
.user-avatar {
  background: #7b1113;
  color: #fff;
  font-size: 2rem;
  width: 48px;
  height: 48px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0;
}
.user-icon {
  font-size: 1.3rem;
}
.bubble {
  padding: 12px 20px;
  border-radius: 16px;
  font-size: 1rem;
  max-width: 340px;
  word-break: break-word;
  white-space: pre-wrap;
  font-weight: 600;
  box-shadow: none;
}
.bot-bubble {
  background: #7b1113;
  color: #fff;
}
.user-bubble {
  background: #fff;
  color: #111;
  border: 2px solid #7b1113;
  border-radius: 20px;
  font-weight: 700;
  font-size: 1.1rem;
  padding: 14px 28px;
  margin: 0;
  display: flex;
  align-items: center;
}
.quick-options {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin: 0 0 0 auto;
  margin-right: 120px;
  align-items: flex-end;
}
.quick-options button {
  background: #7b1113;
  color: #fff;
  border: none;
  padding: 12px 0;
  border-radius: 12px;
  font-size: 1rem;
  font-weight: 700;
  cursor: pointer;
  text-align: center;
  width: 260px;
  transition: background 0.2s;
  outline: none;
}
.quick-options button:hover, .quick-options button:focus {
  background: #b71c1c;
}
.chat-input {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0 0 24px 0;
  background: none;
}
.chat-input input {
  flex: 1;
  max-width: 500px;
  min-width: 220px;
  padding: 10px 16px;
  border-radius: 16px 0 0 16px;
  border: 1.5px solid #b2b2b2;
  font-size: 1rem;
  background: #fff;
  color: #222;
  outline: none;
  transition: border 0.2s;
}
.chat-input input:focus {
  border: 1.5px solid #7b1113;
}
.chat-input button {
  padding: 0 12px;
  background: #fff;
  border: none;
  border-radius: 0 16px 16px 0;
  cursor: pointer;
  display: flex;
  align-items: center;
  transition: background 0.2s;
  border-left: 1.5px solid #b2b2b2;
  height: 38px;
}
.chat-input button:hover {
  background: #f3f3f3;
}
.chat-input svg {
  fill: #014421;
}
</style>