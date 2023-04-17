# Use an official Python runtime as a parent image
FROM python:3.10.6-buster

# Set the working directory to /app
WORKDIR /lp_calles

# Copy the current directory contents into the container at /app
COPY . /lp_calles
COPY requirements.txt /requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run api.py when the container launches
# CMD ["python", "api.py"]

CMD uvicorn api:app --host 0.0.0.0 --port $PORT
