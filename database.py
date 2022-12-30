from firebase_admin import credentials, firestore, initialize_app

# Initialize Firestore DB
cred = credentials.Certificate("keys.json")
default_app = initialize_app(cred)
db = firestore.client()
db_collection = db.collection('learning-gcp')
