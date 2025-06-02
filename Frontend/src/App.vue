<template>
  <div :class="{ 'layout-default': !isLanding, 'layout-full': isLanding }">
    <router-view />
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'
const route = useRoute()

const isLanding = route.path === '/'
</script>
