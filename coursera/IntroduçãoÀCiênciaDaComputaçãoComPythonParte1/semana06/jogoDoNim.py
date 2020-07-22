# -*- coding: utf-8 -*-
import random
import os
"""
JOGO DO NIM

Created on Fri Jul 17 13:00:44 2020

@author: Cassio

At this game, "n" pieces are set in a table for two players. Each player remove,
alternatively at least 1 piece and a maximum of "m" pieces from the table. The
winner is the last to remove a valid number of pieces from the table.

The strategy to win the game is always to leave for the adversary a multiple of
(m + 1) pieces. For the purpose of this course, the computer will always win.
The "victim" will choose the number of pieces on the table "n" and the maximum
number "m" of pieces that will be removed per turn.
"""

def remove(n,m):
    if (n % (m+1)) > 0:
        r = (n % (m+1))
    else:
        r = random.randint(1,m)
        
    return r

def computador_escolhe_jogada(n,m,dificuldade):
    if n > m:
        if dificuldade == 2: #hard
            r = remove(n,m)
        elif dificuldade == 1: #medium
            if (n % 2) == 0:
                r = remove(n,m)
        else: #easy
            r = random.randint(1,m)
    else:
        r = m
    
    print("\nO computador tirou %s peça(s)" %r)
        
    return r
    
def usuario_escolhe_jogada(n,m):
    while True:
        try:
            r = int(input("Quantas peças você vai tirar (Máx: %s peça(s))? " %m))
        except:
            print("Digite um número inteiro maior que 0 e menor ou igual a %s!" %m)
            continue
        if r > 0 and r <= m:
            break
        else:
            print("Digite um número inteiro maior que 0 e menor ou igual a %s!" %m)
            continue
    print("\nVocê tirou %s peça(s)" %r)
    
    return r

def quemComeca(comeca):
    """This function decides who will determine the number of peças on the
       game"""
       
    enterMsg1 = "Quantas peças no tabuleiro? "
    enterMsg2 = "Limite de peças a ser(em) removida(s) por jogada? "
       
    if comeca % 2 == 0:
        print("\nComputador começa escolhendo o número de peças no tabuleiro \
              \n e o número de peças a ser retirado")
        random.seed()
        n = random.randint(10,20)
        m = random.randint(2,6)
        
        print("\n" + enterMsg1 + str(n))
        print(enterMsg2 + str(m))
        
    #*** IMPLEMENTAR ***
    #Função randomica para n onde 'n' vai ser um número randômico entre 10 e 20
    # peças e 'm' será um valor de 1 a 5, dependendo do valor da seed que será
    # os segundos do computador na hora que a função for executada
    else:
        while True:
             try:
                n = int(input(enterMsg1))
                m = int(input(enterMsg2))
                if n > 0 and m > 0 and n > m:
                    break
                else:
                    print("\nAtenção: 'n' e 'm' devem ser inteiros maiores que 0 e 'n' dever ser maior que 'm'")
                    continue
             except:
                print("\nPor favor insira somente números inteiros maiores que 0!\nAtenção: 'n' dever ser maior que 'm'")
    saida(n)
    
    return [n,m]

def saida(numero_pecas):
    """This function prints # for each piece on the table"""
    while numero_pecas >= 1:
        if numero_pecas > 5:
            print("\n" + 5 * "# ")
        else:
            print("\n" + numero_pecas * "# ")
        numero_pecas -= 5
        
    
def partida(comeca, dificuldade):
    """This the function that drives the entire program."""
    
    n_m = quemComeca(comeca) #n_m é uma lista com os valores de [n,m]
    
    #Since the computer has choosen the number of pieces, the user starts
    # playing
    if ((comeca) % 2) == 0:
        print("\nVocê começa")
        whoPlays = "user"
    #Otherwise, if the user has choosen the number of pieces, the computer
    # starts playing.
    else: 
        print("\nComputador começa")
        whoPlays = "computer"
    
    while True:
        #it is requested to you to remove a number of pieces from the table and
        # then the player is changed
        if whoPlays == "user":
            n_m[0] -= usuario_escolhe_jogada(n_m[0],n_m[1]) #updating the value of 'n'
            whoPlays = "computer"
        else:
        #it is requested to the computer to remove a number of pieces from the
        # table and then the player is changed
            n_m[0] -= computador_escolhe_jogada(n_m[0],n_m[1],dificuldade) #updating the value of 'n'
            whoPlays = "user"
        
        print("Agora resta(m) %s peça(s) no tabuleiro." %n_m[0])
        saida(n_m[0])
        
        #if 'n' is equal to 0 (all pieces removed) the game is finished
        if n_m[0] == 0:
            if whoPlays == "user":
                winner = "computador"
                print("\nFim do jogo! O %s ganhou!" %winner)
                return winner
            else:
                winner = "VOCÊ"
                print("\nFim do jogo! %s ganhou!" %winner)
                return winner
        #if 'n' is lower than 'm' but greater than 0, then 'm' = 'n'
        elif n_m[0] < n_m[1]: 
            n_m[1] = n_m[0]
        
def campeonato(comeca, dificuldade):
    match = 1
    user_score = 0
    computer_score = 0
    while match <= 3:
        print("\n**** Rodada %s ****" %match)
        #The function partida receives as input the value comeca that is fixed
        # during the campeonato and sums the match value, to alternate who will
        # start the campeonato
        winner = partida(comeca + match, dificuldade) 
        match+=1
        if winner == "computador":
            computer_score +=1
        else:
            user_score += 1
    print("\nPlacar: Você %s X %s Computador" %(user_score,computer_score)) 

def seleciona_dificuldade():
    chooseDifficulty = "1 -  Médio; 2 - Difícil; Enter para Fácil: "
    try:
        dificuldade = int(input(chooseDifficulty))
        if dificuldade == 2:
            dif = [dificuldade,"difícil"]
        elif dificuldade == 1:
            dif = [dificuldade,"média"]
        else:
            dif = [0,"fácil"]
    except:
        dif = [0,"fácil"]
    
    return dif    
    
def main():
    comeca = 1
    while True:
        print("\n" + 5*"+"," BEM VINDO AO JOGO DO NIM ",5*"+")
        print(3*"-"," Tente ganhar do computador ",3*"-")
        chooseTypeMsg1 = "Escolha '1' para uma única partida e '2' para campeonato com 3 partidas.\nQualquer outro valor para sair: "
        while True:
            try:
                chooseType = int(input(chooseTypeMsg1))
                break
            except:
                print("\nPor favor, insira um número inteiro")
            
        if chooseType == 1:
            dif = seleciona_dificuldade()
            print("\nVocê escolheu partida simples e dificuldade %s" %dif[1])
            partida(comeca, dif[0])
        elif chooseType == 2:
            dif = seleciona_dificuldade()
            print("\nVocê escolheu campeonato e dificuldade %s" %dif[1])
            campeonato(comeca, dif[0])
        else:
            print("\nVocê escolheu sair do jogo. Espero ter ver de volta logo!")
            break
        
        comeca += 1
    
    
        
main()
#print(usuario_escolhe_jogada(10,2))
#print(computador_escolhe_jogada(10,2))