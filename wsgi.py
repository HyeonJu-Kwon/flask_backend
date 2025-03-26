import os
import sys

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from flask_backend.app import app

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'flask_backend')))

if __name__ == "__main__":
    app.run()

