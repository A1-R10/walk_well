FROM python:3.10-slim-bullseye

# Set environment variable to avoid buffering logs
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /walk_well

# Copy the requirements file
COPY requirements.txt requirements.txt

# Install Python dependencies
RUN pip install -r requirements.txt

# Copy all application files
COPY . .

# Command to run the Django application
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
