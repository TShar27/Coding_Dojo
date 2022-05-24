from flask_app import app
from flask_app.controllers import user_controllers
from flask_app.models.ninjas import Ninja

if __name__ == "__main__":
    app.run(debug = True,port=5001)