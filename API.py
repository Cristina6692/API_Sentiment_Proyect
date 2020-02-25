from flask import Flask, request
from src.chats_post import insertUser, insertChat, addUserToChat, addTextToUser
from src.chats_get import mensList
from src.MongoConections import db, chats_coll, users_coll, ponis_coll
from src.errorHandler import jsonErrorHandler

app = Flask(__name__)
# Connect to the database

'''----POST----'''

@app.route('/insert/user/<u_name>')
@jsonErrorHandler
def newUser(u_name):
    #inserta usuario en la colección users
    return insertUser(u_name)

@app.route('/insert/chat/<ChatName>')
def newChat(ChatName):
    #inserta un nuevo chat 
    return insertChat(ChatName)

@app.route('/insert/user/<UserName>/toChat/<ChatID>')
def UserToChat(UserName,ChatID):
    #inserta un usuario a un chat, si el usuario no existe lo crea
    return addUserToChat(UserName,ChatID)

@app.route('/insert/userMessageInChat/<ChatID>')
def mesFromUserToChat(ChatID):
    #inserta mensajes de diferentes usuarios en un chat al que pertenezcan
    return addTextToUser(ChatID)


'''----GET----'''

@app.route('/chat/<ChatID>/list')
def mensajesChat(ChatID):
    #devuelve la lista de los mensajes del chat 
    return mensList(ChatID)


app.run("0.0.0.0", 5000, debug=True)