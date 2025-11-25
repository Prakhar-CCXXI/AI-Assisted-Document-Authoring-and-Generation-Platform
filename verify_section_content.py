"""
Script to verify section content is saved in database
Run this to check if generated content is actually stored
"""

from app import app, db, Project, Section

def verify_content():
    with app.app_context():
        print("=" * 70)
        print("VERIFYING SECTION CONTENT IN DATABASE")
        print("=" * 70)
        print()
        
        # Get all projects
        projects = Project.query.all()
        
        if not projects:
            print("No projects found in database.")
            return
        
        for project in projects:
            print(f"\nProject: {project.name} (ID: {project.id})")
            print(f"Topic: {project.main_topic}")
            print("-" * 70)
            
            sections = Section.query.filter_by(project_id=project.id).order_by(Section.section_number).all()
            
            if not sections:
                print("  No sections found.")
                continue
            
            for section in sections:
                has_content = bool(section.content and section.content.strip())
                content_len = len(section.content) if section.content else 0
                status = "✅ HAS CONTENT" if has_content else "❌ NO CONTENT"
                
                print(f"  Section {section.section_number}: {section.title}")
                print(f"    Status: {status}")
                print(f"    Content length: {content_len} characters")
                
                if has_content:
                    print(f"    Preview: {section.content[:100]}...")
                else:
                    print(f"    ⚠️  This section needs content generation!")
                print()
        
        print("=" * 70)
        print("Verification complete!")
        print("=" * 70)
        print()
        print("If sections show 'NO CONTENT':")
        print("1. Go to project editor in browser")
        print("2. Click '🤖 Generate Content' for each section")
        print("3. Wait for generation to complete")
        print("4. Run this script again to verify")

if __name__ == '__main__':
    verify_content()




