The Med Consultation API is a Django Rest Framework (DRF) based platform designed for online medical consultations, appointment scheduling, and patient management.

Table of Contents
Features
Technologies Used
Project Structure
Installation
Environment Variables
Running the Application
API Documentation
Best Practices Followed
Contributing
License
Features
User authentication and authorization using Django Rest Framework's Token Authentication
Role-based access control (Doctors, Patients, Admin)
Appointment scheduling and management
Patient record management
Secure APIs with Token-based authentication
Comprehensive error handling and input validation
Technologies Used
Programming Language: Python

Framework: Django, Django Rest Framework (DRF)

Database: PostgreSQL

Authentication: Token Authentication

Containerization: Docker

Testing: Pytest

Documentation: DRF's built-in API documentation and Swagger/OpenAPI

Screenshot 2025-02-10 at 11 18 44
Project Structure
med-consultation-api/
├── api/
│   ├── migrations/              # Database migrations
│   ├── __init__.py              # Package initialization
│   ├── admin.py                 # Django admin configuration
│   ├── apps.py                  # App configuration
│   ├── managers.py              # Custom database managers
│   ├── models.py                # Database models
│   ├── serializers.py           # DRF serializers for request and response validation
│   ├── tests.py                 # Unit tests
│   ├── urls.py                  # URL routing for the API
│   └── views.py                 # API view logic
├── media/
│   ├── avatars/                 # User avatar storage
│   └── news/                    # News-related media files
├── root/
│   ├── __init__.py              # Project package initialization
│   ├── asgi.py                  # ASGI configuration
│   ├── settings.py              # Project settings
│   ├── urls.py                  # Root URL routing
│   └── wsgi.py                  # WSGI configuration
├── static/                      # Static files for the project
├── .env.local                   # Local environment variables
├── .env.prod                    # Production environment variables
├── docker-compose.yml           # Docker Compose configuration
├── Dockerfile                   # Docker configuration
├── entrypoint.prod.sh           # Entry point script for production
├── manage.py                    # Django management script
├── mig.sh                       # Migration script helper
├── nginx.conf                   # Nginx configuration
├── pytest.ini                   # Pytest configuration
├── README.md                    # Project documentation
├── requirements.txt             # Python dependencies
└── TODO                         # Pending development tasks
Installation
Prerequisites
Python 3.9+
PostgreSQL
Docker (Optional for containerized deployment)
Steps
Clone the repository:
git clone https://github.com/themusharraf/med-consultation-api.git
cd med-consultation-api
Create a virtual environment and activate it:
python3 -m venv venv
source venv/bin/activate
Install dependencies:
pip install -r requirements.txt
Environment Variables
Create a .env file in the project root by copying .env.example:

cp .env.example .env
Fill in the required environment variables:

DATABASE_URL=postgresql://user:password@localhost:5432/medconsultation
SECRET_KEY=your_django_secret_key
DEBUG=True
ALLOWED_HOSTS=*
Running the Application
Locally
python manage.py migrate
python manage.py runserver
API Documentation
Once the application is running, visit:

DRF's Browsable API: http://localhost:8000/api/
Swagger/OpenAPI: http://127.0.0.1:8000/api/docs#/ (if configured)
Best Practices Followed
Modular Architecture: Organized code into views, serializers, and models.
Database Migrations: Use of Django's migration system.
Environment Variables: Secure and configurable environment settings.
Secure Authentication: Token-based authentication for API security.
Data Validation: Use of DRF serializers for request and response validation.
Exception Handling: Comprehensive error handling for better API responses.
Testing: Unit and integration tests using Pytest.
Logging: Standard logging practices for monitoring and debugging.
Documentation: Auto-generated API documentation with Swagger and DRF.
Containerization: Dockerized application for consistency across environments.
Contributing
Contributions are welcome! Follow these steps:

Fork the repository.
Create a new branch.
Commit your changes.
Submit a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for details.
