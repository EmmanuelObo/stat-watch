from celery.schedules import crontab
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from decouple import config

db = SQLAlchemy()


def generate_app():
	app = Flask(__name__, template_folder='../templates', static_folder='../static')
	app.config['SECRET_KEY'] = config('SECRET_KEY')
	app.config['SQLALCHEMY_DATABASE_URI'] = config('SQLALCHEMY_DATABASE_URI')
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config('SQLALCHEMY_TRACK_MODIFICATIONS', True)
	app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
	app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'
	app.config['CELERY_TIMEZONE'] = 'US/Eastern'
	app.config['CELERYBEAT_SCHEDULE'] = {
		"query-player-names": {
			"task": "task.update_player",
			"schedule": crontab(hour=22, minute=00)
		}
	}
	db.init_app(app)
	return app


app = generate_app()
