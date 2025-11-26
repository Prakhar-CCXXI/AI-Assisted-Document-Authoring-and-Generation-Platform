# Vercel Environment Variables - Ready to Copy

## ⚠️ IMPORTANT: Database URL Issue

Your current database URL uses `localhost`, which **will NOT work on Vercel**. Vercel runs in the cloud and cannot connect to your local machine.

**You need to set up a cloud PostgreSQL database first.**

---

## 🔑 Environment Variables for Vercel

### Variable 1: DATABASE_URL

**⚠️ Your current URL won't work:**
```
postgresql://your_username:PostgreSQL1036@localhost:5432/docxbuilder
```

**You need a cloud database URL. Here's how to get one:**

#### Option 1: Vercel Postgres (Easiest - Recommended)
1. Go to your Vercel project dashboard
2. Click **Storage** tab
3. Click **Create Database** → **Postgres**
4. Create database (free tier available)
5. Copy the connection string
6. It will automatically be formatted correctly

#### Option 2: Supabase (Free Tier)
1. Go to [supabase.com](https://supabase.com)
2. Create account and new project
3. Go to **Project Settings** → **Database**
4. Copy **Connection string** → **URI**
5. Change `postgresql://` to `postgresql+psycopg://`

#### Option 3: Neon (Free Tier)
1. Go to [neon.tech](https://neon.tech)
2. Create account and new project
3. Go to **Connection Details**
4. Copy connection string
5. Change `postgresql://` to `postgresql+psycopg://`
6. Add `?sslmode=require` at the end

**Format for Vercel:**
```
postgresql+psycopg://username:password@host:port/database_name?sslmode=require
```

---

### Variable 2: GEMINI_API_KEY

**Name:** `GEMINI_API_KEY`

**Value:**
```
AIzaSyCjOD2NE6zDxi9IrXUMsbwvWcCYA_lSjvk
```

**Status:** ✅ Ready to use

---

### Variable 3: SECRET_KEY

**Name:** `SECRET_KEY`

**Value:**
```
310dfc0e3e2ad00593be4039fa8bc53c3c6f90ff8965c8069c11c6998ea3e45b
```

**Status:** ✅ Ready to use

---

## 📝 Step-by-Step: Add to Vercel

1. **Go to Vercel Dashboard**
   - Visit: https://vercel.com/dashboard
   - Click on your project (or create new one)

2. **Navigate to Environment Variables**
   - Click **Settings** tab
   - Click **Environment Variables** in left sidebar

3. **Add GEMINI_API_KEY**
   - Click **Add New**
   - **Name:** `GEMINI_API_KEY`
   - **Value:** `AIzaSyCjOD2NE6zDxi9IrXUMsbwvWcCYA_lSjvk`
   - Check: ✅ Production, ✅ Preview, ✅ Development
   - Click **Save**

4. **Add SECRET_KEY**
   - Click **Add New**
   - **Name:** `SECRET_KEY`
   - **Value:** `310dfc0e3e2ad00593be4039fa8bc53c3c6f90ff8965c8069c11c6998ea3e45b`
   - Check: ✅ Production, ✅ Preview, ✅ Development
   - Click **Save**

5. **Add DATABASE_URL** (After setting up cloud database)
   - Click **Add New**
   - **Name:** `DATABASE_URL`
   - **Value:** Paste your cloud database connection string
   - **Important:** Must start with `postgresql+psycopg://`
   - Check: ✅ Production, ✅ Preview, ✅ Development
   - Click **Save**

6. **Redeploy** (if project already deployed)
   - Go to **Deployments** tab
   - Click **⋯** (three dots) on latest deployment
   - Click **Redeploy**

---

## ✅ Quick Checklist

- [ ] Cloud PostgreSQL database created
- [ ] Database connection string obtained
- [ ] Connection string changed to `postgresql+psycopg://` format
- [ ] `GEMINI_API_KEY` added to Vercel
- [ ] `SECRET_KEY` added to Vercel
- [ ] `DATABASE_URL` added to Vercel (with cloud database)
- [ ] All variables enabled for Production, Preview, Development
- [ ] Project redeployed

---

## 🚀 Recommended: Use Vercel Postgres

The easiest option is to use **Vercel Postgres** because:
- ✅ Integrated directly with Vercel
- ✅ Automatically formatted connection string
- ✅ Free tier available
- ✅ No SSL configuration needed
- ✅ Connection string automatically added as environment variable

**Steps:**
1. In your Vercel project dashboard
2. Click **Storage** → **Create Database** → **Postgres**
3. Create database
4. Vercel will automatically add `POSTGRES_URL` or `DATABASE_URL`
5. You can use that, or copy it and add as `DATABASE_URL`

---

## 📋 Summary

**Ready to add now:**
- ✅ `GEMINI_API_KEY` = `AIzaSyCjOD2NE6zDxi9IrXUMsbwvWcCYA_lSjvk`
- ✅ `SECRET_KEY` = `310dfc0e3e2ad00593be4039fa8bc53c3c6f90ff8965c8069c11c6998ea3e45b`

**Need to set up first:**
- ⚠️ `DATABASE_URL` = Set up cloud PostgreSQL database first

---

**Once you have your cloud database URL, you're all set!** 🎉

