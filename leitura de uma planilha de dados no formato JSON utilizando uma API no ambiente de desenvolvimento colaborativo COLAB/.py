import urllib.request
import json

url = "http://seu-usuario.github.io/seu-repositorio/dados"

response = urllib.request.urlopen(url)
data = json.loads(response.read())

# Aqui você pode adicionar a lógica para manipular os dados
