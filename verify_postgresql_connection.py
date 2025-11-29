"""
PostgreSQL Connection Verification Script

This script verifies the PostgreSQL database connection using default PostgreSQL credentials
except for the password.

Default PostgreSQL credentials:
- Username: postgres (default superuser)
- Password: PostgreSQL1036 (custom - only non-default credential)
- Host: localhost (default)
- Port: 5432 (default PostgreSQL port)
- Database: docxbuilder (application database)

It checks:
- Database connection
- Database existence
- Required tables
- Basic query functionality

Usage: python verify_postgresql_connection.py
"""

import os
import sys
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

# Database configuration
# Using default PostgreSQL credentials except for the password
DB_USERNAME = "postgres"  # Default PostgreSQL superuser
DB_PASSWORD = "PostgreSQL1036"  # Custom password (non-default)
DB_HOST = "localhost"  # Default localhost
DB_PORT = "5432"  # Default PostgreSQL port
DB_NAME = "docxbuilder"  # Application database name

# Connection string using psycopg3 driver
CONNECTION_STRING = f"postgresql+psycopg://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Try to use environment variable if available
DATABASE_URL = os.getenv('DATABASE_URL', CONNECTION_STRING)


def print_header(text):
    """Print a formatted header"""
    print("\n" + "=" * 60)
    print(f"  {text}")
    print("=" * 60)


def print_success(text):
    """Print success message"""
    print(f"✅ {text}")


def print_error(text):
    """Print error message"""
    print(f"❌ {text}")


def print_info(text):
    """Print info message"""
    print(f"ℹ️  {text}")


def check_postgresql_service():
    """Check if PostgreSQL service is running (Windows specific)"""
    print_header("Checking PostgreSQL Service")
    
    try:
        import subprocess
        
        # Check if running on Windows
        if sys.platform == "win32":
            result = subprocess.run(
                ['sc', 'query', 'postgresql'],
                capture_output=True,
                text=True,
                timeout=5
            )
            
            if 'RUNNING' in result.stdout:
                print_success("PostgreSQL service is running")
                return True
            elif 'STOPPED' in result.stdout:
                print_error("PostgreSQL service is stopped")
                print_info("Please start the PostgreSQL service from Windows Services")
                return False
            else:
                print_info("Could not determine PostgreSQL service status")
                print_info("Trying to connect anyway...")
                return None
        else:
            # Linux/Mac - check via systemctl or service command
            print_info("Running on non-Windows system - skipping service check")
            print_info("Trying to connect...")
            return None
            
    except Exception as e:
        print_info(f"Could not check service status: {e}")
        print_info("Trying to connect anyway...")
        return None


