# Vercel Deployment Guide

This guide will walk you through deploying your AI-Assisted Document Authoring and Generation Platform to Vercel.

## Prerequisites

1. **Vercel Account**: Sign up at [vercel.com](https://vercel.com) (free tier available)
2. **GitHub/GitLab/Bitbucket Account**: Your code needs to be in a Git repository
3. **PostgreSQL Database**: You'll need a PostgreSQL database (see options below)
4. **Google Gemini API Key**: Get one from [Google AI Studio](https://makersuite.google.com/app/apikey)

## Step 1: Prepare Your Repository

1. **Push your code to GitHub/GitLab/Bitbucket**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit for Vercel deployment"
   git remote add origin <your-repo-url>
   git push -u origin main
   ```

2. **Ensure all files are committed**:
   - `app.py`
   - `ai_service.py`
   - `requirements.txt`
   - `vercel.json`
   - `api/index.py`
   - `runtime.txt`
   - `templates/` directory
   - All other necessary files

## Step 2: Set Up PostgreSQL Database

Vercel doesn't provide built-in PostgreSQL, so you'll need an external service. Here are recommended options:

### Option A: Vercel Postgres (Recommended - Easiest Integration)
1. Go to your Vercel project dashboard
2. Navigate to **Storage** → **Create Database** → **Postgres**
3. Create a new database
4. Copy the connection string (it will be automatically added as `POSTGRES_URL`)

### Option B: Supabase (Free Tier Available)
1. Sign up at [supabase.com](https://supabase.com)
2. Create a new project
3. Go to **Settings** → **Database**
4. Copy the connection string
5. Format: `postgresql+psycopg://postgres:[YOUR-PASSWORD]@[HOST]:5432/postgres`

### Option C: Neon (Free Tier Available)
1. Sign up at [neon.tech](https://neon.tech)
2. Create a new project
3. Copy the connection string from the dashboard

### Option D: Railway (Free Tier Available)
1. Sign up at [railway.app](https://railway.app)
2. Create a new PostgreSQL service
3. Copy the connection string

**Important**: Your connection string should use `psycopg` driver format:
```
postgresql+psycopg://username:password@host:port/database_name
```

## Step 3: Deploy to Vercel

### Method 1: Using Vercel Dashboard (Recommended for First Time)

1. **Go to Vercel Dashboard**:
   - Visit [vercel.com/new](https://vercel.com/new)
   - Sign in with your GitHub/GitLab/Bitbucket account

2. **Import Your Repository**:
   - Click **Import Project**
   - Select your repository
   - Click **Import**

3. **Configure Project Settings**:
   - **Framework Preset**: Other (or leave as default)
   - **Root Directory**: `./` (root of your project)
   - **Build Command**: Leave empty (Vercel will auto-detect)
   - **Output Directory**: Leave empty
   - **Install Command**: `pip install -r requirements.txt`

4. **Set Environment Variables**:
   Click **Environment Variables** and add:

   ```
   DATABASE_URL = postgresql+psycopg://username:password@host:port/database_name
   GEMINI_API_KEY = your_gemini_api_key_here
   SECRET_KEY = your_secret_key_here
   ```

   **Generate SECRET_KEY**:
   ```bash
   python -c "import secrets; print(secrets.token_hex(32))"
   ```

5. **Deploy**:
   - Click **Deploy**
   - Wait for the build to complete (usually 2-5 minutes)

### Method 2: Using Vercel CLI

1. **Install Vercel CLI**:
   ```bash
   npm install -g vercel
   ```

2. **Login to Vercel**:
   ```bash
   vercel login
   ```

3. **Deploy**:
   ```bash
   vercel
   ```

4. **Set Environment Variables**:
   ```bash
   vercel env add DATABASE_URL
   vercel env add GEMINI_API_KEY
   vercel env add SECRET_KEY
   ```

5. **Deploy to Production**:
   ```bash
   vercel --prod
   ```

## Step 4: Initialize Database Tables

After deployment, you need to initialize your database tables. You have two options:

### Option A: Using Vercel CLI (Recommended)

1. **Create a migration script** (`init_db.py`):
   ```python
   import os
   from app import app, db
   
   with app.app_context():
       db.create_all()
       print("Database tables created successfully!")
   ```

2. **Run locally with production database**:
   ```bash
   # Set your production DATABASE_URL
   export DATABASE_URL="your_production_database_url"
   
   # Run the script
   python init_db.py
   ```

### Option B: Using Vercel Functions

Create an API endpoint to initialize the database (only for first-time setup):

1. Create `api/init-db.py`:
   ```python
   from app import app, db
   
   def handler(request):
       with app.app_context():
           db.create_all()
           return {"status": "Database initialized"}, 200
   ```

2. Visit: `https://your-app.vercel.app/api/init-db` (only once!)

**⚠️ Security Note**: Remove or protect the init-db endpoint after use!

## Step 5: Verify Deployment

1. **Check Your Deployment**:
   - Visit your Vercel dashboard
   - Click on your project
   - Check the deployment logs for any errors

2. **Test Your Application**:
   - Visit your deployed URL (e.g., `https://your-app.vercel.app`)
   - Test registration and login
   - Test creating a project
   - Test AI content generation

3. **Check Logs**:
   - In Vercel dashboard, go to **Functions** → **View Logs**
   - Monitor for any runtime errors

## Step 6: Configure Custom Domain (Optional)

1. **Add Domain in Vercel**:
   - Go to your project → **Settings** → **Domains**
   - Add your custom domain
   - Follow DNS configuration instructions

2. **Update DNS Records**:
   - Add the CNAME or A record as instructed by Vercel

## Troubleshooting

### Common Issues

1. **Database Connection Errors**:
   - Verify `DATABASE_URL` is correctly set in environment variables
   - Ensure the database allows connections from Vercel's IPs
   - Check if your database provider requires SSL (add `?sslmode=require` to connection string)

2. **Module Import Errors**:
   - Ensure all dependencies are in `requirements.txt`
   - Check that `api/index.py` correctly imports from parent directory

3. **Build Failures**:
   - Check build logs in Vercel dashboard
   - Ensure Python 3.12 is specified in `runtime.txt`
   - Verify all file paths are correct

4. **AI Generation Not Working**:
   - Verify `GEMINI_API_KEY` is set correctly
   - Check API quota limits
   - Review function logs for error messages

5. **Static Files Not Loading**:
   - Ensure templates are in the correct directory
   - Check that all template files are committed to Git

### Debugging Tips

1. **View Function Logs**:
   ```bash
   vercel logs [deployment-url]
   ```

2. **Test Locally with Vercel**:
   ```bash
   vercel dev
   ```

3. **Check Environment Variables**:
   - Go to Vercel dashboard → Project → Settings → Environment Variables
   - Verify all variables are set for Production, Preview, and Development

## Environment Variables Reference

| Variable | Description | Required | Example |
|----------|-------------|----------|---------|
| `DATABASE_URL` | PostgreSQL connection string | Yes | `postgresql+psycopg://user:pass@host:5432/db` |
| `GEMINI_API_KEY` | Google Gemini API key | Yes | `AIzaSy...` |
| `SECRET_KEY` | Flask session secret key | Yes | `random-hex-string-64-chars` |

## File Structure for Vercel

```
your-project/
├── api/
│   └── index.py          # Vercel serverless function entry point
├── templates/            # HTML templates
│   ├── base.html
│   ├── login.html
│   └── ...
├── app.py               # Main Flask application
├── ai_service.py        # AI service module
├── requirements.txt     # Python dependencies
├── vercel.json         # Vercel configuration
├── runtime.txt         # Python version
└── .vercelignore       # Files to ignore during deployment
```

## Important Notes

1. **Serverless Limitations**:
   - Vercel functions have execution time limits (10 seconds on free tier, 60 seconds on Pro)
   - Long-running AI generation might timeout
   - Consider implementing async processing for long operations

2. **Database Migrations**:
   - Run migrations before deploying
   - Use Alembic for production migrations (recommended)

3. **File Storage**:
   - Vercel is serverless - no persistent file storage
   - All file operations should use in-memory (BytesIO) as your code already does ✅

4. **Cold Starts**:
   - First request after inactivity may be slower
   - Consider using Vercel Pro for better performance

5. **Rate Limiting**:
   - Your app has built-in rate limiting for AI calls
   - Monitor usage to avoid exceeding API quotas

## Next Steps

1. ✅ Set up monitoring and error tracking
2. ✅ Configure automated backups for your database
3. ✅ Set up CI/CD for automatic deployments
4. ✅ Add custom domain
5. ✅ Configure SSL (automatic with Vercel)
6. ✅ Set up database migrations workflow

## Support

- **Vercel Documentation**: [vercel.com/docs](https://vercel.com/docs)
- **Vercel Community**: [github.com/vercel/vercel/discussions](https://github.com/vercel/vercel/discussions)
- **Flask Documentation**: [flask.palletsprojects.com](https://flask.palletsprojects.com)

## Deployment Checklist

- [ ] Code pushed to Git repository
- [ ] PostgreSQL database created and accessible
- [ ] Environment variables configured in Vercel
- [ ] `vercel.json` file created
- [ ] `api/index.py` file created
- [ ] `runtime.txt` file created
- [ ] `requirements.txt` is up to date
- [ ] Database tables initialized
- [ ] Application tested on deployed URL
- [ ] Custom domain configured (optional)
- [ ] Monitoring set up (optional)

---

**Congratulations!** Your application should now be live on Vercel! 🚀

