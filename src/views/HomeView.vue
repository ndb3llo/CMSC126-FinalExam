<script setup lang="ts">
// Component logic here
</script>

<template>
  <div class="w-full h-screen relative overflow-hidden">
    <!-- Background Image -->
    <img
      class="background-image"
      src="../assets/images/oblation statue.jpg"
      alt="UP Cebu Building"
    />

    <!-- Gradient Overlay -->
    <div class="gradient-overlay"></div>

    <!-- Content -->
    <div class="content-wrapper">
      <!-- Logos -->
      <img
        class="w-[200px] mb-8"
        src="../assets/images/UP logos.png"
        alt="UP Logos"
      />

      <!-- Heading -->
      <h1 class="main-heading">
        Welcome to the UP Cebu Campus FAQ Chatbot
      </h1>

      <!-- Button -->
      <router-link to="/chat" class="start-button">
        Start Chatting
      </router-link>
    </div>
  </div>
</template>

<style scoped>
.background-image {
  @apply absolute w-full h-full object-cover;
}

.gradient-overlay {
  @apply absolute bottom-0 w-full h-1/2 bg-gradient-to-t from-red-800 to-transparent;
}
</style>