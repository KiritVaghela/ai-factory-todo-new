FROM node:14

# Set working directory
WORKDIR /usr/src/app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy source files
COPY . .

# Build the app (if needed)
RUN npm run build

# Expose the port
EXPOSE 3000

# Start the application
CMD [ "npm", "start" ]