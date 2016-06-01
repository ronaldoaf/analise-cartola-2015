# -*- coding: cp1252 -*-
from AG import populacao
import json
import time
import cPickle as pickle 



with open('odds.json') as data_file: odds = json.load(data_file)
#with open('jogadores.json') as data_file: jogadores = json.load(data_file)
with open('altletas_que_jogaram_por_rodada4.json') as data_file: jogadores2 = json.load(data_file)
with open('equipes_por_rodada3.json') as data_file: equipes = json.load(data_file)



#============Funções de conversão=================================
def intListToBinString(lista):
    n_digitos=str(len(bin(max(lista)))-2)
    formato='{0:0'+n_digitos+'b}'
    saida='';
    for item in lista: saida+=formato.format(item)
    return saida

def binStringToIntList(string,tamanho):   #tamanho do cromossomo
    n_partes=len(string)/tamanho
    return [int(string[i*tamanho:(i+1)*tamanho],2)  for i in range(n_partes)]

def floatToInt(valor,minimo,maximo,n_partes):
    intervalo=(1.0*maximo-minimo)/n_partes
    return int((valor-1.0*minimo)/intervalo)

def intToFloat(valor,minimo,maximo,n_partes):
    intervalo=(1.0*maximo-minimo)/n_partes
    return float(1.0*minimo+valor*intervalo)

def media(lista):
    return 1.0*sum(lista)/len(lista)

#===========Funções de coleta de dados===========================

def getNomeJogadorPorId(jog_id):
    for  jog in jogadores_ids:
        if int(jog['id'])==int(jog_id): return jog['nome']

def getPontuacao(cod, rodada):
    for reg in jogadores[str(cod)]:
        if int(reg['rodada'].split('.')[1])==int(rodada):
            return reg['pontos_ult']  

def getJog(cod, rodada):
    for jog in jogadores2[rodada-1]:
        if jog['jog_id']==str(cod): return jog


def dif(obj,scout):
    return 1.*obj[scout+'_total']-obj[scout+'_rodada']


def getProbVitoriaCod(cod, rodada):
    time=getJog(cod, rodada)['time']

    
    for e in odds:
        probH=1/e[3] / (1/e[3] + 1/e[4])
        probA=1/e[4] / (1/e[3] + 1/e[4])
        
        if int(e[2])==int(rodada):
            if time==e[0]: return probH
            if time==e[1]: return probA



def getProbVitoriaEquipe(equipe, rodada):
    time=equipe
 
    for e in odds:
        probH=1/e[3] / (1/e[3] + 1/e[4])
        probA=1/e[4] / (1/e[3] + 1/e[4])
        
        if int(e[2])==int(rodada):
            if time==e[0]: return probH
            if time==e[1]: return probA

def ranks(lista, inverte=False):
    seq = sorted(lista, reverse=inverte)
    return [seq.index(v) for v in lista]


def p(posicao):
    if posicao=='goleiro': return 'GOL'
    if posicao=='lateral': return 'LAT'
    if posicao=='zagueiro': return 'ZAG'
    if posicao=='meia': return 'MEI'
    if posicao=='atacante': return 'ATA'
    if posicao=='tecnico': return 'TEC'









p_min=-8
p_max=8

