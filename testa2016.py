import urllib2
import json

response = urllib2.urlopen('https://api.cartolafc.globo.com/atletas/mercado')
data = json.load(response)


results=[]
for j in data['atletas']:    
    RB=j['scout']['RB'] if 'RB' in j['scout'] else 0
    A_G=j['scout']['G'] if 'G' in j['scout'] else 0 + j['scout']['A'] if 'A' in j['scout'] else 0
    #if j['status_id']==7: print '"'+j['apelido']+'"', data['posicoes'][str(j['posicao_id'])]['nome'],j['jogos_num'], '"'+data['clubes'][ str(j['clube_id']) ]['nome']+'"',j['preco_num'],j['variacao_num'], '"' + data['clubes'][str(j['partida']['clube_casa_id'])]['nome']+' X '+data['clubes'][str(j['partida']['clube_visitante_id'])]['nome'] +'"', RB 
    results+=[['"'+j['apelido']+'"', data['posicoes'][str(j['posicao_id'])]['nome'],j['jogos_num'], '"'+data['clubes'][ str(j['clube_id']) ]['nome']+'"',j['preco_num'],j['variacao_num'], '"' + data['clubes'][str(j['partida']['clube_casa_id'])]['nome']+' X '+data['clubes'][str(j['partida']['clube_visitante_id'])]['nome'] +'"', RB,A_G ]
]
for e in sorted(results, key=lambda x: x[-1], reverse=True):
    for i in e:
        print i,

    print ""
