
# funcion usada para verificar si una palabra comienza con vocal
def empieza_con_vocal(palabra):
    return palabra.startswith(('A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'))

# Divide en lineas y luego analiza linea por linea diviendola en palabras para revisar la segunda palabra
def segunda_palabra_vocal_inicial(text):

    """
        Toma la segunda palabra de y revisa si comienza con vocal
    """
    lineas = text.split('\n')
    
    for linea in lineas:
        #revisa si la linea tiene mas de dos palabras para ahi si examinarla
        palabras = linea.split()
        if len(palabras) > 1 and empieza_con_vocal(palabras[1]):
            print(linea)
            

                
                
    
    
    