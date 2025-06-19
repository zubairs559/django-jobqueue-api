# Dockerfile

# Step 1: Use Python base image
FROM python:3.12-slim

# Step 2: Set working directory inside the container
WORKDIR /app

# Step 3: Copy the requirements file
COPY requirements.txt .

# Step 4: Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of the project files
COPY . .

# Step 6: Collect static files (skip if not needed)
RUN python manage.py collectstatic --noinput || true

# Step 7: Expose port 8000 (Django default)
EXPOSE 8000

# Step 8: Run the development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
