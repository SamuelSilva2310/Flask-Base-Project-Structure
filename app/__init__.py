"""Initialize necessary

app, databases ...

"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config 

db = SQLAlchemy() #Initialize database


def create_app(config_class=Config):
	app = Flask(__name__)
	app.config.from_object(Config)


	db.init_app(app)


	# Import Blueprints
	from app.users.routes import users # import the blueprint instance


	# Register blueoprints to our app 
	app.register_blueprint(users)

	return app
