"""
Delete All Data from docxbuilder Database

This script will DELETE ALL DATA from all tables in the docxbuilder database.
This includes:
- All Users
- All Content entries
- All Projects
- All Sections
- All Revisions
- All Feedback
- All Comments

⚠️  WARNING: This action CANNOT be undone!

The script will:
1. Show current data counts
2. Ask for confirmation
3. Delete all data from all tables
4. Preserve table structures (tables will remain, just empty)

Usage: python delete_all_database_data.py
"""

import os
from sqlalchemy import text
from app import app, db, User, Content, Project, Section, Revision, Feedback, Comment


def print_header(text):
    """Print a formatted header"""
    print("\n" + "=" * 70)
    print(f"  {text}")
    print("=" * 70)


def print_success(text):
    """Print success message"""
    print(f"✅ {text}")


def print_error(text):
    """Print error message"""
    print(f"❌ {text}")


def print_info(text):
    """Print info message"""
    print(f"ℹ️  {text}")


def print_warning(text):
    """Print warning message"""
    print(f"⚠️  {text}")


def count_all_records():
    """Count all records in all tables"""
    counts = {}
    try:
        counts['users'] = User.query.count()
        counts['content'] = Content.query.count()
        counts['projects'] = Project.query.count()
        counts['sections'] = Section.query.count()
        counts['revisions'] = Revision.query.count()
        counts['feedback'] = Feedback.query.count()
        counts['comments'] = Comment.query.count()
    except Exception as e:
        print_error(f"Error counting records: {e}")
        return None
    return counts


def show_current_data(counts):
    """Display current data counts"""
    print_header("Current Database Contents")
    
    print_info("Record counts:")
    print(f"  👥 Users: {counts['users']}")
    print(f"  📄 Content entries: {counts['content']}")
    print(f"  📁 Projects: {counts['projects']}")
    print(f"  📝 Sections: {counts['sections']}")
    print(f"  🔄 Revisions: {counts['revisions']}")
    print(f"  👍 Feedback entries: {counts['feedback']}")
    print(f"  💬 Comments: {counts['comments']}")
    
    total = sum(counts.values())
    print(f"\n  📊 TOTAL RECORDS: {total}")
    
    return total


def delete_all_data_sql_method():
    """Delete all data using SQL TRUNCATE (faster method)"""
    print_header("Deleting All Data Using SQL TRUNCATE")
    
    # Order matters due to foreign key constraints
    # We need to disable foreign key checks temporarily or delete in correct order
    tables_to_truncate = [
        'comment',      # Delete first (references section, project, user)
        'feedback',     # Delete second (references section, project, user)
        'revision',     # Delete third (references section, project, user)
        'section',      # Delete fourth (references project)
        'project',      # Delete fifth
        'content',      # Delete sixth (no foreign keys)
        'user'          # Delete last (may be referenced)
    ]
    
    deleted_counts = {}
    
    try:
        with db.engine.connect() as connection:
            # For PostgreSQL, we can use TRUNCATE CASCADE to handle foreign keys
            for table in tables_to_truncate:
                try:
                    print_info(f"Truncating table: {table}...")
                    
                    # Use TRUNCATE CASCADE to handle foreign key constraints
                    result = connection.execute(text(f'TRUNCATE TABLE "{table}" CASCADE'))
                    connection.commit()
                    
                    # Count before deletion for reporting
                    if table == 'user':
                        count = User.query.count()
                    elif table == 'content':
                        count = Content.query.count()
                    elif table == 'project':
                        count = Project.query.count()
                    elif table == 'section':
                        count = Section.query.count()
                    elif table == 'revision':
                        count = Revision.query.count()
                    elif table == 'feedback':
                        count = Feedback.query.count()
                    elif table == 'comment':
                        count = Comment.query.count()
                    else:
                        count = 0
                    
                    deleted_counts[table] = count
                    print_success(f"  ✅ Truncated {table} table")
                    
                except Exception as e:
                    print_error(f"  ❌ Error truncating {table}: {e}")
                    # Try to continue with other tables
                    connection.rollback()
                    
            return deleted_counts
            
    except Exception as e:
        print_error(f"Error during SQL truncate: {e}")
        raise


def delete_all_data_orm_method():
    """Delete all data using SQLAlchemy ORM (safer, respects relationships)"""
    print_header("Deleting All Data Using ORM")
    
    deleted_counts = {}
    
    try:
        # Delete in order to respect foreign key constraints
        # Start with child tables that reference other tables
        
        print_info("Deleting Comments...")
        deleted_counts['comments'] = Comment.query.delete()
        db.session.commit()
        print_success(f"  ✅ Deleted {deleted_counts['comments']} comments")
        
        print_info("Deleting Feedback...")
        deleted_counts['feedback'] = Feedback.query.delete()
        db.session.commit()
        print_success(f"  ✅ Deleted {deleted_counts['feedback']} feedback entries")
        
        print_info("Deleting Revisions...")
        deleted_counts['revisions'] = Revision.query.delete()
        db.session.commit()
        print_success(f"  ✅ Deleted {deleted_counts['revisions']} revisions")
        
        print_info("Deleting Sections...")
        deleted_counts['sections'] = Section.query.delete()
        db.session.commit()
        print_success(f"  ✅ Deleted {deleted_counts['sections']} sections")
        
        print_info("Deleting Projects...")
        deleted_counts['projects'] = Project.query.delete()
        db.session.commit()
        print_success(f"  ✅ Deleted {deleted_counts['projects']} projects")
        
        print_info("Deleting Content entries...")
        deleted_counts['content'] = Content.query.delete()
        db.session.commit()
        print_success(f"  ✅ Deleted {deleted_counts['content']} content entries")
        
        print_info("Deleting Users...")
        deleted_counts['users'] = User.query.delete()
        db.session.commit()
        print_success(f"  ✅ Deleted {deleted_counts['users']} users")
        
        return deleted_counts
        
    except Exception as e:
        db.session.rollback()
        print_error(f"Error during ORM deletion: {e}")
        raise


