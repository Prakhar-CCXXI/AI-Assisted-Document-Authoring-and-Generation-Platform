# Files to Upload to Vercel - Complete List

## 📤 How Vercel Works

**Important**: Vercel doesn't use manual file uploads. Instead, you connect your **GitHub/GitLab/Bitbucket repository** and Vercel automatically deploys from there.

## ✅ Required Files in Your Repository

Upload these files to your Git repository (GitHub/GitLab/Bitbucket):

### Core Application Files
1. `app.py` - Main Flask application
2. `ai_service.py` - AI service module
3. `requirements.txt` - Python dependencies
4. `init_db.py` - Database initialization script

### Vercel Configuration Files (Already Created ✅)
5. `vercel.json` - Vercel configuration
6. `api/index.py` - Serverless function entry point
7. `runtime.txt` - Python version specification
8. `.vercelignore` - Files to ignore during deployment

### Template Files (All files in templates/ folder)
9. `templates/base.html`
10. `templates/login.html`
11. `templates/register.html`
12. `templates/dashboard.html`
13. `templates/submit_form.html`
14. `templates/view_data.html`
15. `templates/create_project.html`
16. `templates/projects_list.html`
17. `templates/project_editor.html`
18. `templates/project_preview.html`
19. `templates/upload.html`

### Documentation Files (Optional but Recommended)
20. `README.md` - Project documentation
21. `VERCEL_DEPLOYMENT.md` - Deployment guide
22. `QUICK_DEPLOY.md` - Quick reference

## 📋 Complete File List (Copy-Paste Ready)

```
app.py
ai_service.py
requirements.txt
init_db.py
vercel.json
api/index.py
runtime.txt
.vercelignore
templates/base.html
templates/login.html
templates/register.html
templates/dashboard.html
templates/submit_form.html
templates/view_data.html
templates/create_project.html
templates/projects_list.html
templates/project_editor.html
templates/project_preview.html
templates/upload.html
README.md
```

## 🚀 Steps to Deploy

### Step 1: Push All Files to GitHub

```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Ready for Vercel deployment"

# Push to GitHub (replace with your repo URL)
git remote add origin https://github.com/yourusername/your-repo-name.git
git branch -M main
git push -u origin main
```

### Step 2: Connect Repository to Vercel

1. Go to [vercel.com/new](https://vercel.com/new)
2. Click **Import Project**
3. Select your GitHub repository
4. Click **Import**

### Step 3: Configure Environment Variables

See the next section for exact values to enter.

### Step 4: Deploy

Click **Deploy** and wait for the build to complete.

---

## 🔑 Environment Variables Setup in Vercel

After importing your repository, you'll see the **Environment Variables** section. Add these three variables:

### Variable 1: DATABASE_URL

**Name**: `DATABASE_URL`

**Value Format**: 
```
postgresql+psycopg://username:password@host:port/database_name
```

**Example Values** (depending on your provider):

**Vercel Postgres**:
```
postgresql+psycopg://default:password@ep-xxx.us-east-1.aws.neon.tech:5432/verceldb?sslmode=require
```

**Supabase**:
```
postgresql+psycopg://postgres:yourpassword@db.xxxxx.supabase.co:5432/postgres
```

**Neon**:
```
postgresql+psycopg://username:password@ep-xxx.us-east-1.aws.neon.tech/neondb?sslmode=require
```

**Railway**:
```
postgresql+psycopg://postgres:password@containers-us-west-xxx.railway.app:5432/railway
```

**How to Get It**:
- **Vercel Postgres**: Vercel Dashboard → Storage → Create Database → Postgres → Copy connection string
- **Supabase**: Project Settings → Database → Connection string
- **Neon**: Dashboard → Your Project → Connection Details → Connection string
- **Railway**: Project → PostgreSQL → Connect → Connection URL

### Variable 2: GEMINI_API_KEY

**Name**: `GEMINI_API_KEY`

**How to Get It**:
1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click **Create API Key** or **Get API Key**
4. Copy the API key (starts with `AIzaSy...`)

**Value Format**:
```
AIzaSyAhsIzBUsUz2l-Oma_6TRdKj-Sei2HNqv0
```
(Replace with your actual API key)

**Example**:
```
AIzaSyAhsIzBUsUz2l-Oma_6TRdKj-Sei2HNqv0
```

### Variable 3: SECRET_KEY

**Name**: `SECRET_KEY`

**How to Generate**:

**Option 1: Using Python (Recommended)**
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

**Option 2: Using Python Interactive**
```python
import secrets
secrets.token_hex(32)
```

**Option 3: Online Generator**
- Visit: https://randomkeygen.com/
- Use a "CodeIgniter Encryption Keys" (64 characters)

**Value Format**: 
A 64-character hexadecimal string

**Example Output**:
```
a1b2c3d4e5f6789012345678901234567890abcdef1234567890abcdef123456
```

**Example** (this is just an example - generate your own!):
```
f8a9b7c6d5e4f3a2b1c0d9e8f7a6b5c4d3e2f1a0b9c8d7e6f5a4b3c2d1e0f9a8
```

## 📝 How to Add Environment Variables in Vercel

### Method 1: During Initial Setup

1. After importing your repository, you'll see **Environment Variables** section
2. Click **Add** or the **+** button
3. Enter the **Name** (e.g., `DATABASE_URL`)
4. Enter the **Value** (paste your connection string/API key)
5. Select environments: ✅ Production, ✅ Preview, ✅ Development
6. Click **Save**
7. Repeat for all three variables

### Method 2: After Deployment

1. Go to your project dashboard on Vercel
2. Click **Settings** → **Environment Variables**
3. Click **Add New**
4. Enter Name and Value
5. Select environments
6. Click **Save**
7. **Redeploy** your project for changes to take effect

## ✅ Verification Checklist

After adding environment variables:

- [ ] `DATABASE_URL` is set (check format: starts with `postgresql+psycopg://`)
- [ ] `GEMINI_API_KEY` is set (check format: starts with `AIzaSy`)
- [ ] `SECRET_KEY` is set (check format: 64 hexadecimal characters)
- [ ] All three are enabled for Production, Preview, and Development
- [ ] No extra spaces or quotes in the values
- [ ] Database connection string includes SSL if required (`?sslmode=require`)

## 🎯 Quick Copy-Paste Commands

### Generate SECRET_KEY
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

### Test Database Connection (After Deployment)
```bash
# Set your production DATABASE_URL
export DATABASE_URL="your_database_url_here"

# Test connection
python -c "from app import app, db; print('Connected!' if db else 'Error')"
```

## ⚠️ Important Notes

1. **Never commit** environment variables to Git
2. **Never share** your API keys or database credentials
3. **Regenerate** SECRET_KEY if it's ever exposed
4. **Use different** SECRET_KEY for production vs development
5. **Database URL** must use `psycopg` driver (not `psycopg2`)

## 🆘 Troubleshooting

### "Invalid DATABASE_URL format"
- Ensure it starts with `postgresql+psycopg://`
- Check for special characters that need URL encoding
- Verify username, password, host, port, and database name are correct

### "GEMINI_API_KEY not working"
- Verify the key starts with `AIzaSy`
- Check if you have API quota remaining
- Ensure no extra spaces in the value

### "SECRET_KEY too short"
- Must be exactly 64 hexadecimal characters
- Regenerate using the Python command above

---

**Ready to deploy!** Follow these steps and your app will be live on Vercel! 🚀

