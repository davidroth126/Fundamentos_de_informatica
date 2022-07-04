import requests

r = requests.get("https://dog.ceo/api/breeds/list/all")

# A_ El dominio al que estamos consultando es dog.ceo .

print("El status code es:",r.status_code) 

print("El content type es:", r.headers["Content-Type"])

breeds = requests.get("https://dog.ceo/api/breeds/list")

print("Se almacenan:",len(breeds.json()["message"]),"breeds.")

print(breeds.json()["message"][11])

# Esta es la url que esperaria para ver las imagenes de boxer por el hecho de que es el elemnto 11 https://dog.ceo/api/breeds/11/images ,
# tambien podria esperar."https://dog.ceo/api/breeds/boxer/images .

Boxer = (breeds.json()["message"][11])

with open("recursos/cocker_cute.png", 'w') as file:  
    file.write(str("https:\/\/images.dog.ceo\/breeds\/boxer\/28082007167-min.jpg"))

 # "https:\/\/images.dog.ceo\/breeds\/boxer\/28082007167-min.jpg"

