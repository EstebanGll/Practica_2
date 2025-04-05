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

###10. procesar datos de un grupo de jugadores por rondas hasta el ranking final
###representar

def ordenar_datos(datos_jugador):
    #Primero ordenamos por puntaje cada kill da 3 puntos, cada asistencia da 1, y la muerte quita 1
    datos_tabla = {}
    #.items da los pares clave-valor
    for jugador, stats in datos_jugador.items():
        kills = stats['kills']
        assists = stats['assists']
        deaths = 1 if stats['deaths'] else 0

        puntaje = kills * 3 + assists - deaths

        #devuelve los datos del jugador con el puntaje
        datos_tabla[jugador] = {
            'kills': kills,
            'assists': assists,
            'deaths': deaths,
            'MVPs': 0,
            'Puntaje': puntaje
        }
    # Ordenar por puntaje descendente 
    # sorted(datos, key = dato en el que se basa para ordenar, reverse = True >- de mayor a menor)
    # x[1]["Puntaje"] accede al puntaje del jugador, x es la tupla clave - valor 
    # esto genera una tupla de valores
    tabla_ordenada = sorted(datos_tabla.items(), key=lambda x: x[1]['Puntaje'], reverse=True)
        
    # accedemos al primer jugador, el con mayor puntaje
    # [0] primer jugador y [1] sus stats
    tabla_ordenada[0][1]["MVPs"] = 1
    return tabla_ordenada

def imprimir_tabla_ronda(datos_jugadores):
    
    # Formato impresion tabla
    
    # :^8 = ^ alineacion central y un ancho de 8 espacios 
    print(f"{"Jugador":^8} {"Kills":^8} {"Asistencias":^8} {"Muertes":^8} {"MVPs":^8} {"Puntos":^8}")
    
    print(56*"-")
    
    for jugador, stats in datos_jugadores:
        print(f"{jugador:^8} {stats['kills']:^8} {stats['assists']:^8} {stats['deaths']:^8} {stats['MVPs']:^8} {stats['Puntaje']:^8}")
    
    print(56*"-")
    print()
   
"""def acumular_resultados(lista_de_tuplas):
    acumulado = []
    datos_jugador = ('Jugador', {'kills': 0,'assists': 0,'deaths': 0,'MVPs': 0,'Puntaje': 0})

    for n in range(len(lista_de_tuplas)):
        lista_de_tuplas[n]
        
    

    return acumulado"""
    
def acumular_rondas(rondas_ordenadas):
    acumulador = {}

    for ronda in rondas_ordenadas:
        for jugador, stats in ronda:
            if jugador not in acumulador:
                acumulador[jugador] = {
                    'kills': 0,
                    'assists': 0,
                    'deaths': 0,
                    'MVPs': 0,
                    'Puntaje': 0
                }

            # Sumamos cada estadística
            for clave in stats:
                acumulador[jugador][clave] += stats[clave]

    # Devolvemos los datos acumulados en una lista de tuplas ordenadas por Puntaje descendente
    return sorted(acumulador.items(), key=lambda x: x[1]['Puntaje'], reverse=True)

    

   
def imprimir_todo(datos_jugadores):
    
    # generamos la lista donde estaran las tablas ordenadas por estadisticas
    lista_ordenada = []  
    
    # imprimir datos por ronda
    for n in range(len(datos_jugadores)):
        print(f"Ranking ronda :{n + 1}")
        tabla_ordenada = ordenar_datos(datos_jugadores[n])
        
        # cargamos a la nuevo lista con los datos ordenados
        lista_ordenada.append(tabla_ordenada)
        imprimir_tabla_ronda(tabla_ordenada)
      
    # imprimir datos ronda final
    
    # acumulamos los datos de todas las rondas ya con puntaje
    acumulados = acumular_rondas(lista_ordenada)
    
    print("Ranking Final")
    # ordenamos por puntaje para imprimirlo
    #orden_final = sorted(acumulados.items(), key=lambda x: x[1]['Puntaje'], reverse=True)
    imprimir_tabla_ronda(acumulados)
    
    
    