def delete_all_data():
    """Main function to delete all data from the database"""
    print_header("⚠️  DELETE ALL DATABASE DATA")
    
    print_warning("This operation will DELETE ALL DATA from the docxbuilder database!")
    print()
    print("This includes:")
    print("  - All user accounts (Users)")
    print("  - All content entries (Content)")
    print("  - All AI projects (Projects)")
    print("  - All document sections (Sections)")
    print("  - All revision history (Revisions)")
    print("  - All user feedback (Feedback)")
    print("  - All user comments (Comments)")
    print()
    print_warning("⚠️  THIS ACTION CANNOT BE UNDONE! ⚠️")
    print()
    print_info("Note: Table structures will be preserved (tables will remain, just empty)")
    print()
    
    # Ensure we start with a clean transaction state
    try:
        db.session.rollback()
    except:
        pass
    
    # Count current records
    print_info("Counting current records...")
    counts = count_all_records()
    
    if counts is None:
        print_error("Could not count records. Aborting.")
        return
    
    total_records = show_current_data(counts)
    
    if total_records == 0:
        print_success("\n✅ Database is already empty. Nothing to delete.")
        return
    
    # Confirmation
    print_header("CONFIRMATION REQUIRED")
    print_warning("Type 'DELETE ALL DATA' (exactly) to confirm deletion:")
    response = input("> ").strip()
    print()
    
    if response != 'DELETE ALL DATA':
        print_error("❌ Operation cancelled. No data was deleted.")
        print_info("You must type exactly 'DELETE ALL DATA' (without quotes) to confirm.")
        return
    
    print()
    print_header("STARTING DELETION PROCESS")
    print()
    
    # Ask user which method to use
    print_info("Choose deletion method:")
    print("  1. SQL TRUNCATE (Faster, uses raw SQL)")
    print("  2. ORM Delete (Safer, uses SQLAlchemy ORM)")
    print()
    
    try:
        choice = input("Enter choice (1 or 2, default is 1): ").strip()
        if not choice:
            choice = '1'
    except KeyboardInterrupt:
        print_error("\n❌ Operation cancelled by user.")
        return
    
    deleted_counts = {}
    
    try:
        if choice == '2':
            # Use ORM method
            deleted_counts = delete_all_data_orm_method()
        else:
            # Use SQL TRUNCATE method (default, faster)
            deleted_counts = delete_all_data_sql_method()
        
        # Verify deletion
        print()
        print_header("Verifying Deletion")
        print_info("Counting remaining records...")
        
        final_counts = count_all_records()
        if final_counts:
            remaining_total = sum(final_counts.values())
            if remaining_total == 0:
                print_success("✅ All data deleted successfully!")
            else:
                print_warning(f"⚠️  Warning: {remaining_total} records still remain")
                print_info("Final counts:")
                for table, count in final_counts.items():
                    if count > 0:
                        print(f"  - {table}: {count}")
        
        # Summary
        print()
        print_header("✅ DELETION COMPLETED SUCCESSFULLY")
        print()
        print("Summary of deleted data:")
        if 'users' in deleted_counts or 'user' in deleted_counts:
            count = deleted_counts.get('users', deleted_counts.get('user', 0))
            print(f"  👥 Users: {count}")
        if 'content' in deleted_counts:
            print(f"  📄 Content entries: {deleted_counts['content']}")
        if 'projects' in deleted_counts or 'project' in deleted_counts:
            count = deleted_counts.get('projects', deleted_counts.get('project', 0))
            print(f"  📁 Projects: {count}")
        if 'sections' in deleted_counts or 'section' in deleted_counts:
            count = deleted_counts.get('sections', deleted_counts.get('section', 0))
            print(f"  📝 Sections: {count}")
        if 'revisions' in deleted_counts or 'revision' in deleted_counts:
            count = deleted_counts.get('revisions', deleted_counts.get('revision', 0))
            print(f"  🔄 Revisions: {count}")
        if 'feedback' in deleted_counts:
            print(f"  👍 Feedback entries: {deleted_counts['feedback']}")
        if 'comments' in deleted_counts or 'comment' in deleted_counts:
            count = deleted_counts.get('comments', deleted_counts.get('comment', 0))
            print(f"  💬 Comments: {count}")
        
        print()
        print_success("Database tables are now empty but still exist.")
        print_info("You can start fresh by creating new users, projects, and content.")
        print_info("To recreate tables, run: python init_db.py")
        print()
        
    except Exception as e:
        db.session.rollback()
        print()
        print_header("❌ ERROR: DELETION FAILED")
        print_error(f"Error: {str(e)}")
        print()
        print_info("The database transaction has been rolled back.")
        print_info("No data was deleted. Please check the error above and try again.")
        print()
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    try:
        with app.app_context():
            delete_all_data()
    except KeyboardInterrupt:
        print("\n\n⚠️  Operation cancelled by user.")
        print("No data was deleted.")
    except Exception as e:
        print_error(f"\n❌ Fatal error: {e}")
        import traceback
        traceback.print_exc()

