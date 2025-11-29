# Environment Variables Setup Guide for Vercel

## 🔑 Three Required Environment Variables

You need to add these three environment variables in your Vercel project settings:

---

## 1. DATABASE_URL

### What It Is
PostgreSQL database connection string for your application.

### How to Get It

#### Option A: Vercel Postgres (Easiest - Recommended)
1. Go to your Vercel project dashboard
2. Click **Storage** tab
3. Click **Create Database** → **Postgres**
4. Create database (free tier available)
5. Copy the **Connection String** (automatically formatted correctly)

**Example**:
```
postgresql+psycopg://default:password@ep-xxx.us-east-1.aws.neon.tech:5432/verceldb?sslmode=require
```

#### Option B: Supabase (Free Tier Available)
1. Go to [supabase.com](https://supabase.com)
2. Create account and new project
3. Go to **Project Settings** → **Database**
4. Find **Connection string** → **URI**
5. Copy the connection string
6. **Important**: Change `postgresql://` to `postgresql+psycopg://`

**Example**:
```
postgresql+psycopg://postgres:yourpassword@db.xxxxx.supabase.co:5432/postgres
```

#### Option C: Neon (Free Tier Available)
1. Go to [neon.tech](https://neon.tech)
2. Create account and new project
3. Go to **Connection Details**
4. Copy the connection string
5. **Important**: Change `postgresql://` to `postgresql+psycopg://`
6. Add `?sslmode=require` at the end if not present

**Example**:
```
postgresql+psycopg://username:password@ep-xxx.us-east-1.aws.neon.tech/neondb?sslmode=require
```

#### Option D: Railway (Free Tier Available)
1. Go to [railway.app](https://railway.app)
2. Create account and new project
3. Add **PostgreSQL** service
4. Click on PostgreSQL → **Connect** → **Connection URL**
5. Copy the connection string
6. **Important**: Change `postgresql://` to `postgresql+psycopg://`

**Example**:
```
postgresql+psycopg://postgres:password@containers-us-west-xxx.railway.app:5432/railway
```

### Format Requirements
- Must start with: `postgresql+psycopg://`
- Format: `postgresql+psycopg://username:password@host:port/database_name`
- Add `?sslmode=require` if your provider requires SSL

### How to Add in Vercel
1. Go to Project → **Settings** → **Environment Variables**
2. Click **Add New**
3. **Name**: `DATABASE_URL`
4. **Value**: Paste your connection string
5. Select: ✅ Production, ✅ Preview, ✅ Development
6. Click **Save**

---

## 2. GEMINI_API_KEY

### What It Is
Google Gemini API key for AI content generation features.

### How to Get It

1. **Go to Google AI Studio**:
   - Visit: [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)
   - Or: [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)

2. **Sign In**:
   - Use your Google account
   - Accept terms if prompted

3. **Create API Key**:
   - Click **Create API Key** or **Get API Key**
   - Select or create a Google Cloud project
   - Copy the API key (starts with `AIzaSy...`)

4. **Save the Key**:
   - Copy it immediately (you won't see it again)
   - Store it securely

### Format
- Starts with: `AIzaSy`
- Length: Usually 39 characters
- Example: `AIzaSyAhsIzBUsUz2l-Oma_6TRdKj-Sei2HNqv0`

### How to Add in Vercel
1. Go to Project → **Settings** → **Environment Variables**
2. Click **Add New**
3. **Name**: `GEMINI_API_KEY`
4. **Value**: Paste your API key (no quotes, no spaces)
5. Select: ✅ Production, ✅ Preview, ✅ Development
6. Click **Save**

### Important Notes
- Keep your API key secret
- Don't commit it to Git
- Monitor usage to avoid exceeding quota
- Free tier has rate limits

---

## 3. SECRET_KEY

### What It Is
Flask session encryption key for secure user sessions and cookies.

### How to Generate

#### Method 1: Python Command (Recommended)
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

**Output Example**:
```
a1b2c3d4e5f6789012345678901234567890abcdef1234567890abcdef123456
```

#### Method 2: Python Interactive
```python
import secrets
secrets.token_hex(32)
```

#### Method 3: Online Generator
- Visit: https://randomkeygen.com/
- Use **CodeIgniter Encryption Keys** (64 characters)

### Format Requirements
- **Length**: Exactly 64 characters
- **Type**: Hexadecimal (0-9, a-f)
- **Example**: `f8a9b7c6d5e4f3a2b1c0d9e8f7a6b5c4d3e2f1a0b9c8d7e6f5a4b3c2d1e0f9a8`

### How to Add in Vercel
1. Generate the key using the command above
2. Go to Project → **Settings** → **Environment Variables**
3. Click **Add New**
4. **Name**: `SECRET_KEY`
5. **Value**: Paste the generated 64-character string
6. Select: ✅ Production, ✅ Preview, ✅ Development
7. Click **Save**

### Important Notes
- **Never share** this key
- **Use different** keys for production and development
- **Regenerate** if ever exposed
- **Keep it secret** - it encrypts user sessions

---

## 📋 Complete Setup Checklist

### Before Adding Variables
- [ ] Database created and accessible
- [ ] Gemini API key obtained
- [ ] SECRET_KEY generated

### Adding Variables in Vercel
- [ ] `DATABASE_URL` added
- [ ] `GEMINI_API_KEY` added
- [ ] `SECRET_KEY` added
- [ ] All three enabled for Production
- [ ] All three enabled for Preview
- [ ] All three enabled for Development
- [ ] No extra spaces or quotes in values

### After Adding Variables
- [ ] Redeploy project (if variables added after deployment)
- [ ] Test application
- [ ] Verify database connection works
- [ ] Verify AI generation works
- [ ] Check function logs for errors

---

## 🎯 Quick Reference Table

| Variable | Format | Example | Where to Get |
|----------|--------|---------|--------------|
| `DATABASE_URL` | `postgresql+psycopg://user:pass@host:port/db` | `postgresql+psycopg://postgres:pass@host:5432/db` | Database provider dashboard |
| `GEMINI_API_KEY` | `AIzaSy...` (39 chars) | `AIzaSyAhsIzBUsUz2l-Oma_6TRdKj-Sei2HNqv0` | [Google AI Studio](https://makersuite.google.com/app/apikey) |
| `SECRET_KEY` | 64 hex characters | `a1b2c3d4e5f6789012345678901234567890abcdef1234567890abcdef123456` | Generate with Python command |

---

## 🆘 Troubleshooting

### "Invalid DATABASE_URL"
- ✅ Check it starts with `postgresql+psycopg://`
- ✅ Verify username, password, host, port, database are correct
- ✅ Add `?sslmode=require` if SSL is required
- ✅ URL-encode special characters in password

### "GEMINI_API_KEY not working"
- ✅ Verify it starts with `AIzaSy`
- ✅ Check no extra spaces before/after
- ✅ Verify API key is active in Google AI Studio
- ✅ Check API quota hasn't been exceeded

### "SECRET_KEY error"
- ✅ Must be exactly 64 characters
- ✅ Must be hexadecimal (0-9, a-f)
- ✅ No spaces or special characters
- ✅ Regenerate if unsure

### Variables Not Working After Adding
- ✅ **Redeploy** your project after adding variables
- ✅ Check variables are enabled for the correct environment
- ✅ Verify no typos in variable names
- ✅ Check function logs in Vercel dashboard

---

## 📝 Step-by-Step: Adding Variables in Vercel Dashboard

1. **Go to Your Project**:
   - Visit [vercel.com/dashboard](https://vercel.com/dashboard)
   - Click on your project

2. **Navigate to Settings**:
   - Click **Settings** tab
   - Click **Environment Variables** in left sidebar

3. **Add First Variable**:
   - Click **Add New** button
   - **Key**: `DATABASE_URL`
   - **Value**: Paste your database connection string
   - Check: ✅ Production, ✅ Preview, ✅ Development
   - Click **Save**

4. **Add Second Variable**:
   - Click **Add New** again
   - **Key**: `GEMINI_API_KEY`
   - **Value**: Paste your API key
   - Check: ✅ Production, ✅ Preview, ✅ Development
   - Click **Save**

5. **Add Third Variable**:
   - Click **Add New** again
   - **Key**: `SECRET_KEY`
   - **Value**: Paste your generated key
   - Check: ✅ Production, ✅ Preview, ✅ Development
   - Click **Save**

6. **Redeploy** (if project already deployed):
   - Go to **Deployments** tab
   - Click **⋯** (three dots) on latest deployment
   - Click **Redeploy**

---

**All set!** Your environment variables are configured. 🎉

