from os import lseek

import requests 

pedido = requests.get("https://macowins-server.herokuapp.com/prendas/1") #usamos get para solicitar algo al servidor(pido un recurso).
print(pedido)
print(pedido.json()) #json es un tipo de formato en el cual el servidor le devuelve las informacion al cliente.(es un diccionario)
#una aplicacion rest es un aplicacion en la cual se correlacionan las urls con los verbos https.

#"response[404]"el status code habla de como fue la conexion(como fue el estado de este pedido).

#cuando hacemos un request(pedido) nos devuelve:: 1_el status code.2_

print(pedido.headers) #el header tiene la metadata del pedido.

#status code         #"http.cat"
print(pedido.status_code)

