from character_app import app
from character_app.controllers import users, characters, battles

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)
