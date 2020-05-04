# -*- coding: utf-8 -*-
"""
Chapter 10 - Arquivos e Excesso~es (Exemplo - page 272 until )
Book: Curso Intensivo de Python
Date: 24Apr2020
Obs.: 
"""

#filename = "alice.txt"
#filename = "text_files/alice.txt"

def count_words(filename):
    try:
        with open (filename) as f:
            contents = f.read()
    except:
#        msg = "Sorry, the fiel " + filename + " does not exist!"
#        print (msg)
        pass
    else:
        #Counts the approximated number of words in the file
        words = contents.split()
        num_words = len(words)
        print ("The file " + filename + " has about " + str(num_words) + " words")

filename = "text_files/alice.txt"
count_words(filename)

filename = "text_files/siddhartha.txt"
count_words(filename)

#The name was intentionally written wrongly
filename = "text_files/mobby_dick.txt"
count_words(filename)

filename = "text_files/little_women.txt"
count_words(filename)

for book in ["text_files/alice.txt","text_files/siddhartha.txt", \
             "text_files/mobby_dick.txt","text_files/little_women.txt"]:
    count_words(book)