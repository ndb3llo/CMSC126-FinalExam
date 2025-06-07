<template>
  <div class="landing-container">
    <!-- Upper Half -->
    <div class="upper-half"></div>

    <!-- Logos (centered over both halves) -->
    <transition name="fade" appear>
      <div class="logo-container fade-delay">
        <img src="/uplogo.png" alt="UP Logos" />
      </div>
    </transition>

    <!-- Lower Half -->
    <div class="lower-half">
      <transition name="fade" appear>
        <h1 class="welcome-text">Welcome to faqUP!</h1>
      </transition>

      <transition name="fade" appear>
        <h2 class="subtitle-text">The official UP Cebu Chatbot</h2>
      </transition>

      <transition name="slide-fade-up" appear>
        <button @click="$router.push('/chat')">Start Chatting</button>
      </transition>
    </div>
  </div>
</template>



<style scoped>

.fade-enter-active,
.fade-appear-active {
  transition: opacity 2.5s ease;
}

.fade-enter-from,
.fade-appear-from {
  opacity: 0;
}

.fade-enter-to,
.fade-appear-to {
  opacity: 1;
}

@keyframes fadeInBackground {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

.landing-container {
  height: 100vh;
  width: 100vw;
  display: flex;
  flex-direction: column;
  overflow: hidden;
  position: relative;
}

/* Upper Half Image */
.upper-half {
  flex: 1;
  background-image: url('/UpperBG.png');
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
  background-repeat: repeat;
  animation: fadeInBackground 1.5s ease-in-out forwards;
}

/* Logo Positioned Center */
.logo-container {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 2;
}

.logo-container img {
  width: 400px;
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
  animation: fadeInBackground 1.5s ease-in-out forwards;
  opacity: 0; /* Required for animation delay to work */
}

.lower-half h1 {
  font-size: 2.5rem;
  margin: 0.5rem 0;
}

.lower-half h2 {
  font-size: 1.5rem;
  margin: 0.5rem 0 2rem;
}

.lower-half h1.welcome-text {
  font-size: 2.5rem;
  margin: 0.5rem 0 0.2rem;
  font-weight: bold;
}

.lower-half h2.subtitle-text {
  font-size: 1.5rem;
  margin: 0 0 2rem;
  font-style: italic;
  line-height: 1.2;
}

.lower-half button {
  background-color: #006400; /* dark green */
  color: white;
  padding: 0.8rem 2rem;
  font-size: 1rem;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: 3.0s;
}

.lower-half button:hover {
  background-color: #004d00;
}

/* Base animation for slide up + fade */
.slide-fade-up-enter-active,
.slide-fade-up-appear-active {
  animation: slideFadeUp 2.5s ease forwards;
}

.slide-fade-up-enter-from,
.slide-fade-up-appear-from {
  opacity: 0;
  transform: translateY(20px);
}

.slide-fade-up-enter-to,
.slide-fade-up-appear-to {
  opacity: 1;
  transform: translateY(0);
}

.slide-fade-delay {
  animation-delay: 2.5s;
  opacity: 0;
}

/* Define the keyframes */
@keyframes slideFadeUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

</style>
