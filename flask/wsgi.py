import os

from dotenv import load_dotenv

from app import app

load_dotenv()
app.secret_key = os.environ.get("SECRET_KEY")

if __name__ == "__main__":
    app.run(host=os.environ.get("FLASK_SERVER_HOST"), port=os.environ.get("FLASK_SERVER_PORT"),
            debug=os.environ.get("FLASK_SERVER_DEBUG"))
