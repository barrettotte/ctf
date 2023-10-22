FROM mysql:latest

ENV MYSQL_ROOT_PASSWORD=password
ENV MYSQL_DATABASE=aurora

COPY ./aurora-compromise/aurora.sql /

EXPOSE 3306

CMD ["mysqld"]

# docker build -t deadface-aurora .
# docker run -d -p 3306:3306 deadface-aurora
# docker exec -it CONTAINER_ID mysql -u root -p password
