from pymongo import MongoClient

# Connect to the database
client = MongoClient("mongodb://localhost:27017/sentimental_chats_db")

def connectCollection(database, collection):
    #conecta con mongodb y devuelve la base de datos y la colección 
    db = client[database]
    coll = client.get_default_database()[collection]
    return db, coll




db, users_coll = connectCollection('sentimental_chats_db', 'users')
db, chats_coll = connectCollection('sentimental_chats_db', 'chats')
db, ponis_coll = connectCollection('sentimental_chats_db', 'mylittlepony')