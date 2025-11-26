# Vercel Deployment Checklist

Use this checklist to ensure everything is ready for deployment.

## Pre-Deployment Checklist

### Code Preparation
- [ ] All code is committed to Git
- [ ] Repository is pushed to GitHub/GitLab/Bitbucket
- [ ] `vercel.json` file exists and is correct
- [ ] `api/index.py` file exists
- [ ] `runtime.txt` file exists with Python version
- [ ] `requirements.txt` is up to date with all dependencies
- [ ] `.vercelignore` file exists (optional but recommended)
- [ ] No hardcoded credentials in code
- [ ] All environment variables use `os.getenv()`

### Database Setup
- [ ] PostgreSQL database created
- [ ] Database connection string obtained
- [ ] Database allows external connections (if needed)
- [ ] SSL mode configured (if required by provider)
- [ ] Database credentials are secure

### API Keys & Secrets
- [ ] Google Gemini API key obtained
- [ ] Flask SECRET_KEY generated (use: `python -c "import secrets; print(secrets.token_hex(32))"`)
- [ ] All API keys are ready to add to Vercel

### Testing
- [ ] Application runs locally without errors
- [ ] Database connection works locally
- [ ] AI generation works with API key
- [ ] All routes are accessible
- [ ] Templates render correctly

## Deployment Steps

### Step 1: Vercel Setup
- [ ] Vercel account created
- [ ] Connected to GitHub/GitLab/Bitbucket
- [ ] Repository imported to Vercel

### Step 2: Environment Variables
- [ ] `DATABASE_URL` added to Vercel
- [ ] `GEMINI_API_KEY` added to Vercel
- [ ] `SECRET_KEY` added to Vercel
- [ ] All variables set for Production, Preview, and Development

### Step 3: Deploy
- [ ] Initial deployment triggered
- [ ] Build completed successfully
- [ ] No build errors in logs
- [ ] Deployment URL obtained

### Step 4: Database Initialization
- [ ] Database tables created (using `init_db.py` or migration)
- [ ] Tables verified in database
- [ ] Test user can be created

### Step 5: Verification
- [ ] Application loads at deployment URL
- [ ] Registration page works
- [ ] Login page works
- [ ] Dashboard accessible after login
- [ ] Project creation works
- [ ] AI content generation works
- [ ] Document download works

## Post-Deployment

### Monitoring
- [ ] Function logs checked for errors
- [ ] Application performance monitored
- [ ] Error tracking set up (optional)

### Security
- [ ] Environment variables are secure
- [ ] No sensitive data in logs
- [ ] HTTPS is enabled (automatic with Vercel)
- [ ] Database credentials are secure

### Optimization (Optional)
- [ ] Custom domain configured
- [ ] Database connection pooling configured
- [ ] Caching implemented (if needed)
- [ ] CDN configured (automatic with Vercel)

## Troubleshooting Checklist

If deployment fails:
- [ ] Check build logs in Vercel dashboard
- [ ] Verify all dependencies in `requirements.txt`
- [ ] Check Python version in `runtime.txt`
- [ ] Verify file paths are correct
- [ ] Check environment variables are set
- [ ] Verify database connection string format
- [ ] Check API keys are valid
- [ ] Review function logs for runtime errors

## Files to Verify

- [ ] `vercel.json` - Configuration file
- [ ] `api/index.py` - Serverless entry point
- [ ] `runtime.txt` - Python version
- [ ] `requirements.txt` - Dependencies
- [ ] `app.py` - Main application
- [ ] `ai_service.py` - AI service
- [ ] `templates/` - All template files
- [ ] `init_db.py` - Database initialization

## Quick Test Commands

```bash
# Test locally with Vercel
vercel dev

# Check environment variables
vercel env ls

# View logs
vercel logs [deployment-url]

# Test database connection
python -c "from app import app, db; print('DB OK' if db else 'DB Error')"
```

---

**Status**: ⬜ Not Started | 🟡 In Progress | ✅ Complete

