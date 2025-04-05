import string
import random
import unicodedata

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

#4. Comprueba las condiciones dadas de un usuario ingresado
def validacion_usuario(usuario):
        if (len(usuario) >= 5 and
        any(ch.isdigit() for ch in usuario) and
        any(ch.isupper() for ch in usuario) and
        usuario.isalnum()):
            return "El nombre de usuario es válido."
        else:
            return "EL nombre de usuario no cumple con los requisitos"

#5. determinar el tiempo de reaccion de un jugador si es normal, rapido o lento

def categoria_tiempo_reaccion(tiempo):
    c = "Categoria: "

    if tiempo > 500:
        return c + "Lento"
    elif tiempo >= 200 and tiempo <= 500:
        return c + "Normal"
    else:
        return c + "Rapido"
        
#6. encontrar menciones de alguna palabra en una lista de textos

def mencion_palabra_en_lineas(palabra_ingresada, texto):
    palabra_ingresada = palabra_ingresada.lower()
    conteo = 0
    for linea in texto:
        palabras = linea.split()
        
        for palabra in palabras:
            palabra = palabra.lower()
            if palabra == palabra_ingresada:
                conteo += 1
    
    return conteo

#7.generar un codigo de descuento con usuario,fecha actual 
#y caracteres alfanumericos hasta completar 30 caracteres en total
def generador_codigo(usuario, fecha):
    fecha_formato = fecha.strftime("%Y%m%d")
    
    # determino cuantos caracteres llevo al momento para ver con cuantos debo completar
    x = int(len(usuario)+ len(fecha_formato)) 
    
    restante = 28 - x 
    #28 porque dos seran los -
    
    #genero un string con valores random
    caracteres=string.ascii_uppercase + string.digits
    
    
    return usuario.upper() + "-" + fecha_formato.upper() + "-" +''.join(random.choices(caracteres, k= restante))
 
#8. determine si dos palabras son anagramas
def verificar_anagrama(palabra1, palabra2):
    palabra1 = palabra1.replace(" ", "").lower()
    palabra2 = palabra2.replace(" ", "").lower()
    if sorted(palabra1) == sorted(palabra2):
        return "Son anagramas."
    else:
        return "No son anagramas."

#9. Tengo una lista de nombres y datos con errores a corregir 
# para evitar amontonar codigo 
# dividire cada condicion de correcion en una funcion


def eliminar_nulos(lista):       
    lista = [x for x in lista if x and x.strip()]
    return lista


    
def eliminar_espacio_en_blanco(lista):
    # .strip() elimina espacios al inicio y al finaly  
    return [x.strip().replace("  ", " ") for x in lista]

def palabras_formato_titulo(lista):
        
        lista=[x.title() for x in lista]
        return lista

def eliminar_repetidos(lista):

        lista_sin_repetidos=[]
        for x in lista:
            if x not in lista_sin_repetidos:
                lista_sin_repetidos.append(x)
        return lista_sin_repetidos


#union de todas las funciones de limpieza
def limpieza_lista(lista):
    
        lista = eliminar_nulos(lista)
        lista = eliminar_espacio_en_blanco(lista)
        lista = palabras_formato_titulo(lista)
        lista = eliminar_repetidos(lista)
        return lista

    
                
                
    
    
    