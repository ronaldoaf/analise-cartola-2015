import json


with open('jogadores.json') as data_file: jogadores = json.load(data_file)
with open('altletas_que_jogaram_por_rodada4.json') as data_file: jogadores2 = json.load(data_file)
with open('equipes_por_rodada3.json') as data_file: equipes = json.load(data_file)
with open('id-nome-jogadores.json') as data_file: jogadores_ids = json.load(data_file)
with open('selecao.json') as data_file: selecao = json.load(data_file)
#with open('posicoes.json') as data_file: posicoes = json.load(data_file)

times=['atl', 'ava', 'cam', 'cfc', 'cha', 'cor', 'cru', 'fig', 'fla', 'flu', 'goi', 'gre', 'int', 'jec', 'pal', 'pon', 'san', 'sao', 'spt', 'vas']


def getNomeJogadorPorId(jog_id):
    for  jog in jogadores_ids:
        if int(jog['id'])==int(jog_id): return jog['nome']

def getPontuacao(cod, rodada):
    for reg in jogadores[str(cod)]:
        if int(reg['rodada'].split('.')[1])==int(rodada):
            return reg['pontos_ult']  


"""
soma_pontos=0
for i in range(38):
    for sel in selecao['enzobrinho'][str(i+1)]:
        try:
            soma_pontos+=getPontuacao(sel['id'], str(i+1))
        except:
            print sel
print soma_pontos
"""




def getJog(cod, rodada):
    for jog in jogadores2[rodada-1]:
        if jog['jog_id']==str(cod): return jog


def dif(obj,scout):
    return obj[scout+'_total']-obj[scout+'_rodada']

rod=10

for jog in jogadores2[rod-1]:
    print '"'+getNomeJogadorPorId(jog['jog_id'])+'"', jog['media_ant'], jog['posicao'], jog['mando']

x=1/0


rod=10

a=getJog('73649',rod)
b=getJog('38957',rod)

print 'media', a['media_ant'], b['media_ant']
print 'pontos_ant', a['pontos_ant'], b['pontos_ant']
print 'SG', dif(a,'SG'), dif(b,'SG')
print 'RB', dif(a,'RB')/(a['num_jogos']-1.0), dif(b,'RB')/(a['num_jogos']-1.0)
print 'FC', dif(a,'FC'), dif(b,'FC')
print 'FD', dif(a,'FD'), dif(b,'FD')
print 'FF', dif(a,'FF'), dif(b,'FF')
print 'PE', dif(a,'PE'), dif(b,'PE')
print 'A', dif(a,'A'), dif(b,'A')
print 'G', dif(a,'G'), dif(b,'G')
print 'Mando', int(a['mando']), int(b['mando'])
#a=jogadores['50427'][rod-1]
#b=jogadores['69014'][rod-1]


print getPontuacao('50427',rod), getPontuacao('69014',rod)



x=1/0


pos={'GOL':[],'LAT':[],'ZAG':[],'MEI':[],'ATA':[],'TEC':[]}
rodada='10'
for nome_time in selecao:
    if rodada in selecao[nome_time]:
        for jog in selecao[nome_time][rodada]:
            try:
                pos[jog['posicao']]+=[jog['id']]
            except:
                jog



for posicao in ['GOL', 'LAT', 'ZAG', 'MEI', 'ATA', 'TEC']:
    print posicao
    num=len(pos[posicao])
    freq_pos=[]
    for jog_id in list(set(pos[posicao])):
        freq_pos+=[[ jog_id, sum(1.0 for i in pos[posicao] if i==jog_id)/num]]

    if posicao=='GOL': k=1
    if posicao=='LAT': k=2
    if posicao=='ZAG': k=2
    if posicao=='MEI': k=3
    if posicao=='ATA': k=3
    if posicao=='TEC': k=1

    for reg in sorted(freq_pos, key=lambda x: x[1], reverse=True)[:k]:
        print getNomeJogadorPorId(reg[0]), str(100*round(reg[1],4))+'%'
        #soma_pontos+=getPontuacao(reg[0], rodada)





