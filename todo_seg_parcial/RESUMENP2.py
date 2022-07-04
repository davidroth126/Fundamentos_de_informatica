#WEB


# INTERNET = Internet se podría definir como la red de redes de computadoras, 
# conectadas por medio de un cableado físico que permite intercambiar información entre todos sus usuarios.

# A la computadora que ejecuta el programa que proporciona el recurso o información se la denomina servidor
#  y a la computadora que consume un recurso o información se la denomina cliente. 

# WEB == La Web en particular, diminutivo de World Wide Web, es un conjunto de páginas interconectadas por las cuales podemos navegar.

# CLOUD COMPUTING = La computación en la nube o Cloud Computing es el consumo o prestación bajo demanda de recursos tecnologicos a través de Internet.


# PROTOCOLO DE COMUNICACION ENTRE EL SERVIDOR Y EL CLIENTE= HTTP:

#CARACTERISTICAS
#  Pedido-Respuesta: se abre una conexión por cada pedido, que surge del cliente, y el servidor procesa el pedido y responde, luego la cierra cuando ha enviado la respuesta
#  Stateless: el protocolo per-sé no maneja ninguna noción de memoria de pedidos anteriores
#  Textual: se intercambian mensajes de sólo texto
#  Basado en códigos de respuesta: incluso para los flujos de error; no hay memoria compartida, continuaciones, excepciones ni eventos

# PRESENTACION DE DATOS DEL SERVIDOR CORREN PARTE DEL CLIENTE.
# Lo que el servidor responde normalmente es el código fuente de una página escrita usando una combinación de lenguajes, 
# que es interpretado por un programa del cliente, el mismo programa que también es responsable de crear las conexiones HTTP.
# (El cliente se encarga de presentar (renderizar) la respuesta al usuario final)

# LAMADO NAVEGADOR / BROWSER = PROGRAMA ENCARGADO DE INTERPRETAR EL CODIGO DEL SERVIDOR.
# EJ= HTML, CSS, JS


############ 

# PRIMER PASO: (REQUEST / PEDIDO)
import requests

# r = requests.get('https://macowins-server.herokuapp.com/prendas/1')
# print(r.json())
# TE DA LA INFO QUE TIENE EL DOMINIO EN PRENDAS 1

# print(r.headers)
# transmiten información acerca del navegador del cliente, de la página solicitada, del servidor
# La primera línea es la línea del request, que contiene su información básica (método HTTP, URL y versión).

# print( r.status_code)
# es el codigo de estado o codigo de error: son una serie de códigos de tres cifras estandarizados y que están relacionados con una serie de determinados errores que pueden suceder al introducir en nuestro navegador una dirección web.
# por ej el 200 es que esta okey. el


# print(r.content)
# te va a impprimir el contentido del codigo 

# r = requests.get('https://macowins-server.herokuapp.com/prendas?tipo=saco')
# con el ?tipo ..... = traes todas las prendas que son sacos.

# r = requests.get('https://macowins-server.herokuapp.com/prendas?talle=40&tipo=pantalon')
# ahora agrego el & seria que CONSULTA el talle y el pantalon. (dos caracteristicas)


# URLs Y URIs
# https://macowins-server.herokuapp.com/ventas/?_page=3?
# ESTA ES UNA URL O DIRECCION

# UNA URL Es cualquier string con un formato particular llamado URI para que nos permita localizar un recurso (en internet)

# COMPUESTO de las URIs:
# un protocolo
# un dominio = es un nombre fácil de recordar asociado a una dirección IP 
# opcionalmente, un puerto
# una ruta
# opcionalmente, parámetros
# opcionalmente, un fragmento, que indica en que sección queremos obtener del recurso que estamos consultando.

# EJ DE URI ==> protocolo://dominio:puerto/ruta#fragmento?parametro1=valor1&parametro2=valor2



# requests.get('http://google.com:8902',timeout=5)
# el timeout es que va a esperar 5 segs a recibir una respuesta del dispositivo antes de volver a re-enviar una trama.
# aca da error porque el puerto al que estamos intentando conectarnos no es el adecuado. 
# en otro casoque puede que el dominio no exista en internet.

# Otra forma de llegar a una maquina a traves de un dominio.
import os

# hostname = "google.com"
# response = os.system("ping -c 1 " + hostname)

# cada computadora tiene un ip distinto a google.


# CABECERAS HTTP con HEADERS
# Las cabeceras HTTP y los códigos de estado son útiles para ayudar a los programas de intermediario 
# y cliente a comprender la información sobre las solicitudes y las respuestas para las aplicaciones.
# Las cabeceras HTTP contienen información de metadatos. 

# INFO QUE DA .headers:
# X-Powered-By: QUIEN: nos dice que software es el que está corriendo en el servidor. No siempre es muy confiable
# Content-Length: TAMAÑO: nos dice el tamaño de la respuesta
# Date: FECHA: nos dice la fecha en que se generó la respuesta
# Content-Type: TIPO: nos dice el tipo de contenido que estamos recibiendo, el cual podría ser: sonido, video, imagen, archivo css.
# content type: nos dice que formato tiene la respuesta que devuelve la api.


