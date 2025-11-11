# NewApplication

A Django-based blog website featuring a Persian company template, designed for publishing articles with user authentication and media management.

## Description

This project is a web application built with Django 5.2.8 that provides a platform for publishing and managing blog articles. It includes a responsive Persian-language template with features like article listings, user authentication, image uploads, and an admin interface for content management.

The application uses PostgreSQL as the database backend and includes static file handling for CSS, JavaScript, and images.

## Features

- **Article Management**: Create, edit, and publish articles with titles, content, and images
- **User Authentication**: Built-in Django user system for authors
- **Responsive Design**: Bootstrap-based Persian template with mobile-friendly layout
- **Admin Panel**: Django admin interface for content management
- **Media Uploads**: Support for article images and static assets
- **Search Functionality**: Frontend search form (implementation pending)
- **Social Media Integration**: Links to Telegram, Twitter, Instagram, YouTube, and Aparat
- **Category System**: Sidebar categories for organizing content
- **Advertisement Support**: Built-in ad placement areas

## Technologies Used

- **Backend**: Django 5.2.8
- **Database**: PostgreSQL
- **Frontend**: HTML5, CSS3, Bootstrap, JavaScript, jQuery
- **Icons**: Font Awesome
- **Fonts**: Persian Vazir font

## Installation

### Prerequisites

- Python 3.8+
- PostgreSQL database
- pip package manager

### Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd NewApplication
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install django psycopg2-binary
   ```

4. **Configure the database**:
   - Create a PostgreSQL database
   - Update database credentials in `core/settings.py`:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': 'your_database_name',
             'USER': 'your_username',
             'PASSWORD': 'your_password',
             'HOST': 'localhost',
             'PORT': 5432
         }
     }
     ```

5. **Run migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser** (optional, for admin access):
   ```bash
   python manage.py createsuperuser
   ```

7. **Collect static files**:
   ```bash
   python manage.py collectstatic
   ```

## Usage

1. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

2. **Access the application**:
   - Homepage: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

3. **Create articles**:
   - Log in to the admin panel
   - Navigate to App > Articles
   - Add new articles with title, content, and images

## Project Structure

```
NewApplication/
├── core/                    # Main Django project settings
│   ├── settings.py         # Project configuration
│   ├── urls.py             # Main URL routing
│   └── wsgi.py             # WSGI configuration
├── App/                     # Blog application
│   ├── models.py           # Article model
│   ├── views.py            # Homepage view
│   ├── urls.py             # App URL routing
│   ├── admin.py            # Admin configuration
│   └── migrations/         # Database migrations
├── templates/              # HTML templates
│   ├── index.html          # Homepage template
│   └── ...                 # Other templates
├── static/                 # Static files (CSS, JS, images)
│   ├── css/
│   ├── js/
│   ├── img/
│   └── fonts/
├── convert_static.py       # Utility for static file conversion
├── manage.py               # Django management script
└── README.md               # This file
```

## Current Status

The project includes:
- ✅ Basic Django setup with PostgreSQL
- ✅ Article model with image upload
- ✅ Responsive Persian homepage template
- ✅ Admin panel integration
- ✅ Static file management

**Note**: The application is currently in development. Article detail views, search functionality, and user-facing article management are not yet implemented.

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and commit: `git commit -am 'Add feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For questions or support, please contact the development team.