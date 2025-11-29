# Debugging Guide: Content Generation Not Working

## Quick Diagnosis Steps

### Step 1: Test AI Service Directly

Run this to verify AI is working:
```bash
python test_ai_generation.py
```

**Expected Output:**
- ✅ Should show "AI service is working!"
- ✅ Should show generated content

**If it fails:**
- Check your `GEMINI_API_KEY` environment variable
- Verify API key is correct: `AIzaSyAhsIzBUsUz2l-Oma_6TRdKj-Sei2HNqv0`
- Check internet connection

### Step 2: Test AI Endpoint (Flask must be running)

1. Start Flask app:
   ```bash
   python app.py
   ```

2. In another terminal, run:
   ```bash
   python test_ai_endpoint.py
   ```

**Expected Output:**
- ✅ Status Code: 200
- ✅ Should show generated content preview

**If it fails:**
- Check Flask terminal for error messages
- Verify API key is set in environment
- Check if model is available

### Step 3: Check Database Content

Run this to see what's actually in the database:
```bash
python verify_section_content.py
```

**Expected Output:**
- Should show sections with "✅ HAS CONTENT" if content was generated
- Should show "❌ NO CONTENT" if content wasn't generated

### Step 4: Test in Browser

1. Open your project editor in browser
2. Open Developer Tools (F12) → Console tab
3. Click "🤖 Generate Content" for a section
4. Watch for:
   - Console messages: "Generating content for section X..."
   - Flask terminal: Should show generation progress
   - Success message: "✅ Content generated successfully!"

**If it fails:**
- Check browser console for JavaScript errors
- Check Flask terminal for Python errors
- Look for error messages in alerts

## Common Issues and Fixes

### Issue 1: "Gemini API key not configured"

**Fix:**
```powershell
# PowerShell
$env:GEMINI_API_KEY='AIzaSyAhsIzBUsUz2l-Oma_6TRdKj-Sei2HNqv0'

# Or create .env file in project root:
# GEMINI_API_KEY=AIzaSyAhsIzBUsUz2l-Oma_6TRdKj-Sei2HNqv0
```

### Issue 2: "No working Gemini model found"

**Possible causes:**
- API key is invalid or expired
- API quota exceeded
- Model names changed

**Fix:**
- Verify API key is correct
- Check Google AI Studio for available models
- Update model list in `ai_service.py`

### Issue 3: Content generates but doesn't save

**Symptoms:**
- Console shows "Content generated successfully"
- But database shows "NO CONTENT"

**Fix:**
- Check Flask terminal for database errors
- Verify PostgreSQL is running
- Check database connection string

### Issue 4: "Content not generated yet" in downloaded file

**Possible causes:**
- Content wasn't generated (click "Generate Content" button)
- Content wasn't saved to database
- Download route reading wrong data

**Fix:**
1. Generate content for each section first
2. Verify with `verify_section_content.py`
3. Then download

## Manual Intervention Required

If you see these errors, you may need to:

1. **Update API Key:**
   - Get new key from Google AI Studio
   - Update in `.env` file or environment variable

2. **Check API Quota:**
   - Visit Google Cloud Console
   - Check if you've exceeded free tier limits

3. **Update Model Names:**
   - Visit Google AI Studio
   - Check available models
   - Update `models_to_try` list in `ai_service.py`

4. **Database Issues:**
   - Verify PostgreSQL is running
   - Check connection string in `app.py`
   - Verify database `docxbuilder` exists

## Testing Checklist

- [ ] AI service test passes (`test_ai_generation.py`)
- [ ] AI endpoint test passes (`test_ai_endpoint.py`)
- [ ] Database verification shows content (`verify_section_content.py`)
- [ ] Browser console shows no errors
- [ ] Flask terminal shows successful generation
- [ ] Content appears in textarea after generation
- [ ] Downloaded DOCX contains generated content

## Still Not Working?

1. Share the output of `python test_ai_generation.py`
2. Share the output of `python verify_section_content.py`
3. Share Flask terminal output when clicking "Generate Content"
4. Share browser console output (F12 → Console)




