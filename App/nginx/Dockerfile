#Use the Nginx image
FROM nginx

# Remove the default nginx.conf
RUN rm /etc/nginx/conf.d/default.conf

# Replace with our own nginx.conf
COPY nginx.conf /etc/nginx/conf.d/

COPY ssl/example.crt /etc/nginx/ssl/example.crt

COPY ssl/example.key /etc/nginx/ssl/example.key
