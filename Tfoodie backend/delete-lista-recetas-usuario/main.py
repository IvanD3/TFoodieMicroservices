import pymongo
import dns
import json
from bson.json_util import loads, dumps
from bson.objectid import ObjectId
#Método que añade una relación de favoritos entre usuario y receta
#Recibiremos en la petición un json que incluirá:
#id de usuario de Firebase
#id de receta en su base de datos
def deleteListaCompraUsuario(relacion):
    usuarioReceta = relacion.get_json()
    miDB = conexionDB()
    #TODO: comprobar que la receta no esté ya en la base de datos
    eliminar(coleccion(miDB,"ListaCompra"),usuarioReceta)

#Método que establece conexión con el documento "Recetas" de nuestra base de datos MongoDB
def conexionDB():
    claveDB = #Aquí va la clave de servicio de MongoDB
    cliente = pymongo.MongoClient(claveDB)
    return cliente["Recetas"]
#Método que conecta con una colección concrta
def coleccion(miDB,coleccion):
    return miDB[coleccion]

def formatoRegistro(usuarioReceta):
    return {"_idUsuario" : usuarioReceta["_idUsuario"]}
#Método que inserta una relacion entre usuario y receta en una colección
#En este caso particular, la colección será "Favoritos"
def eliminar(coleccion, usuarioReceta):
    registro = formatoRegistro(usuarioReceta)
    coleccion.delete_many(registro)