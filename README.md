# Doctor Booking System

<img width="427" alt="Снимок экрана 2025-02-10 213834" src="https://github.com/user-attachments/assets/055336ee-b287-4fc4-9e16-f99c654e9f3d" />


## Overview

Doctor Booking System is a web-based platform designed to facilitate doctor appointments and scheduling. It provides an efficient way for patients to book appointments and for doctors to manage their schedules.

## Features

- User authentication (patients & doctors)
- Online appointment booking
- Doctor profile management
- Appointment scheduling and notifications
- Admin panel for managing users and appointments

## Technologies Used

- **Backend:** Django (Python)
- **Database:** PostgreSQL
- **Authentication:** Django Authentication System
- **Styling:** Bootstrap

## Installation

Follow these steps to set up the project locally:

### Prerequisites

Ensure you have the following installed:

- Python 3
- PostgreSQL
- Git

### Steps

1. **Clone the repository**

   ```sh
   git clone https://github.com/ibr446/doctor-booking6.git
   cd doctor-booking6
   ```

2. **Create a virtual environment and activate it**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**

   ```sh
   pip install -r requirements.txt
   ```

4. **Set up environment variables** Create a `.env` file in the project root and add the following:

   ```env
   DATABASE_URL=your_postgresql_connection_string
   SECRET_KEY=your_django_secret_key
   DEBUG=True
   ```

5. **Run migrations**

   ```sh
   python manage.py migrate
   ```

6. **Create a superuser** (for admin access)

   ```sh
   python manage.py createsuperuser
   ```

7. **Start the development server**

   ```sh
   python manage.py runserver
   ```

## Usage

- Patients can register, log in, browse available doctors, and book appointments.
- Doctors can manage their schedules and view upcoming appointments.
- Admins have control over user management and system settings.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Commit your changes.
4. Push to your branch and submit a pull request.

## License

This project is licensed under the MIT License.

## Contact

For any inquiries or issues, feel free to reach out:

- GitHub: [ibr446](https://github.com/ibr446)


