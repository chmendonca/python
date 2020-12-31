# -*- coding: utf-8 -*-
"""
Created on Mon Dec 2020
@author: Cassio H. Mendonca
"""


from datetime import datetime
import os
import sys
import time, timeit

inicio = timeit.default_timer()

import scrappingBot.files as files
import scrappingBot.importingData_class_v1 as impData

# =============================================================================
# function1: This function concentrates all commands to execute the logic that
#   will download the pages of the selection 
# =============================================================================
def importing_all(extract_time, year, month, day, selected_state_name, selected_state_xpath_index, selected_region_name, selected_sub_region_name, selected_category_name, selected_category_xpath_index, selected_filter):
    sOlx = impData.ScrappingOlx()
    sOlx.doing_nothing()
    sOlx.trying_to_close_pop_up()
    sOlx.openingState(selected_state_xpath_index)
    sOlx.doing_nothing()
    sOlx.trying_to_close_pop_up()
    sOlx.openingRegion(selected_region_name)
    sOlx.doing_nothing()
    sOlx.trying_to_close_pop_up()
    if selected_sub_region_name == 'Não Aplicável':
        pass
    else:
        sOlx.openingSubRegion(selected_sub_region_name)
        sOlx.trying_to_close_pop_up()
        sOlx.doing_nothing()
    sOlx.openingCategory(selected_category_xpath_index)
    sOlx.trying_to_close_pop_up()
    sOlx.doing_nothing()
    '''
    if selected_filter == 2:
        sOlx.filtering_around_places()
    '''
    while not(sOlx.end_of_download):
        sOlx.collecting_data()
        sOlx.switching_pages()
    sOlx.doing_nothing()
    
    input('hit enter to continue')
    sOlx.closing_connection()
    sOlx.saving_data(extract_time, year, month, day, selected_state_name, selected_region_name, selected_sub_region_name, selected_category_name)
    
# =============================================================================
# Listing all available states in Brazil
# Obs.: The option "Brazil" is not available because it requires speficic rules
#   to download the data
# =============================================================================
states = ['RJ','SP','MG','PR','RS','SC','ES','BA','PE','DF','CE','MS','GO','AM','RN','PB','PA','MT','AL','SE','MA','AC','RO','TO','PI','AP','RR']

# =============================================================================
# Listing all available areas (regions) under each state
# Obs.: The areas were listed as dictionary because each state could have one
#   or more areas (regions)
# =============================================================================
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

