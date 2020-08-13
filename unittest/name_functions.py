# def get_formatted_name(first,last):
def get_formatted_name(first,last,middle=''):
    """Gera um nome completo formatado de modo elegante"""
    # full_name = first + ' ' + last
    if middle == '':
        full_name = first + ' ' + last
    else:     
        full_name = first + ' ' + middle + ' ' + last
    
    return full_name.title()