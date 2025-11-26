"""
Database initialization script
Run this script to create all database tables
Usage: python init_db.py
"""

import os
from app import app, db

# You can set DATABASE_URL here or use environment variable
# DATABASE_URL = os.getenv('DATABASE_URL')

def init_database():
    """Initialize database tables"""
    with app.app_context():
        try:
            print("Creating database tables...")
            db.create_all()
            print("✅ Database tables created successfully!")
            print("\nTables created:")
            print("  - User")
            print("  - Content")
            print("  - Project")
            print("  - Section")
            print("  - Revision")
            print("  - Feedback")
            print("  - Comment")
        except Exception as e:
            print(f"❌ Error creating tables: {e}")
            import traceback
            traceback.print_exc()

if __name__ == '__main__':
    init_database()

