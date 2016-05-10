import urllib2
import json

response = urllib2.urlopen('https://api.cartolafc.globo.com/atletas/mercado')
data = json.load(response)

#for atleta in data['atletas']:
#    if atleta['status_id']==7: print atleta['atleta_id'],atleta['preco_num']

jogadores2016=[ {'id': atleta['atleta_id'],'preco':atleta['preco_num'], 'nome':atleta['apelido']} for atleta in data['atletas']  if atleta['status_id']==7 ]


#print jogadores2016

with open('jogadores.json') as data_file: jogadores = json.load(data_file)


#jogadores2015=[ {'id':jog_id, 'preco':jogadores[jog_id][-1]['preco'] } for jog_id in jogadores.keys() ]


jogadores2015=[ {'id': jog_id, 'preco': jogadores[jog_id][-1]['preco']}  for jog_id in jogadores.keys() if len(jogadores[jog_id])>0 and jogadores[jog_id][-1].has_key('preco') ]



for jog16 in jogadores2016:
    for jog15 in jogadores2015:
        if int(jog16['id'])==int(jog15['id']): print jog16['id'], jog15['preco'],jog16['preco'],'"'+jog16['nome']+'"'

