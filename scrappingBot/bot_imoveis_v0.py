# -*- coding: utf-8 -*-
"""
Created on Mon Dec 2020
@author: Cassio H. Mendonca
"""


from datetime import datetime
import os
import sys
import time, timeit

import scrappingBot.importingData_class_v1 as impData

def importing_all(selected_state,selected_region,selected_category):
    sOlx = impData.ScrappingOlx()
    sOlx.doing_nothing()
    sOlx.openingState(selected_state)
    sOlx.doing_nothing()
    sOlx.openingRegion(selected_region)
    sOlx.doing_nothing()
    sOlx.openingCategory(selected_category)
    sOlx.closing_connection()

now = datetime.now()

extrat_time = str(now.year) + str(now.month) + str(now.day) + '_' + str(now.hour) + 'h' + str(now.minute) + 'm'
print(extrat_time)

states = ['RJ','SP','MG','PR','RS','SC','ES','BA','PE','DF','CE','MS','GO','AM','RN','PB','PA','MT','AL','SE','MA','AC','RO','TO','PI','AP','RR','BRASIL']
categories = ['IMÓVEIS','AUTO E PEÇAS','PARA SUA CASA','ELETRÔNICOS E CELULARES','MÚSICA E HOBBIES','ESPORTE E LAZER','ARTIGOS INFANTIS','ANIMAIS DE ESTIMAÇÃO','MODA E BELEZA','AGRO E INDÚSTRIA','COMÉRCIO E ESCRITÓRIO','SERVIÇOS','VAGAS DE EMPREGO']
areas = {'AC':['Rio Branco','Outras Cidades'],
'AL':['Maceió','Outras Cidades'],
'AP':['Macapá','Outras Cidades'],
'AM':['DDD 92 - Região de Manaus','DDD 97 - Leste do Amazonas'],
'BA':['DDD 71 - Salvador','DDD 73 - Sul da Bahia','DDD 74 - Juazeiro, Jacobina e região','DDD 75 - F. de Santana, Alagoinhas e região','DDD 77 - V da Conquista, Barreiras e região'],
'CE':['DDD 85 - Fortaleza e região','DDD 88 - Juazeiro do Norte, Sobral e região'],
'DF':['Brasília','Outras Cidades'],
'ES':['DDD 27 - Norte do Espírito Santo','DDD 28 - Sul do Espírito Santo'],
'GO':['DDD 62 - Grande Goiânia e Anápolis','DDD 64 - Rio Verde, Caldas Novas e região'],
'MA':['DDD 98 - Região de São Luís','DDD 99 - Imperatriz, Caxias e região'],
'MT':['DDD 65 - Cuiabá e região','DDD 66 - Rondonópolis, Sinop e região'],
'MS':['Campo Grande','Corumbá','Dourados','Outras cidades','Três Lagoas'],
'MG':['DDD 31 - Belo Horizonte e região,','DDD 32 - Juiz de Fora e região','DDD 33 - Gov. Valadares, T. Otoni e região','DDD 34 - Uberlândia, Uberaba e região','DDD 35 - Poços de Caldas e Varginha','DDD 37 - Divinópolis e região','DDD 38 - Mtes Claros, Diamantina e região'],
'PA':['DDD 91 - Região de Belém','DDD 93 - Região de Santarém','DDD 94 - Região de Marabá'],
'PB':['João Pessoa','Campina Grande, Guarabira e região','Monteiro, Picuí e região','Patos, Sousa e região','Santa Rita, Bayeux e região'],
'PR':['DDD 41 - Curitiba e região','DDD 42 - Pta Grossa, Guarapuava e região','DDD 43 - Londrina e região','DDD 44 - Maringá e região','DDD 45 - Foz do Iguaçu, Cascavel e região','DDD 46 - F. Beltrão e Pato Branco e região'],
'PE':['DDD 81 - Grande Recife','DDD 87 - Petrolina, Garanhuns e região'],
'PI':['DDD 86 - Teresina, Parnaíba e região','DDD 89 - Picos, Floriano e região'],
'RJ':{'DDD 21 - Rio de Janeiro e região':['Centro','Zona Norte','Zona Oeste','Zona Sul','Baixada Fluminense','Niterói','São Gonçalo','Itaboraí e região','Mangaratiba','Teresópolis e região'],'DDD 22 - Norte do Estado e Região dos Lagos':['Norte do Estado','Região de Nova Friburgo','Região dos Lagos'],'DDD 24 - Serra, Angra dos Reis e região':['Costa Verde','Região de Três Rios','Região Serrana','Vale do Paraíba']},
'RN':['Natal','Outras Cidades'],
'RS':['DDD 51 - Porto Alegre e região','DDD 53 - Pelotas, Bagé, Rio Gde e região','DDD 54 - Caxias do Sul e região','DDD 55 - Sta Maria, Cruz Alta e região'],'RO':['Porto Velho','Outras Cidades'],
'RR':['Boa Vista','Outras cidades'],
'SC':['DDD 47 - Norte de Santa Catarina','DDD 48 - Florianópolis e região','DDD 49 - Oeste de Santa Catarina'],
'SP':['DDD 11 - São Paulo e região','DDD 12 - V. do Paraíba e Litoral Norte','DDD 13 - Baixada Santista e Litoral Sul','DDD 14 - Bauru, Marília e região','DDD 15 - Sorocaba e região','DDD 16 - Ribeirão Preto e região','DDD 17 - S. José do Rio Preto e região','DDD 18 - Presidente Prudente e região','DDD 19 - Grande Campinas'],
'SE':['Aracaju','Outras Cidades'],
'TO':['Palmas','Outras Cidades']}
sub_areas = {'DDD 92 - Região de Manaus':['Manaus','Outras cidades'],'DDD 97 - Leste do Amazonas':['Região do Centro Amazonense','Região do Norte Amazonense','Região do Sudoeste Amazonense','Região do Sul Amazonense'],'DDD 71 - Salvador':['Salvador','Grande Salvador','Outras cidades'],'DDD 73 - Sul da Bahia':['Todas as cidades'],'DDD 74 - Juazeiro, Jacobina e região':['Todas as cidades'],'DDD 75 - F. de Santana, Alagoinhas e região':['Todas as cidades'],'DDD 77 - V da Conquista, Barreiras e região':['Todas as cidades'],'DDD 85 - Fortaleza e região':['Fortaleza','Grande Fortaleza','Outras cidades'],'DDD 27 - Norte do Espírito Santo':['Vitória','Outras cidades','Vila Velha','Afonso Cláudio e região','Guarapari e região','Região de Colatina e Nova Venécia','Região de Linhares e São Mateus','Santa Teresa e região'],'DDD 28 - Sul do Espírito Santo':['Afonso Cláudio e região','Cachoeiro de Itapemirim e Região sul','Guarapari e região'],'DDD 62 - Grande Goiânia e Anápolis':['Região Campinas','Região Central','Região Leste','Região Macambira e Cascavél','Região Mendanha','Região Noroeste','Região Norte','Região Oeste','Região Sudeste','Região Sudoeste','Região Sul','Vale do Meia Ponte','Grande Goiânia','Outras cidades'],'DDD 64 - Rio Verde, Caldas Novas e região':['Todas as cidades'],'DDD 98 - Região de São Luís':['São Luís','Outras Cidades'],'DDD 99 - Imperatriz, Caxias e região':['Todas as cidades'],'DDD 65 - Cuiabá e região':['Cuiabá','Outras Cidades'],'DDD 66 - Rondonópolis, Sinop e região':['Todas as cidades'],'DDD 31 - Belo Horizonte e região':['Barreiro','Pampulha','Venda Nova','Zona Centro-sul','Zona Leste','Zona Nordeste','Zona Noroeste','Zona Norte','Zona Oeste','Grande Belo Horizonte','Ouro Preto e Cons. Lafayete','Região de Ipatinga','Região de Sete Lagoas','Zona da Mata'],'DDD 32 - Juiz de Fora e região':['Barbacena e São João Del Rei','Região de Juiz de Fora','Região de Muriaé, Ubá e Viçosa'],'DDD 33 - Gov. Valadares, T. Otoni e região':['Manhuaçu','Região de Governador Valadares','Região de Ipatinga','Região de Teófilo Otoni','Vale do Jequitinhonha'],'DDD 34 - Uberlândia, Uberaba e região':['Alto Paranaíba','Triângulo Mineiro'],'DDD 35 - Poços de Caldas e Varginha':['Poços de Caldas e Pouso Alegre','Região de Itajubá','Região de Lavras','Região de Passos','Região de Varginha e Alfenas'],'DDD 37 - Divinópolis e região':['Região Central Mineira','Região de Divinópolis e Formiga','Região de Sete Lagoas'],'DDD 38 - Mtes Claros, Diamantina e região':['Noroeste de Minas','Norte de Minas','Região de Montes Claros','Região de Pirapora e Curvelo','Vale do Jequitinhonha'],'DDD 91 - Região de Belém':['Belém','Outras Cidades'],'DDD 93 - Região de Santarém':['Todas as cidades'],'DDD 94 - Região de Marabá':['Todas as cidades'],'DDD 41 - Curitiba e região':['Bairro Novo','Boa Vista','Boqueirão','Cajuru','Cidade Industrial','Fazendinha Portão','Matriz','Pinheirinho','Santa Felicidade','Grande Curitiba','Outras cidades'],'DDD 42 - Pta Grossa, Guarapuava e região':['Região de Guarapuava','Região de Ponta Grossa e Telêmaco Borba','Sudeste Paranaense'],'DDD 43 - Londrina e região':['Centro-norte Paranaense','Nordeste Paranaense','Região de Londrina'],'DDD 44 - Maringá e região':['Centro-oeste Paranaense','Norte Paranaense','Oeste Paranaense','Região de Maringá'],'DDD 45 - Foz do Iguaçu, Cascavel e região':['Região de Cascavel','Região de Foz do Iguaçu'],'DDD 46 - F. Beltrão e Pato Branco e região':['Centro-sul Paranaense','Sudoeste Paranaense'],
'PE':['DDD 81 - Grande Recife','DDD 87 - Petrolina, Garanhuns e região'}

for state in states:
    if state != states[-1]:
        print(state + ', ', end='')
    else:
        print(state)

selected_state = input('Digite a sigla do Estado: ')
print('\n')

if selected_state.upper() in states:
    selected_state = selected_state.upper()
    regions = areas[selected_state]
    region_number = 1
    for region in regions:
        print('(' + str(region_number) + ') ' + region)
        region_number += 1
    state_status = True
else:
    state_status = False

selected_region = int(input('Digite o número da região: '))
print('\n')

if state_status and selected_region in range(1,len(regions)+1):
    category_number = 1
    for category in categories:
        print(str(category_number) + ' - ' + category)
        category_number += 1
    selected_category = int(input('Escolha o número da categoria: '))
    print('\n')
    region_status = True
else:
    region_status = False

if state_status and region_status and selected_category in range(1,len(categories) + 1):
    selected_category = categories[selected_category - 1]
    selected_region = regions[selected_region - 1]
    print('Estado escolhida:', selected_state)
    print('Região escolhida:', selected_region)
    print('Categoria escolhida: ', selected_category)
    importing_all(int(states.index(selected_state)) + 1, int(regions.index(selected_region)) + 1, int(categories.index(selected_category)) + 1)
else:
    print('Escolha inválida. Tente novamente!\n')