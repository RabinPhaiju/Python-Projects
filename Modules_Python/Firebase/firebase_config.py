import os
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('firebase_config.env')
load_dotenv(dotenv_path=dotenv_path)

def get_firebase_config():
    apiKey = os.getenv('apiKey')
    authDomain = os.getenv('authDomain')
    databaseURL = os.getenv('databaseURL')
    projectId = os.getenv('projectId')
    storageBucket = os.getenv('storageBucket')
    messagingSenderId = os.getenv('messagingSenderId')
    appId = os.getenv('appId')
    measurementId = os.getenv('measurementId')
    
    FirebaseConfig = {
        'apiKey':apiKey,
        'authDomain':authDomain,
        'databaseURL':databaseURL,
        'projectId':projectId,
        'storageBucket':storageBucket, 
        'messagingSenderId':messagingSenderId,
        'appId':appId,
        'measurementId':measurementId, 
    }
    
    return FirebaseConfig