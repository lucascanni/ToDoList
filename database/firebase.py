import firebase_admin, pyrebase
from firebase_admin import credentials
from dotenv import dotenv_values, load_dotenv
import os
import json

load_dotenv()

# config={
#     "FIREBASE_SERVICE_ACCOUNT_KEY": os.getenv("FIREBASE_SERVICE_ACCOUNT_KEY"),
#     "FIREBASE_CONFIG": os.getenv("FIREBASE_CONFIG")
# }

config = dotenv_values("docker-env")

cred = firebase_admin.credentials.Certificate(json.loads(config['FIREBASE_SERVICE_ACCOUNT_KEY']))
firebase_admin.initialize_app(cred)

firebase = pyrebase.initialize_app(json.loads(config['FIREBASE_CONFIG']))
db=firebase.database()