# una APLICACION WEB tiene un servidor responde pedidos x HTTP (VERBOS)

# VERBOS = GET (CONSULTA, TRAE), POST (AGREGA ELEMENTOS / PUBLICO), DELETE (UN ELEMENTO DE LA BASE), PUT (CAMBIAR)
# y un SITIO WEB es un conjunto de paginas web
# una pagina web = 1 html

# GET /ventas/: consultar todos (listar)
# DELETE /ventas/: borrar todos
# POST /ventas/: crear uno dentro de ventas

# EJEMPLO DE POST
# headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
# data =  { "tipo": "chomba", "talle": "XS" }
#  r = requests.post('https://macowins-server.herokuapp.com/prendas', data=json.dumps(data), headers=headers)
# PORQUE EL SERVIDOR necesita que le especifiquemos el tipo de contenido, para que cuando creemos algo sepa de qué tipo de cosa estamos hablando.



p = requests.get('https://ponyweb.ml/v1/character/all')

# print(p.json()["data"][0])
# es una lista de diccionarios, entonces le pido el primer elemento.

# print(p.json()["data"].keys)
# si lee este es un diccionario, y le pido que me de una lista de llaves.

# print("cantidad de ponies:",len(response.json()["data"]))
# para la cantidad de ponies

#print(" la app tiene:",len(p.json()["data"]), "elementos")
# CUANTOS ELEMENTOS TIENE ESTA LISTA.

# el ideal seria que sea www.ponyweb.com/ponies/44 (lo que esperabamos)
# O www.ponyweb.com/ponies?id=44

h = requests.get('https://ponyweb.ml/v1/song/all')

# print(h.json())

# para la cancion 40
print(h.json()["data"][39])

# el nombre de la cancion
print(h.json()["data"][39]["name"])

# PARA GUARDARLO EN UN ARCHIVO:
# response = requests.get("https://ponyweb.ml/v1/character/44")     (el url)
# pony44 = response.json()["data"][0]
#with open(pony44["name"]+".txt", 'w') as file:
#    file.write(str(pony44))


#############################################



# HTML
# Para presentar los datos provenientes del servidor del lado del cliente, 
# se utiliza HTML, que no es un lenguaje de programación, sino más bien un sitema de eqtiqueas 
# que está pensado para mostrar contenido.

# Un documento HTML está formado por partes:
# 1. Una línea que contiene información sobre la versión de HTML (no siempre),
# 2. Una cabecera (delimitada por el elemento HEAD)
# 3. Un cuerpo, con el contenido del documento (delimitado por el elemento BODY).
#Y todo el documento tiene que ir entre las etiquetas <html></html> e inicia con la etiqueta <!DOCTYPE html>






# <!DOCTYPE html>
# <html lang="en">
# <head>
#    <meta charset="UTF-8">
#    <meta http-equiv="X-UA-Compatible" content="IE=edge">
#    <meta name="viewport" content="width=device-width, initial-scale=1.0">
#    <link rel="stylesheet" href="style.css"> (con el nombre del archivo css)
#    <title>Document</title>
#</head>
#<body>
#    <section class="header">
#        <div>
#            <h1> La Mocha</h1>
#            <!-- Esto es un comentario-->
#            <h2> SI NO TENEMOS BUENOS PRECIOS  
#                <br>
#                ¿POR CUAL ESPERÁS BUENA CALIDAD?</h2>
#        </div>
        
#    </section>
#    <section class="sucursales">
#        <div> 
#         <h3> La Plata </h3>
#         <p>Calle Falsa 1243</p>
#        </div>
#    </section>

    
#</body>
#</html>

########
# si quiero que la mocha sea clickeble y te lleve a un link
#<h1>
#     <a href="https://google.com">La Mocha</a>
#</h1>


# una imagen
# <img src="lamocha.png" class="img1">


# si quiero que apretando la imagen me lleve a un link
# <a href="https://google.com">
#            <img src="lamocha.png" class="img1">
# </a>

# un boton que diga holaaa
# <button onclick="alert('holHOLAaa')">CLICKEAME</button>




# CSS
# Los documentos HTML pueden ser estilados, mediante el uso del lenguaje CSS.
# En estas se escriben los estilos que se deben aplicar a las diferentes partes del documentos HTML,


#body {
#    margin: 0;
#    padding: 0;
#    background-color: blue;
#}

#h1{
    
#    background-color: #eb1036;
#    width: 26%;
#    margin-left: -1%;
#    height: 61px;
#    padding-top: 10px;
#    padding-left: 28px;
#    font-size: 44px;
#}

#.header{
#    background-color: blue;
#    height: 18vw;


#}

#h2{
#    color: white;
#    padding: 0 0 0 20%;
#    font-size: 20px;
#    font-family:'Times New Roman', Times, serif
#}
#.sucursales{
#    background-color: antiquewhite;
#    width: 100%;
#    height: 15vw;
    
#}

#.sucursales div{
#    padding-left: 9%;
#    padding-top: 2%;
#}
#/* es un comentario */

