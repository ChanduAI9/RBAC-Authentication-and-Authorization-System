# RBAC System - Role-Based Access Control

## Overview

This project implements a Role-Based Access Control (RBAC) system using Django, allowing for secure user authentication and authorization. Users are assigned roles, and each role is associated with specific permissions. The system ensures that users can only access the resources and perform actions they are authorized to, based on their assigned roles.

## Features

- **Role-Based Access Control**: Users are assigned roles (Admin, User, Moderator) that determine their access to specific resources and actions.
- **Permissions**: Each role has a set of permissions, which can be checked using the `has_permission` method in the `User` model.
- **Endpoint for Testing**: A dedicated `/tester/` endpoint is available for testing user roles and permissions.

## Requirements

- Python 3.x
- Django REST Framework
- SQLite (used for development)
  
## Installation

1. Clone the repository:
    ```bash
    cd rbac_project
    ```

2. Set up a virtual environment:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply database migrations:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser (optional):
    ```bash
    python manage.py createsuperuser
    ```

## Testing the System

### `/tester/` Endpoint

The `/tester/` endpoint allows you to manually test the system by checking if a user has the correct permissions based on their assigned role.

### How to Test:

1. **Run the server**:
    ```bash
    python manage.py runserver
    ```

2. **Access the `/tester/` endpoint**:
    - Visit `http://127.0.0.1:8000/tester/` in your browser.
    - You will see a list of users with their roles and whether they have specific permissions (e.g., `can_view_data`, `can_edit_data`).

3. **Example Tests**:
    - **Admin User**:
        - Should have all permissions (`can_view_data`, `can_edit_data`, `can_delete_data`).
    - **Normal User**:
        - Should only have the `can_view_data` permission.
    - **Moderator User**:
        - Should have `can_view_data` and `can_edit_data` permissions, but not `can_delete_data`.

### Sample Input for Testing Permissions

- **Admin User**:
    - Username: `admin_user`
    - Password: `admin123`
    - Role: Admin
    - Permissions: `can_view_data`, `can_edit_data`, `can_delete_data`
  
- **Normal User**:
    - Username: `normal_user`
    - Password: `user123`
    - Role: User
    - Permissions: `can_view_data`
  
- **Moderator User**:
    - Username: `moderator_user`
    - Password: `moderator123`
    - Role: Moderator
    - Permissions: `can_view_data`, `can_edit_data`

### Expected Output

- **Admin User**:
    - Should have all permissions listed: `can_view_data`, `can_edit_data`, `can_delete_data`.

- **Normal User**:
    - Should only have `can_view_data`.

- **Moderator User**:
    - Should have `can_view_data` and `can_edit_data`, but not `can_delete_data`.

## Security Best Practices

- Passwords are securely hashed using Django's default password hashing mechanism.
- Role and permission checking is done using the `has_permission` method to ensure users can only perform actions they are authorized to.

## Conclusion

This RBAC system is designed to be flexible, allowing roles and permissions to be easily managed, tested, and extended. The `/tester/` endpoint provides an easy way to test and validate the system's functionality.
