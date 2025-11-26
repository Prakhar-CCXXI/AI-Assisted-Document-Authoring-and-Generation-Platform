# Quick Deploy to Vercel - Quick Reference

## 🚀 Fast Track Deployment (5 Steps)

### 1. Push to GitHub
```bash
git init
git add .
git commit -m "Ready for Vercel deployment"
git remote add origin <your-repo-url>
git push -u origin main
```

### 2. Create PostgreSQL Database
Choose one:
- **Vercel Postgres** (easiest): Dashboard → Storage → Create Database → Postgres
- **Supabase**: supabase.com → New Project → Copy connection string
- **Neon**: neon.tech → New Project → Copy connection string

### 3. Deploy to Vercel
1. Go to [vercel.com/new](https://vercel.com/new)
2. Import your GitHub repository
3. Add these **Environment Variables**:
   ```
   DATABASE_URL = postgresql+psycopg://user:pass@host:port/db
   GEMINI_API_KEY = your_api_key_here
   SECRET_KEY = generate_with: python -c "import secrets; print(secrets.token_hex(32))"
   ```
4. Click **Deploy**

### 4. Initialize Database
After deployment, run:
```bash
# Set production DATABASE_URL
export DATABASE_URL="your_production_database_url"

# Initialize tables
python init_db.py
```

### 5. Test Your App
Visit: `https://your-app.vercel.app`

---

## 📋 Required Files (Already Created ✅)

- ✅ `vercel.json` - Vercel configuration
- ✅ `api/index.py` - Serverless function entry point
- ✅ `runtime.txt` - Python version
- ✅ `.vercelignore` - Ignore patterns
- ✅ `init_db.py` - Database initialization script

## 🔑 Environment Variables Needed

| Variable | Where to Get |
|----------|-------------|
| `DATABASE_URL` | Your PostgreSQL provider |
| `GEMINI_API_KEY` | [Google AI Studio](https://makersuite.google.com/app/apikey) |
| `SECRET_KEY` | Generate: `python -c "import secrets; print(secrets.token_hex(32))"` |

## ⚠️ Important Notes

1. **Database**: Must be PostgreSQL with `psycopg` driver
2. **Connection String Format**: `postgresql+psycopg://user:pass@host:port/db`
3. **SSL**: Some providers require `?sslmode=require` at the end
4. **Cold Starts**: First request may be slow (serverless limitation)

## 🆘 Troubleshooting

- **Build fails?** Check `requirements.txt` has all dependencies
- **Database error?** Verify `DATABASE_URL` format and SSL settings
- **AI not working?** Check `GEMINI_API_KEY` is set correctly
- **500 errors?** Check Vercel function logs in dashboard

## 📚 Full Guide

See `VERCEL_DEPLOYMENT.md` for detailed instructions.

