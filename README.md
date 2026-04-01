# Finance-Backend-API-Django-


# Finance Backend API (Django)

## Features
- User & Role Management (Admin, Analyst, Viewer)
- Financial Records CRUD
- Record Filtering (by type, category)
- Dashboard Summary API (income, expense, balance)
- Role-Based Access Control 
- Input Validation 

## Tech Stack
- Django
- Django REST Framework
- Python

## Setup Instructions
1. Clone the repo
2. Install dependencies:
   pip install django djangorestframework
3. Run migrations:
   python manage.py migrate
4. Create superuser:
   python manage.py createsuperuser
5. Run server:
   python manage.py runserver

## API Endpoints
- /api/users/ (Admin only)
- /api/records/
- /api/dashboard/

## Notes
- RBAC enforced using custom permission classes
- Filtering supported using query parameters
