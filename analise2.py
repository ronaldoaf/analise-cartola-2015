import urllib2
import json

response = urllib2.urlopen('https://api.cartolafc.globo.com/atletas/mercado')
data = json.load(response)

#for atleta in data['atletas']:
#    if atleta['status_id']==7: print atleta['atleta_id'],atleta['preco_num']

#jogadores2016=[ {'id': atleta['atleta_id'],'preco':atleta['preco_num'], 'nome':atleta['apelido']} for atleta in data['atletas']  if atleta['status_id']==7 ]


#print jogadores2016

#with open('jogadores.json') as data_file: jogadores = json.load(data_file)


#jogadores2015=[ {'id':jog_id, 'preco':jogadores[jog_id][-1]['preco'] } for jog_id in jogadores.keys() ]


#jogadores2015=[ {'id': jog_id, 'preco': jogadores[jog_id][-1]['preco']}  for jog_id in jogadores.keys() if len(jogadores[jog_id])>0 and jogadores[jog_id][-1].has_key('preco') ]



#for jog16 in jogadores2016:
#    for jog15 in jogadores2015:
#        if int(jog16['id'])==int(jog15['id']): print jog16['id'], jog15['preco'],jog16['preco'],'"'+jog16['nome']+'"'


#jogadores2015=[ {'id': jog_id, 'preco': jogadores[jog_id][-1]['preco']}  for jog_id in jogadores.keys() if len(jogadores[jog_id])>0 and jogadores[jog_id][-1].has_key('preco') ]


for j in data['atletas']:    
    RB=j['scout']['RB'] if 'RB' in j['scout'] else 0
    if j['status_id']==7: print '"'+j['apelido']+'"', data['posicoes'][str(j['posicao_id'])]['nome'],j['jogos_num'], '"'+data['clubes'][ str(j['clube_id']) ]['nome']+'"',j['preco_num'],j['variacao_num'], '"' + data['clubes'][str(j['partida']['clube_casa_id'])]['nome']+' X '+data['clubes'][str(j['partida']['clube_visitante_id'])]['nome'] +'"', RB 


#for jog_id in jogadores.keys():
#    try:
#        print jogadores[jog_id][0]['preco']
#    except:
#        pass
