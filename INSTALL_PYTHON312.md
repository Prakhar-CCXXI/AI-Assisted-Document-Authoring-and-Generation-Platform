# How to Install Python 3.12 on Windows

## Method 1: Official Python Installer (Recommended)

1. **Download Python 3.12:**
   - Go to: https://www.python.org/downloads/release/python-3120/
   - Scroll down to "Files" section
   - Download: **Windows installer (64-bit)** (or 32-bit if needed)
   - File name: `python-3.12.0-amd64.exe` (or latest 3.12.x version)

2. **Run the Installer:**
   - Double-click the downloaded `.exe` file
   - **IMPORTANT:** Check the box "Add Python 3.12 to PATH" at the bottom
   - Click "Install Now" (or "Customize installation" if you want to change location)
   - Wait for installation to complete

3. **Verify Installation:**
   - Open a new Command Prompt or PowerShell window
   - Run: `python3.12 --version` or `py -3.12 --version`
   - You should see: `Python 3.12.x`

## Method 2: Using py launcher (Windows)

Windows has a `py` launcher that can manage multiple Python versions:

1. **Download and install Python 3.12** (same as Method 1)

2. **Use py launcher:**
   ```bash
   py -3.12 --version
   ```

3. **Create virtual environment with Python 3.12:**
   ```bash
   py -3.12 -m venv venv312
   ```

4. **Activate the virtual environment:**
   ```bash
   venv312\Scripts\activate
   ```

## Method 3: Using Microsoft Store

1. Open Microsoft Store
2. Search for "Python 3.12"
3. Click "Install"
4. Note: This method may have limitations with some packages

## After Installation

### Verify Both Versions Work:

```bash
# Check Python 3.13 (your current version)
python --version
# or
py -3.13 --version

# Check Python 3.12 (newly installed)
py -3.12 --version
```

### Create a Virtual Environment with Python 3.12:

```bash
# Navigate to your project directory
cd C:\Users\PRAKHAR\OneDrive\Desktop\OceanAI

# Create venv with Python 3.12
py -3.12 -m venv venv

# Activate it
venv\Scripts\activate

# Verify Python version in venv
python --version
# Should show: Python 3.12.x

# Install dependencies
pip install -r requirements.txt
```

## Troubleshooting

### If Python 3.12 is not found:
- Make sure you checked "Add Python to PATH" during installation
- Restart your terminal/command prompt after installation
- Try using `py -3.12` instead of `python`

### If you want to set Python 3.12 as default:
- You can create an alias or update your PATH
- Or always use `py -3.12` command

### Check installed Python versions:
```bash
py --list
```

This will show all installed Python versions on your system.