"""
soma_pontos=0
for i in range(38):
    pos={'GOL':[],'LAT':[],'ZAG':[],'MEI':[],'ATA':[],'TEC':[]}
    rodada=str(i+1)
    for nome_time in selecao:
        if rodada in selecao[nome_time]:
            for jog in selecao[nome_time][rodada]:
                try:
                    pos[jog['posicao']]+=[jog['id']]
                except:
                    print jog



    for posicao in ['GOL', 'LAT', 'ZAG', 'MEI', 'ATA', 'TEC']:
        #print posicao
        num=len(pos[posicao])
        freq_pos=[]
        for jog_id in list(set(pos[posicao])):
            freq_pos+=[[ jog_id, sum(1.0 for i in pos[posicao] if i==jog_id)/num]]

        if posicao=='GOL': k=1
        if posicao=='LAT': k=2
        if posicao=='ZAG': k=2
        if posicao=='MEI': k=3
        if posicao=='ATA': k=3
        if posicao=='TEC': k=1
        
        for reg in sorted(freq_pos, key=lambda x: x[1], reverse=True)[:k]:
            #print getNomeJogadorPorId(reg[0]), str(100*round(reg[1],4))+'%'
            soma_pontos+=getPontuacao(reg[0], rodada)

print soma_pontos 
"""


      
#for jog in selecao['enzosobrinho']['2']:
#    print jog['posicao'], '|', getNomeJogadorPorId(jog['id'])

"""
for cartola in selecao.keys:
    for rod in selecao[cartola].kesy():
        for jog in selecao[cartola][rod]:
            print jog

"""






"""


soma_total=0
for i in range(4,38):
    rodada_num=i+1
    opcoes_rodada=[]
    for jog in jogadores[rodada_num-1]:        
        if jog['posicao']=='zagueiro':
            num_jogos=jog['num_jogos']-1
            if num_jogos>0:
                RB=1.0*(jog['RB_total']-jog['RB_rodada'])
                FD=1.0*(jog['FD_total']-jog['FD_rodada'])
                FC=1.0*(jog['FC_total']-jog['FC_rodada'])
                FS=1.0*(jog['FS_total']-jog['FS_rodada'])
                PE=1.0*(jog['PE_total']-jog['PE_rodada'])
                CA=1.0*(jog['CA_total']-jog['CA_rodada'])
                DD=1.0*(jog['DD_total']-jog['DD_rodada'])
                GS=1.0*(jog['GS_total']-jog['GS_rodada'])
                MANDO=1.0*jog['mando']
                #indice=RB-0.3*FC+2*MANDO
                indice=PE-FC
                #indice=(RB+0.3*FS-0.17*PE-0.3*FC+0.5*FD)/num_jogos
                opcoes_rodada+=[ {'indice': indice, 'pontos': jog['pontos_ult'] }   ]
                
    soma_total+=sum(e['pontos'] for e in sorted(opcoes_rodada,key=lambda x: x['indice'],reverse=True)[:2])

print soma_total
    
#print jog['jog_id'], \
#    num_jogos, \
#    1.0*(jog['DD_total']-jog['DD_rodada'])/num_jogos,\
#    1.0*(jog['SG_total']-jog['SG_rodada'])/num_jogos, \
#    jog['pontos_ant'], \
#    jog['media_ant'], \
#    int(jog['mando']), \
#    jog['pontos_ult']


"""



