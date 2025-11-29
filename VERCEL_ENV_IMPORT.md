# How to Import .env File to Vercel

## ⚠️ Important Note

**Vercel does NOT support uploading .env files directly.** You need to manually add each environment variable in the Vercel dashboard.

However, I've created a `.env` file with all your values for reference.

---

## 📋 Your .env File Contents

The `.env` file has been created with:

```
DATABASE_URL=postgresql+psycopg://your_username:PostgreSQL1036@localhost:5432/docxbuilder
GEMINI_API_KEY=AIzaSyAhsIzBUsUz2l-Oma_6TRdKj-Sei2HNqv0
SECRET_KEY=310dfc0e3e2ad00593be4039fa8bc53c3c6f90ff8965c8069c11c6998ea3e45b
```

---

## 🔑 How to Add to Vercel (Step-by-Step)

### Step 1: Go to Vercel Dashboard
1. Visit: https://vercel.com/dashboard
2. Click on your project (or create new one)

### Step 2: Open Environment Variables
1. Click **Settings** tab
2. Click **Environment Variables** (left sidebar)

### Step 3: Add Each Variable

#### Variable 1: DATABASE_URL
1. Click **Add New**
2. **Name:** `DATABASE_URL`
3. **Value:** `postgresql+psycopg://your_username:PostgreSQL1036@localhost:5432/docxbuilder`
4. Check: ✅ Production, ✅ Preview, ✅ Development
5. Click **Save**

⚠️ **NOTE:** This database URL uses `localhost` which **WON'T WORK on Vercel**. You need a cloud database. See below.

#### Variable 2: GEMINI_API_KEY
1. Click **Add New**
2. **Name:** `GEMINI_API_KEY`
3. **Value:** `AIzaSyAhsIzBUsUz2l-Oma_6TRdKj-Sei2HNqv0`
4. Check: ✅ Production, ✅ Preview, ✅ Development
5. Click **Save**

#### Variable 3: SECRET_KEY
1. Click **Add New**
2. **Name:** `SECRET_KEY`
3. **Value:** `310dfc0e3e2ad00593be4039fa8bc53c3c6f90ff8965c8069c11c6998ea3e45b`
4. Check: ✅ Production, ✅ Preview, ✅ Development
5. Click **Save**

---

## ⚠️ CRITICAL: Database URL Issue

Your database URL uses `localhost` which **will NOT work on Vercel** because:
- Vercel runs in the cloud
- It cannot connect to your local machine
- You need a cloud PostgreSQL database

### Solution: Use Vercel Postgres (Easiest)

1. In your Vercel project dashboard
2. Click **Storage** tab
3. Click **Create Database** → **Postgres**
4. Create database (free tier available)
5. Copy the connection string
6. Use that as your `DATABASE_URL` instead

**Or use other cloud providers:**
- **Supabase**: supabase.com → Create Project → Settings → Database
- **Neon**: neon.tech → Create Project → Connection Details
- **Railway**: railway.app → Create Project → Add PostgreSQL

---

## ✅ Quick Copy-Paste Values

### For Vercel Dashboard:

**DATABASE_URL:**
```
postgresql+psycopg://your_username:PostgreSQL1036@localhost:5432/docxbuilder
```
(⚠️ Replace with cloud database URL for Vercel)

**GEMINI_API_KEY:**
```
AIzaSyAhsIzBUsUz2l-Oma_6TRdKj-Sei2HNqv0
```

**SECRET_KEY:**
```
310dfc0e3e2ad00593be4039fa8bc53c3c6f90ff8965c8069c11c6998ea3e45b
```

---

## 📝 Alternative: Using Vercel CLI (Advanced)

If you have Vercel CLI installed, you can add variables via command line:

```bash
# Install Vercel CLI (if not installed)
npm install -g vercel

# Login
vercel login

# Add environment variables
vercel env add DATABASE_URL
vercel env add GEMINI_API_KEY
vercel env add SECRET_KEY
```

Then paste the values when prompted.

---

## 🎯 Summary

1. ✅ `.env` file created with all values
2. ⚠️ You still need to manually add them in Vercel dashboard
3. ⚠️ Replace `DATABASE_URL` with cloud database connection string
4. ✅ `GEMINI_API_KEY` and `SECRET_KEY` are ready to use

---

**The `.env` file is ready, but remember to add the values manually in Vercel!** 🚀