n_bits=8
num_vars=53
#def valor(n):
def valor(codigo_genetico):
    #codigo_genetico='101101101101101101101101101101101101101101101101101101101101101101101101101101101101'
    n_partes=2**n_bits
    vs=[intToFloat(e,p_min,p_max,n_partes) for e in binStringToIntList(codigo_genetico,n_bits)]


    #print vs
    #vs=[0.65, 1.55, 1.15, 1.5, 1.3, 1.89, 1.7875, 0.7375, 0.8125]
    soma_total=0
    for i in range(22,38):
        rod=i+1
        posParms={'GOL':[],'LAT':[],'ZAG':[],'MEI':[],'ATA':[], 'TEC':[]}

        for jog in jogadores2[rod-1]:
            n=jog['num_jogos']
            if n>3:
                if not jog['posicao']=='tecnico':                
                    parms={'id' : jog['jog_id'],
                           'media': jog['media_ant'],
                           'pontos_ant': jog['pontos_ant'],
                           'RB': dif(jog, 'RB')/n,
                           'FD': dif(jog, 'RB')/n,
                           'FF': dif(jog, 'FF')/n,
                           'FC': dif(jog, 'FC')/n,
                           'FS': dif(jog, 'FS')/n,
                           'CA': dif(jog, 'CA')/n,
                           'G': dif(jog, 'G')/n,
                           'A': dif(jog, 'A')/n,
                           'I': dif(jog, 'I')/n,
                           'DD': dif(jog, 'DD')/n,
                           'SG': dif(jog, 'SG')/n,
                           'GS': dif(jog, 'GS')/n,
                           'PE': dif(jog, 'PE')/n,
                           'mando':jog['mando'],
                           'prob':getProbVitoriaEquipe(jog['time'], rod),
                           'pontos':jog['pontos_ult'] }        
                else:
                    parms={'id' : jog['jog_id'],
                           'media': jog['media_ant'],
                           'pontos_ant': jog['pontos_ant'],
                           'mando':jog['mando'],
                           'prob':getProbVitoriaEquipe(jog['time'], rod),
                           'pontos':jog['pontos_ult'] }    

                posParms[p( jog['posicao'] )]+=[parms]

        for pos_nome in posParms.keys():
            num=len(posParms[pos_nome])
            inc=1.0/num
            for parm in posParms[pos_nome][0].keys():
                if parm not in ['id', 'mando', 'pontos']:
                    posParms[pos_nome].sort(key=lambda x: x[parm])
                    for i in range(len(posParms[pos_nome])): posParms[pos_nome][i][parm]=i*inc

        posParms['TEC'].sort(key=lambda x: x['prob'])
        posParms['ZAG'].sort(key=lambda x: vs[0]*x['prob'] + vs[1]*x['media']+ vs[2]*x['RB'] +vs[52]*x['FC'] + vs[3]*x['FF'] +  vs[4]*x['FD'] +  vs[5]*x['SG'] +  vs[6]*x['G'] + vs[7]*x['PE'] + vs[8]*x['CA'] + vs[9]*x['mando'] )
        posParms['LAT'].sort(key=lambda x: vs[10]*x['prob'] + vs[11]*x['media']+ vs[12]*x['RB'] +vs[13]*x['FC'] + vs[14]*x['FF'] +  vs[15]*x['FD'] +  vs[16]*x['SG'] +  vs[17]*x['G'] + vs[18]*x['PE'] +vs[19]*x['A'] +vs[20]*x['FS'] +  vs[21]*x['mando'] )
        
        posParms['MEI'].sort(key=lambda x: vs[22]*x['prob'] + vs[23]*x['media']+ vs[24]*x['RB'] +vs[25]*x['FC'] + vs[26]*x['FF'] +  vs[27]*x['FD'] +  vs[28]*x['G'] + vs[29]*x['PE'] +vs[30]*x['A'] +vs[31]*x['FS'] +  vs[32]*x['mando'] )
        posParms['ATA'].sort(key=lambda x: vs[33]*x['prob'] + vs[34]*x['media']+ vs[35]*x['RB'] +vs[36]*x['FC'] + vs[37]*x['FF'] +  vs[38]*x['FD'] +  vs[39]*x['G'] + vs[40]*x['PE'] +vs[41]*x['A'] +vs[42]*x['FS'] +vs[43]*x['I']+  vs[44]*x['mando'] )

        posParms['GOL'].sort(key=lambda x: vs[45]*x['prob'] + vs[46]*x['media'] + vs[47]*x['DD'] + vs[48]*x['SG'] + vs[49]*x['GS'] + vs[50]*x['FC'] + vs[51]*x['CA'])

        
        soma_total+=posParms['GOL'][-1]['pontos']
        
        soma_total+=posParms['LAT'][-1]['pontos']
        soma_total+=posParms['LAT'][-2]['pontos']
        
        soma_total+=posParms['ZAG'][-1]['pontos']
        soma_total+=posParms['ZAG'][-2]['pontos']
        
        soma_total+=posParms['MEI'][-1]['pontos']
        soma_total+=posParms['MEI'][-2]['pontos']
        soma_total+=posParms['MEI'][-3]['pontos']
        
        soma_total+=posParms['ATA'][-1]['pontos']
        soma_total+=posParms['ATA'][-2]['pontos']
        soma_total+=posParms['ATA'][-3]['pontos']
        
        soma_total+=posParms['TEC'][-1]['pontos']

    return round(soma_total*38/16,2)




#codigo_genetico='101101101101101101101101101101101101101101101101101101101101101101101101101101101101101101101101101101101101101101101101101101101101101101101101101101101101101'
#n_partes=2**n_bits
#vs=[intToFloat(e,p_min,p_max,n_partes) for e in binStringToIntList(codigo_genetico,n_bits)]


print valor('1010011011010001111000100110110011000110000111100111111111100110011110001100011111010010110000001101100001111110110010111110011010011101000010100101010011000011011000001100011110111011011100001100000011100100010001001101010111110000000000001100110110001101100110101110110011111110111100110110110101001000011110100010000110110010000110011001111011111101100101011111101011000000011111110110110011110011111011111111001111110001')

quit()


pop=populacao(funcao_aptidao=valor, \
              numero_de_cromossomos=num_vars, \
              numero_genes_por_cromossomo=n_bits, \
              tamanho_inicial=50, \
              tamanho=50, \
              taxa_de_reproducao=0.95, \
              taxa_de_mutacao=0.02, \
              metodo_de_selecao=0 \
              )

start_time = time.time()

for i in range(50):
    print i, media([e.aptidao for e in pop.indiv])
    pop.evolucao(1)


print media([e.aptidao for e in pop.indiv])

print pop.indiv[0].codigo_genetico



pickle.dump( pop,open( "pop.pickle", "wb" ) )

# your code
elapsed_time = time.time() - start_time
print elapsed_time

#print valor('010010110101101000101000111000010010011011101001111100010001110111100100')

