# PostgreSQL Database Setup Guide

This guide will help you set up PostgreSQL for the Flask application.

## Prerequisites

1. **Install PostgreSQL** (if not already installed)
   - Windows: Download from https://www.postgresql.org/download/windows/
   - Mac: `brew install postgresql` or download from https://www.postgresql.org/download/macos/
   - Linux: `sudo apt-get install postgresql` (Ubuntu/Debian)

2. **Create a Database**
   - Open PostgreSQL command line or pgAdmin
   - Create a new database (e.g., `oceanaidb`)

## Configuration Options

### Option 1: Environment Variable (Recommended)

Set the `DATABASE_URL` environment variable with your PostgreSQL credentials.

#### Windows PowerShell:
```powershell
$env:DATABASE_URL="postgresql://username:password@localhost:5432/oceanaidb"
```

#### Windows Command Prompt:
```cmd
set DATABASE_URL=postgresql://username:password@localhost:5432/oceanaidb
```

#### Linux/Mac:
```bash
export DATABASE_URL="postgresql://username:password@localhost:5432/oceanaidb"
```

**To make it permanent:**
- Windows: Add it to System Environment Variables
- Linux/Mac: Add to `~/.bashrc` or `~/.zshrc`

### Option 2: Direct Configuration in app.py

If you prefer, you can directly update the `DATABASE_URL` in `app.py`:

```python
DATABASE_URL = 'postgresql://your_username:your_password@localhost:5432/your_database'
```

## Connection String Format

```
postgresql://username:password@host:port/database_name
```

**Components:**
- `username`: Your PostgreSQL username (default is often `postgres`)
- `password`: Your PostgreSQL password
- `host`: Database host (usually `localhost` for local, or IP address for remote)
- `port`: PostgreSQL port (default is `5432`)
- `database_name`: Name of your database (e.g., `oceanaidb`)

## Example Connection Strings

### Local Database:
```
postgresql://postgres:mypassword@localhost:5432/oceanaidb
```

### Remote Database:
```
postgresql://user:pass@192.168.1.100:5432/mydb
```

### With Custom Port:
```
postgresql://postgres:password@localhost:5433/oceanaidb
```

## Creating the Database

1. **Using psql (Command Line):**
   ```bash
   psql -U postgres
   CREATE DATABASE oceanaidb;
   \q
   ```

2. **Using pgAdmin:**
   - Right-click on "Databases" → "Create" → "Database"
   - Enter database name: `oceanaidb`
   - Click "Save"

## Installing Dependencies

After setting up PostgreSQL, install the required Python package:

```bash
pip install -r requirements.txt
```

This will install `psycopg2-binary` which is the PostgreSQL adapter for Python.

## Testing the Connection

1. Start your Flask application:
   ```bash
   python app.py
   ```

2. The application will automatically create the required tables on first run.

3. If you see any connection errors, verify:
   - PostgreSQL service is running
   - Database exists
   - Credentials are correct
   - Port is accessible (default 5432)

## Database Tables

The application will create two tables:

1. **User** - Stores user accounts (username, email, password_hash)
2. **Content** - Stores pasted content with:
   - `content_id` (Primary Key, Auto-increment)
   - `username` (String)
   - `password` (String - stores password hash)
   - `content_pasted` (Text)
   - `created_at` (DateTime)

## Troubleshooting

### Connection Refused
- Ensure PostgreSQL service is running
- Check if port 5432 is open
- Verify host address

### Authentication Failed
- Double-check username and password
- Ensure user has access to the database

### Database Does Not Exist
- Create the database first (see "Creating the Database" above)

### Module Not Found (psycopg2)
- Run: `pip install psycopg2-binary`

## Security Notes

- **Never commit database credentials to version control**
- Use environment variables for production
- Consider using a `.env` file with `python-dotenv` for local development
- Use strong passwords for your PostgreSQL user