"""
for rod in range(38):
    for jog in jogadores[rod]:
        if not jog['posicao']=='tecnico':
            equipes[rod][ jog['time'] ]['G_rodada']+=jog['G_rodada']
            equipes[rod][ jog['time'] ]['DD_rodada']+=jog['DD_rodada']
            equipes[rod][ jog['time'] ]['A_rodada']+=jog['A_rodada']
            equipes[rod][ jog['time'] ]['CA_rodada']+=jog['CA_rodada']
            equipes[rod][ jog['time'] ]['CV_rodada']+=jog['CV_rodada']
            equipes[rod][ jog['time'] ]['DP_rodada']+=jog['DP_rodada']
            equipes[rod][ jog['time'] ]['FC_rodada']+=jog['FC_rodada']
            equipes[rod][ jog['time'] ]['FD_rodada']+=jog['FD_rodada']
            equipes[rod][ jog['time'] ]['FF_rodada']+=jog['FF_rodada']
            equipes[rod][ jog['time'] ]['FS_rodada']+=jog['FS_rodada']
            equipes[rod][ jog['time'] ]['FT_rodada']+=jog['FT_rodada']
            equipes[rod][ jog['time'] ]['GC_rodada']+=jog['GC_rodada']
            equipes[rod][ jog['time'] ]['GS_rodada']+=jog['GS_rodada']
            equipes[rod][ jog['time'] ]['I_rodada']+=jog['I_rodada']
            equipes[rod][ jog['time'] ]['PE_rodada']+=jog['PE_rodada']
            equipes[rod][ jog['time'] ]['PE_rodada']+=jog['PE_rodada']
            equipes[rod][ jog['time'] ]['PP_rodada']+=jog['PP_rodada']
            equipes[rod][ jog['time'] ]['RB_rodada']+=jog['RB_rodada']
            equipes[rod][ jog['time'] ]['SG_rodada']+=jog['SG_rodada']

            equipes[rod][ jog['time'] ]['G_total']+=jog['G_total']
            equipes[rod][ jog['time'] ]['DD_total']+=jog['DD_total']
            equipes[rod][ jog['time'] ]['A_total']+=jog['A_total']
            equipes[rod][ jog['time'] ]['A_total']+=jog['A_total']
            equipes[rod][ jog['time'] ]['CA_total']+=jog['CA_total']
            equipes[rod][ jog['time'] ]['CV_total']+=jog['CV_total']
            equipes[rod][ jog['time'] ]['DP_total']+=jog['DP_total']
            equipes[rod][ jog['time'] ]['FC_total']+=jog['FC_total']
            equipes[rod][ jog['time'] ]['FD_total']+=jog['FD_total']
            equipes[rod][ jog['time'] ]['FF_total']+=jog['FF_total']
            equipes[rod][ jog['time'] ]['FS_total']+=jog['FS_total']
            equipes[rod][ jog['time'] ]['FT_total']+=jog['FT_total']
            equipes[rod][ jog['time'] ]['GC_total']+=jog['GC_total']
            equipes[rod][ jog['time'] ]['GS_total']+=jog['GS_total']
            equipes[rod][ jog['time'] ]['I_total']+=jog['I_total']
            equipes[rod][ jog['time'] ]['PE_total']+=jog['PE_total']
            equipes[rod][ jog['time'] ]['PE_total']+=jog['PE_total']
            equipes[rod][ jog['time'] ]['PP_total']+=jog['PP_total']
            equipes[rod][ jog['time'] ]['RB_total']+=jog['RB_total']
            equipes[rod][ jog['time'] ]['SG_total']+=jog['SG_total']
        
            equipes[rod][ jog['time_contra'] ]['G_contra_rodada']+=jog['G_rodada']
            equipes[rod][ jog['time_contra'] ]['DD_contra_rodada']+=jog['DD_rodada']
            equipes[rod][ jog['time_contra'] ]['A_contra_rodada']+=jog['A_rodada']
            equipes[rod][ jog['time_contra'] ]['CA_contra_rodada']+=jog['CA_rodada']
            equipes[rod][ jog['time_contra'] ]['CV_contra_rodada']+=jog['CV_rodada']
            equipes[rod][ jog['time_contra'] ]['DP_contra_rodada']+=jog['DP_rodada']
            equipes[rod][ jog['time_contra'] ]['FC_contra_rodada']+=jog['FC_rodada']
            equipes[rod][ jog['time_contra'] ]['FD_contra_rodada']+=jog['FD_rodada']
            equipes[rod][ jog['time_contra'] ]['FF_contra_rodada']+=jog['FF_rodada']
            equipes[rod][ jog['time_contra'] ]['FS_contra_rodada']+=jog['FS_rodada']
            equipes[rod][ jog['time_contra'] ]['FT_contra_rodada']+=jog['FT_rodada']
            equipes[rod][ jog['time_contra'] ]['GC_contra_rodada']+=jog['GC_rodada']
            equipes[rod][ jog['time_contra'] ]['GS_contra_rodada']+=jog['GS_rodada']
            equipes[rod][ jog['time_contra'] ]['I_contra_rodada']+=jog['I_rodada']
            equipes[rod][ jog['time_contra'] ]['PE_contra_rodada']+=jog['PE_rodada']
            equipes[rod][ jog['time_contra'] ]['PE_contra_rodada']+=jog['PE_rodada']
            equipes[rod][ jog['time_contra'] ]['PP_contra_rodada']+=jog['PP_rodada']
            equipes[rod][ jog['time_contra'] ]['RB_contra_rodada']+=jog['RB_rodada']
            equipes[rod][ jog['time_contra'] ]['SG_contra_rodada']+=jog['SG_rodada']

            equipes[rod][ jog['time_contra'] ]['G_contra_total']+=jog['G_total']
            equipes[rod][ jog['time_contra'] ]['DD_contra_total']+=jog['DD_total']
            equipes[rod][ jog['time_contra'] ]['A_contra_total']+=jog['A_total']
            equipes[rod][ jog['time_contra'] ]['A_contra_total']+=jog['A_total']
            equipes[rod][ jog['time_contra'] ]['CA_contra_total']+=jog['CA_total']
            equipes[rod][ jog['time_contra'] ]['CV_contra_total']+=jog['CV_total']
            equipes[rod][ jog['time_contra'] ]['DP_contra_total']+=jog['DP_total']
            equipes[rod][ jog['time_contra'] ]['FC_contra_total']+=jog['FC_total']
            equipes[rod][ jog['time_contra'] ]['FD_contra_total']+=jog['FD_total']
            equipes[rod][ jog['time_contra'] ]['FF_contra_total']+=jog['FF_total']
            equipes[rod][ jog['time_contra'] ]['FS_contra_total']+=jog['FS_total']
            equipes[rod][ jog['time_contra'] ]['FT_contra_total']+=jog['FT_total']
            equipes[rod][ jog['time_contra'] ]['GC_contra_total']+=jog['GC_total']
            equipes[rod][ jog['time_contra'] ]['GS_contra_total']+=jog['GS_total']
            equipes[rod][ jog['time_contra'] ]['I_contra_total']+=jog['I_total']
            equipes[rod][ jog['time_contra'] ]['PE_contra_total']+=jog['PE_total']
            equipes[rod][ jog['time_contra'] ]['PE_contra_total']+=jog['PE_total']
            equipes[rod][ jog['time_contra'] ]['PP_contra_total']+=jog['PP_total']
            equipes[rod][ jog['time_contra'] ]['RB_contra_total']+=jog['RB_total']
            equipes[rod][ jog['time_contra'] ]['SG_contra_total']+=jog['SG_total']

with open('equipes_por_rodada3.json', 'w') as  arquivo_saida:
    json.dump(equipes, arquivo_saida)


"""





