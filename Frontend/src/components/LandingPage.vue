<template>
  <div class="landing-container">
    <!-- Upper Half -->
    <div class="upper-half"></div>

    <!-- Logos (centered over both halves) -->
    <div class="logo-container">
      <img src="/uplogo.png" alt="UP Logos" />
    </div>

    <!-- Lower Half -->
    <div class="lower-half">
      <h1>Welcome to faqUP</h1>
      <h2>The official UP Cebu Chatbot</h2>
      <button @click="$router.push('/chat')">Start Chatting</button>
    </div>
  </div>
</template>

<style scoped>
.landing-container {
  height: 100vh;
  display: flex;
  flex-direction: column;
  overflow: hidden;
  position: relative;
}

/* Upper Half Image */
.upper-half {
  flex: 1;
  background-image: url('/UpperHalf.png');
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
  background-repeat: no-repeat;
}

/* Logo Positioned Center */
.logo-container {
  position: absolute;
  top: 40%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 2;
}

.logo-container img {
  width: 200px;
  height: auto;
}

/* Lower Half */
.lower-half {
  flex: 1;
  background-color: #7b1113; /* UP Maroon */
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  color: white;
  text-align: center;
  padding-top: 2rem;
}

.lower-half h1 {
  font-size: 2.5rem;
  margin: 0.5rem 0;
}

.lower-half h2 {
  font-size: 1.5rem;
  margin: 0.5rem 0 2rem;
}

.lower-half button {
  background-color: #006400; /* dark green */
  color: white;
  padding: 0.8rem 2rem;
  font-size: 1rem;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: 0.3s;
}

.lower-half button:hover {
  background-color: #004d00;
}
</style>
