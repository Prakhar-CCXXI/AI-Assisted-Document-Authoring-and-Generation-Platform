# How to Connect Your Database to the App

## Your Database Information

- **Username**: `postgres` (default)
- **Password**: `PostgreSQL1036`
- **Host**: `localhost` (default)
- **Port**: `5432` (default)
- **Database Name**: `docxbuilder` (needs to be created)

---

## Step 1: Create the Database

First, you need to create the database if it doesn't exist.

### Option A: Using psql (Command Line)

1. **Open Command Prompt or PowerShell**

2. **Connect to PostgreSQL:**
   ```bash
   psql -U postgres
   ```
   Enter password when prompted: `PostgreSQL1036`

3. **Create the database:**
   ```sql
   CREATE DATABASE docxbuilder;
   ```

4. **Verify it was created:**
   ```sql
   \l
   ```
   You should see `docxbuilder` in the list.

5. **Exit psql:**
   ```sql
   \q
   ```

### Option B: Using pgAdmin (GUI)

1. **Open pgAdmin** (if installed)

2. **Connect to PostgreSQL server:**
   - Right-click on "PostgreSQL" → "Connect Server"
   - Enter password: `PostgreSQL1036`

3. **Create database:**
   - Right-click on "Databases" → "Create" → "Database"
   - Name: `docxbuilder`
   - Click "Save"

---

## Step 2: Set Up Database Connection

You have **3 options** to connect your database:

### Option 1: Environment Variable (Recommended)

#### Windows PowerShell:
```powershell
$env:DATABASE_URL="postgresql+psycopg://postgres:PostgreSQL1036@localhost:5432/docxbuilder"
```

#### Windows Command Prompt:
```cmd
set DATABASE_URL=postgresql+psycopg://postgres:PostgreSQL1036@localhost:5432/docxbuilder
```

#### Make it Permanent (Windows):
1. Press `Win + R`, type `sysdm.cpl`, press Enter
2. Click "Environment Variables"
3. Under "User variables", click "New"
4. Variable name: `DATABASE_URL`
5. Variable value: `postgresql+psycopg://postgres:PostgreSQL1036@localhost:5432/docxbuilder`
6. Click "OK" on all dialogs

#### Mac/Linux:
```bash
export DATABASE_URL="postgresql+psycopg://postgres:PostgreSQL1036@localhost:5432/docxbuilder"
```

**To make it permanent**, add to `~/.bashrc` or `~/.zshrc`:
```bash
echo 'export DATABASE_URL="postgresql+psycopg://postgres:PostgreSQL1036@localhost:5432/docxbuilder"' >> ~/.bashrc
source ~/.bashrc
```

### Option 2: Create .env File

1. **Create a file named `.env`** in your project root folder

2. **Add this line:**
   ```
   DATABASE_URL=postgresql+psycopg://postgres:PostgreSQL1036@localhost:5432/docxbuilder
   ```

3. **The app will automatically read it** (python-dotenv is installed)

### Option 3: Direct in app.py (Not Recommended)

The app already has a default connection string in `app.py` (line 27):
```python
DATABASE_URL = 'postgresql+psycopg://postgres:PostgreSQL1036@localhost:5432/docxbuilder'
```

**This should work if the database exists!** Just make sure the database `docxbuilder` is created.

---

## Step 3: Verify PostgreSQL is Running

### Windows:
1. Press `Win + R`, type `services.msc`, press Enter
2. Look for "postgresql" service
3. Make sure it's "Running"
4. If not, right-click → "Start"

### Mac:
```bash
brew services list
# Look for postgresql
```

### Linux:
```bash
sudo systemctl status postgresql
# Or
sudo service postgresql status
```

---

## Step 4: Test the Connection

### Method 1: Run the App

```bash
python app.py
```

If connection is successful, you'll see:
```
 * Running on http://127.0.0.1:5000
```

If there's an error, check the error message.

### Method 2: Initialize Database Tables

```bash
python init_db.py
```

**Expected output:**
```
Creating database tables...
✅ Database tables created successfully!

Tables created:
  - User
  - Content
  - Project
  - Section
  - Revision
  - Feedback
  - Comment
```

### Method 3: Test Connection with Python

Create a test file `test_db.py`:
```python
import os
from app import app, db

with app.app_context():
    try:
        # Try to connect
        db.engine.connect()
        print("✅ Database connection successful!")
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
```

Run:
```bash
python test_db.py
```

---

## Complete Setup Example

### Windows PowerShell:

```powershell
# 1. Set environment variable
$env:DATABASE_URL="postgresql+psycopg://postgres:PostgreSQL1036@localhost:5432/docxbuilder"

# 2. Create database (if not exists)
psql -U postgres -c "CREATE DATABASE docxbuilder;"

# 3. Initialize tables
python init_db.py

# 4. Run the app
python app.py
```

### Windows Command Prompt:

```cmd
REM 1. Set environment variable
set DATABASE_URL=postgresql+psycopg://postgres:PostgreSQL1036@localhost:5432/docxbuilder

REM 2. Create database (if not exists)
psql -U postgres -c "CREATE DATABASE docxbuilder;"

REM 3. Initialize tables
python init_db.py

REM 4. Run the app
python app.py
```

---

## Connection String Format

```
postgresql+psycopg://username:password@host:port/database_name
```

**Your connection string:**
```
postgresql+psycopg://postgres:PostgreSQL1036@localhost:5432/docxbuilder
```

**Breakdown:**
- `postgresql+psycopg://` - Protocol (psycopg3 driver)
- `postgres` - Username
- `PostgreSQL1036` - Password
- `localhost` - Host
- `5432` - Port
- `docxbuilder` - Database name

---

## Troubleshooting

### Error: "database 'docxbuilder' does not exist"

**Solution:** Create the database first (see Step 1)

```sql
psql -U postgres
CREATE DATABASE docxbuilder;
\q
```

### Error: "password authentication failed"

**Solution:** 
- Verify password is correct: `PostgreSQL1036`
- Check if username is `postgres` (default)
- Try resetting PostgreSQL password

### Error: "could not connect to server"

**Solution:**
- Make sure PostgreSQL service is running
- Check if port 5432 is correct
- Verify host is `localhost`

### Error: "psycopg module not found"

**Solution:**
```bash
pip install psycopg[binary]
# Or
pip install -r requirements.txt
```

### Error: "connection refused"

**Solution:**
- Start PostgreSQL service
- Check firewall settings
- Verify PostgreSQL is listening on port 5432

### Error: "relation does not exist"

**Solution:** Initialize database tables:
```bash
python init_db.py
```

---

## Quick Checklist

- [ ] PostgreSQL is installed
- [ ] PostgreSQL service is running
- [ ] Database `docxbuilder` is created
- [ ] Environment variable `DATABASE_URL` is set (or .env file created)
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Database tables initialized (`python init_db.py`)
- [ ] App runs without connection errors

---

## Next Steps After Connection

1. **Initialize Database Tables:**
   ```bash
   python init_db.py
   ```

2. **Run the Application:**
   ```bash
   python app.py
   ```

3. **Access the App:**
   - Open browser: http://localhost:5000
   - Register a new user
   - Start using the app!

---

## Summary

**Your Database Connection String:**
```
postgresql+psycopg://postgres:PostgreSQL1036@localhost:5432/docxbuilder
```

**Quick Setup:**
1. Create database: `CREATE DATABASE docxbuilder;`
2. Set environment variable or create .env file
3. Run: `python init_db.py`
4. Run: `python app.py`

**That's it! Your database is now connected.** 🎉

