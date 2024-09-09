# Advanced API Project

## Overview
A Django project with Django REST Framework (DRF) for managing `Author` and `Book` models, featuring nested serializers, CRUD operations, and permissions.

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/<your-username>/Alx_DjangoLearnLab.git
    cd Alx_DjangoLearnLab/advanced-api-project
    ```

2. Install dependencies:

    ```bash
    pip install django djangorestframework
    ```

3. Apply migrations:

    ```bash
    python manage.py migrate
    ```

4. (Optional) Create a superuser:

    ```bash
    python manage.py createsuperuser
    ```

## API Endpoints

| Method | Endpoint                 | Description                   |
|--------|--------------------------|-------------------------------|
| GET    | `/api/books/`             | List all books                |
| POST   | `/api/books/`             | Create a new book             |
| GET    | `/api/books/<id>/`        | Retrieve a book by ID         |
| PUT    | `/api/books/<id>/update/` | Update a book by ID           |
| DELETE | `/api/books/<id>/delete/` | Delete a book by ID           |

## Features
- **Generic Views**: List, retrieve, create, update, and delete books.
- **Nested Serializers**: Handle author-book relationships.
- **Permissions**: Authenticated users can create, update, and delete; unauthenticated users can only view.

---
