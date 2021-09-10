import pickle
import glob

def save_obj(obj, name):
    with open('db/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name):
    with open('db/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)


def load_database():

    if len(glob.glob('db/*')) == 0:
        print("No Database Found.")
        return {}
    
    else:
        db = load_obj('db')
        return db

def save_database(db):
    save_obj(db,'db')