# Use a specific version of the Python image to ensure reproducibility
FROM python:3.11-alpine3.17

# Create a dedicated working directory
ENV WORKDIR /app
WORKDIR ${WORKDIR}

# Copy the source code into the container
COPY . ${WORKDIR}

# Install dependencies with pip
RUN pip3 install --no-cache-dir --upgrade pip \
    && pip3 install --no-cache-dir -r requirements.txt

# Run the command to start the application
CMD ["python3", "main.py"]
