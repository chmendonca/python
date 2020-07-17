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
        n -= r
        print("\nO computador tirou %s peça(s)" %r)
        print("Agora resta(m) %s peça(s) no tabuleiro." %n)
    else:
        r = m
        n -= r
        print("\nO computador tirou %s peça(s)" %r)
        print("Agora resta(m) %s peça(s) no tabuleiro." %n)
        
    return n
    
def usuario_escolhe_jogada(n,m):
    while True:
        try:
            r = int(input("Quantas peças você vai tirar?"))
        except:
            print("Digite um número inteiro!")
            continue
        if r <= m:
            break
        else:
            print("Digite um número inteiro menor ou igual a %s" %m)
            continue
    n -= r
    print("\nVocê tirou %s peça(s)" %r)
    print("Agora resta(m) %s peça(s) no tabuleiro." %n)
    
    return n

def partida():
    """n, number of pieces on table; m, maximum number of pieces to be removed;"""
    enterMsg1 = "Entre com o número de peças na mesa (n) e\no número máximo de peças a ser removido por jogada (m)"
    enterMsg2 = "Digite n,m: "
    while True:
        print (enterMsg1)
        i = input(enterMsg2)
        try:
            [n,m] = i.split(",")
            [n,m] = [int(n),int(m)]
            if n > m:
                break
            else:
                print("\nAtenção: 'n' dever ser maior que 'm'")
        except:
            print("\nPor favor insira somente números inteiros!\nAtenção: 'n' dever ser maior que 'm'")
    
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
            n = usuario_escolhe_jogada(n,m)
            whoPlays = "computer"
        else:
        #it is requested to the computer to remove a number of pieces from the
        # table and then the player is changed
            n = computador_escolhe_jogada(n,m)
            whoPlays = "user"
        
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