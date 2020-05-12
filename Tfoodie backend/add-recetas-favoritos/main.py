import pymongo
import dns
import json
from bson.json_util import loads, dumps
from bson.objectid import ObjectId
#Método que añade una relación de favoritos entre usuario y receta
#Recibiremos en la petición un json que incluirá:
#id de usuario de Firebase
#id de receta en su base de datos
def addFavoritos(request):
    request_json = request.get_json(silent=True)
    request_args = request.args
    if request_json and '_idUsuario' in request_json and '_idReceta' in request_json:
        idUsuario = request_json["_idUsuario"]
        idReceta = request_json["_idReceta"].strip("{$oid: }")
    elif request_args and '_idUsuario' in request_json and '_idReceta' in request_json:
        idUsuario = request_args["_idUsuario"]
        idReceta = request_args["_idReceta"].strip("{$oid: }")
    miDB = conexionDB()
    registro = {"_idUsuario" : idUsuario,"_idReceta" : idReceta}
    coleccion(miDB,"Favoritos").insert_one(registro)
#Método que establece conexión con el documento "Recetas" de nuestra base de datos MongoDB
def conexionDB():
    claveDB = #Aquí va la clave de servicio de MongoDB
    cliente = pymongo.MongoClient(claveDB)
    return cliente["Recetas"]
#Método que conecta con una colección concreta
def coleccion(miDB,coleccion):
    return miDB[coleccion]
#Método que limpia el texto para quedarnos con el id en limpio
def formateoIdReceta(idReceta):
    recetaFotmateada = idReceta.strip("{$oid: }")
    return recetaFotmateada
#Método que da formato al registro
def formatoRegistro(usuarioReceta):
    registro = {"_idUsuario" : usuarioReceta["_idUsuario"],"_idReceta" : formateoIdReceta(usuarioReceta["_idReceta"])}
    return registro
#Método que inserta una relacion entre usuario y receta en una colección
#En este caso particular, la colección será "Favoritos"
def insertar(coleccion, usuarioReceta):
    idUsuario = usuarioReceta["_idUsuario"]
    idReceta = usuarioReceta["_idReceta"].strip("{$oid: }")
    registro = {"_idUsuario" : idUsuario}
    coleccion.insert_one(registro)