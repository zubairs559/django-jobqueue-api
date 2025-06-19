# 📚 Django Job Queue API

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Django](https://img.shields.io/badge/Django-5.x-green)
![License](https://img.shields.io/badge/License-MIT-brightgreen)
![Status](https://img.shields.io/badge/Status-Completed-blue)

A Django-based REST API project that implements:

* CRUD operations on a `Book` model
* JWT authentication with role-based access
* A thread-based job queue with graceful shutdown
* Swagger UI for testing

---

## 🧾 Assignment Requirements vs Implementation

### ✅ Original Requirements:

1. **CRUD API with Python**

   * ✅ Built using Django
   * ✅ Handled JSON requests/responses
   * ✅ Used SQLite (bonus: DB integration)
2. **JWT Authentication Module**

   * ✅ Login, logout with token generation
   * ✅ Secured endpoints using middleware
   * ✅ Bonus: Refresh tokens + role-based access
3. **Concurrency in Practice**

   * ✅ Used `threading` module for job queue
   * ✅ Accepted concurrent tasks
   * ✅ Worker pool & graceful shutdown
4. **Python + Database Integration**

   * ✅ Used Django ORM with SQLite
   * ✅ Implemented persistent storage + transactions
   * ✅ Auto migrations handled via `manage.py`
5. **Dockerize a Python App**

   * 🚫 Skipped (as per discussion)

### ✨ Additional Features Implemented:

* Swagger UI with JWT Bearer token support
* Auto-collected static files for admin/Swagger
* README with badges, ToC, and clean structure
* GitHub version control and SSH-based push

---

## 📑 Table of Contents

* [Tech Stack](#-tech-stack)
* [Features Implemented](#-features-implemented)
* [Setup Instructions](#-setup-instructions)
* [Authentication (JWT)](#-authentication-jwt)
* [Book API Endpoints](#-book-api-endpoints-protected)
* [Job Queue API](#-job-queue-api)
* [Swagger UI Testing](#-test-with-swagger-ui)
* [Limitations](#-not-included)
* [Author](#-author)
* [Conclusion](#-conclusion)

---

## 🚀 Tech Stack

* Python 3.12
* Django 5.x
* Django REST Framework
* SimpleJWT for token authentication
* Threading (built-in Python module)
* SQLite (default Django DB)

---

## ✅ Features Implemented

### 1. CRUD API (Book)

* Endpoints to Create, Read, Update, Delete books
* JSON request/response handling

### 2. JWT Authentication

* Register, Login, Logout APIs
* Access + Refresh token support
* Role-based access for endpoints

### 3. Concurrency: Job Queue

* Tasks added to a job queue
* Executed via worker threads
* Graceful shutdown support

### 4. Swagger UI

* Auto-generated API documentation
* JWT token-based testing directly from browser

---

## 📦 Setup Instructions

### 1. Clone the Repo

```bash
git clone git@github.com:zubairs559/django-jobqueue-api.git
cd django-jobqueue-api
```

### 2. Create & Activate Virtual Env

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py migrate
```

### 5. Start the Server

```bash
python manage.py runserver
```

---

## 🔑 Authentication (JWT)

### Register:

`POST /api/auth/register/`

```json
{
  "username": "zubair",
  "password": "zubair",
  "email": "zubair@example.com"
}
```

### Login:

`POST /api/auth/login/`

Returns access + refresh tokens. Use the `access` token for Swagger authorization:

```
Bearer <access_token>
```

---

## 📘 Book API Endpoints (Protected)

| Method | Endpoint           | Description       |
| ------ | ------------------ | ----------------- |
| GET    | `/api/books/`      | List all books    |
| POST   | `/api/books/`      | Create a new book |
| GET    | `/api/books/<id>/` | Get a single book |
| PUT    | `/api/books/<id>/` | Update a book     |
| DELETE | `/api/books/<id>/` | Delete a book     |

---

## ⚙️ Job Queue API

### Add Job:

`POST /api/jobs/`

```json
{
  "task_type": "long_task"
}
```

### Get Job Status:

`GET /api/jobs/<job_id>/`

Returns current job status: `pending`, `in_progress`, `completed`

---

## 🧪 Test with Swagger UI

Visit:

```
http://localhost:8000/swagger/
```

1. Click **Authorize** button
2. Paste JWT token as:

```
Bearer <your_access_token>
```

3. Use available endpoints directly

---

## 🚫 Not Included

* Docker (skipped as per requirement)
* External DB (used SQLite)
* Deployment (local-only setup)

---

## 🧑‍💻 Author

**Mohmmad Zubair** &#x20;
GitHub: [zubairs559](https://github.com/zubairs559)

---

## 🏁 Conclusion

This project covers core backend skills including:

* Django API development
* JWT authentication
* Role-based access control
* Concurrency and thread handling

Perfect as a hands-on assignment or portfolio project. ✅
