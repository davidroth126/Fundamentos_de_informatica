import requests

r = requests.get("https://macowins-server.herokuapp.com/prendas/1")

#El dominio es macowins-server.herokuapp.com

print("El status code es:", r.status_code )
# el status code es de 200, nos devuelve en la terminal.

print("El content type es:", r.headers["Content-Type"]) # r.headers["Content-Type"] es el codigo para saber el content tyoe, igualmente lo tenemos que printear.

prendas = requests.get("https://macowins-server.herokuapp.com/prendas") 

print("Se almacenan:",len(prendas.json()),"prendas") # esto es para printear cuantas prendas tenemos.

print("El primer elemento de la url es ",(prendas.json()[0]),) # si quiero que me devuelva el primer elemento con su info. y aca vemos que es una lista con diccionario.

"https://macowins-server.herokuapp.com/prendas/10" # asi esperaria que sea la url para la prenda 10.


"https://macowins-server.herokuapp.com/ventas" # asi espero que sea la url para las ventas.

prenda1 = (prendas.json()[0])
with open(prenda1["tipo"]+".txt", 'w') as file:  
    file.write(str(prenda1))


# para crear un archivo y que guarde el script de los datos de la prenda 1. Nombrandolo con una de las llaves del diccionario. 