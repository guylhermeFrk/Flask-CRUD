class Config:
	SECRET_KEY = '|Xef?qJ-xMt6SG>Wp#2LP`?]j%~MP='
	SQLALCHEMY_ECHO = False
	SQLALCHEMY_TRACK_MODIFICATIONS = False


class LocalConfig(Config):
	AMBIENTE = 'Local'
	DEBUG = True
	PORT = 5000
	SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgresFrk95@localhost:5432/flask_crud'