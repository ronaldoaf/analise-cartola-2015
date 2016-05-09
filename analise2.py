import urllib2
import json

response = urllib2.urlopen('https://api.cartolafc.globo.com/atletas/mercado')
data = json.load(response)

for atleta in data['atletas']:
    if atleta['status_id']==7: print atleta['atleta_id'],atleta['preco_num']
