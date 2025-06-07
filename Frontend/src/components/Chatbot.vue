<template>
  <div class="main-layout">
    <header class="main-header">
      <img src="/upclogo.jpg" alt="UP Cebu Logo" class="header-logo" />
      <span class="header-title">UP Cebu FAQ</span>
    </header>
    <aside class="sidebar">
      <div class="sidebar-header">
        <img src="/upclogo.jpg" alt="UP Cebu Logo" class="sidebar-logo" />
        <span class="sidebar-appname">UP Cebu Chatbot</span>
      </div>
      <nav class="sidebar-nav">
        <input
          v-model="searchQuery"
          placeholder="Search chat..."
          class="sidebar-search"
        />
        <button class="sidebar-btn active" @click="startNewChat">New Chat</button>
        <div class="chat-history">
          <div
            v-for="(chat, index) in filteredChats"
            :key="index"
            class="chat-history-item"
            :class="{ selected: index === selectedChatIndex }"
          >
            <span v-if="editingChatIndex !== index" @click="selectChat(index)" class="chat-title">
              {{ chat.title }}
            </span>
            <input
              v-else
              v-model="editingTitle"
              @keyup.enter="saveChatTitle(index)"
              @blur="saveChatTitle(index)"
              class="edit-chat-input"
              :class="{ editing: editingChatIndex === index }"
            />
            <div class="menu-wrapper">
              <button class="menu-btn" @click.stop="toggleMenu(index)">⋮</button>
              <teleport to="body">
                <div
                  v-if="activeMenuIndex === index"
                  class="dropdown-menu"
                  :style="menuPosition"
                  ref="menu"
                >
                  <button @click="renameChat(index)">Rename</button>
                  <button @click="deleteChat(index)">Delete</button>
                </div>
              </teleport>
            </div>
          </div>
        </div>
      </nav>
    </aside>
    <div class="chat-area">
      <div class="chat-body">
        <div class="message-container">
          <!-- Initial bot message -->
          <div class="message-row bot-row" v-if="messages.length === 0">
            <img src="/upclogo.jpg" class="avatar bot-avatar" />
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
              <img src="/upclogo.jpg" class="avatar bot-avatar" />
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

      chats: [],
      selectedChatIndex: null,
      searchQuery: '',
      activeMenuIndex: null,
      menuPosition: {},
      editingChatIndex: null,
      editingTitle: '',
    }
  },
  computed: {
    filteredChats() {
      return this.chats.filter(chat =>
        chat.title.toLowerCase().includes(this.searchQuery.toLowerCase())
      );
    }
  },
  methods: {
    startNewChat() {
      if (this.messages.length > 0) {
        const title = this.messages.find(m => m.sender === 'user')?.text || 'Untitled Chat';
        this.chats.unshift({
          title: title.slice(0, 30),
          messages: [...this.messages]
        });
      }
      this.messages = [];
      this.selectedChatIndex = null;
    },
    selectChat(index) {
      this.selectedChatIndex = index;
      this.messages = [...this.chats[index].messages];
    },
    sendQuickMessage(msg) {
      this.input = msg;
      this.sendMessage();
    },
    async sendMessage() {
      const userMessage = this.input.trim();
      if (!userMessage) return;
      this.messages.push({ sender: 'user', text: userMessage });
      this.input = '';

      // Call backend API
      try {
        const response = await fetch('http://127.0.0.1:8000/chatbot_api/', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ user_input: userMessage })
        });
        const data = await response.json();
        this.messages.push({ sender: 'bot', text: data.response });
      } catch (error) {
        this.messages.push({ sender: 'bot', text: "Sorry, I couldn't connect to the server." });
      }

      this.$nextTick(() => {
        const chatBody = document.querySelector('.chat-body');
        if (chatBody) chatBody.scrollTop = chatBody.scrollHeight;
      });
    },
    toggleMenu(index) {
      if (this.activeMenuIndex === index) {
        this.activeMenuIndex = null;
        return;
      }

      this.$nextTick(() => {
        const btn = event.currentTarget;
        const rect = btn.getBoundingClientRect();
        this.menuPosition = {
          top: `${rect.bottom + 4}px`,
          left: `${rect.left - 100}px`,
          position: 'absolute',
          zIndex: 9999
        };
        this.activeMenuIndex = index;
      });
    },
    renameChat(index) {
      this.editingChatIndex = index;
      this.editingTitle = this.chats[index].title;
      this.activeMenuIndex = null;
      this.$nextTick(() => {
        const input = document.querySelector('.edit-chat-input');
        if (input) input.focus();
      });
    },
     toggleMenu(index) {
      if (this.activeMenuIndex === index) {
        this.activeMenuIndex = null;
        return;
      }

      this.$nextTick(() => {
        const btn = event.currentTarget;
        const rect = btn.getBoundingClientRect();
        this.menuPosition = {
          top: `${rect.bottom + 4}px`,
          left: `${rect.left - 100}px`,
          position: 'absolute',
          zIndex: 9999
        };
        this.activeMenuIndex = index;
      });
    },
    renameChat(index) {
      this.editingChatIndex = index;
      this.editingTitle = this.chats[index].title;
      this.activeMenuIndex = null;
      this.$nextTick(() => {
        const input = document.querySelector('.edit-chat-input');
        if (input) input.focus();
      });
    },
    saveChatTitle(index) {
      if (this.editingTitle.trim()) {
        this.chats[index].title = this.editingTitle.trim();
      }
      this.editingChatIndex = null;
    },
    saveChatTitle(index) {
      if (this.editingTitle.trim()) {
        this.chats[index].title = this.editingTitle.trim();
      }
      this.editingChatIndex = null;
    },
    deleteChat(index) {
      this.chats.splice(index, 1);
      if (this.selectedChatIndex === index) {
        this.messages = [];
        this.selectedChatIndex = null;
      }
      this.activeMenuIndex = null;
    },
    handleClickOutside(event) {
      if (!event.target.closest('.dropdown-menu') && !event.target.closest('.menu-btn')) {
        this.activeMenuIndex = null;
      }
    }
  },
  mounted() {
    document.addEventListener('click', this.handleClickOutside);
  },
  beforeDestroy() {
    document.removeEventListener('click', this.handleClickOutside);
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
  background: #7b1113;
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

.sidebar-search {
  margin-bottom: 12px;
  padding: 8px 12px;
  border-radius: 8px;
  border: none;
  font-size: 0.95rem;
  font-family: 'Inter', sans-serif;
  outline: none;
  background: #f9f9f9;
  color: #111;
  width: 180px;
}

.sidebar-search::placeholder {
  color: #666;
}
.sidebar-btn {
  background-color: transparent;
  color: white;
  font-size: 1rem;
  padding: 10px 16px;
  border: 1px solid #ccc;
  border-radius: 8px;
  font-weight: 500;
  cursor: pointer;
  width: 180px;
  text-align: center;
  transition: all 0.2s;
  font-family: 'Inter', sans-serif;
}

.sidebar-btn:hover,
.sidebar-btn.active {
  background-color: #7b1113;
  border-color: #aaa;
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
.chat-history {
  display: flex;
  flex-direction: column;
  margin-top: 12px;
  max-height: 50vh;
  overflow-y: auto;
  gap: 8px;
  padding-right: 12px;
}
.chat-history-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: relative;
  padding: 6px; 
  border-radius: 10px; 
  transition: background-color 0.2s, color 0.2s;
}

.chat-title {
  flex: 1;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  cursor: pointer;
  padding-right: 10px;
}

.menu-wrapper {
  position: relative;
  z-index: 999;
}

.menu-btn {
  background: none;
  border: none;
  color: #ccc;
  font-size: 18px;
  cursor: pointer;
  padding: 2px 6px;
}

.menu-btn:hover {
  color: #fff;
}

.dropdown-menu {
  background: #222;
  border: 1px solid #555;
  border-radius: 8px;
  padding: 8px 0;
  display: flex;
  flex-direction: column;
  z-index: 9999;
  min-width: 120px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  position: absolute;
}

.dropdown-menu button {
  background: none;
  border: none;
  padding: 8px 12px;
  color: #ddd;
  text-align: left;
  font-size: 0.95rem;
  cursor: pointer;
  width: 100%;
}

.dropdown-menu button:hover {
  background: #444;
}

.dropdown-menu button:last-child {
  color: #ff6b6b;
}

.chat-history-item:hover,
.chat-history-item.selected {
  background: #014421;
  color: #ffe082;
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

.edit-chat-input {
  flex: 1;
  padding: 4px 8px;
  font-size: 0.95rem;
  border-radius: 6px;
  border: 1px solid #ccc;
  outline: none;
  background: #fff;
  color: #111;
  max-width: 140px;
}
.edit-chat-input.editing {
  border-color: #7b1113;
}

</style>