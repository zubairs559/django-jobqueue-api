📚 Django Job Queue API

A Django-based REST API project that implements:

CRUD operations on a Book model

JWT authentication with role-based access

A thread-based job queue with graceful shutdown

Swagger UI for testing

🚀 Tech Stack

Python 3.12

Django 5.x

Django REST Framework

SimpleJWT for token authentication

Threading (built-in Python module)

SQLite (default Django DB)

✅ Features Implemented

1. CRUD API (Book)

Endpoints to Create, Read, Update, Delete books

JSON request/response handling

2. JWT Authentication

Register, Login, Logout APIs

Access + Refresh token support

Role-based access for endpoints

3. Concurrency: Job Queue

Tasks added to a job queue

Executed via worker threads

Graceful shutdown support

4. Swagger UI

Auto-generated API documentation

JWT token-based testing directly from browser

📦 Setup Instructions

1. Clone the Repo

git clone git@github.com:zubairs559/django-jobqueue-api.git
cd django-jobqueue-api

2. Create & Activate Virtual Env

python -m venv venv
venv\Scripts\activate  # On Windows

3. Install Dependencies

pip install -r requirements.txt

4. Run Migrations

python manage.py migrate

5. Start the Server

python manage.py runserver

🔑 Authentication (JWT)

Register:

POST /api/auth/register/

{
  "username": "zubair",
  "password": "zubair",
  "email": "zubair@example.com"
}

Login:

POST /api/auth/login/ Returns access + refresh tokens.

Use the access token for Swagger authorization:

Bearer <access_token>

📘 Book API Endpoints (Protected)

Method

Endpoint

Description

GET

/api/books/

List all books

POST

/api/books/

Create a new book

GET

/api/books//

Get a single book

PUT

/api/books//

Update a book

DELETE

/api/books//

Delete a book

⚙️ Job Queue API

Add Job:

POST /api/jobs/

{
  "task_type": "long_task"
}

Get Job Status:

GET /api/jobs/<job_id>/

Returns current job status: pending, in_progress, completed

🧪 Test with Swagger UI

Visit:

http://localhost:8000/swagger/

Click Authorize button

Paste JWT token as:

Bearer <your_access_token>

Use available endpoints directly

🚫 Not Included

Docker (skipped as per requirement)

External DB (used SQLite)

Deployment (local-only setup)

🧑‍💻 Author

Mohmmad ZubairGitHub: zubairs559

🏁 Conclusion

This project covers core backend skills including:

Django API development

JWT authentication

Role-based access control

Concurrency and thread handling

Perfect as a hands-on assignment or portfolio project. ✅