"""
extra={\
    'G_rodada':0,\
    'DD_rodada':0,\
    'A_rodada':0,\
    'A_rodada':0,\
    'CA_rodada':0,\
    'CV_rodada':0,\
    'DP_rodada':0,\
    'FC_rodada':0,\
    'FD_rodada':0,\
    'FF_rodada':0,\
    'FS_rodada':0,\
    'FT_rodada':0,\
    'GC_rodada':0,\
    'GS_rodada':0,\
    'I_rodada':0,\
    'PE_rodada':0,\
    'PE_rodada':0,\
    'PP_rodada':0,\
    'RB_rodada':0,\
    'SG_rodada':0,\

    'G_total':0,\
    'DD_total':0,\
    'A_total':0,\
    'A_total':0,\
    'CA_total':0,\
    'CV_total':0,\
    'DP_total':0,\
    'FC_total':0,\
    'FD_total':0,\
    'FF_total':0,\
    'FS_total':0,\
    'FT_total':0,\
    'GC_total':0,\
    'GS_total':0,\
    'I_total':0,\
    'PE_total':0,\
    'PE_total':0,\
    'PP_total':0,\
    'RB_total':0,\
    'SG_total':0,\
    
    'G_contra_rodada':0,\
    'DD_contra_rodada':0,\
    'A_contra_rodada':0,\
    'A_contra_rodada':0,\
    'CA_contra_rodada':0,\
    'CV_contra_rodada':0,\
    'DP_contra_rodada':0,\
    'FC_contra_rodada':0,\
    'FD_contra_rodada':0,\
    'FF_contra_rodada':0,\
    'FS_contra_rodada':0,\
    'FT_contra_rodada':0,\
    'GC_contra_rodada':0,\
    'GS_contra_rodada':0,\
    'I_contra_rodada':0,\
    'PE_contra_rodada':0,\
    'PE_contra_rodada':0,\
    'PP_contra_rodada':0,\
    'RB_contra_rodada':0,\
    'SG_contra_rodada':0,\

    'G_contra_total':0,\
    'DD_contra_total':0,\
    'A_contra_total':0,\
    'A_contra_total':0,\
    'CA_contra_total':0,\
    'CV_contra_total':0,\
    'DP_contra_total':0,\
    'FC_contra_total':0,\
    'FD_contra_total':0,\
    'FF_contra_total':0,\
    'FS_contra_total':0,\
    'FT_contra_total':0,\
    'GC_contra_total':0,\
    'GS_contra_total':0,\
    'I_contra_total':0,\
    'PE_contra_total':0,\
    'PE_contra_total':0,\
    'PP_contra_total':0,\
    'RB_contra_total':0,\
    'SG_contra_total':0}

for i in range(len(equipes)):
    for equipe_nome in equipes[i].keys():
        equipes[i][equipe_nome].update(extra)

        

with open('equipes_por_rodada2.json', 'w') as  arquivo_saida:
    json.dump(equipes, arquivo_saida)
    
"""




