def strip_string(list_of_strings):
    list_of_stripped_strings = []
    for string in list_of_strings:
        list_of_stripped_strings.append(string.strip().title())
    return list_of_stripped_strings

def menor_nome(list_of_strings):
    list_of_stripped_strings = strip_string(list_of_strings)
    len_first_string = len(list_of_stripped_strings[0])
    smaller_string = list_of_stripped_strings[0]
    for string in list_of_stripped_strings:
        if len(string) < len_first_string:
            len_first_string = len(string)
            smaller_string = string
    return smaller_string

'''
print(menor_nome(['maria', 'josé', 'PAULO', 'Catarina']))
# deve devolver 'José'

print(menor_nome(['maria', ' josé  ', '  PAULO', 'Catarina  ']))
# deve devolver 'José'

print(menor_nome(['Bárbara', 'JOSÉ  ', 'Bill']))
# deve devolver José
'''