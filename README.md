# Flask Authentication Web App

A secure web application built with Flask that provides user registration, login, and authentication functionality.

## Features

- ✅ User Registration with validation
- ✅ Secure Login with password hashing
- ✅ Session-based authentication
- ✅ Protected routes (dashboard)
- ✅ Modern, responsive UI
- ✅ Flash messages for user feedback
- ✅ PostgreSQL database for user and content storage
- ✅ Content submission with text paste functionality
- ✅ Content storage with username, password, and content tracking

## Installation

1. **Clone or navigate to the project directory:**
   ```bash
   cd OceanAI
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up PostgreSQL Database:**
   - See `POSTGRESQL_SETUP.md` for detailed instructions
   - Set the `DATABASE_URL` environment variable with your PostgreSQL credentials
   - Format: `postgresql://username:password@host:port/database_name`
   - Example: `postgresql://postgres:mypassword@localhost:5432/oceanaidb`

## Running the Application

1. **Start the Flask server:**
   ```bash
   python app.py
   ```

2. **Open your browser and navigate to:**
   ```
   http://localhost:5000
   ```

## Usage

### Register a New User
1. Click on "Register here" or navigate to `/register`
2. Fill in:
   - Username (must be unique)
   - Email (must be unique)
   - Password (minimum 6 characters)
   - Confirm Password
3. Click "Register"

### Login
1. Navigate to `/login` or the home page
2. Enter your username and password
3. Click "Login"
4. You'll be redirected to the dashboard upon successful login

### Submit Content
1. Click "Upload Content" on the dashboard
2. A dialog will open automatically with a personalized greeting
3. Paste your text in the text area
4. Click "Submit" to save the content to the database

### Logout
1. Click the "Logout" button on the dashboard
2. You'll be logged out and redirected to the login page

## Project Structure

```
OceanAI/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── POSTGRESQL_SETUP.md   # PostgreSQL setup guide
├── config_example.py     # Database configuration example
└── templates/
    ├── base.html         # Base template with styling
    ├── login.html        # Login page
    ├── register.html     # Registration page
    ├── dashboard.html    # Protected dashboard page
    └── upload.html       # Content upload page with dialog
```

## Security Features

- Passwords are hashed using Werkzeug's secure password hashing
- Session-based authentication
- Protected routes using decorators
- Input validation
- SQL injection protection (via SQLAlchemy ORM)

## Technologies Used

- **Flask** - Web framework
- **Flask-SQLAlchemy** - Database ORM
- **Werkzeug** - Password hashing and security utilities
- **PostgreSQL** - Production-ready database
- **psycopg2** - PostgreSQL adapter for Python

## Database Schema

### User Table
- `id` (Primary Key)
- `username` (Unique)
- `email` (Unique)
- `password_hash` (Hashed password)

### Content Table
- `content_id` (Primary Key, Auto-increment)
- `username` (String)
- `password` (String - stores password hash)
- `content_pasted` (Text)
- `created_at` (DateTime)

## Notes

- **PostgreSQL Setup Required**: You must configure PostgreSQL before running the app
- See `POSTGRESQL_SETUP.md` for detailed database setup instructions
- The database tables will be created automatically on first run
- The secret key is randomly generated each time the app starts (for production, use a fixed secret key)
- For production, consider:
  - Setting a fixed SECRET_KEY in environment variables
  - Using HTTPS
  - Adding rate limiting
  - Implementing password reset functionality
  - Regular database backups

## License

This project is open source and available for educational purposes.

