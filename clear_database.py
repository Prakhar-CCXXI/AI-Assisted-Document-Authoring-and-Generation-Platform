"""
WARNING: This script will DELETE ALL DATA from all database tables.
This includes:
- All Users
- All Content entries
- All Projects
- All Sections
- All Revisions
- All Feedback

This action CANNOT be undone!

Run this script only if you want to completely clear your database.
"""

from app import app, db, User, Content, Project, Section, Revision, Feedback, Comment

def clear_all_data():
    """Delete all data from all tables"""
    with app.app_context():
        print("=" * 70)
        print("⚠️  WARNING: DATABASE CLEARING OPERATION")
        print("=" * 70)
        print()
        print("This will DELETE ALL DATA from the following tables:")
        print("  - User (all user accounts)")
        print("  - Content (all pasted content)")
        print("  - Project (all AI projects)")
        print("  - Section (all document sections)")
        print("  - Revision (all content revisions)")
        print("  - Feedback (all user feedback)")
        print("  - Comment (all user comments)")
        print()
        
        # Ensure we start with a clean transaction state
        try:
            db.session.rollback()  # Rollback any existing transaction
        except:
            pass
        
        # Count current records
        try:
            user_count = User.query.count()
            content_count = Content.query.count()
            project_count = Project.query.count()
            section_count = Section.query.count()
            revision_count = Revision.query.count()
            feedback_count = Feedback.query.count()
            comment_count = Comment.query.count()
            
            print("Current database contents:")
            print(f"  Users: {user_count}")
            print(f"  Content entries: {content_count}")
            print(f"  Projects: {project_count}")
            print(f"  Sections: {section_count}")
            print(f"  Revisions: {revision_count}")
            print(f"  Feedback entries: {feedback_count}")
            print(f"  Comments: {comment_count}")
            print()
            
            total_records = user_count + content_count + project_count + section_count + revision_count + feedback_count + comment_count
            
            if total_records == 0:
                print("✅ Database is already empty. Nothing to delete.")
                return
            
        except Exception as e:
            print(f"⚠️  Error counting records: {e}")
            print("Continuing with deletion anyway...")
            print()
        
        # Confirmation
        print("=" * 70)
        response = input("Are you ABSOLUTELY SURE you want to delete ALL data? Type 'DELETE ALL' to confirm: ")
        print()
        
        if response != 'DELETE ALL':
            print("❌ Operation cancelled. No data was deleted.")
            return
        
        print("🗑️  Starting deletion process...")
        print()
        
        # Ensure we start with a fresh transaction
        db.session.rollback()
        
        # Initialize counters
        deleted_comments = 0
        deleted_feedback = 0
        deleted_revisions = 0
        deleted_sections = 0
        deleted_projects = 0
        deleted_content = 0
        deleted_users = 0
        
        try:
            # Delete in order to respect foreign key constraints
            # Each deletion is wrapped in its own try-except to handle errors gracefully
            
            # Delete Comments first (references Section and Project)
            try:
                print("Deleting Comments...")
                deleted_comments = Comment.query.delete()
                db.session.commit()  # Commit immediately after each deletion
                print(f"  ✅ Deleted {deleted_comments} comments")
            except Exception as e:
                db.session.rollback()
                print(f"  ⚠️  Error deleting comments: {e}")
                print("  Continuing with other deletions...")
            
            # Delete Feedback (references Section)
            try:
                print("Deleting Feedback entries...")
                deleted_feedback = Feedback.query.delete()
                db.session.commit()  # Commit immediately after each deletion
                print(f"  ✅ Deleted {deleted_feedback} feedback entries")
            except Exception as e:
                db.session.rollback()
                print(f"  ⚠️  Error deleting feedback: {e}")
                print("  Continuing with other deletions...")
            
            # Delete Revisions (references Section)
            try:
                print("Deleting Revisions...")
                deleted_revisions = Revision.query.delete()
                db.session.commit()  # Commit immediately after each deletion
                print(f"  ✅ Deleted {deleted_revisions} revisions")
            except Exception as e:
                db.session.rollback()
                print(f"  ⚠️  Error deleting revisions: {e}")
                print("  Continuing with other deletions...")
            
            # Delete Sections (references Project)
            try:
                print("Deleting Sections...")
                deleted_sections = Section.query.delete()
                db.session.commit()  # Commit immediately after each deletion
                print(f"  ✅ Deleted {deleted_sections} sections")
            except Exception as e:
                db.session.rollback()
                print(f"  ⚠️  Error deleting sections: {e}")
                print("  Continuing with other deletions...")
            
            # Delete Projects
            try:
                print("Deleting Projects...")
                deleted_projects = Project.query.delete()
                db.session.commit()  # Commit immediately after each deletion
                print(f"  ✅ Deleted {deleted_projects} projects")
            except Exception as e:
                db.session.rollback()
                print(f"  ⚠️  Error deleting projects: {e}")
                print("  Continuing with other deletions...")
            
            # Delete Content
            try:
                print("Deleting Content entries...")
                deleted_content = Content.query.delete()
                db.session.commit()  # Commit immediately after each deletion
                print(f"  ✅ Deleted {deleted_content} content entries")
            except Exception as e:
                db.session.rollback()
                print(f"  ⚠️  Error deleting content: {e}")
                print("  Continuing with other deletions...")
            
            # Delete Users (last, in case there are any references)
            try:
                print("Deleting Users...")
                deleted_users = User.query.delete()
                db.session.commit()  # Commit immediately after each deletion
                print(f"  ✅ Deleted {deleted_users} users")
            except Exception as e:
                db.session.rollback()
                print(f"  ⚠️  Error deleting users: {e}")
                print("  Continuing...")
            
            print()
            print("=" * 70)
            print("✅ DELETION PROCESS COMPLETED")
            print("=" * 70)
            print()
            print("Summary:")
            print(f"  - Users deleted: {deleted_users}")
            print(f"  - Content entries deleted: {deleted_content}")
            print(f"  - Projects deleted: {deleted_projects}")
            print(f"  - Sections deleted: {deleted_sections}")
            print(f"  - Revisions deleted: {deleted_revisions}")
            print(f"  - Feedback entries deleted: {deleted_feedback}")
            print(f"  - Comments deleted: {deleted_comments}")
            print()
            print("The database tables still exist but are now empty.")
            print("You can start fresh by creating new users, projects, and content.")
            
        except Exception as e:
            db.session.rollback()
            print()
            print("=" * 70)
            print("❌ ERROR: Failed to delete data")
            print("=" * 70)
            print(f"Error: {str(e)}")
            print()
            print("The database has been rolled back. No data was deleted.")
            import traceback
            traceback.print_exc()

if __name__ == '__main__':
    clear_all_data()


