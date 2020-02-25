from src.MongoConections import db, chats_coll, users_coll, ponis_coll
from flask import request
from src.errorHandler import jsonErrorHandler
from bson.json_util import dumps


@jsonErrorHandler
def mensList(chat_id):
    chats=(chats_coll.distinct("_id"))
    if int(chat_id) in chats:
        mensajes=chats_coll.find({"_id":int(chat_id)},{"_id":0,"mensajes":1})
        return dumps(mensajes)
    else:
        return "No existe el chat"