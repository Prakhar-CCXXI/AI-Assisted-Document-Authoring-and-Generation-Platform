"""
Migration script to add project_id columns to Feedback, Revision, and Comment tables
Run this script to update the database schema for the Interactive Refinement Interface
"""

from app import app, db, Feedback, Revision, Comment, Section
from sqlalchemy import text, inspect

def migrate_database_schema():
    """Add project_id columns to Feedback, Revision, and Comment tables"""
    with app.app_context():
        print("=" * 70)
        print("DATABASE SCHEMA MIGRATION")
        print("=" * 70)
        print()
        
        inspector = inspect(db.engine)
        
        # Check and migrate Feedback table
        print("1. Checking Feedback table...")
        feedback_columns = [col['name'] for col in inspector.get_columns('feedback')]
        
        if 'project_id' not in feedback_columns:
            print("   ⚠️  project_id column missing. Adding...")
            try:
                db.engine.execute(text("ALTER TABLE feedback ADD COLUMN project_id INTEGER"))
                print("   ✅ Column added")
                
                # Populate project_id from sections
                print("   Populating project_id from sections...")
                feedbacks = Feedback.query.all()
                updated = 0
                for feedback in feedbacks:
                    section = Section.query.get(feedback.section_id)
                    if section:
                        feedback.project_id = section.project_id
                        updated += 1
                
                db.session.commit()
                print(f"   ✅ Updated {updated} feedback records")
            except Exception as e:
                print(f"   ❌ Error: {e}")
                db.session.rollback()
        else:
            print("   ✅ project_id column exists")
            # Check for null values
            null_count = db.session.query(Feedback).filter(Feedback.project_id == None).count()
            if null_count > 0:
                print(f"   Found {null_count} records without project_id. Updating...")
                feedbacks = Feedback.query.filter(Feedback.project_id == None).all()
                for feedback in feedbacks:
                    section = Section.query.get(feedback.section_id)
                    if section:
                        feedback.project_id = section.project_id
                db.session.commit()
                print(f"   ✅ Updated {len(feedbacks)} records")
        
        print()
        
        # Check and migrate Revision table
        print("2. Checking Revision table...")
        revision_columns = [col['name'] for col in inspector.get_columns('revision')]
        
        if 'project_id' not in revision_columns:
            print("   ⚠️  project_id column missing. Adding...")
            try:
                db.engine.execute(text("ALTER TABLE revision ADD COLUMN project_id INTEGER"))
                print("   ✅ Column added")
                
                # Populate project_id from sections
                print("   Populating project_id from sections...")
                revisions = Revision.query.all()
                updated = 0
                for revision in revisions:
                    section = Section.query.get(revision.section_id)
                    if section:
                        revision.project_id = section.project_id
                        updated += 1
                
                db.session.commit()
                print(f"   ✅ Updated {updated} revision records")
            except Exception as e:
                print(f"   ❌ Error: {e}")
                db.session.rollback()
        else:
            print("   ✅ project_id column exists")
            # Check for null values
            null_count = db.session.query(Revision).filter(Revision.project_id == None).count()
            if null_count > 0:
                print(f"   Found {null_count} records without project_id. Updating...")
                revisions = Revision.query.filter(Revision.project_id == None).all()
                for revision in revisions:
                    section = Section.query.get(revision.section_id)
                    if section:
                        revision.project_id = section.project_id
                db.session.commit()
                print(f"   ✅ Updated {len(revisions)} records")
        
        print()
        
        # Check and migrate Comment table
        print("3. Checking Comment table...")
        try:
            comment_columns = [col['name'] for col in inspector.get_columns('comment')]
            
            if 'project_id' not in comment_columns:
                print("   ⚠️  project_id column missing. Adding...")
                try:
                    db.engine.execute(text("ALTER TABLE comment ADD COLUMN project_id INTEGER"))
                    print("   ✅ Column added")
                    
                    # Populate project_id from sections
                    print("   Populating project_id from sections...")
                    comments = Comment.query.all()
                    updated = 0
                    for comment in comments:
                        section = Section.query.get(comment.section_id)
                        if section:
                            comment.project_id = section.project_id
                            updated += 1
                    
                    db.session.commit()
                    print(f"   ✅ Updated {updated} comment records")
                except Exception as e:
                    print(f"   ❌ Error: {e}")
                    db.session.rollback()
            else:
                print("   ✅ project_id column exists")
                # Check for null values
                null_count = db.session.query(Comment).filter(Comment.project_id == None).count()
                if null_count > 0:
                    print(f"   Found {null_count} records without project_id. Updating...")
                    comments = Comment.query.filter(Comment.project_id == None).all()
                    for comment in comments:
                        section = Section.query.get(comment.section_id)
                        if section:
                            comment.project_id = section.project_id
                    db.session.commit()
                    print(f"   ✅ Updated {len(comments)} records")
        except Exception as e:
            print(f"   ⚠️  Comment table may not exist yet: {e}")
            print("   (This is OK if you haven't created any comments yet)")
        
        print()
        print("=" * 70)
        print("✅ MIGRATION COMPLETE!")
        print("=" * 70)
        print()
        print("All tables have been updated. You can now use the app normally.")
        print()
        print("Note: The columns are currently nullable to allow existing data.")
        print("After verifying everything works, you can make them NOT NULL if desired.")

if __name__ == '__main__':
    migrate_database_schema()

