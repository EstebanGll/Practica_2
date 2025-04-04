import string

# funcion usada para verificar si una palabra comienza con vocal
def empieza_con_vocal(palabra):
    return palabra.startswith(('A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'))

#1. Divide en lineas y luego analiza linea por linea diviendola en palabras 
# para revisar la segunda palabra y verificar si comienza con vocal
def segunda_palabra_vocal_inicial(text):
    
    lineas = text.split('\n')
    
    for linea in lineas:
        #revisa si la linea tiene mas de dos palabras para ahi si examinarla
        palabras = linea.split()
        if len(palabras) > 1 and empieza_con_vocal(palabras[1]):
            print(linea)
        
#2. revisa de una lista de strings cual tiene mas palabras 
def lista_texto_mas_largo(lista):
    
    texto_mas_largo = ""
    cantidad_palabras = 0
    for linea in lista:
        palabras = linea.split()
        
        if len(palabras) > cantidad_palabras:
            cantidad_palabras = len(palabras)
            texto_mas_largo = linea
            
    return texto_mas_largo

#3. revisa de un string de varias lineas cuales poseen la palabra clave 
def filtrar_lineas_por_palabra(palabra_clave, texto):
    lineas = texto.split('\n')
    
    for linea in lineas:
        palabras = linea.split()
        
        # Eliminar signos de puntuación de cada palabra
        palabras_limpias = [palabra.strip(string.punctuation) for palabra in palabras]
        
        if palabra_clave in palabras_limpias:
            print(linea)
    
                
                
    
    
    