# =============================================================================
# Listing all available sub-areas (sub-regions) under each area (region)
# Obs.: The sub-areas were listed as dictionary because the areas could
#   have one or more sub-areas (sub-regions). There are areas that do not have
#   sub-areas
# =============================================================================
sub_areas = {'DDD 92 - Região de Manaus':['Manaus','Outras cidades'],'DDD 97 - Leste do Amazonas':['Região do Centro Amazonense','Região do Norte Amazonense','Região do Sudoeste Amazonense','Região do Sul Amazonense'],'DDD 71 - Salvador':['Salvador','Grande Salvador','Outras cidades'],'DDD 73 - Sul da Bahia':['Todas as cidades'],'DDD 74 - Juazeiro, Jacobina e região':['Todas as cidades'],'DDD 75 - F. de Santana, Alagoinhas e região':['Todas as cidades'],'DDD 77 - V da Conquista, Barreiras e região':['Todas as cidades'],'DDD 85 - Fortaleza e região':['Fortaleza','Grande Fortaleza','Outras cidades'],'DDD 27 - Norte do Espírito Santo':['Vitória','Outras cidades','Vila Velha','Afonso Cláudio e região','Guarapari e região','Região de Colatina e Nova Venécia','Região de Linhares e São Mateus','Santa Teresa e região'],'DDD 28 - Sul do Espírito Santo':['Afonso Cláudio e região','Cachoeiro de Itapemirim e Região sul','Guarapari e região'],'DDD 62 - Grande Goiânia e Anápolis':['Região Campinas','Região Central','Região Leste','Região Macambira e Cascavél','Região Mendanha','Região Noroeste','Região Norte','Região Oeste','Região Sudeste','Região Sudoeste','Região Sul','Vale do Meia Ponte','Grande Goiânia','Outras cidades'],'DDD 64 - Rio Verde, Caldas Novas e região':['Todas as cidades'],'DDD 98 - Região de São Luís':['São Luís','Outras Cidades'],'DDD 99 - Imperatriz, Caxias e região':['Todas as cidades'],'DDD 65 - Cuiabá e região':['Cuiabá','Outras Cidades'],'DDD 66 - Rondonópolis, Sinop e região':['Todas as cidades'],'DDD 31 - Belo Horizonte e região':['Barreiro','Pampulha','Venda Nova','Zona Centro-sul','Zona Leste','Zona Nordeste','Zona Noroeste','Zona Norte','Zona Oeste','Grande Belo Horizonte','Ouro Preto e Cons. Lafayete','Região de Ipatinga','Região de Sete Lagoas','Zona da Mata'],'DDD 32 - Juiz de Fora e região':['Barbacena e São João Del Rei','Região de Juiz de Fora','Região de Muriaé, Ubá e Viçosa'],'DDD 33 - Gov. Valadares, T. Otoni e região':['Manhuaçu','Região de Governador Valadares','Região de Ipatinga','Região de Teófilo Otoni','Vale do Jequitinhonha'],'DDD 34 - Uberlândia, Uberaba e região':['Alto Paranaíba','Triângulo Mineiro'],'DDD 35 - Poços de Caldas e Varginha':['Poços de Caldas e Pouso Alegre','Região de Itajubá','Região de Lavras','Região de Passos','Região de Varginha e Alfenas'],'DDD 37 - Divinópolis e região':['Região Central Mineira','Região de Divinópolis e Formiga','Região de Sete Lagoas'],'DDD 38 - Mtes Claros, Diamantina e região':['Noroeste de Minas','Norte de Minas','Região de Montes Claros','Região de Pirapora e Curvelo','Vale do Jequitinhonha'],'DDD 91 - Região de Belém':['Belém','Outras Cidades'],'DDD 93 - Região de Santarém':['Todas as cidades'],'DDD 94 - Região de Marabá':['Todas as cidades'],'DDD 41 - Curitiba e região':['Bairro Novo','Boa Vista','Boqueirão','Cajuru','Cidade Industrial','Fazendinha Portão','Matriz','Pinheirinho','Santa Felicidade','Grande Curitiba','Outras cidades'],'DDD 42 - Pta Grossa, Guarapuava e região':['Região de Guarapuava','Região de Ponta Grossa e Telêmaco Borba','Sudeste Paranaense'],'DDD 43 - Londrina e região':['Centro-norte Paranaense','Nordeste Paranaense','Região de Londrina'],'DDD 44 - Maringá e região':['Centro-oeste Paranaense','Norte Paranaense','Oeste Paranaense','Região de Maringá'],'DDD 45 - Foz do Iguaçu, Cascavel e região':['Região de Cascavel','Região de Foz do Iguaçu'],'DDD 46 - F. Beltrão e Pato Branco e região':['Centro-sul Paranaense','Sudoeste Paranaense'],'DDD 81 - Grande Recife':['Recife','Grande Recife','Outras cidades'],'DDD 87 - Petrolina, Garanhuns e região':['Região de São Francisco Pernambucano','Região do Agreste Pernambucano','Região do Sertão Pernambucano'],'DDD 86 - Teresina, Parnaíba e região':['Teresina','Outras Cidades'],'DDD 89 - Picos, Floriano e região':['Todas as cidades'],'DDD 51 - Porto Alegre e região':['Campus PUC','Centro','Extremo Sul','Leste','Moinhos de Vento','Norte','Praia de Belas','Sul','Grande Porto Alegre','Outras cidades'],'DDD 53 - Pelotas, Bagé, Rio Gde e região':['Região de Bagé','Sudeste Rio-grandense'],'DDD 54 - Caxias do Sul e região':['Região de Carazinho','Região de Caxias do Sul','Região de Erechim','Região de Gramado e Canela','Região de Não Me Toque e Soledade','Região de Passo Fundo','Região de Vacaria'],'DDD 55 - Sta Maria, Cruz Alta e região':['Noroeste do Estado','Norte do Estado','Oeste do Estado','Região de Cruz Alta e Ijuí','Região de Santa Maria'],'DDD 47 - Norte de Santa Catarina':['Região de Joinville e Norte do Estado','Região do Vale do Itajaí'],'DDD 48 - Florianópolis e região':['Centro','Continente','Leste','Norte','Sul','Grande Florianópolis','Outras cidades'],'DDD 49 - Oeste de Santa Catarina':['Região de Chapecó','Região de Joaçaba','Região de Xanxerê e Concórdia','Regiões de Curitibanos e C. dos Lages'],'DDD 11 - São Paulo e região':['Centro','Zona Leste','Zona Norte','Zona Oeste','Zona Sul','ABCD','Alphaville e Tamboré','Outras cidades','Interior','Região de Bragança','Região de Jundiaí'],'DDD 12 - V. do Paraíba e Litoral Norte':['Litoral Norte','Região de Campos do Jordão','Vale do Paraíba'],'DDD 13 - Baixada Santista e Litoral Sul':['Litoral Sul','Outras cidades','Região de Santos'],'DDD 14 - Bauru, Marília e região':['Região de Avaré','Região de Bauru','Região de Botucatu','Região de Jaú','Região de Lins','Região de Marília','Região de Ourinhos'],'DDD 15 - Sorocaba e região':['Região de Capão Bonito','Região de Itapetininga','Região de Itapeva','Região de Piedade e Ibiúna','Região de Sorocaba','Região de Tatuí'],'DDD 16 - Ribeirão Preto e região':['Região de Araraquara','Região de Franca','Região de Jaboticabal','Região de Ribeirão Preto','Região de São Carlos'],'DDD 17 - S. José do Rio Preto e região':['Região de Barretos','Região de Catanduva','Região de Jales e Votuporanga','Região de São José do Rio Preto'],'DDD 18 - Presidente Prudente e região':['Pres. Prudente, Araçatuba e região','Região de Adamantina e Dracena','Região de Araçatuba','Região de Assis'],'DDD 19 - Grande Campinas':['Mogi Mirin e Pirrassununga','Região de Campinas','Região de Limeira','Região de Piracicaba','Região de Rio Claro']}

