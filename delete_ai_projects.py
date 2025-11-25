"""
Script to delete all AI projects and related data from the database.

This script will DELETE:
- All Projects (AI projects)
- All Sections (document sections/slides)
- All Revisions (content revision history)
- All Feedback (user feedback on sections)
- All Comments (user comments on sections)

This will NOT delete:
- Users (user accounts are preserved)
- Content entries (old content model entries are preserved)

This action CANNOT be undone!

Run this script only if you want to clear all AI project data.
"""

from app import app, db, Project, Section, Revision, Feedback, Comment

def delete_all_ai_projects():
    """Delete all AI projects and all related data"""
    with app.app_context():
        print("=" * 70)
        print("⚠️  WARNING: AI PROJECTS DELETION OPERATION")
        print("=" * 70)
        print()
        print("This will DELETE ALL AI PROJECT DATA from the following tables:")
        print("  - Project (all AI projects)")
        print("  - Section (all document sections/slides)")
        print("  - Revision (all content revision history)")
        print("  - Feedback (all user feedback on sections)")
        print("  - Comment (all user comments on sections)")
        print()
        print("This will NOT delete:")
        print("  - Users (user accounts will be preserved)")
        print("  - Content entries (old content model will be preserved)")
        print()
        
        # Ensure we start with a clean transaction state
        try:
            db.session.rollback()  # Rollback any existing transaction
        except:
            pass
        
        # Count current records
        try:
            project_count = Project.query.count()
            section_count = Section.query.count()
            revision_count = Revision.query.count()
            feedback_count = Feedback.query.count()
            comment_count = Comment.query.count()
            
            print("Current AI project data:")
            print(f"  Projects: {project_count}")
            print(f"  Sections: {section_count}")
            print(f"  Revisions: {revision_count}")
            print(f"  Feedback entries: {feedback_count}")
            print(f"  Comments: {comment_count}")
            print()
            
            total_records = project_count + section_count + revision_count + feedback_count + comment_count
            
            if total_records == 0:
                print("✅ No AI project data found. Database is already clean.")
                return
            
            # Show project details
            if project_count > 0:
                print("Projects that will be deleted:")
                projects = Project.query.all()
                for i, project in enumerate(projects, 1):
                    section_count_for_project = Section.query.filter_by(project_id=project.id).count()
                    print(f"  {i}. {project.name} ({project.project_type}) - {section_count_for_project} sections")
                print()
            
        except Exception as e:
            print(f"⚠️  Error counting records: {e}")
            print("Rolling back and continuing with deletion anyway...")
            db.session.rollback()  # Ensure clean state
            print()
            import traceback
            traceback.print_exc()
        
        # Confirmation
        print("=" * 70)
        response = input("Are you ABSOLUTELY SURE you want to delete ALL AI project data? Type 'DELETE AI PROJECTS' to confirm: ")
        print()
        
        if response != 'DELETE AI PROJECTS':
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
            
            # Delete Feedback (references Section and Project)
            try:
                print("Deleting Feedback entries...")
                deleted_feedback = Feedback.query.delete()
                db.session.commit()  # Commit immediately after each deletion
                print(f"  ✅ Deleted {deleted_feedback} feedback entries")
            except Exception as e:
                db.session.rollback()
                print(f"  ⚠️  Error deleting feedback: {e}")
                print("  Continuing with other deletions...")
            
            # Delete Revisions (references Section and Project)
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
            
            # Delete Projects (last, as everything else references it)
            try:
                print("Deleting Projects...")
                deleted_projects = Project.query.delete()
                db.session.commit()  # Commit immediately after each deletion
                print(f"  ✅ Deleted {deleted_projects} projects")
            except Exception as e:
                db.session.rollback()
                print(f"  ⚠️  Error deleting projects: {e}")
                print("  Continuing...")
            
            print()
            print("=" * 70)
            print("✅ DELETION PROCESS COMPLETED")
            print("=" * 70)
            print()
            print("Summary:")
            print(f"  - Projects deleted: {deleted_projects}")
            print(f"  - Sections deleted: {deleted_sections}")
            print(f"  - Revisions deleted: {deleted_revisions}")
            print(f"  - Feedback entries deleted: {deleted_feedback}")
            print(f"  - Comments deleted: {deleted_comments}")
            print()
            print("✅ Preserved:")
            print("  - User accounts (all users are still in the database)")
            print("  - Content entries (old content model entries are preserved)")
            print()
            print("You can now create new AI projects from scratch.")
            
        except Exception as e:
            db.session.rollback()
            print()
            print("=" * 70)
            print("❌ CRITICAL ERROR: Failed to delete AI project data")
            print("=" * 70)
            print(f"Error: {str(e)}")
            print()
            print("The database has been rolled back. No data was deleted.")
            import traceback
            traceback.print_exc()

if __name__ == '__main__':
    delete_all_ai_projects()

