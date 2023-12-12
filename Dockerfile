# Use an official Python runtime as a parent image
FROM --platform=linux/amd64 python:3.11.4-slim-buster as build

# Set the working directory in the container
WORKDIR  /main

# Add current directory code to working directory
ADD . /main

# Install any needed packages specified in requirements.txt
COPY requirements.txt /main
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 8080

# Run app.py when the container launches
CMD ["python", "main.py"]