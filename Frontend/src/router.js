import { createRouter, createWebHistory } from 'vue-router'
import LandingPage from '@/components/LandingPage.vue'
import Chatbot from '@/components/Chatbot.vue'

const routes = [
  { path: '/', component: LandingPage },
  { path: '/chat', component: Chatbot },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
