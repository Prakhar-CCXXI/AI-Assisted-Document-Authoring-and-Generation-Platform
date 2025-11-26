# Environment Variables - Ready for Vercel

## ✅ Values Ready to Copy

### 1. GEMINI_API_KEY

**In Vercel Dashboard:**
- **Name:** `GEMINI_API_KEY`
- **Value:** `AIzaSyCjOD2NE6zDxi9IrXUMsbwvWcCYA_lSjvk`
- **Environments:** ✅ Production, ✅ Preview, ✅ Development

---

### 2. SECRET_KEY

**In Vercel Dashboard:**
- **Name:** `SECRET_KEY`
- **Value:** `310dfc0e3e2ad00593be4039fa8bc53c3c6f90ff8965c8069c11c6998ea3e45b`
- **Environments:** ✅ Production, ✅ Preview, ✅ Development

---

### 3. DATABASE_URL

**⚠️ CRITICAL ISSUE:** Your database URL uses `localhost` which **will NOT work on Vercel**.

**Your current URL (won't work):**
```
postgresql://your_username:PostgreSQL1036@localhost:5432/docxbuilder
```

**You need a cloud PostgreSQL database. Here are your options:**

#### Option 1: Vercel Postgres (Recommended - Easiest)

1. Go to your Vercel project dashboard
2. Click **Storage** tab
3. Click **Create Database** → **Postgres**
4. Create database (free tier available)
5. Copy the connection string
6. It will be automatically formatted correctly
7. Use that as your `DATABASE_URL`

**In Vercel Dashboard:**
- **Name:** `DATABASE_URL`
- **Value:** [Connection string from Vercel Postgres]
- **Environments:** ✅ Production, ✅ Preview, ✅ Development

#### Option 2: Supabase (Free Tier)

1. Go to [supabase.com](https://supabase.com)
2. Create account and new project
3. Go to **Project Settings** → **Database**
4. Find **Connection string** → **URI**
5. Copy it
6. **Change** `postgresql://` to `postgresql+psycopg://`

**Example:**
```
postgresql+psycopg://postgres:yourpassword@db.xxxxx.supabase.co:5432/postgres
```

#### Option 3: Neon (Free Tier)

1. Go to [neon.tech](https://neon.tech)
2. Create account and new project
3. Go to **Connection Details**
4. Copy connection string
5. **Change** `postgresql://` to `postgresql+psycopg://`
6. **Add** `?sslmode=require` at the end

**Example:**
```
postgresql+psycopg://username:password@ep-xxx.us-east-1.aws.neon.tech/neondb?sslmode=require
```

---

## 📝 How to Add in Vercel

1. **Go to Vercel Dashboard**
   - Visit: https://vercel.com/dashboard
   - Click on your project

2. **Navigate to Environment Variables**
   - Click **Settings** tab
   - Click **Environment Variables** (left sidebar)

3. **Add Each Variable**
   - Click **Add New**
   - Enter **Name** (exactly as shown)
   - Enter **Value** (copy from above)
   - Check all three: ✅ Production, ✅ Preview, ✅ Development
   - Click **Save**
   - Repeat for all 3 variables

4. **Redeploy** (if already deployed)
   - Go to **Deployments** tab
   - Click **⋯** (three dots) on latest deployment
   - Click **Redeploy**

---

## ✅ Quick Checklist

- [ ] Cloud PostgreSQL database created
- [ ] Database connection string obtained
- [ ] Connection string changed to `postgresql+psycopg://` format
- [ ] `GEMINI_API_KEY` added: `AIzaSyCjOD2NE6zDxi9IrXUMsbwvWcCYA_lSjvk`
- [ ] `SECRET_KEY` added: `310dfc0e3e2ad00593be4039fa8bc53c3c6f90ff8965c8069c11c6998ea3e45b`
- [ ] `DATABASE_URL` added (with cloud database connection string)
- [ ] All variables enabled for Production, Preview, Development
- [ ] Project redeployed

---

## 🎯 Summary

**Ready to add now:**
- ✅ `GEMINI_API_KEY` = `AIzaSyCjOD2NE6zDxi9IrXUMsbwvWcCYA_lSjvk`
- ✅ `SECRET_KEY` = `310dfc0e3e2ad00593be4039fa8bc53c3c6f90ff8965c8069c11c6998ea3e45b`

**Action needed:**
- ⚠️ Set up cloud PostgreSQL database first, then add `DATABASE_URL`

---

**Once you have your cloud database, you're ready to deploy!** 🚀

