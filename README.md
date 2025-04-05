## Autor
Esteeven Andres Gallegos Calle 
Legajo: 18031/8


# Proyecto: Analisis de Partidas y MVPs + Actividades extra

Este proyecto analiza los resultados de varias partidas, generando rankings y determinando los MVPs.
y complementa desarrollando las demas actividades con los markdown de explicacion para ver que se hace en cada actividad

# Instalacion de Dependencias

Para ejecutar este proyecto, se recomienda crear un entorno virtual y luego instalar las dependencias necesarias.

### 1. Crear un entorno virtual (opcional pero recomendado)
```bash
python -m venv venv
```

### 2. Activar el entorno virtual
- En Windows:
  ```bash
  venv\Scripts\activate
  ```
- En macOS/Linux:
  ```bash

  source venv/bin/activate
  ```

### 3. Instalar dependencias
Ejecuta el siguiente comando en la terminal dentro del proyecto:
```bash
pip install -r requirements.txt
```
Si el archivo `requirements.txt` no está presente, puedes generarlo con:
```bash
pip freeze > requirements.txt
```

## Ejecución del Proyecto

Para analizar los datos, ejecuta el script principal dentro de la carpeta notebooks:
```bash
python Ej10.py
```

Si deseas trabajar desde un **notebook**, asegurate de estar en el entorno virtual y luego abre Jupyter Notebook:
```bash
jupyter notebook
```
Dentro de Jupyter, navega hasta la carpeta `notebooks` y abre el archivo correspondiente.

## Estructura del Proyecto
```
proyecto/
│── notebooks/           # Notebooks con analisis y resultados
    │── Ej10.py              # Script principal del ejercicio
│── src/                 # Código fuente y funciones
│   ├── funciones.py     # Modulo con funciones principales
│── requirements.txt     # Dependencias del proyecto
│── README.md            # Instrucciones y documentación
```