# =============================================================================
# Listing all available options
# Not all sub-options were listed because it is a PoC and it was decided that
#   it should be an improvement for future releases
# =============================================================================
categories = ['IMÓVEIS','AUTO E PEÇAS','PARA SUA CASA','ELETRÔNICOS E CELULARES','MÚSICA E HOBBIES','ESPORTE E LAZER','ARTIGOS INFANTIS','ANIMAIS DE ESTIMAÇÃO','MODA E BELEZA','AGRO E INDÚSTRIA','COMÉRCIO E ESCRITÓRIO','SERVIÇOS','VAGAS DE EMPREGO']



# =============================================================================
# step1: checking if exists the cartola.json file
# If exists, it skips this step. Else it will create a new empty file
# =============================================================================
if not(files.checkingIfExistsFile('olx.json')):
    files.creatingFile(False,'olx.json')

# =============================================================================
# step2: getting the time and date of the download
# =============================================================================
now = datetime.now()

extract_time = str(now.year) + str(now.month) + str(now.day) + '_' + str(now.hour) + 'h' + str(now.minute) + 'm'

# =============================================================================
# function1: This function concentrates all commands to execute the logic that
#   will download the pages of the selection 
# =============================================================================
#generating and printing a list of states available
for state in states:
    if state != states[-1]:
        print(state + ', ', end='')
    else:
        print(state)

selected_state_name = input('Digite a sigla do Estado: ')
print('\n')

