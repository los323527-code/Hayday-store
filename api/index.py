import os
import sys

# The Django project lives in ./shop when Vercel Root Directory is api-shop.
PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "shop"))
if PROJECT_DIR not in sys.path:
    sys.path.insert(0, PROJECT_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")

from shop.wsgi import application

# Vercel's Python runtime looks for a module-level WSGI app.
app = application
