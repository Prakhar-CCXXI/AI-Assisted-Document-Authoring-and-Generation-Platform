# Create Your .env File

## 📄 .env File Content

Create a file named `.env` in your project root with this exact content:

```
DATABASE_URL=postgresql+psycopg://your_username:PostgreSQL1036@localhost:5432/docxbuilder
GEMINI_API_KEY=AIzaSyCjOD2NE6zDxi9IrXUMsbwvWcCYA_lSjvk
SECRET_KEY=310dfc0e3e2ad00593be4039fa8bc53c3c6f90ff8965c8069c11c6998ea3e45b
```

## 📝 How to Create the File

### Option 1: Manual Creation
1. Create a new file in your project root
2. Name it exactly: `.env` (with the dot at the beginning)
3. Copy and paste the content above
4. Save the file

### Option 2: Using Command Line

**Windows (PowerShell):**
```powershell
@"
DATABASE_URL=postgresql+psycopg://your_username:PostgreSQL1036@localhost:5432/docxbuilder
GEMINI_API_KEY=AIzaSyCjOD2NE6zDxi9IrXUMsbwvWcCYA_lSjvk
SECRET_KEY=310dfc0e3e2ad00593be4039fa8bc53c3c6f90ff8965c8069c11c6998ea3e45b
"@ | Out-File -FilePath .env -Encoding utf8
```

**Mac/Linux:**
```bash
cat > .env << 'EOF'
DATABASE_URL=postgresql+psycopg://your_username:PostgreSQL1036@localhost:5432/docxbuilder
GEMINI_API_KEY=AIzaSyCjOD2NE6zDxi9IrXUMsbwvWcCYA_lSjvk
SECRET_KEY=310dfc0e3e2ad00593be4039fa8bc53c3c6f90ff8965c8069c11c6998ea3e45b
EOF
```

## ⚠️ Important Notes

1. **Vercel doesn't use .env files directly** - You still need to add these values in Vercel Dashboard → Settings → Environment Variables

2. **Database URL Issue**: Your database URL uses `localhost` which **won't work on Vercel**. You need a cloud PostgreSQL database. See `VERCEL_ENV_IMPORT.md` for details.

3. **File Location**: The `.env` file should be in your project root (same folder as `app.py`)

4. **Don't Commit**: Make sure `.env` is in your `.gitignore` file (it should be already)

## 📋 Exact Content (Copy This)

```
DATABASE_URL=postgresql+psycopg://your_username:PostgreSQL1036@localhost:5432/docxbuilder
GEMINI_API_KEY=AIzaSyCjOD2NE6zDxi9IrXUMsbwvWcCYA_lSjvk
SECRET_KEY=310dfc0e3e2ad00593be4039fa8bc53c3c6f90ff8965c8069c11c6998ea3e45b
```

## ✅ Verification

After creating the file, verify it exists:
- **Windows**: `dir .env` or check in File Explorer
- **Mac/Linux**: `ls -la .env`

The file should contain exactly 3 lines (one for each variable).

---

**The content is ready! Create the `.env` file manually with the content above.** 📝

