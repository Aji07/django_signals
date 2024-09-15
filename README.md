# Django Signals Project

This project demonstrates Django signals and their behavior in terms of synchronous execution, threading, and transaction handling.

## Features
- Demonstrates default Django signal behavior (synchronous, single-threaded, and in the same transaction).
- Uses Django's built-in `User` model for signal triggers.
- Sample app `users` for signal handling.

## Getting Started

### Prerequisites
- Python 3.x
- Django 4.x or higher

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Aji07/django_signals.git
   cd django-signals

Install dependencies:
    pip install -r requirements.txt

Run the project:
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver

To test the signal, create or save a User instance. For example:
    
    python manage.py shell

    from django.contrib.auth.models import User
    user = User.objects.create(username='testuser', email='test@example.com')

