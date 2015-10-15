import pymongo
import os



CONNECTION_STRING = "mongodb://210.45.66.91"  # replace it with your settings
CONNECTION = pymongo.MongoClient(CONNECTION_STRING)

'''Leave this as is if you dont have other configuration'''
DATABASE = CONNECTION.databank
POSTS_COLLECTION = DATABASE.posts
APPLICATIONS_COLLECTION = DATABASE.applications
USERS_COLLECTION = DATABASE.users
SETTINGS_COLLECTION = DATABASE.settings
MOLECULES_PATH='databank'

MAIL_SERVER = 'mail.ustc.edu.cn'
MAIL_PORT =  25
MAIL_USE_TLS = False
MAIL_USE_SSL = False
MAIL_USERNAME = 'lhrkkk@mail.ustc.edu.cn'
MAIL_PASSWORD = 'starnada'
DEFAULT_MAIL_SENDER = 'lhr'


SECRET_KEY = ""
basedir = os.path.abspath(os.path.dirname(__file__))
secret_file = os.path.join(basedir, '.secret')
if os.path.exists(secret_file):
    # Read SECRET_KEY from .secret file
    f = open(secret_file, 'r')
    SECRET_KEY = f.read().strip()
    f.close()
else:
    # Generate SECRET_KEY & save it away
    SECRET_KEY = os.urandom(24)
    f = open(secret_file, 'w')
    f.write(SECRET_KEY)
    f.close()
    # Modeify .gitignore to include .secret file
    gitignore_file = os.path.join(basedir, '.gitignore')
    f = open(gitignore_file, 'a+')
    if '.secret' not in f.readlines() and '.secret\n' not in f.readlines():
        f.write('.secret\n')
    f.close()

LOG_FILE = "app.log"

DEBUG = True  # set it to False on production