FROM nginx:latest

COPY nginx.conf /etc/nginx/nginx.conf
WORKDIR /etc/nginx

CMD ["nginx", "-g", "daemon off;"]

EXPOSE 80