#if the state is in the list it continues allowing the selections 
if selected_state_name.upper() in states:
    #sets the status to true to indicate that a valid choice has been made
    state_status = True 
    selected_state_name = selected_state_name.upper()
    #get the list of regions under the state
    regions = areas[selected_state_name]
    #generating and printing a list of regions available
    region_number = 1
    for region in regions:
        print('(' + str(region_number) + ') ' + region)
        region_number += 1
    #this selection was inserted here to ensure that it will not be available if an invalid choice has been made
    selected_region = int(input('Digite o número da região: '))
    print('\n')
else:
    #sets the status to false to indicate that an invalid choice has been made
    state_status = False

#if the state is valid and the region is in the list it continues allowing the selections 
if state_status and selected_region in range(1,len(regions)+1):
    #sets the status to true to indicate that a valid choice has been made
    region_status = True
    #get the region to check if there are sub-regions under that
    region = regions[selected_region - 1]
    #check if the region is in the keys of sub-areas dictionary
    if region in sub_areas.keys():
        #get the sub-regions list
        sub_regions = sub_areas[region]
        #generating and printing a list of sub-regions available
        sub_region_number = 1
        for sub_region in sub_regions:
            print('(' + str(sub_region_number) + ') ' + sub_region)
            sub_region_number += 1
        selected_sub_region = int(input('Escolha o número da sub-região: '))
        print('\n')
    else:
        #variable to False to indicate that no sub-regions are available
        selected_sub_region = False
    #generating and printing a list of categories available    
    category_number = 1
    for category in categories:
        print(str(category_number) + ' - ' + category)
        category_number += 1
    selected_category = int(input('Escolha o número da categoria: '))
    print('\n')
    print('1 - Todos os bairros e cidades')
    print('2 - Filtrar por bairros / cidades')
    selected_filter = int(input('Escolha o número do filtro: '))
    print('\n')
else:
    #sets the status to false to indicate that an invalid choice has been made
    region_status = False

#if all choices were valid (except by sub-region) it enters on this 'if logic'
if state_status and region_status and selected_category in range(1,len(categories) + 1):
    #getting the name of region (it was input a number)
    selected_region_name = regions[selected_region - 1]
    #getting the name of category (it was input a number)
    selected_category_name = categories[selected_category - 1]
    print('Estado escolhida:', selected_state_name)
    print('Região escolhida:', selected_region_name)
    try:
        #getting the name of sub-region (it was input a number), if exists
        selected_sub_region_name = sub_regions[selected_sub_region - 1]
        
    except:
        #variable to False to indicate that no sub-region name is available
        selected_sub_region_name = 'Não Aplicável'
    print('Sub-Região escolhida:', selected_sub_region_name)
    print('Categoria Escolhida:', selected_category_name)
    if selected_filter == 1:
        print('Filtro escolhido: Todos os bairros e cidades')
    else:
        print('Filtro escolhido: Filtrar por bairros / cidades')
    #getting the index in the list to set the xpath value
    selected_state_xpath_index = int(states.index(selected_state_name)) + 1
    selected_category_xpath_index = int(categories.index(selected_category_name)) + 1

    importing_all(extract_time, str(now.year), str(now.month), str(now.day), selected_state_name, selected_state_xpath_index, selected_region_name, selected_sub_region_name, selected_category_name, selected_category_xpath_index, selected_filter)
    
else:
    #if any choice is invalid it sets a message to the user
    print('Escolha inválida. Tente novamente!\n')

fim = timeit.default_timer()
print ('\n>>>>>>>>\nduracao: %f\n<<<<<<<<' % (fim - inicio))


'''
//*[@id="ad-list"]/li[6]/a/div/div[3]/div/h2
//*[@id="ad-list"]/li[6]/a/div/div[3]/div/div/p
//*[@id="ad-list"]/li[6]/a/div/div[3]/div/p/text()


//*[@id="ad-list"]/li[7]/a/div/div[3]/div/h2
//*[@id="ad-list"]/li[7]/a/div/div[3]/div/span



'''