# Use python runtime as the parent image
FROM ubuntu:latest

# Update ubuntu packages
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Update pip
RUN pip install --upgrade pip

# Install any needed packages
RUN pip install -r requirements.txt

# Define environment variables
ENV APP_NAME CryptoBot

# Run app.py when the container launches
CMD ["python", "app.py"]
