def maiusculas(frase):
    string = ''
    for letter in frase:
        if letter.isupper():
            #print(letter,end="")
            string += letter
    return string
    #print('\n')

'''
print(maiusculas('Programamos em python 2?'))
# deve devolver 'P'

print(maiusculas('Programamos em Python 3.'))
# deve devolver 'PP'

print(maiusculas('PrOgRaMaMoS em python!'))
# deve devolver 'PORMMS'
'''