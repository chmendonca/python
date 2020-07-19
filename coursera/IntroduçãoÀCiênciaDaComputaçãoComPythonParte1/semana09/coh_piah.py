# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 11:33:27 2020

@author: Cassio
"""

"""
Bem-vindo ao detector automático de COH-PIAH.
Informe a assinatura típica de um aluno infectado:

Entre o tamanho médio de palavra: 4.79
Entre a relação Type-Token: 0.72
Entre a Razão Hapax Legomana: 0.56
Entre o tamanho médio de sentença: 80.5
Entre a complexidade média da sentença: 2.5
Entre o tamanho médio de frase: 31.6
return [4.79,0.72,0.56,80.5,2.5,31.6]

Digite o texto 1 (aperte enter para sair): Navegadores antigos tinham uma frase gloriosa:"Navegar é preciso; viver não é preciso". Quero para mim o espírito [d]esta frase, transformada a forma para a casar como eu sou: Viver não é necessário; o que é necessário é criar. Não conto gozar a minha vida; nem em gozá-la penso. Só quero torná-la grande,ainda que para isso tenha de ser o meu corpo e a (minha alma) a lenha desse fogo. Só quero torná-la de toda a humanidade;ainda que para isso tenha de a perder como minha. Cada vez mais assim penso.Cada vez mais ponho da essência anímica do meu sangueo propósito impessoal de engrandecer a pátria e contribuirpara a evolução da humanidade.É a forma que em mim tomou o misticismo da nossa Raça.

Digite o texto 2 (aperte enter para sair): Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres. 

Digite o texto 3 (aperte enter para sair): NOSSA alegria diante dum sistema metafisico, nossa satisfação em presença duma construção do pensamento, em que a organização espiritual do mundo se mostra num conjunto lógico, coerente a harmônico, sempre dependem eminentemente da estética; têm a mesma origem que o prazer, que a alta satisfação, sempre serena afinal, que a atividade artística nos proporciona quando cria a ordem e a forma a nos permite abranger com a vista o caos da vida, dando-lhe transparência.

Digite o texto 4 (aperte enter para sair):
return ["Navegadores antigos tinham uma frase gloriosa:"Navegar é preciso; viver não é preciso". Quero para mim o espírito [d]esta frase, transformada a forma para a casar como eu sou: Viver não é necessário; o que é necessário é criar. Não conto gozar a minha vida; nem em gozá-la penso. Só quero torná-la grande,ainda que para isso tenha de ser o meu corpo e a (minha alma) a lenha desse fogo. Só quero torná-la de toda a humanidade;ainda que para isso tenha de a perder como minha. Cada vez mais assim penso.Cada vez mais ponho da essência anímica do meu sangueo propósito impessoal de engrandecer a pátria e contribuirpara a evolução da humanidade.É a forma que em mim tomou o misticismo da nossa Raça.",
        "Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres.",
        "NOSSA alegria diante dum sistema metafisico, nossa satisfação em presença duma construção do pensamento, em que a organização espiritual do mundo se mostra num conjunto lógico, coerente a harmônico, sempre dependem eminentemente da estética; têm a mesma origem que o prazer, que a alta satisfação, sempre serena afinal, que a atividade artística nos proporciona quando cria a ordem e a forma a nos permite abranger com a vista o caos da vida, dando-lhe transparência."]

O autor do texto 2 está infectado com COH-PIAH

