# -*- coding: cp1252 -*-
from AG import populacao
from math import exp,log
from random import lognormvariate as rand_lognormal, normalvariate as rand_normal,random
from csv import reader
from dircache import listdir
import sys
def round_low(num):
    return round(num-0.01*(1 if num>0 else -1),0)

D=24*60*60

def media(dados,n=0):
    if n==0: n=len(dados)

    n=len(dados)-n
    
    try:
        return 1.0*sum(dado for dado in dados[n:])/len(dados[n:])
    except:
        return 0.0

#variança
def var(dados):
    m =media(dados)
    return sum((m -d)**2 for d in dados)/(len(dados)-1)



#funcao fatorial que nao achei na Math do python 2.5
# A funcao factorial so tem a partir da 2.6
def fatorial(x):
    prod=1
    for i in range(1,x+1):
        prod*=i
    return prod

def gama_(x):
    return fatorial(x-1)

def bassel(k, x):
    infinito = 15  
    soma = 0
    for m in range(infinito):
        soma+= ((0.25*x**2)**m)/(fatorial(m) * fatorial(k+m))

    return ((0.5 * x) ** k) * soma


def skellam(k, m1, m2):
    return exp(-(m1 + m2)) * ((m1 / m2) ** (k / 2.0)) * bassel(abs(k), 2 * (m1 * m2) ** 0.5)



#Funções de conversão
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


p_min=0.1
p_max=2.5

