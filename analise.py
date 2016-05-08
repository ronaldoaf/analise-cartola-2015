# -*- coding: cp1252 -*-
import json



with open('jogadores.json') as data_file: jogadores = json.load(data_file)
with open('selecao.json') as data_file: selecao = json.load(data_file)
with open('posicoes.json') as data_file: posicoes = json.load(data_file)

def getPreco(cod, rodada):
    for reg in jogadores[str(cod)]:
        if int(reg['rodada'].split('.')[1])==int(rodada):
            return reg['preco']-reg['preco_variacao']

def getValorizacao(cod, rodada):
    for reg in jogadores[str(cod)]:
        if int(reg['rodada'].split('.')[1])==int(rodada):
            return reg['preco_variacao']  




"""
#Relacao Preço do Time valorização
precos=[]
for time in selecao.keys():
    
    try:        
        selecao_time_rodada_ids=[e['id'] for e in selecao[time]['1'] ]
        print time, sum(getPreco( cod ,1) for cod in  selecao_time_rodada_ids  ), sum(getValorizacao( cod ,1) for cod in  selecao_time_rodada_ids  )
        
    except:
        pass
"""

for jog_id in jogadores.keys():
    
    if len(jogadores[jog_id])>=1:
        reg=jogadores[jog_id][0]           
        if reg['rodada']=='2015.01' and reg['atleta_jogou']==True: print reg['preco']-reg['preco_variacao'], reg['preco_variacao'] 
  




"""

goleiros_1_rodada=[]
for cod in posicoes['goleiro']:
    for reg in jogadores[cod]:
        if reg['rodada']=='2015.04' and reg['atleta_jogou']==True:
            goleiros_1_rodada+=[  {'preco': reg['preco']-reg['preco_variacao'] , 'cod':  cod}  ]


selecao_goleiros_1_rodada=[]
#print goleiros_1_rodada
for time in selecao.keys():
    if '4' in selecao[time]:
        try:
            selecao_goleiros_1_rodada+=[ selecao[time]['4'][0]['id'] ]
        except:
            pass


   
for jogador in goleiros_1_rodada:
    print jogador['preco'], round(100*sum( 1 for j in  selecao_goleiros_1_rodada if int(jogador['cod'])==int(j) )/len(selecao_goleiros_1_rodada),0),'%'

"""









print "OK"
