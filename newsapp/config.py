import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	LANGUAGES = ['en', 'zh']

	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
	PC_UPLOAD_DIR = os.path.join(basedir, 'static/images')
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
	'sqlite:///' + os.path.join(basedir, 'newsdb.db')

	SQLALCHEMY_TRACK_MODIFICATIONS = False

