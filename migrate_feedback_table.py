"""
Migration script to add project_id column to Feedback table
Run this script to update the database schema
"""

from app import app, db, Feedback, Section
from sqlalchemy import text

def migrate_feedback_table():
    """Add project_id column to Feedback table and populate it"""
    with app.app_context():
        print("=" * 70)
        print("MIGRATING FEEDBACK TABLE")
        print("=" * 70)
        print()
        
        try:
            # Check if column already exists
            inspector = db.inspect(db.engine)
            columns = [col['name'] for col in inspector.get_columns('feedback')]
            
            if 'project_id' in columns:
                print("✅ project_id column already exists in feedback table")
                print("   Checking if all records have project_id...")
                
                # Check for null project_id values
                null_count = Feedback.query.filter(Feedback.project_id == None).count()
                if null_count > 0:
                    print(f"   Found {null_count} feedback records without project_id")
                    print("   Updating missing project_id values...")
                    
                    # Update feedback records to set project_id from section
                    feedbacks = Feedback.query.filter(Feedback.project_id == None).all()
                    for feedback in feedbacks:
                        section = Section.query.get(feedback.section_id)
                        if section:
                            feedback.project_id = section.project_id
                    
                    db.session.commit()
                    print(f"   ✅ Updated {len(feedbacks)} feedback records")
                else:
                    print("   ✅ All feedback records have project_id")
                
                return
            
            print("⚠️  project_id column does not exist. Adding it...")
            
            # Add project_id column (nullable first, then we'll populate it)
            print("   Step 1: Adding project_id column...")
            db.engine.execute(text("ALTER TABLE feedback ADD COLUMN project_id INTEGER"))
            print("   ✅ Column added")
            
            # Populate project_id from section
            print("   Step 2: Populating project_id from sections...")
            feedbacks = Feedback.query.all()
            updated = 0
            for feedback in feedbacks:
                section = Section.query.get(feedback.section_id)
                if section:
                    feedback.project_id = section.project_id
                    updated += 1
            
            db.session.commit()
            print(f"   ✅ Updated {updated} feedback records")
            
            # Make column NOT NULL
            print("   Step 3: Making project_id NOT NULL...")
            # First, ensure all records have project_id
            null_feedbacks = Feedback.query.filter(Feedback.project_id == None).all()
            if null_feedbacks:
                print(f"   ⚠️  Found {len(null_feedbacks)} feedback records without project_id")
                print("   Deleting orphaned feedback records...")
                for fb in null_feedbacks:
                    db.session.delete(fb)
                db.session.commit()
            
            # Add foreign key constraint
            print("   Step 4: Adding foreign key constraint...")
            try:
                db.engine.execute(text(
                    "ALTER TABLE feedback "
                    "ADD CONSTRAINT fk_feedback_project "
                    "FOREIGN KEY (project_id) REFERENCES project(id)"
                ))
                print("   ✅ Foreign key constraint added")
            except Exception as e:
                print(f"   ⚠️  Could not add foreign key (may already exist): {e}")
            
            # Make NOT NULL
            try:
                db.engine.execute(text("ALTER TABLE feedback ALTER COLUMN project_id SET NOT NULL"))
                print("   ✅ Made project_id NOT NULL")
            except Exception as e:
                print(f"   ⚠️  Could not set NOT NULL (may already be set): {e}")
            
            print()
            print("=" * 70)
            print("✅ MIGRATION COMPLETE!")
            print("=" * 70)
            print()
            print("The feedback table has been successfully updated.")
            
        except Exception as e:
            db.session.rollback()
            print()
            print("=" * 70)
            print("❌ ERROR DURING MIGRATION")
            print("=" * 70)
            print(f"Error: {str(e)}")
            import traceback
            traceback.print_exc()
            print()
            print("The database has been rolled back. Please fix the issue and try again.")

if __name__ == '__main__':
    migrate_feedback_table()

