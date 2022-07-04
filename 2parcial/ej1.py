import requests

r = requests.get("https://dog.ceo/api/breeds/list/all")

# A_ El dominio al que estamos consultando es dog.ceo .

print("El status code es:",r.status_code) 

print("El content type es:", r.headers["Content-Type"])