def verify_connection():
    """Verify database connection"""
    print_header("Testing Database Connection")
    
    print_info(f"Connection String: postgresql+psycopg://{DB_USERNAME}:***@{DB_HOST}:{DB_PORT}/{DB_NAME}")
    print_info("Attempting to connect...")
    
    try:
        engine = create_engine(DATABASE_URL, echo=False)
        
        # Test connection
        with engine.connect() as connection:
            print_success("Successfully connected to PostgreSQL!")
            
            # Get PostgreSQL version
            result = connection.execute(text("SELECT version();"))
            version = result.fetchone()[0]
            print_info(f"PostgreSQL Version: {version.split(',')[0]}")
            
            return True, engine
            
    except ImportError as e:
        print_error("psycopg module not found!")
        print_info("Please install it using: pip install psycopg[binary]")
        print_info("Or run: pip install -r requirements.txt")
        return False, None
        
    except SQLAlchemyError as e:
        error_msg = str(e)
        
        if "password authentication failed" in error_msg.lower():
            print_error("Authentication failed!")
            print_info(f"Username: {DB_USERNAME}")
            print_info(f"Password: {DB_PASSWORD}")
            print_info("Please verify your credentials in the script or environment variable")
            
        elif "database" in error_msg.lower() and "does not exist" in error_msg.lower():
            print_error("Database does not exist!")
            print_info(f"Database '{DB_NAME}' not found")
            print_info(f"Please create it using: CREATE DATABASE {DB_NAME};")
            
        elif "could not connect" in error_msg.lower() or "connection refused" in error_msg.lower():
            print_error("Connection refused!")
            print_info("PostgreSQL service may not be running")
            print_info(f"Host: {DB_HOST}, Port: {DB_PORT}")
            print_info("Please ensure PostgreSQL is running and accessible")
            
        else:
            print_error(f"Connection failed: {error_msg}")
            
        return False, None
        
    except Exception as e:
        print_error(f"Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return False, None


def check_database_exists(engine):
    """Check if the database exists"""
    print_header("Checking Database")
    
    try:
        with engine.connect() as connection:
            # Check if we can query the database
            result = connection.execute(text("SELECT current_database();"))
            db_name = result.fetchone()[0]
            
            print_success(f"Connected to database: {db_name}")
            
            if db_name == DB_NAME:
                print_success(f"Database name matches expected: {DB_NAME}")
            else:
                print_info(f"Connected to '{db_name}' instead of '{DB_NAME}'")
            
            return True
            
    except Exception as e:
        print_error(f"Error checking database: {e}")
        return False


def list_tables(engine):
    """List all tables in the database"""
    print_header("Checking Database Tables")
    
    try:
        with engine.connect() as connection:
            # Get list of tables
            result = connection.execute(text("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public'
                ORDER BY table_name;
            """))
            
            tables = [row[0] for row in result.fetchall()]
            
            if tables:
                print_success(f"Found {len(tables)} table(s):")
                for table in tables:
                    print_info(f"  - {table}")
            else:
                print_info("No tables found in the database")
                print_info("Run 'python init_db.py' to create tables")
            
            return tables
            
    except Exception as e:
        print_error(f"Error listing tables: {e}")
        return []


def check_required_tables(tables):
    """Check if required tables exist"""
    print_header("Checking Required Tables")
    
    required_tables = [
        'user',
        'content',
        'project',
        'section',
        'revision',
        'feedback',
        'comment'
    ]
    
    missing_tables = []
    found_tables = []
    
    for table in required_tables:
        if table in [t.lower() for t in tables]:
            found_tables.append(table)
            print_success(f"Table '{table}' exists")
        else:
            missing_tables.append(table)
            print_error(f"Table '{table}' not found")
    
    if not missing_tables:
        print_success("All required tables are present!")
        return True
    else:
        print_info(f"Missing {len(missing_tables)} table(s). Run 'python init_db.py' to create them.")
        return False


def test_query(engine):
    """Test a simple query"""
    print_header("Testing Database Query")
    
    try:
        with engine.connect() as connection:
            # Execute a simple query
            result = connection.execute(text("SELECT 1 as test_value;"))
            value = result.fetchone()[0]
            
            if value == 1:
                print_success("Query executed successfully!")
                print_info("Database is ready to use")
                return True
            else:
                print_error("Query returned unexpected result")
                return False
                
    except Exception as e:
        print_error(f"Query test failed: {e}")
        return False


def main():
    """Main verification function"""
    print("\n" + "=" * 60)
    print("  PostgreSQL Connection Verification")
    print("=" * 60)
    
    print_info("Configuration (using default PostgreSQL credentials):")
    print_info(f"  Host: {DB_HOST} (default)")
    print_info(f"  Port: {DB_PORT} (default)")
    print_info(f"  Username: {DB_USERNAME} (default)")
    print_info(f"  Password: *** (custom)")
    print_info(f"  Database: {DB_NAME}")
    
    if os.getenv('DATABASE_URL'):
        print_info("  Using DATABASE_URL from environment variable")
    else:
        print_info("  Using default connection string")
    
    # Check PostgreSQL service (Windows)
    if sys.platform == "win32":
        check_postgresql_service()
    
    # Verify connection
    connection_success, engine = verify_connection()
    
    if not connection_success:
        print("\n" + "=" * 60)
        print_error("Connection verification failed!")
        print_info("Please check the error messages above and fix the issues.")
        print("=" * 60)
        sys.exit(1)
    
    # Check database
    if not check_database_exists(engine):
        print_error("Database check failed!")
        sys.exit(1)
    
    # List tables
    tables = list_tables(engine)
    
    # Check required tables
    tables_ok = check_required_tables(tables)
    
    # Test query
    query_ok = test_query(engine)
    
    # Final summary
    print_header("Verification Summary")
    
    if connection_success and query_ok:
        print_success("✅ Database connection is working correctly!")
        
        if tables_ok:
            print_success("✅ All required tables are present!")
            print("\n🎉 Your PostgreSQL database is fully configured and ready to use!")
        else:
            print_info("⚠️  Some tables are missing. Run 'python init_db.py' to create them.")
        
        print("\nNext steps:")
        print("  1. If tables are missing, run: python init_db.py")
        print("  2. Start your Flask application: python app.py")
        print("  3. Access the app at: http://localhost:5000")
    else:
        print_error("Some verification checks failed. Please review the errors above.")
        sys.exit(1)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Verification cancelled by user")
        sys.exit(1)
    except Exception as e:
        print_error(f"Unexpected error during verification: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

