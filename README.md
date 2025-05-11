# Django Bookstore Project

This is a Django-based web application for managing a bookstore. Users can browse books, leave reviews, and search for books. The project is containerized using Docker for easy setup and deployment.

---

## Features

- **User Authentication**: Login, signup, and logout functionality using `django-allauth`.
- **Book Management**: View book details, leave reviews, and browse all books.
- **Search Functionality**: Search for books by title or author.
- **Permissions**: Restrict access to certain views based on user permissions.
- **Responsive Design**: Custom CSS for styling, including a background image.
- **Dockerized**: Fully containerized for easy deployment.

---

## Requirements

- Python 3.12
- Docker and Docker Compose
- Pipenv (for dependency management)

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/witkowskilukas/Bookstore.git
cd django-bookstore
```

### 2. Set Up Environment Variables

Create a `.env` file in the root directory and add the following:

```env
DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
```

### 3. Build and Run the Docker Container

```bash
docker-compose up --build
```

This will build the Docker image and start the application.

---

## Usage

### Access the Application

- Open your browser and go to: [http://localhost:8000](http://localhost:8000)

### Admin Panel

- Access the admin panel at: [http://localhost:8000/admin/](http://localhost:8000/admin/)
- Create a superuser to access the admin panel:

```bash
docker-compose exec web python manage.py createsuperuser
```

---

## Project Structure

```
books/
├── books/                  # Main app for managing books and reviews
│   ├── models.py           # Database models for books and reviews
│   ├── views.py            # Views for handling requests
│   ├── urls.py             # URL routing for the app
│   ├── templates/          # HTML templates
│   └── static/             # Static files (CSS, images)
├── config/                 # Project configuration
│   ├── settings.py         # Django settings
│   ├── urls.py             # Project-level URL routing
│   └── wsgi.py             # WSGI entry point
├── Dockerfile              # Docker configuration
├── docker-compose.yml      # Docker Compose configuration
├── Pipfile                 # Pipenv dependencies
├── Pipfile.lock            # Locked dependencies
└── README.md               # Project documentation
```

---

## Key Features

### 1. **Book Management**
- Books are stored in the database with fields like title, author, price, and cover image.
- Users can view book details and leave reviews.

### 2. **User Authentication**
- Login, signup, and logout functionality using `django-allauth`.
- Permissions are enforced for accessing certain views.

### 3. **Search Functionality**
- Users can search for books by title or author.

### 4. **Responsive Design**
- Custom CSS for styling, including a background image.

---

## Deployment

### Collect Static Files

Before deploying to production, collect static files:

```bash
docker-compose exec web python manage.py collectstatic
```

### Run Migrations

Apply database migrations:

```bash
docker-compose exec web python manage.py migrate
```

---

## Testing

Run tests using the following command:

```bash
docker-compose exec web python manage.py test
```

---

## Docker Configuration

### Dockerfile

The `Dockerfile` is configured to use Python 3.12 and Pipenv for dependency management:

```dockerfile
FROM python:3.12.0

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system --deploy --ignore-pipfile

# Copy the rest of the project
COPY . /code/
```

### Docker Compose

The `docker-compose.yml` file defines two services: `web` (Django app) and `db` (PostgreSQL database):

```yaml
version: '3.12'

services:
  web:
    build: .
    command: gunicorn config.wsgi -b 0.0.0.0:8000
    volumes:
      - .:/code
    ports:
      - 8000:8000
    depends_on:
      - db
    environment:
      - "DJANGO_SECRET_KEY=your-secret-key"
      - "DJANGO_DEBUG=True"
      - "DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1"

  db:
    image: postgres:13
    volumes:
      - postgres_data:/var/lib/postgresql/data/
```

---

## Dependencies

The project uses the following dependencies, as specified in the `Pipfile.lock`:

- **Django**: The web framework used for building the application.
- **django-allauth**: For user authentication and social login.
- **django-crispy-forms**: For better form rendering.
- **django-debug-toolbar**: For debugging during development.
- **gunicorn**: For running the application in production.
- **psycopg2-binary**: PostgreSQL database adapter.
- **whitenoise**: For serving static files in production.
- **Pillow**: For handling image uploads.

---

## Acknowledgments

- [Django Documentation](https://docs.djangoproject.com/)
- [Docker Documentation](https://docs.docker.com/)
- [django-allauth](https://django-allauth.readthedocs.io/)

---

## Contact

For questions or feedback, please contact [witkowskilukasz86@gmail.com](mailto:witkowskilukasz86@gmail.com).
```

### Notes:
- Replace `your-secret-key`, `your-username`, and `your-email@example.com` with your actual values.
