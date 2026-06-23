# Contact Management System (Django)

A web-based contact management application built with Django. Create and manage
contacts, each with multiple phone numbers, emails, and address details.

## Features

- Add, edit, view, and delete contacts
- Multiple phone numbers and emails per contact
- Additional fields: address, country code, gender
- Server-rendered UI styled with Bootstrap
- Django admin for data management

## Tech Stack

- **Backend:** Python, Django 4.2
- **Database:** SQLite (default; swappable via Django settings)
- **Frontend:** Django templates + Bootstrap
- **Containerization:** Docker

## Getting Started

### Prerequisites
- Python 3.8+ (or Docker)

### Run locally

```bash
# 1. Clone the repository
git clone https://github.com/MarwaSayedHashem/PhoneBook.git
cd PhoneBook

# 2. (Recommended) create a virtual environment
python -m venv venv
source venv/bin/activate        # on Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply database migrations
python manage.py migrate

# 5. (Optional) create an admin user
python manage.py createsuperuser

# 6. Start the development server
python manage.py runserver
```

Then open http://127.0.0.1:8000/ in your browser.

### Run with Docker

```bash
docker build -t phonebook .
docker run -p 8000:8000 phonebook
```

## Configuration

Sensitive settings are read from environment variables (with safe local-dev
fallbacks):

| Variable | Description | Default |
|---|---|---|
| `DJANGO_SECRET_KEY` | Django secret key | insecure dev key |
| `DJANGO_DEBUG` | `True`/`False` | `True` |
| `DJANGO_ALLOWED_HOSTS` | Comma-separated hosts | `*` |

In production, always set `DJANGO_SECRET_KEY` and `DJANGO_DEBUG=False`.

## Project Structure

```
PhoneBook/
├── phonebook/      # Project settings, URLs, WSGI/ASGI
├── contacts/       # Contacts app: models, views, forms, templates
├── manage.py
├── requirements.txt
└── Dockerfile
```

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
