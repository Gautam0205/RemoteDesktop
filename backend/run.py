# run.py (or the script where you run the Flask application)
from app import app, db

if __name__ == "__main__":
    # Run the Flask application in debug mode
    app.run(debug=True)
