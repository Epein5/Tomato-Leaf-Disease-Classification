FROM python:3.10.11

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

COPY ML/sequential_model.pth /app/ML/

# COPY static/Images /app/static/Images

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application code into the container2
COPY . .

# Expose the port on which the FastAPI application will run
EXPOSE 5000

# Set the command to run the FastAPI application
CMD ["uvicorn", "BACKEND.main:app", "--host", "0.0.0.0", "--port", "5000"]