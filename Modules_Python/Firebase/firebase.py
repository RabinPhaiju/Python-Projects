from firebase_config import get_firebase_config
import pyrebase

firebase = pyrebase.initialize_app(get_firebase_config())

auth = firebase.auth()
storage = firebase.storage()
realtime_db = firebase.database()

# Authentication
def login():
    email = 'test@test.com'
    password = 'test1234'
    try:
        log = auth.sign_in_with_email_and_password(email,password)
        print(log)
    except:
        print('error')
        
def signup():
    email = 'test@test5.com'
    password = 'test12345'
    try:
        sign = auth.create_user_with_email_and_password(email,password)
        print(sign)
    except:
        print('user already exist')
        
# Storage
def upload_file():
    filename = 'test.txt'
    cloud_path = 'test/files/test.txt'
    upload = storage.child(cloud_path).put(filename)
    print(upload)

def get_file_url():
    print(storage.child('test/files/test.txt').get_url(None))

def download_file():
    storage.child('test/files/test.txt').download("","download_file.txt")

# Realtime Database:
def push_data():
    data = {'name':'test','age':34,'address':'Bhaktapur'}
    # realtime_db.child('user').child('admin').child('my_own_id').set(data)
    realtime_db.child('user').child('customer').push(data)

def update_data():
    realtime_db.child('user').child('customer').child('-Mq7l-QOVsuJ8vxIgbl1').update({'name':'test_upate'})
    
def delete_data():
    realtime_db.child('user').child('customer').child('-Mq7l-QOVsuJ8vxIgbl1').remove()

def get_data():
    # users = realtime_db.child("user/admin").get()
    # users = realtime_db.child("user").child('admin').get()
    users = realtime_db.child("user").get()
    for user in users.each():
        print('val=',user.val(),'key=',user.key())

def read_data():
    # users = realtime_db.child("user").child('admin').order_by_child('name').equal_to('rabin').get()
    # users = realtime_db.child("user").child('admin').order_by_child('age').start_at(30).get()
    users = realtime_db.child("user").child('admin').order_by_child('name').get()
    for user in users.each():
        print('val=',user.val(),'key=',user.key())

# read_data()