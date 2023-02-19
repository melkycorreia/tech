import requests
import pandas as pd

url = "http://exemplo.com/planilha.json"

response = requests.get(url)
data = pd.read_json(response.content)

# Aqui você pode adicionar a lógica para manipular os dados
