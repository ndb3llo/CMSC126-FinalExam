# frontend/Dockerfile
FROM node:20-alpine

# Set working directory
WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm install

# Copy the rest of the Vue project
COPY . .

# Expose the port Vite will run on
EXPOSE 5173

# Start the development server
CMD ["npm", "run", "dev"]
