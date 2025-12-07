# Personal Finance Tracker

A Django-based web application for tracking personal finances, including income and expenses, with category management and user authentication.

## Features

- User registration and login
- Add, edit, and delete transactions
- Categorize transactions (Income/Expense)
- View transaction history
- Simple and clean UI for easy navigation

## Tech Stack

- Python 3.x
- Django 5.x
- SQLite (default database)
- HTML/CSS (frontend templates)

## Installation and Setup

1. **Clone the repository**
    ```bash
    git clone https://github.com/Amrit-Maan/Personal_finance_tracker_project.git
    cd Personal_finance_tracker_project
    ```

2. **Create a virtual environment**
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment**
    - **Windows:**
      ```bash
      venv\Scripts\activate
      ```
    - **Mac/Linux:**
      ```bash
      source venv/bin/activate
      ```

4. **Install dependencies**
    ```bash
    pip install django
    ```
    *Optional:* If you have a `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

5. **Apply migrations**
    ```bash
    python manage.py migrate
    ```

6. **Create a superuser (optional, for admin access)**
    ```bash
    python manage.py createsuperuser
    ```

7. **Run the development server**
    ```bash
    python manage.py runserver
    ```

8. **Open the application in your browser**
    ```
    http://127.0.0.1:8000/
    ```

## Usage

- Register a new account or log in.
- Add income or expense transactions and categorize them.
- View all transactions in a list.
- Logout when finished.
