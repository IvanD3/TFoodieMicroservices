import pymongo
import dns
import json
from bson.json_util import loads, dumps
from bson.objectid import ObjectId
def listaRecetas(request):
    rquery = request.get_json()
    miDB = conexionDB()
    return consultaRecetasPorID(rquery, coleccion(miDB,"ListaCompra"), coleccion(miDB,"Receta"))

def conexionDB():
    claveDB = #Aquí va la clave de servicio de MongoDB
    cliente = pymongo.MongoClient(claveDB)
    return cliente["Recetas"]
def coleccion(miDB,coleccion):
    return miDB[coleccion]
def consultaRecetasPorID(rquery,miColeccionFavoritos,miColeccionRecetas):
    mydoc = miColeccionFavoritos.find(rquery)
    consulta_str = []
    for x in mydoc:
        consulta_str.append(dumps(consultaRecetaEnRecetas(x["_idReceta"], miColeccionRecetas)))
    return dumps(consulta_str)
def consultaRecetaEnRecetas(idReceta, miColeccion):
    return miColeccion.find_one({"_id": ObjectId(idReceta)})