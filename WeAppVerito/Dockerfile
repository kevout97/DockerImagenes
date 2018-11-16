FROM nginx

COPY webpage /usr/share/nginx/html

COPY config/webapp.conf /etc/nginx/conf.d

CMD ["nginx", "-g", "daemon off;"]