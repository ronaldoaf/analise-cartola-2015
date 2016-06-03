import json



with open('altletas_que_jogaram_por_rodada4.json') as data_file: jogadores = json.load(data_file)
with open('equipes_por_rodada3.json') as data_file: equipes = json.load(data_file)
with open('selecao.json') as data_file: selecao = json.load(data_file)
#with open('posicoes.json') as data_file: posicoes = json.load(data_file)

times=['atl', 'ava', 'cam', 'cfc', 'cha', 'cor', 'cru', 'fig', 'fla', 'flu', 'goi', 'gre', 'int', 'jec', 'pal', 'pon', 'san', 'sao', 'spt', 'vas']


for rod in range(len(equipes)):
    for nome_time in equipes[rod]:
        if 'vitorias' not in  equipes[rod][nome_time]:
            equipes[rod][nome_time]['vitorias']=0
            equipes[rod][nome_time]['empates']=0
            equipes[rod][nome_time]['derrotas']=0
            equipes[rod][nome_time]['pontos']=0
            
        equipes[rod][nome_time]['vitorias']+=1 if equipes[rod][nome_time]['r']==1 else 0
        equipes[rod][nome_time]['empates']+=1 if equipes[rod][nome_time]['r']==0 else 0
        equipes[rod][nome_time]['derrotas']+=1 if equipes[rod][nome_time]['r']==-1 else 0
        equipes[rod][nome_time]['pontos']+=3 if equipes[rod][nome_time]['r']==1 else (1 if equipes[rod][nome_time]['r']==0 else 0 )




with open('equipes_por_rodada4.json', 'w') as  arquivo_saida:
    json.dump(equipes, arquivo_saida)

    
"""
for cartola in selecao.keys:
    for rod in selecao[cartola].kesy():
        for jog in selecao[cartola][rod]:
            print jog

"""



"""


print 'jog_id num_jogos DD SG pontos_ant media_ant mando G_sofridos FD_sofridos FF_sofridos G_feito_adversario FD_feito_adversario FF_feito_adversario pontos'

for i in range(4,38):
    rodada_num=i+1
    for jog in jogadores[rodada_num-1]:
        if jog['posicao']=='goleiro':
            num_jogos=jog['num_jogos']-1
            if num_jogos>0:
                print jog['jog_id'], \
                    num_jogos, \
                    1.0*(jog['DD_total']-jog['DD_rodada'])/num_jogos,\
                    1.0*(jog['SG_total']-jog['SG_rodada'])/num_jogos, \
                    jog['pontos_ant'], \
                    jog['media_ant'], \
                    int(jog['mando']), \
                    1.0*(equipes[rodada_num-1][jog['time']]['G_contra_total']-equipes[rodada_num-1][jog['time']]['G_contra_rodada'])/rodada_num, \
                    1.0*(equipes[rodada_num-1][jog['time']]['FD_contra_total']-equipes[rodada_num-1][jog['time']]['FD_contra_rodada'])/rodada_num, \
                    1.0*(equipes[rodada_num-1][jog['time']]['FF_contra_total']-equipes[rodada_num-1][jog['time']]['FF_contra_rodada'])/rodada_num,\
                    1.0*(equipes[rodada_num-1][jog['time_contra']]['G_total']-equipes[rodada_num-1][jog['time_contra']]['G_rodada'])/rodada_num, \
                    1.0*(equipes[rodada_num-1][jog['time_contra']]['FD_total']-equipes[rodada_num-1][jog['time_contra']]['FD_rodada'])/rodada_num, \
                    1.0*(equipes[rodada_num-1][jog['time_contra']]['FF_total']-equipes[rodada_num-1][jog['time_contra']]['FF_rodada'])/rodada_num, \
                    jog['pontos_ult']



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