n_bits=8
num_vars=4+2+3
#def valor(n):
def valor(codigo_genetico):
    #codigo_genetico='000010100111000000101101101000000101111101100000011110010100110101010000'
    n_partes=2**n_bits
    vs=[intToFloat(e,p_min,p_max,n_partes) for e in binStringToIntList(codigo_genetico,n_bits)]

    #print vs
    #vs=[0.65, 1.55, 1.15, 1.5, 1.3, 1.89, 1.7875, 0.7375, 0.8125]


    def ZPD(k,m1,m2):
        tm1=vs[0]
        t0=vs[1]
        t1=vs[2]
        t2=vs[3]
        
        am1=skellam(-1, m1, m2)
        a0=skellam(0, m1, m2)
        a1=skellam(1, m1, m2)
        a2=skellam(2, m1, m2)
        
        x=(1-tm1*am1-t0*a0-t1*a1 -t2*a2)/(1-am1-a0-a1-a2)

        if k==0:
            z=t0
        elif k==1:
            z=t1
        elif k==-1:
            z=tm1
        else:
            z=x
            
        return z *skellam(k, m1, m2)




    #ATENÇÃO
    #a desvatangem ou vantagem sempre refe-se ao time da casa
    def calcProbHandicapCasa(h,l1,l2):
        h_int= int(round_low(h))
        h_dec= h - h_int
        P_casa=sum(ZPD(k,l1,l2)  for  k in range(-h_int+1,11))
        P_empate=ZPD(-h_int,l1,l2)
        P_visit=1-(P_casa+P_empate)
        #P_casa =  sum(bivar_poisson(g1,g2,l1,l2) for g1 in range(10) for g2 in range(10) if g1-g2>-h_int)
        #P_empate =  sum(bivar_poisson(g1,g2,l1,l2) for g1 in range(10) for g2 in range(10) if g1-g2==-h_int)
        #P_visit =  sum(bivar_poisson(g1,g2,l1,l2) for g1 in range(10) for g2 in range(10) if g1-g2<-h_int)


        if h_dec==0:
            return P_casa/(P_casa+P_visit)
        elif h_dec ==-0.25:
            return P_casa/(P_casa+P_empate/2+P_visit)
        elif h_dec ==-0.5:
            return P_casa

        elif h_dec ==0.5:
            return 1-P_visit
        elif h_dec == 0.25:
            return 1-(P_visit/(P_casa+P_empate/2+P_visit))

    def calcProbHandicapVisit(hand,l1,l2):
        return 1-calcProbHandicapCasa(hand,l1,l2)

    def calcRetornoHandicap_050(selecao,handicap,odds1,odds2,g1,g2):
        return eval("odds"+str(selecao))-1 if (-1)**selecao*(g1-g2+handicap)<0 else 0 if (-1)**selecao*(g1-g2+handicap)==0 else -1
        
    def calcRetornoHandicap_025(selecao,handicap,odds1,odds2,g1,g2):
        return (float(calcRetornoHandicap_050(selecao,handicap+0.25,odds1,odds2,g1,g2))+float(calcRetornoHandicap_050(selecao,handicap-0.25,odds1,odds2,g1,g2)))/2

    def calcRetornoHandicap(selecao,handicap,odds1,odds2,g1,g2): 
        return calcRetornoHandicap_025(selecao,handicap,odds1,odds2,g1,g2) if handicap%0.5 else calcRetornoHandicap_050(selecao,handicap,odds1,odds2,g1,g2)







    def BS_Hand(g1,g2,nivel,probH):
        retorno=calcRetornoHandicap(1,nivel,2.00,2.00,g1,g2)
        if retorno==-1.0: v=0.0
        elif retorno==-0.5: v=0.25
        elif retorno==0.0: v=0.5
        elif retorno==0.5: v=0.75
        else: v=1.0
        return (probH-v)**2
        
    #prob
    def pH(m1,m2):
        return sum( ZPD(k,m1,m2 ) for k in range(1,10) )

    def pD(m1,m2):
        return ZPD(0,m1,m2)

    def pA(m1,m2):
        return 1 - (pH(m1,m2) +  pD(m1,m2) )

    def g(n):
        return exp(-n/100000.0)




    def gols(MS,equipe):
        if MS=='M':
            return [(e[0],e[1]) for e in equipe['jC'][-4:]] + [(e[0],e[2]*vs[4]) for e in equipe['jF'][-4:]]
        
        if MS=='S':
            return [(e[0],e[2]*vs[5]) for e in equipe['jC'][-4:]] + [(e[0],e[1]) for e in equipe['jF'][-4:]]


    BS=0
    cont=0
    lucro=0
    for arq in listdir("planilhas1"):    
        equipes={}
        jogos=[]

        lucro=0
        apostas=0
        
        f=open('planilhas1\\'+arq,'rUb')
        arquivo = reader(f)

        for linha in arquivo:
            jogos.append({"t":int(linha[0])/D, \
                          "H":linha[3], \
                          "A":linha[4], \
                          "gH":int(linha[5]), \
                          "gA":int(linha[6]), \
                          "nivel":float(linha[7]) if len(linha[7])>0 else '', \
                          "oddsU":float(linha[8]) if len(linha[8])>0 else '', \
                          "oddsO":float(linha[9]) if len(linha[9])>0 else '' \


                          })

            if not equipes.has_key(linha[3]): equipes[linha[3]]={'jC':[],'jF':[]}  
            if not equipes.has_key(linha[4]): equipes[linha[4]]={'jC':[],'jF':[]} 


        #print equipes
        for j in jogos:
            #Testa
            if len( equipes[j['H']]['jC'])>=4 and len(equipes[j['A']]['jF'])>=4:
                golsMH=gols('M', equipes[j['H']])
                golsMA=gols('M', equipes[j['A']])
                golsSH=gols('S', equipes[j['H']])
                golsSA=gols('S', equipes[j['A']])
                
                atH=sum([ e[1]*g(j['t']-e[0]) for e in golsMH])/sum([g(j['t']-e[0]) for e in golsMH])
                dfH=sum([ e[1]*g(j['t']-e[0]) for e in golsSH])/sum([g(j['t']-e[0]) for e in golsSH])

                
                atA=sum([ e[1]*g(j['t']-e[0]) for e in golsMA])/sum([g(j['t']-e[0]) for e in golsMA])
                dfA=sum([ e[1]*g(j['t']-e[0]) for e in golsSA])/sum([g(j['t']-e[0]) for e in golsSA])

                mH=vs[6]*(atH+vs[7]*dfA)/(1+vs[7])
                mA=1.2*(vs[8]*atA+dfH)/(1+vs[8])

                #print j['gH']-j['gA'],calcProbHandicapCasa(j['nivel'],mH,mA)
                try:
                    if calcProbHandicapCasa(j['nivel'],mH,mA)*j['oddsU']>1.1 and calcProbHandicapCasa(j['nivel'],mH,mA)*j['oddsU']<1.5:
                        lucro+=calcRetornoHandicap(1,j['nivel'],j['oddsU'],j['oddsO'],j['gH'],j['gA'])
                    #if (1-calcProbHandicapCasa(j['nivel'],mH,mA))*j['oddsO']>1.1 and (1-calcProbHandicapCasa(j['nivel'],mH,mA))*j['oddsO'] <1.5:
                    #    lucro+=calcRetornoHandicap(2,j['nivel'],j['oddsU'],j['oddsO'],j['gH'],j['gA'])
                except:
                    x=0
                    
                #r=[1,0,0] if j['gH']>j['gA'] else ([0,1,0] if j['gH']==j['gA'] else [0,0,1] )
                #BS+=BS_Hand(j['gH'],j['gA'],j['nivel'], calcProbHandicapCasa(j['nivel'],mH,mA))
                #cont+=1

                #probHCasas=(1/j['oddsU'])/(1/j['oddsU'] + 1/1/j['oddsO'])
                #try:
                #    BS+=BS_Hand(j['gH'],j['gA'],j['nivel'], probHCasas)
                #    cont+=1
                #except:
                #    x=0
            #Atualiza
            equipes[j['H']]['jC']+=[ [j['t'], j['gH'], j['gA'] ] ]
            equipes[j['A']]['jF']+=[ [j['t'], j['gH'], j['gA'] ] ]
    return lucro
    #return cont/BS
    #return 2*(cont/BS)/1.61223 + lucro/46.0
    #return [lucro,BS/cont]



pop=populacao(funcao_aptidao=valor, \
              numero_de_cromossomos=num_vars, \
              numero_genes_por_cromossomo=n_bits, \
              tamanho_inicial=30, \
              tamanho=30, \
              taxa_de_reproducao=0.95, \
              taxa_de_mutacao=0.015, \
              metodo_de_selecao=0 \
              )

for i in range(50):
    print media([e.aptidao for e in pop.indiv])
    pop.evolucao(1)


print media([e.aptidao for e in pop.indiv])

#print pop.indiv[0].codigo_genetico




print valor('010010110101101000101000111000010010011011101001111100010001110111100100')
