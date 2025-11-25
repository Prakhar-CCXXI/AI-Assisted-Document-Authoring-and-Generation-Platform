# Interactive Refinement Interface - API Documentation

## Overview
This document describes the API endpoints for the Interactive Refinement Interface feature, which allows users to refine document sections using AI, provide feedback, add comments, and manage revision history.

## Base URL
All endpoints are prefixed with `/api/`

## Authentication
All endpoints require authentication via session (user must be logged in). The `@login_required` decorator ensures this.

---

## Endpoints

### 1. Refine Section Content

**POST** `/api/refine-content/<section_id>`

Refines the content of a specific section based on a user's refinement prompt.

**Request Body:**
```json
{
  "prompt": "Shorten to 100 words and make more formal."
}
```

**Response (Success - 200):**
```json
{
  "success": true,
  "revision": {
    "id": 987,
    "project_id": 123,
    "section_id": 456,
    "user_id": 789,
    "prompt": "Shorten to 100 words and make more formal.",
    "generated_content": "The refined content goes here...",
    "created_at": "2025-11-25T10:00:00Z"
  },
  "section": {
    "id": 456,
    "project_id": 123,
    "title": "Market Overview",
    "current_content": "The refined content goes here..."
  }
}
```

**Response (Error - 400/429/500):**
```json
{
  "error": "Error message here"
}
```

**Rate Limiting:** 10 requests per user per 60 seconds

---

### 2. Get Revision History

**GET** `/api/sections/<section_id>/revisions`

Retrieves the revision history for a section (last 10 revisions).

**Response (Success - 200):**
```json
{
  "success": true,
  "revisions": [
    {
      "id": 987,
      "project_id": 123,
      "section_id": 456,
      "user_id": 789,
      "prompt": "Shorten to 100 words",
      "generated_content": "Refined content...",
      "created_at": "2025-11-25T10:00:00Z"
    },
    {
      "id": 986,
      "project_id": 123,
      "section_id": 456,
      "user_id": 789,
      "prompt": "Make more formal",
      "generated_content": "Previous refined content...",
      "created_at": "2025-11-25T09:45:00Z"
    }
  ]
}
```

---

### 3. Restore Revision

**POST** `/api/sections/<section_id>/revisions/<revision_id>/restore`

Restores a previous revision as the current content. Creates a new revision entry for the restore action.

**Response (Success - 200):**
```json
{
  "success": true,
  "revision": {
    "id": 988,
    "project_id": 123,
    "section_id": 456,
    "user_id": 789,
    "prompt": "Restored from revision 987 (original prompt: Shorten to 100 words)",
    "generated_content": "Restored content...",
    "created_at": "2025-11-25T10:15:00Z"
  },
  "section": {
    "id": 456,
    "project_id": 123,
    "title": "Market Overview",
    "current_content": "Restored content..."
  }
}
```

---

### 4. Add Comment

**POST** `/api/sections/<section_id>/comments`

Adds a comment to a section.

**Request Body:**
```json
{
  "text": "This section needs more examples."
}
```

**Response (Success - 200):**
```json
{
  "success": true,
  "comment": {
    "id": 55,
    "project_id": 123,
    "section_id": 456,
    "user_id": 789,
    "text": "This section needs more examples.",
    "created_at": "2025-11-25T10:20:00Z",
    "username": "john_doe"
  }
}
```

---

### 5. Get Comments

**GET** `/api/sections/<section_id>/comments`

Retrieves all comments for a section (last 50).

**Response (Success - 200):**
```json
{
  "success": true,
  "comments": [
    {
      "id": 55,
      "project_id": 123,
      "section_id": 456,
      "user_id": 789,
      "text": "This section needs more examples.",
      "created_at": "2025-11-25T10:20:00Z",
      "username": "john_doe"
    }
  ]
}
```

---

### 6. Set Feedback (Like/Dislike)

**POST** `/api/feedback/<section_id>`

Records user feedback (like/dislike) for a section.

**Request Body:**
```json
{
  "liked": true
}
```
or
```json
{
  "like_status": "like"
}
```

**Response (Success - 200):**
```json
{
  "success": true,
  "like_status": "like"
}
```

---

## Database Models

### Revision
- `id` (Primary Key)
- `section_id` (Foreign Key)
- `project_id` (Foreign Key)
- `user_id` (Foreign Key, nullable)
- `content` (Text) - The refined content
- `refinement_prompt` (Text) - User's refinement request
- `created_at` (DateTime)

### Comment
- `id` (Primary Key)
- `project_id` (Foreign Key)
- `section_id` (Foreign Key)
- `user_id` (Foreign Key, nullable)
- `text` (Text) - Comment text
- `created_at` (DateTime)

### Feedback
- `id` (Primary Key)
- `section_id` (Foreign Key, unique)
- `project_id` (Foreign Key)
- `user_id` (Foreign Key, nullable)
- `like_status` (String) - 'like', 'dislike', or None
- `created_at` (DateTime)
- `updated_at` (DateTime)

---

## Security Features

1. **XSS Prevention**: Input sanitization for prompts and comments
2. **Rate Limiting**: 10 LLM calls per user per 60 seconds
3. **Authentication**: All endpoints require logged-in user
4. **Content Sanitization**: Output content is sanitized before storage

---

## LLM Integration

The refinement uses Google Gemini API via `ai_service.py`:
- Function: `refine_content_section(original_content, refinement_prompt, section_title, project_topic)`
- Context-aware: Only includes the single section's content
- Logging: All prompts and responses are logged for auditability
- Error Handling: Comprehensive error handling with user-friendly messages

---

## Example Usage

### Refine Content
```javascript
fetch('/api/refine-content/456', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({
    prompt: "Shorten to 100 words and make more formal."
  })
})
.then(res => res.json())
.then(data => {
  if (data.success) {
    console.log('Refined content:', data.section.current_content);
    console.log('Revision ID:', data.revision.id);
  }
});
```

### Get Revision History
```javascript
fetch('/api/sections/456/revisions')
.then(res => res.json())
.then(data => {
  if (data.success) {
    data.revisions.forEach(rev => {
      console.log(`Revision ${rev.id}: ${rev.prompt}`);
    });
  }
});
```

### Restore Revision
```javascript
fetch('/api/sections/456/revisions/987/restore', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'}
})
.then(res => res.json())
.then(data => {
  if (data.success) {
    console.log('Content restored!');
  }
});
```

---

## Notes

- All timestamps are in ISO 8601 format
- Revision history shows last 10 revisions
- Comments show last 50 comments
- Rate limiting is per-user, in-memory (resets on server restart)
- Content is sanitized to prevent XSS attacks

