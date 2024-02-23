 #Use the official PostgreSQL image as the base image
FROM postgres:latest

# Set environment variables for PostgreSQL database initialization
ENV POSTGRES_DB places_db
ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD postgres

# Copy the SQL initialization script to the container
COPY init.sql /docker-entrypoint-initdb.d/

# Expose the PostgreSQL port
EXPOSE 5432