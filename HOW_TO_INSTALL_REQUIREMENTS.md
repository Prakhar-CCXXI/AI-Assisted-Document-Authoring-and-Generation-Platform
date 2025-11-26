# How to Install Requirements File

## Quick Installation

### Step 1: Open Terminal/Command Prompt

**Windows:**
- Press `Win + R`, type `cmd` or `powershell`, press Enter
- Or search for "Command Prompt" or "PowerShell" in Start menu

**Mac/Linux:**
- Press `Cmd + Space` (Mac) or `Ctrl + Alt + T` (Linux)
- Type "Terminal" and press Enter

### Step 2: Navigate to Project Directory

```bash
cd "C:\Users\PRAKHAR\OneDrive\Desktop\AI-Assisted-Document-Authoring-and-Generation-Platform"
```

**Or if you're already in the project folder, skip this step.**

### Step 3: Install Requirements

**Basic Installation:**
```bash
pip install -r requirements.txt
```

**If you get permission errors, use:**
```bash
pip install --user -r requirements.txt
```

**For Python 3 specifically (if you have multiple Python versions):**
```bash
python -m pip install -r requirements.txt
```

**Or:**
```bash
python3 -m pip install -r requirements.txt
```

---

## Recommended: Using Virtual Environment

### Why Use Virtual Environment?
- Isolates project dependencies
- Prevents conflicts with other projects
- Cleaner project management

### Step-by-Step with Virtual Environment

#### 1. Create Virtual Environment

**Windows:**
```bash
python -m venv venv
```

**Mac/Linux:**
```bash
python3 -m venv venv
```

#### 2. Activate Virtual Environment

**Windows (Command Prompt):**
```bash
venv\Scripts\activate
```

**Windows (PowerShell):**
```bash
venv\Scripts\Activate.ps1
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

**You'll see `(venv)` in your terminal prompt when activated.**

#### 3. Install Requirements

```bash
pip install -r requirements.txt
```

#### 4. Deactivate (when done)

```bash
deactivate
```

---

## Troubleshooting

### Problem: "pip is not recognized"

**Solution:**
```bash
python -m pip install -r requirements.txt
```

**Or install pip first:**
```bash
python -m ensurepip --upgrade
```

### Problem: "Permission denied" or "Access denied"

**Solution 1: Use --user flag**
```bash
pip install --user -r requirements.txt
```

**Solution 2: Run as Administrator (Windows)**
- Right-click Command Prompt → "Run as administrator"
- Then run: `pip install -r requirements.txt`

**Solution 3: Use virtual environment (Recommended)**
- Follow the virtual environment steps above

### Problem: "No module named 'pip'"

**Solution:**
```bash
python -m ensurepip --upgrade
python -m pip install --upgrade pip
```

### Problem: "Python version not found"

**Solution:**
- Make sure Python is installed
- Check installation: `python --version` or `python3 --version`
- If not installed, download from python.org

### Problem: "Package installation fails"

**Solution 1: Upgrade pip first**
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

**Solution 2: Install packages one by one**
- Open requirements.txt
- Install each package individually to identify the problematic one

**Solution 3: Check Python version**
- Some packages require Python 3.8+
- Check: `python --version`
- This project requires Python 3.12 (see runtime.txt)

---

## What Gets Installed

Your `requirements.txt` contains:

```
Flask==3.0.0                    # Web framework
Flask-SQLAlchemy==3.1.1        # Database ORM
Werkzeug==3.0.1                # Security utilities
psycopg[binary]==3.2.13        # PostgreSQL adapter
python-docx==1.1.0             # Word document generation
google-generativeai==0.3.2     # Google Gemini AI
python-pptx==0.6.23            # PowerPoint generation
python-dotenv==1.0.0           # Environment variable management
```

**Total:** 8 packages + their dependencies

---

## Verify Installation

After installation, verify packages are installed:

```bash
pip list
```

You should see all packages from requirements.txt in the list.

**Or check specific package:**
```bash
pip show flask
pip show google-generativeai
```

---

## Complete Installation Example

```bash
# 1. Navigate to project
cd "C:\Users\PRAKHAR\OneDrive\Desktop\AI-Assisted-Document-Authoring-and-Generation-Platform"

# 2. Create virtual environment (optional but recommended)
python -m venv venv

# 3. Activate virtual environment
venv\Scripts\activate

# 4. Upgrade pip
python -m pip install --upgrade pip

# 5. Install requirements
pip install -r requirements.txt

# 6. Verify installation
pip list
```

---

## Quick Reference

| Command | Description |
|--------|-------------|
| `pip install -r requirements.txt` | Install all packages |
| `pip list` | Show installed packages |
| `pip show <package>` | Show package details |
| `pip uninstall <package>` | Remove a package |
| `pip freeze > requirements.txt` | Save current packages |

---

## Next Steps After Installation

1. **Set up environment variables:**
   - Create `.env` file or set environment variables
   - `DATABASE_URL` - PostgreSQL connection string
   - `GEMINI_API_KEY` - Google Gemini API key
   - `SECRET_KEY` - Flask secret key

2. **Initialize database:**
   ```bash
   python init_db.py
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```

---

**Installation complete!** Your project dependencies are now installed. 🎉

