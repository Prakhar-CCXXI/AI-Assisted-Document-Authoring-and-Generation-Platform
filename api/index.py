"""
Vercel serverless function entry point for Flask application
This file wraps the Flask app to work with Vercel's serverless architecture
"""

import sys
import os

# Add the parent directory to the path so we can import app
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

# Import the Flask app
from app import app

# Vercel Python runtime expects the WSGI application
# Export as both 'app' and 'application' for compatibility
application = app

# For Vercel, we can also export directly
__all__ = ['app', 'application']

