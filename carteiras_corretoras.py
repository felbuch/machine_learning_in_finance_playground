import requests

url = 'https://br.advfn.com/jornal/2021/04/abril-carteiras-recomendadas-de-todas-corretoras-bancos-e-casas-de-analises'
r = requests.get(ur)
print(r.text)