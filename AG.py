# -*- coding: cp1252 -*-
from math import exp, log
from random import random



class indviduo:
    def __init__(self,codigo_genetico,funcao_aptidao):
        self.codigo_genetico=codigo_genetico
        self.aptidao=funcao_aptidao(codigo_genetico)
        
    def __cmp__(self, other):
        if self.aptidao < other.aptidao: return -1
        elif self.aptidao > other.aptidao:return 1
        else: return 0

        
class populacao:    
    def __init__(self, funcao_aptidao,numero_de_cromossomos,numero_genes_por_cromossomo, tamanho_inicial=10000,tamanho=1000,taxa_de_mutacao=0.01,taxa_de_reproducao=0.95,metodo_de_selecao=0):
        def codigo_genetico_random(numero_de_genes):
            saida=''
            for i in range(numero_de_genes): saida+=str(int(round(random(),0)))
            return saida
        
        self.funcao_aptidao=funcao_aptidao
        self.numero_de_cromossomos=numero_de_cromossomos
        self.tamanho=tamanho_inicial
        self.tamanho=tamanho
        self.numero_genes_por_cromossomo=numero_genes_por_cromossomo
        self.taxa_de_mutacao=taxa_de_mutacao
        self.taxa_de_reproducao=taxa_de_reproducao
        self.metodo_de_selecao=metodo_de_selecao
        self.indiv=[indviduo(codigo_genetico_random(numero_de_cromossomos*numero_genes_por_cromossomo), funcao_aptidao)  for i in range(tamanho_inicial)]
        
        self.selecao()

    def selecao(self):
        #Dizimação
        if self.metodo_de_selecao==0:
            self.indiv=sorted(self.indiv,reverse=True)
            self.indiv=self.indiv[:self.tamanho]

        #Roleta
        elif self.metodo_de_selecao==1:
            def roulette_select(population, fitnesses, num):
                """ Roulette selection, implemented according to:
                    <http://stackoverflow.com/questions/177271/roulette
                    -selection-in-genetic-algorithms/177278#177278>
                """
                total_fitness = float(sum(fitnesses))
                rel_fitness = [f/total_fitness for f in fitnesses]
                # Generate probability intervals for each individual
                probs = [sum(rel_fitness[:i+1]) for i in range(len(rel_fitness))]
                # Draw new population
                new_population = []
                for n in xrange(num):
                    r = random()
                    for (i, individual) in enumerate(population):
                        if r <= probs[i]:
                            new_population.append(individual)
                            break
                return new_population

            
            populacao_atual=sorted(self.indiv,reverse=True)
            lst_aptidoes=[e.aptidao for e in populacao_atual]            
            if min(lst_aptidoes)<0:lst_aptidoes=[e.aptidao-min(lst_aptidoes) for e in populacao_atual]
            self.indiv=roulette_select(populacao_atual, lst_aptidoes, self.tamanho)


        #Torneio
        elif self.metodo_de_selecao==2:
            pop_atual=sorted(self.indiv, key=lambda x: random())
            self.indiv=[max([pop_atual[i],pop_atual[i+len(pop_atual)/2]]) for i in range(len(pop_atual)/2) ]

        self.indiv=sorted(self.indiv,reverse=True)

    def mutacao(self,codigo_genetico):
        codigo_genetico_alterado=''
        for bit in codigo_genetico:
            codigo_genetico_alterado+=bit if random()>self.taxa_de_mutacao else str(int(not(int(bit))))

        return codigo_genetico_alterado
        
    

    def cruzamento(self):
        #Embalhara populacao
        self.indiv=sorted(self.indiv,key=lambda x: random() )
        
        for j in range(self.tamanho/2):            
            pai=self.indiv[j].codigo_genetico
            mae=self.indiv[j+self.tamanho/2].codigo_genetico
            
            n=self.numero_de_cromossomos*self.numero_genes_por_cromossomo
            
            corte=1+sorted(range(n-1),key=lambda x: random())[0]

            if random()<self.taxa_de_reproducao:
                codigo_filho1=pai[:corte]+mae[corte:corte+(n/2)]+pai[corte+(n/2):]
                codigo_filho2=mae[:corte]+pai[corte:corte+(n/2)]+mae[corte+(n/2):]   
            else:
                codigo_filho1=pai
                codigo_filho2=mae

            #Mutacao
            for codigo in [codigo_filho1,codigo_filho2]:
                self.indiv+=[indviduo(self.mutacao(codigo), self.funcao_aptidao)]
                


    def evolucao(self,numero_de_geracoes=1):
        for i in range(numero_de_geracoes):
            self.cruzamento()
            self.selecao()






