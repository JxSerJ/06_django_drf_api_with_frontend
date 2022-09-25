FROM node:13.12.0-alpine as build
WORKDIR /app
COPY package*.json ./
RUN npm install -g npm
RUN apk add --update python3 make g++ && rm -rf /var/cache/apk/*
RUN echo "PLEASE WAIT! Downloading and installing deps. This can take at least 120 seconds" && npm i -ddd
COPY . ./
RUN ls -la
CMD npm run build
