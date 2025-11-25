# AI Features Setup Guide

## Overview
This project now includes comprehensive AI-powered content generation features using Google's Gemini API.

## Features Implemented

### 1. AI-Powered Content Generation
- **Section-by-section generation**: Each section/slide is generated individually using LLM
- **Context-aware**: Each generation considers previous sections for coherence
- **Stored in database**: All generated content is linked to projects and sections

### 2. Interactive Refinement Interface
- **Editor-style interface**: Visual document structure display
- **Per-section refinement**:
  - AI Refinement Prompt textbox (e.g., "Make this more formal", "Convert to bullet points")
  - Like/Dislike buttons for feedback
  - Comment box for user notes
- **All data persisted**: Revisions, prompts, and comments stored in database

### 3. AI-Generated Templates
- **"AI-Suggest Outline" button**: Generates section headers or slide titles
- **User provides**: Main topic only
- **System generates**: Complete outline structure
- **User can**: Accept, edit, or discard generated template

## Setup Instructions

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

This will install:
- `google-generativeai==0.3.2` - Google Gemini SDK for LLM integration
- `python-pptx==0.6.23` - For PowerPoint generation (future feature)

### Step 2: Configure Gemini API Key

**Your API key is already configured in the code!**

The API key `AIzaSyCjOD2NE6zDxi9IrXUMsbwvWcCYA_lSjvk` is set as default in `ai_service.py`.

**Option 1: Use Default (Already Set)**
The API key is already configured in the code, so it should work immediately.

**Option 2: Environment Variable (Recommended for Production)**
```bash
# Windows PowerShell
$env:GEMINI_API_KEY="AIzaSyCjOD2NE6zDxi9IrXUMsbwvWcCYA_lSjvk"

# Windows Command Prompt
set GEMINI_API_KEY=AIzaSyCjOD2NE6zDxi9IrXUMsbwvWcCYA_lSjvk

# Linux/Mac
export GEMINI_API_KEY="AIzaSyCjOD2NE6zDxi9IrXUMsbwvWcCYA_lSjvk"
```

**Option 3: Create .env file**
Create a `.env` file in the project root:
```
GEMINI_API_KEY=AIzaSyCjOD2NE6zDxi9IrXUMsbwvWcCYA_lSjvk
```

**Get a new API key (if needed):**
1. Go to https://makersuite.google.com/app/apikey
2. Sign in with your Google account
3. Create a new API key
4. Copy and use it

### Step 3: Database Migration
The new tables will be created automatically when you run the app:
- `project` - Stores projects
- `section` - Stores sections/slides
- `revision` - Tracks content revisions
- `feedback` - Stores user feedback

Run the app:
```bash
python app.py
```

## Usage Guide

### Creating a New AI Project

1. **Navigate to Projects**
   - Go to `/projects` or click "Projects" in navigation

2. **Create Project**
   - Click "Create New Project"
   - Enter project name
   - Select type: Word Document or PowerPoint
   - Enter main topic

3. **Generate Outline**
   - Check "Use AI to suggest outline"
   - Click "🤖 AI Suggest Outline"
   - Review generated outline
   - Edit if needed, or proceed

4. **Create Project**
   - Click "Create Project"
   - You'll be redirected to the editor

### Using the Editor

1. **Generate Content**
   - For each section, click "🤖 Generate Content"
   - AI generates context-aware content
   - Content appears in the editor

2. **Refine Content**
   - Click "✏️ Refine Content"
   - Enter refinement prompt (e.g., "Make this more formal")
   - Click "Apply Refinement"
   - Content is updated based on your request

3. **Provide Feedback**
   - Click 👍 Like or 👎 Dislike
   - Add comments in the comment box
   - All feedback is saved automatically

4. **Edit Manually**
   - Click in content editor to edit directly
   - Changes are saved automatically

## API Endpoints

### Project Management
- `GET /projects` - List all projects
- `POST /projects/create` - Create new project
- `GET /projects/<id>/editor` - Open project editor

### AI Generation
- `POST /api/generate-outline` - Generate AI outline
- `POST /api/generate-content/<section_id>` - Generate section content
- `POST /api/refine-content/<section_id>` - Refine section content

### Section Management
- `POST /api/add-section` - Add new section
- `POST /api/update-section/<section_id>` - Update section

### Feedback
- `POST /api/feedback/<section_id>` - Save feedback (like/dislike, comment)

## Database Schema

### Project Table
- `id` - Primary Key
- `name` - Project name
- `project_type` - 'word' or 'powerpoint'
- `main_topic` - Main topic/theme
- `username` - Owner username
- `outline` - JSON string of outline
- `created_at`, `updated_at` - Timestamps

### Section Table
- `id` - Primary Key
- `project_id` - Foreign Key to Project
- `section_number` - Section order
- `title` - Section/slide title
- `content` - Generated/edited content
- `section_type` - 'section' or 'slide'
- `created_at`, `updated_at` - Timestamps

### Revision Table
- `id` - Primary Key
- `section_id` - Foreign Key to Section
- `content` - Content at this revision
- `refinement_prompt` - User's refinement request
- `created_at` - Timestamp

### Feedback Table
- `id` - Primary Key
- `section_id` - Foreign Key to Section (unique)
- `like_status` - 'like', 'dislike', or NULL
- `comment` - User comment
- `created_at`, `updated_at` - Timestamps

## Cost Considerations

The app uses `gemini-pro` model by default. Gemini API offers:
- Free tier with generous quotas
- Good quality content generation
- Fast response times

Monitor your usage at: https://makersuite.google.com/app/apikey

## Troubleshooting

### "Error generating content"
- Check Gemini API key is set correctly
- Verify you have API quota available
- Check internet connection
- Ensure API key is enabled for Gemini API

### "Module not found: google.generativeai"
- Run: `pip install google-generativeai`

### Database errors
- Ensure PostgreSQL is running
- Check database connection
- Run app to auto-create tables

## Future Enhancements

- Export to Word/PowerPoint files
- Batch content generation
- Template library
- Collaboration features
- Version history viewer

