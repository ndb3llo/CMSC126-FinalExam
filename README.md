# Project Setup Guide

This guide provides instructions for setting up and running the project, including both frontend and backend components using Vue 3 with Vite and Docker Compose.

---

## 🌐 Project Links

- Demo Video: https://drive.google.com/file/d/1EwzTir413GPsC4-QCnUeB787dwCpdV82/view?usp=sharing
- Deployed Site: https://cmsc-126-final-exam.vercel.app/

---

## 🔧 Prerequisites

- Docker Desktop (includes Docker Compose): https://www.docker.com/
- Git: https://git-scm.com/
- VSCode: https://code.visualstudio.com/
- Volar Extension for Vue: https://marketplace.visualstudio.com/items?itemName=Vue.volar  
  (Disable Vetur if it's installed)

---

## 🚀 Getting Started

1. Install Docker Desktop and Git if you haven’t already.

2. Open your terminal or command prompt.

3. Clone the repository:

   git clone https://github.com/your/repo.git

4. Navigate into the project folder:

   cd repo

5. Start the development environment with Docker Compose:

   docker-compose up --build

6. Open your browser and visit:
   - Frontend: http://localhost:5173
   - Backend: http://localhost:8000

---

## ⚙️ Frontend Development (Vue 3 + Vite)

This template uses Vue 3 and Vite for the frontend.

### Project Setup

   npm install

### Compile and Hot-Reload for Development

   npm run dev

### Compile and Minify for Production

   npm run build

### Customize Configuration

   See the Vite Configuration Reference: https://vite.dev/config/
