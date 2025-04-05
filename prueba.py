datos_ronda = {
    'Shadow': {'kills': 1, 'assists': 2, 'deaths': True},
    'Blaze': {'kills': 0, 'assists': 1, 'deaths': False},
    'Viper': {'kills': 2, 'assists': 0, 'deaths': True},
    'Frost': {'kills': 1, 'assists': 1, 'deaths': False},
    'Reaper': {'kills': 1, 'assists': 1, 'deaths': True}
}


def ordenar_datos(datos_ronda):
    #Primero ordenamos por puntaje cada kill da 3 puntos, cada asistencia da 1, y la muerte quita 1
    datos_tabla = {}
    #.items da los pares clave-valor
    for jugador, stats in datos_ronda.items():
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
    
tabla_ordenada = ordenar_datos(datos_ronda)
imprimir_tabla_ronda(tabla_ordenada)

#tenemos una lista de rondas, las ordenaremos y los acumularemos
def acumular_rondas(lista_rondas):
    resumen_total = {}

    for ronda in lista_rondas:
        # Obtener tabla ordenada con MVP de esa ronda
        tabla_ordenada = ordenar_datos(ronda)

        for jugador, stats in tabla_ordenada:
            if jugador not in resumen_total:
                resumen_total[jugador] = {
                    'kills': 0,
                    'assists': 0,
                    'deaths': 0,
                    'MVPs': 0,
                    'Puntaje': 0
                }

            # Acumulamos los datos
            resumen_total[jugador]['kills'] += stats['kills']
            resumen_total[jugador]['assists'] += stats['assists']
            resumen_total[jugador]['deaths'] += stats['deaths']
            resumen_total[jugador]['MVPs'] += stats['MVPs']
            resumen_total[jugador]['Puntaje'] += stats['Puntaje']

    return resumen_total
