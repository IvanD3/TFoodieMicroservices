import pymongo
import dns
from bson.json_util import loads, dumps
import math
import random
import json
def recetaRandom30(request):
    rquery = request.get_json()
    claveDB = #Aquí va la clave de servicio de MongoDB
    cliente = pymongo.MongoClient(claveDB)
    #Nombre de la base de datos
    db = "Recetas"
    #Nombre de la coleccion
    coleccion = "Receta"
    miDB = cliente[db]
    base = miDB[coleccion]
    consulta = []
    N = base.count()
    R = 0
    #Lio de narices
    for i in range(0,30):
        R = random.randrange(N)
        consulta_str = dumps(base.find(rquery).limit(1).skip(R))
        consulta_json = json.loads(consulta_str)
        consulta.append(json.dumps(consulta_json[0]))
        #print(loads(consulta))
    consulta_json = dumps(consulta)
    return consulta_json