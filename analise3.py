import json



with open('altletas_que_jogaram_por_rodada2.json') as data_file: jogadores = json.load(data_file)
#with open('selecao.json') as data_file: selecao = json.load(data_file)
#with open('posicoes.json') as data_file: posicoes = json.load(data_file)

times=['atl', 'ava', 'cam', 'cfc', 'cha', 'cor', 'cru', 'fig', 'fla', 'flu', 'goi', 'gre', 'int', 'jec', 'pal', 'pon', 'san', 'sao', 'spt', 'vas']






"""
for i in range(38):
    rodada_num=i+1
    rodada={}
    for j in range(len(jogadores[rodada_num-1])):

        cofronto=jogadores[rodada_num-1][j]['confronto']
        time=jogadores[rodada_num-1][j]['time']
        pos=cofronto.index(jogadores[rodada_num-1][j]['time'])
        time_contra=cofronto[6:] if pos==0 else cofronto[:3]
        #print time,time_contra
        jogadores[rodada_num-1][j]['time_contra']=time_contra



with open('altletas_que_jogaram_por_rodada2.json', 'w') as  arquivo_saida:
    json.dump(jogadores, arquivo_saida)

"""




equipes=[]
for i in range(38):
    rodada_num=i+1
    rodada={}
    for time in times:
        rodada[time]={'gP':0, 'gC':0, 'mando':False, 'r':0}
    
    for jogador in jogadores[rodada_num-1]:
        time=jogador['time']
        time_contra=jogador['time_contra']        
        if jogador['posicao']!='tecnico':
            rodada[time]['gP']+=jogador['G_rodada']
            rodada[time_contra]['gC']+=jogador['G_rodada']
            
            rodada[time]['mando']=jogador['mando']
            rodada[time_contra]['mando']=not jogador['mando']
            
    
    for time in rodada.keys():
        gP=rodada[time]['gP']
        gC=rodada[time]['gC']
        rodada[time]['r']=1 if  gP > gC else (-1 if  gP < gC else 0)


    equipes+=[rodada]

with open('equipes_por_rodada.json', 'w') as  arquivo_saida:
    json.dump(equipes, arquivo_saida)
    
print 'OK'
