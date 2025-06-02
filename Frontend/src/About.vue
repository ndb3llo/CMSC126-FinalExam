<template>
  <div class="about">
    <h1>About Page</h1>
    <p>This is the about page of faqUP Chatbot.</p>
    <button @click="$router.push('/')">Go Back</button>
  </div>
</template>

<style scoped>
.about {
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
button {
  margin-top: 1rem;
  padding: 0.5rem 1.5rem;
  font-size: 1rem;
  border: none;
  background: red;
  color: white;
  border-radius: 5px;
  cursor: pointer;
}
</style>
