# class Sorting:

#     def getting_list(self, lista):
#         return lista

#     def direct_order_list(self,input_list):
#         '''it was not necessary to set the direct order list to solve the exercise, but once I had done the function, I used in the solution'''
#         len_input_list = len(input_list)
#         ordered_list = []
#         for item in input_list:
#             ordered_list.append(item)
#             ordered_list_pos = len(ordered_list) - 1
#             for pos in range(ordered_list_pos,len_input_list - 1):
#                 if ordered_list[ordered_list_pos] > input_list[pos + 1]: 
#                     ordered_list[ordered_list_pos],input_list[pos + 1] = input_list[pos + 1],ordered_list[ordered_list_pos]
#         return ordered_list
    
#     def ordenada(self,lista):
#         input_list = self.getting_list(lista)
#         ordered_list = self.direct_order_list(input_list)
#         if input_list == ordered_list:
#             return True
#         else:
#             return False

# lista = [8,9,-7,3,0]
# st = Sorting()
# print(st.ordenada(lista))

def getting_list(lista):
    return lista

def direct_order_list(input_list):
    '''it was not necessary to set the direct order list to solve the exercise, but once I had done the function, I used in the solution'''
    len_input_list = len(input_list)
    ordered_list = []
    for item in input_list:
        ordered_list.append(item)
        ordered_list_pos = len(ordered_list) - 1
        for pos in range(ordered_list_pos,len_input_list - 1):
            if ordered_list[ordered_list_pos] > input_list[pos + 1]: 
                ordered_list[ordered_list_pos],input_list[pos + 1] = input_list[pos + 1],ordered_list[ordered_list_pos]
    return ordered_list

def ordenada(lista):
    input_list = getting_list(lista)
    ordered_list = direct_order_list(input_list)
    if input_list == ordered_list:
        return True
    else:
        return False