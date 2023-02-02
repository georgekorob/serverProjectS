FROM node:18.13.0-alpine as builder

RUN npm install -g npm@9.4.0
COPY ["package.json", "package-lock.json*", "./"]
RUN npm ci --silent
COPY ./ ./
RUN npm run build

FROM nginx:1.23.1-alpine
COPY --from=builder ./build /var/www

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/nginx.conf
