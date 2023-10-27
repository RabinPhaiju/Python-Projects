import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
import pandas as pd

cred = credentials.Certificate('etech-1234-1f2417a825e4.json')
firebase_admin.initialize_app(cred)
firestore_db = firestore.client()

def add_update_data_firestore():
    doc_ref = firestore_db.collection('test').document('adsf')
    doc_ref.set({
        'first': 'rabin',
        'last': 'phaiju',
        'born': 1994 # while updating if remove a key will also remove in firestore
    })

    
def read_data_firestore():
    users_ref = firestore_db.collection('products')
    docs = users_ref.stream()

    for doc in docs:
        print(f'{doc.id} => {doc.to_dict()}')
    
def save_to_sheet():
    users_ref = firestore_db.collection('products')
    docs = users_ref.stream()
    doc_list = []
    for doc in docs:
        doc_list.append(doc.to_dict())
    pd.DataFrame(doc_list).to_csv('output.csv', header=True, index=False)

save_to_sheet()