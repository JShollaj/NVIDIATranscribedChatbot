# Use the official Python image as the base image
FROM python:3.8-slim-buster

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create the .streamlit directory and copy the secrets file
RUN mkdir -p /root/.streamlit
COPY .streamlit/secrets.toml /root/.streamlit/secrets.toml

# Copy the rest of the project files and the data directory into container
COPY . .
COPY Data /app/data

# Expose the Streamlit port
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "NVIDIA_Chatbot.py"]