texto = "Muito além, nos confins inexplorados da região mais brega da Borda Ocidental desta Galáxia, há um pequeno sol amarelo e esquecido. Girando em torno deste sol, a uma distancia de cerca de 148 milhões de quilômetros, há um planetinha verde-azulado absolutamente insignificante, cujas formas de vida, descendentes de primatas, são tão extraordinariamente primitivas que ainda acham que relógios digitais são uma grande ideia."
calcula_assinatura(texto)
>[5.571428571428571, 0.8253968253968254, 0.6984126984126984, 210.0, 4.5, 45.888888888888886]
"""

import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma 
    assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]
    
#    print([4.79,0.72,0.56,80.5,2.5,31.6])
#
#    return [4.79,0.72,0.56,80.5,2.5,31.6]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista 
       contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos
#    return ['Navegadores antigos tinham uma frase gloriosa:"Navegar é preciso; viver não é preciso". Quero para mim o espírito [d]esta frase, transformada a forma para a casar como eu sou: Viver não é necessário; o que é necessário é criar. Não conto gozar a minha vida; nem em gozá-la penso. Só quero torná-la grande,ainda que para isso tenha de ser o meu corpo e a (minha alma) a lenha desse fogo. Só quero torná-la de toda a humanidade;ainda que para isso tenha de a perder como minha. Cada vez mais assim penso.Cada vez mais ponho da essência anímica do meu sangueo propósito impessoal de engrandecer a pátria e contribuirpara a evolução da humanidade.É a forma que em mim tomou o misticismo da nossa Raça.',
#        'Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres.',
#        'NOSSA alegria diante dum sistema metafisico, nossa satisfação em presença duma construção do pensamento, em que a organização espiritual do mundo se mostra num conjunto lógico, coerente a harmônico, sempre dependem eminentemente da estética; têm a mesma origem que o prazer, que a alta satisfação, sempre serena afinal, que a atividade artística nos proporciona quando cria a ordem e a forma a nos permite abranger com a vista o caos da vida, dando-lhe transparência.']

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do 
       texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da 
       sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da 
       frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras 
       que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras
       diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

### Funções para cálculo dos traços linguísticos ###
def calculo_basico(texto):
    '''Esta função calcula os valores básicos utilizados para os cálculos de
       traços linguísticos.'''
       
    sentencas = separa_sentencas(texto)
#    print(sentencas)
#    print(len(sentencas))
    
    frases = []
    for sentenca in sentencas:
        frases.append(separa_frases(sentenca))
        if len(frases) > 1:
            frases[0]=frases[0]+frases[1]
            del frases[1]
    frases = frases[0]    
#    print(frases)
#    print(len(frases))
    
    palavras = []
    for frase in frases:
        palavras.append(separa_palavras(frase))
        if len(palavras) > 1:
            palavras[0]=palavras[0]+palavras[1]
            del palavras[1]
    palavras = palavras[0]
#    print(palavras)
#    print(len(palavras))
    
    return [sentencas,frases,palavras]
    
    
def tamanho_médio_palavra(palavras):
    '''Tamanho médio de palavra é a soma dos tamanhos das palavras dividida
       pelo número total de palavras.'''
    
    soma_tamanho_palavras = 0
    for palavra in palavras:
        soma_tamanho_palavras += len(palavra)
#    print(soma_tamanho_palavras)
    
    return soma_tamanho_palavras/len(palavras)

def relacao_type_token(palavras):
    '''Relação Type-Token é o número de palavras diferentes dividido pelo 
       número total de palavras. Por exemplo, na frase "O gato caçava o rato",
       temos 5 palavras no total (o, gato, caçava, o, rato) mas somente 4 
       diferentes (o, gato, caçava, rato).'''
       
    num_palavras_diferentes = n_palavras_diferentes(palavras)
#    print(num_palavras_diferentes)
    
    return num_palavras_diferentes/len(palavras)
   
def razao_hapax_legomana(palavras):
    '''Razão Hapax Legomana é o número de palavras que aparecem uma única vez 
       dividido pelo total de palavras. Por exemplo, na frase "O gato caçava o
       rato", temos 5 palavras no total (o, gato, caçava, o, rato) mas somente
       3 que aparecem só uma vez (gato, caçava, rato).'''
    
    num_palavras_unicas = n_palavras_unicas(palavras)
#    print(num_palavras_unicas)
    
    return num_palavras_unicas/len(palavras) 
       
def tamanho_medio_sentenca(sentencas):
    '''Tamanho médio de sentença é a soma dos números de caracteres em todas as
       sentenças dividida pelo número de sentenças (os caracteres que separam
       uma sentença da outra não devem ser contabilizados como parte da
       sentença).'''
       
    soma_caracteres_todas_sentencas = 0
    for sentenca in sentencas:
#        print(len(sentenca))
        soma_caracteres_todas_sentencas += len(sentenca)
#    print(soma_caracteres_todas_sentencas)
    
    return soma_caracteres_todas_sentencas/len(sentencas)

def complexidade_media_sentenca(sentencas,frases):
    '''Complexidade de sentença é o número total de frases divido pelo número 
       de sentenças.'''
       
#    print(len(sentencas))
#    print(len(frases))
    
    return len(frases)/len(sentencas)

def tamanho_medio_frase(frases):
    '''Tamanho médio de frase é a soma do número de caracteres em cada frase
       dividida pelo número de frases no texto (os caracteres que separam uma
       frase da outra não devem ser contabilizados como parte da frase).'''
    
    soma_caracteres_todas_frases = 0
    for frase in frases:
        soma_caracteres_todas_frases += len(frase)
#    print(soma_caracteres_todas_frases)
    
    return soma_caracteres_todas_frases/len(frases)

### Funçoes a serem implementadas para o trabalho de fim de curso ###
def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve
       devolver o grau de similaridade nas assinaturas.'''
    
    somatorio = 0
    for index in range(6):
        numerador = abs(as_a[index]-as_b[index])
#        print("numerador[%s]: " %index + str(numerador))
        somatorio +=numerador
#    print("somatorio[%s]: " %index + str(somatorio))
    
    s_ab = somatorio/6
#    print("s_ab: " + str(s_ab))
        
    return s_ab

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do
       texto.'''
    
    basico = calculo_basico(texto) #isto retorna [sentencas,frases,palavras]
       
    wal = tamanho_médio_palavra(basico[2])
    ttr = relacao_type_token(basico[2])
    hlr = razao_hapax_legomana(basico[2])
    sal = tamanho_medio_sentenca(basico[0])
    sac = complexidade_media_sentenca(basico[0],basico[1])
    pal = tamanho_medio_frase(basico[1])
    
    return [wal, ttr, hlr, sal, sac, pal]


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura 
       ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade
       de ter sido infectado por COH-PIAH.'''
       
    assinaturas = []   
    for texto in textos:
        assinaturas.append(calcula_assinatura(texto))
#    print(assinaturas)
    graus_de_similaridade = []
    for assinatura in assinaturas:
        graus_de_similaridade.append(compara_assinatura(assinatura,ass_cp))
#    print(graus_de_similaridade)
    
    mais_similar = graus_de_similaridade.index(min(graus_de_similaridade)) + 1
    
    print ("\nO autor do texto %s está infectado com COH-PIAH" %mais_similar)
    
    return mais_similar
        

def main():
    ass_cp = le_assinatura()
    textos = le_textos()
    avalia_textos(textos,ass_cp)
    
main()
texto_teste = "Muito além, nos confins inexplorados da região mais brega da Borda Ocidental desta Galáxia, há um pequeno sol amarelo e esquecido. Girando em torno deste sol, a uma distancia de cerca de 148 milhões de quilômetros, há um planetinha verde-azulado absolutamente insignificante, cujas formas de vida, descendentes de primatas, são tão extraordinariamente primitivas que ainda acham que relógios digitais são uma grande ideia."
