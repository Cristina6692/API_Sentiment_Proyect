from src.MongoConections import db, chats_coll, users_coll, ponis_coll
from flask import request
from src.errorHandler import jsonErrorHandler


def insertUser(u_name):
    #Comprueba si ya existe ese nombre y si no crea un nuevo usuario.
    names = (users_coll.distinct("user_name"))
    if u_name in names:
        return "El usuario ya existe"
    else:
        user_info = {"user_name":u_name}
        users_coll.insert_one(user_info)
        
        return "Usuario creado"

@jsonErrorHandler
def insertChat(c_name):
    #Crea un nuevo chat 
    chats = list(chats_coll.distinct('chat_name'))
    print(chats)
    if c_name in chats:
        return 'El chat ya existe'
    else:
        if chats:
            n = max(chats_coll.distinct('_id'))+1
            chat_info = {'chat_name': c_name,
                    '_id': int(n),
                    'user_name':[],
                    'mensajes':[]}
            chats_coll.insert_one(chat_info)

        else:
            n = 1

        chat_info = {'chat_name': c_name,
                        '_id': int(n),
                        'user_name':[],
                        'mensajes':[]}
        chats_coll.insert_one(chat_info)
    return 'Se ha creado un nuevo chat'


@jsonErrorHandler
def addUserToChat(u_name, c_id):
    #inserta usuario en chat
    names = (chats_coll.distinct('user_name'))
    if u_name in names:
        return f'{u_name} ya está en el grupo'
    else:
        chats_coll.update({'_id':int(c_id)},{'$push':{'user_name':u_name}})
        return f'{u_name} ha entrado en el grupo {c_id}'


@jsonErrorHandler
def addTextToUser(chat_id):
    #inserta el mensaje de un usuario en un chat
    user = request.args.get('user_name')
    texto = request.args.get('texto')
    names = (chats_coll.distinct('user_name'))
    if user in names:
        chats_coll.update({'_id':int(chat_id)},{'$push':{'mensajes':{'autor':user, 'texto':texto}}})
        return 'Usuario en el grupo, se ha añadido su mensaje'
    else:
        return 'El usuario no está en el grupo'
    