"""

jogadores_pontuacao={}
jogadores_media={}
for i in range(38):
    rodada_num=i+1
    for j in range(len(jogadores[rodada_num-1])):
        jog_id=jogadores[rodada_num-1][j]['jog_id'] 
        if jog_id not in jogadores_pontuacao: jogadores_pontuacao[jog_id]=0
        if jog_id not in jogadores_media: jogadores_media[jog_id]=0
        
        jogadores[rodada_num-1][j]['pontos_ant']=jogadores_pontuacao[jog_id]
        jogadores[rodada_num-1][j]['media_ant']=jogadores_media[jog_id]
        
        jogadores_pontuacao[jog_id]=jogadores[rodada_num-1][j]['pontos_ult']
        jogadores_media[jog_id]=jogadores[rodada_num-1][j]['pontos_media']
        #jogou=jogadores[rodada_num-1][j]['atleta_jogou']
        #jogadores[rodada_num-1][j]['jog_id']   

with open('altletas_que_jogaram_por_rodada4.json', 'w') as  arquivo_saida:
    json.dump(jogadores, arquivo_saida)

"""


"""
jogadores_jogos={}
for i in range(38):
    rodada_num=i+1
    for j in range(len(jogadores[rodada_num-1])):
        jog_id=jogadores[rodada_num-1][j]['jog_id'] 
        if jog_id not in jogadores_jogos: jogadores_jogos[jog_id]=0
        jogou=jogadores[rodada_num-1][j]['atleta_jogou']
        jogadores_jogos[jog_id]+=jogou        
        jogadores[rodada_num-1][j]['num_jogos']=jogadores_jogos[jog_id]
    



with open('altletas_que_jogaram_por_rodada3.json', 'w') as  arquivo_saida:
    json.dump(jogadores, arquivo_saida)
"""



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
"""


print 'OK'
