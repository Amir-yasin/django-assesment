# Django-Assesment

Create a Django API with django rest framework

- [ ]  users with custom roles - admin, coach, agent, football player
- [ ]  sign up and social sign up (google, facebook)
- [ ]  login and social login
- [ ]  password reset

Overview

This project is an Role-based user registration API built with Django rest framework. It supports four different user roles: Admin, Coach, Agent, and Football Player, allowing each user to have customized functionalities based on their role. The platform also integrates social login/signup (Google, Facebook), password reset, and JWT authentication for secure access.

Features

Custom User Roles:

Admin

Coach

Agent

Football Player


Registration and Authentication:

User registration with role-based access

Secure login/logout functionality

Social login (Google, Facebook)

JWT-based authentication


Password Reset:

Secure password reset via email


REST API:

Full integration of Django REST framework for easy API access and interaction


Extensible Design:

Easy to extend with more user roles or functionality if needed



Tech Stack

Backend: Django, Django REST Framework

Authentication: dj-rest-auth, allauth (Google, Facebook)

Database: SQLite (for development), can be switched to PostgreSQL or MySQL

Front-end: (Optional) To be integrated with a front-end framework like React, Vue.js, etc.

Hosting: Suitable for deployment on platforms like Heroku, DigitalOcean, or AWS EC2


Installation and Setup

Requirements

Python 3.x

Django 5.1.2

Virtualenv (recommended)

Social Authentication keys (Google, Facebook)


Setup Instructions

1. Clone the repository:

git clone https://github.com/Amir-yasin/Django-assessment.git
cd Django-assessment


2. Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


3. Install the dependencies:

pip install -r requirements.txt


4. Set up the database:

python manage.py migrate


5. Create a superuser:

python manage.py createsuperuser


6. Run the development server:

python manage.py runserver


7. Navigate to http://127.0.0.1:8000/ in your browser.



Social Authentication Setup

To enable social login with Google and Facebook, follow these steps:

1. Google:

Go to Google Developer Console and create a new project.

Enable the Google+ API and create OAuth 2.0 credentials.

Add your CLIENT_ID and SECRET_KEY in your Django settings.



2. Facebook:

Go to Facebook for Developers and create a new app.

Set up Facebook Login and get the CLIENT_ID and SECRET_KEY.

Add these keys to your Django settings.




Environment Variables

For security reasons, ensure you store sensitive information like secret keys, database credentials, and API keys in environment variables:

SECRET_KEY='your-secret-key'
DEBUG=True
ALLOWED_HOSTS=127.0.0.1, localhost

API Endpoints

Authentication

Register: /dj-rest-auth/registration/

Login: /dj-rest-auth/login/

Password Reset: /dj-rest-auth/password/reset/


Social Authentication

Google Login: /dj-rest-auth/social/google/

Facebook Login: /dj-rest-auth/social/facebook/


Folder Structure

├── AssessmentProject
│   ├── settings.py       # Django settings
│   ├── urls.py           # URL routes
│   ├── wsgi.py           # WSGI for deployment
├── CustomUsersApp
│   ├── models.py         # CustomUser model with roles
│   ├── serializers.py    # Custom registration serializer
│   ├── views.py          # Custom views for registration and password reset
├── templates              # Templates for social authentication
├── manage.py              # Django management script

Future Enhancements

User Dashboard: Customized dashboards for each user role.

Notification System: Notify users of important updates.

Analytics Dashboard: Integrate reports and analytics for admin users.


Contributing

We welcome contributions! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

Steps to Contribute

1. Fork the repository.


2. Create a new branch:

git checkout -b feature/your-feature-name


3. Make your changes and commit them:

git commit -m 'Add some feature'


4. Push to the branch:

git push origin feature/your-feature-name


5. Open a pull request.


