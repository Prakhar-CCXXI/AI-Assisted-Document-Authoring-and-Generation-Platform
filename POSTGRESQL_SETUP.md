# PostgreSQL Database Setup Guide

This guide will help you set up PostgreSQL for the Flask application.

## Quick Start - Verify Connection

After setting up PostgreSQL, verify your connection by running:

```bash
python verify_postgresql_connection.py
```

**Your Database Credentials:**
- Username: `admin`
- Password: `1234`
- Host: `localhost`
- Port: `5432`
- Database: `docxbuilder`

## Prerequisites

1. **Install PostgreSQL** (if not already installed)
   - Windows: Download from https://www.postgresql.org/download/windows/
   - Mac: `brew install postgresql` or download from https://www.postgresql.org/download/macos/
   - Linux: `sudo apt-get install postgresql` (Ubuntu/Debian)

2. **Create a Database**
   - Open PostgreSQL command line or pgAdmin
   - Create a new database: `docxbuilder`

## Configuration Options

### Option 1: Environment Variable (Recommended)

Set the `DATABASE_URL` environment variable with your PostgreSQL credentials.

#### Windows PowerShell:
```powershell
$env:DATABASE_URL="postgresql+psycopg://postgres:PostgreSQL1036@localhost:5432/docxbuilder"
```

#### Windows Command Prompt:
```cmd
set DATABASE_URL=postgresql+psycopg://postgres:PostgreSQL1036@localhost:5432/docxbuilder
```

#### Linux/Mac:
```bash
export DATABASE_URL="postgresql+psycopg://postgres:PostgreSQL1036@localhost:5432/docxbuilder"
```

**To make it permanent:**
- Windows: Add it to System Environment Variables
- Linux/Mac: Add to `~/.bashrc` or `~/.zshrc`

### Option 2: Direct Configuration in app.py

If you prefer, you can directly update the `DATABASE_URL` in `app.py`:

```python
DATABASE_URL = 'postgresql+psycopg://postgres:PostgreSQL1036@localhost:5432/docxbuilder'
```

**Note:** The app already has this as the default connection string, so if you create the `docxbuilder` database, it will work automatically.

## Connection String Format

```
postgresql+psycopg://username:password@host:port/database_name
```

**Components:**
- `postgresql+psycopg://` - Protocol (psycopg3 driver - required for this app)
- `username`: Your PostgreSQL username (default is `postgres`)
- `password`: Your PostgreSQL password (`PostgreSQL1036`)
- `host`: Database host (usually `localhost` for local, or IP address for remote)
- `port`: PostgreSQL port (default is `5432`)
- `database_name`: Name of your database (`docxbuilder`)

**Your Connection String:**
```
postgresql+psycopg://postgres:PostgreSQL1036@localhost:5432/docxbuilder
```

## Example Connection Strings

### Your Local Database (Default):
```
postgresql+psycopg://postgres:PostgreSQL1036@localhost:5432/docxbuilder
```

### Remote Database:
```
postgresql+psycopg://postgres:PostgreSQL1036@192.168.1.100:5432/docxbuilder
```

### With Custom Port:
```
postgresql+psycopg://postgres:PostgreSQL1036@localhost:5433/docxbuilder
```

**Important:** Always use `postgresql+psycopg://` (not `postgresql://`) because this app uses the psycopg3 driver.

## Creating the Database

1. **Using psql (Command Line):**
   ```bash
   psql -U postgres
   ```
   Enter password when prompted: `PostgreSQL1036`
   
   Then run:
   ```sql
   CREATE DATABASE docxbuilder;
   \q
   ```

2. **Using pgAdmin:**
   - Right-click on "Databases" → "Create" → "Database"
   - Enter database name: `docxbuilder`
   - Click "Save"

## Installing Dependencies

After setting up PostgreSQL, install the required Python package:

```bash
pip install -r requirements.txt
```

This will install `psycopg[binary]` (psycopg3) which is the PostgreSQL adapter for Python used by this application.

## Testing the Connection

### Method 1: Use the Verification Script (Recommended)

Run the dedicated verification script to check your database connection:

```bash
python 


```

This script will check:
- PostgreSQL service status
- Database connection
- Database existence
- Required tables
- Basic query functionality

**Expected output on success:**
```
✅ Database connection is working correctly!
✅ All required tables are present!
🎉 Your PostgreSQL database is fully configured and ready to use!
```

### Method 2: Start Flask Application

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



### Method 3: Initialize Database Tables

Run the initialization script:
```bash
python init_db.py
```

This will create all required tables and verify the connection.

## Database Tables

The application will create the following tables automatically:

1. **User** - Stores user accounts (username, email, password_hash)
2. **Content** - Stores pasted content
3. **Project** - Stores AI-powered projects
4. **Section** - Stores document sections/slides
5. **Revision** - Tracks content revisions
6. **Feedback** - Stores user feedback (like/dislike)
7. **Comment** - Stores user comments

**To initialize tables manually:**
```bash
python init_db.py
```

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

### Module Not Found (psycopg)
- Run: `pip install psycopg[binary]`
- Or: `pip install -r requirements.txt`

## Security Notes

- **Never commit database credentials to version control**
- Use environment variables for production
- Consider using a `.env` file with `python-dotenv` for local development
- Use strong passwords for your PostgreSQL user



