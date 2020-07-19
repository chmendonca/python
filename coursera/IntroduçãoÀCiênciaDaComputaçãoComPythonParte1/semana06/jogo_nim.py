# -*- coding: utf-8 -*-
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

def computador_escolhe_jogada(n,m):
    if n > m:
        r = n%(m+1)
        print("\nO computador tirou %s peça(s)" %r)
    else:
        r = m
        print("\nO computador tirou %s peça(s)" %r)
        
    return r
    
def usuario_escolhe_jogada(n,m):
    while True:
        try:
            r = int(input("Quantas peças você vai tirar? "))
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

def partida():
    """n, number of pieces on table; m, maximum number of pieces to be removed;"""
    enterMsg1 = "Quantas peças? "
    enterMsg2 = "Limite de peças por jogada? "
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
    
    #following the rules of the exercise, if 'n' is multiple of ('m'+1), the 
    # computer invites you to start the game
    if n%(m+1) == 0:
        print("\nVocê começa")
        whoPlays = "user"
    #if the 'n' is not multiple of ('m'+1), the computer starts the game
    else:
        print("\nComputador começa")
        whoPlays = "computer"
    
    while True:
        #it is requested to you to remove a number of pieces from the table and
        # then the player is changed
        if whoPlays == "user":
            n -= usuario_escolhe_jogada(n,m) #updating the value of 'n'
            whoPlays = "computer"
        else:
        #it is requested to the computer to remove a number of pieces from the
        # table and then the player is changed
            n -= computador_escolhe_jogada(n,m) #updating the value of 'n'
            whoPlays = "user"
        
        print("Agora resta(m) %s peça(s) no tabuleiro." %n)
        
        #if 'n' is equal to 0 (all pieces removed) the game is finished
        if n == 0:
            if whoPlays == "user":
                winner = "computador"
                print("\nFim do jogo! O %s ganhou!" %winner)
                return winner
            else:
                winner = "VOCÊ"
                print("\nFim do jogo! %s ganhou!" %winner)
                return winner
        #if 'n' is lower than 'm' but greater than 0, then 'm' = 'n'
        elif n < m: 
            m = n
        
def campeonato():
    match = 1
    u = 0
    c = 0
    while match <= 3:
        print("\n**** Rodada %s ****" %match)
        winner = partida()
        match+=1
        if winner == "computador":
            c+=1
        else:
            u+=1
    print("\nPlacar: Você %s X %s Computador" %(u,c)) 

def main():
    print(5*"+"," BEM VINDO AO JOGO DO NIM ",5*"+")
    print(3*"-"," Tente ganhar do computador ",3*"-")
    choseTypeMsg1 = "Escolha '1' para uma única partida e '2' para campeonato com 3 partidas.\nQualquer outro valor para sair: "
    c = 0;
    while c == 0:
        c = input(choseTypeMsg1)
        try:
            c = int(c)
        except:
            print("\nPor favor, insira um número inteiro")
    
    if c == 1:
        print("\nVocê escolheu partida simples")
        partida()
    elif c == 2:
        print("\nVocê escolheu campeonato")
        campeonato()
    else:
        print("\nVocê escolheu sair do jogo. Espero ter ver de volta logo!")
        
main()
#print(usuario_escolhe_jogada(10,2))
#print(computador_escolhe_jogada(10,2))