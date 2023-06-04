# Proyecto de Pruebas Funcionales con Selenium y Behave

Este proyecto tiene como objetivo realizar pruebas funcionales utilizando Selenium y Behave en Python. Se implementan una serie de pruebas que verifican diferentes funcionalidades en un navegador web.

## Requisitos

Asegúrate de tener instalados los siguientes elementos antes de ejecutar el proyecto:

- Python 3.x
- Selenium
- Behave

Puedes instalar las dependencias necesarias utilizando el administrador de paquetes de Python, pip:

```
pip install selenium
```
```
pip install -U behave
```
## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

- **features**: Contiene los archivos `.feature` que definen los escenarios de prueba utilizando el lenguaje Gherkin.
- **steps**: Contiene los archivos `.py` que implementan los pasos definidos en los escenarios de prueba.
- **utils**: Contiene archivos `.py` con funciones de utilidad para el proyecto.
- **README.md**: El archivo que estás leyendo actualmente.

## Escenarios de Prueba

El proyecto incluye los siguientes escenarios de prueba sobre el sitio web "lidl.es":

### Prueba 1: Verificar el título del navegador

Este escenario se encarga de verificar que el título del navegador sea correcto después de visitar una página específica.

### Prueba 2: Contar productos

En este escenario, se realiza una búsqueda de productos y se verifica que el número total de resultados coincida con el valor esperado.

### Prueba 3: Verificar el título del navegador después de la búsqueda

Después de realizar una búsqueda, se verifica que el título del navegador cambia.

### Prueba 4: Verificar el título de la búsqueda

En este escenario, se verifica que el título de la página de resultados de búsqueda sea el esperado.

### Prueba 5: Añadir producto al carrito de compra

En este escenario, se simula la acción de agregar un producto al carrito de compra y se verifica que se muestre un mensaje de confirmación.

## Ejecución de las Pruebas

Para ejecutar las pruebas, sigue los siguientes pasos:

1. Asegúrate de tener instaladas todas las dependencias mencionadas en los requisitos.
2. Clona o descarga el repositorio en tu máquina local.
3. Navega a la carpeta raíz del proyecto desde la línea de comandos.
4. Ejecuta el siguiente comando para iniciar las pruebas:

```
behave
```

El framework Behave se encargará de leer los archivos `.feature` y ejecutar los pasos correspondientes definidos en los archivos `.py` dentro de la carpeta `steps`.
