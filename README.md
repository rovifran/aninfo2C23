# Quiero Retruco: Implementación del Juego de Truco en Python con PyGame
## Trabajo Practico Aninfo 2C2023

Bienvenido al proyecto Quiero Retruco, una implementación del juego de Truco en Python con la ayuda de PyGame. 
Este proyecto permite a dos personas jugar una partida de Truco desde la misma computadora, 
con la opción de personalizar la cantidad de puntos y jugar con flor, siguiendo las [reglas oficiales del Truco](https://asart.com.ar/el-reglamento/#truco-carta-jugada).

El juego se desarrolla en un entorno interactivo, donde los jugadores se turnan para jugar cartas. Esta implementación busca proporcionar una experiencia fiel al juego tradicional, permitiendo a los jugadores sumergirse en la emoción del Truco directamente desde su computadora.

## Tecnologias
Para desarrollar este proyecto se utilizo el lenguaje de programacion Python, junto con la libreria PyGame para la interfaz grafica.

## Instrucciones de Instalación
Para poder jugar al Truco en tu computadora, se deben seguir estos pasos:

1. El pimer requisito es tener instalado Python 3.x en tu sistema. Se puede descargar la última versión desde [python.org](https://www.python.org/).

2. Para instalar las librerias necesarias para correr el juego, es necesario ejecutar el siguiente comando:
   ```bash
   pip install -r requirements.txt
   ```   
## Como correr el proyecto
Clona este repositorio en tu máquina:
```bash
git clone git@github.com:rovifran/aninfo2C23.git
```
Navega al directorio del proyecto:

```bash
cd aninfo2C23/src
```
### Linux/iOS
Ejecuta el juego:

```bash
python3 truco.py
```
### Windows

```bash
python truco.py
```

## Pruebas
El proyecto tiene pruebas que se ejecutan estando en el directorio `src`, con el comando:
### Linux
```bash
python3 -m tests.tests_<nombre del modulo>
```
### Windows
```bash
python -m tests.tests_<nombre del modulo>
```

## Problemas conocidos
ninguno porque somos re capos. Si se detecta alguno entonces tan capos no somos, cualquier comportamiento inesperado / errores / bugs que se quieran reportar, se deben hacer abriendo un **issue** respetando el formato de estos. 

## Contribuciones
Dado que el juego esta en pleno desarrollo, todo aporte que se pueda realizar para el progreso de este es bienvenido! Simplemente hay que realizar los cambios a aportar en un *fork* del repositorio, y luego hacer la **Pull Request** correspondiente, luego el codigo sera verificado por los desarrolladores y si todo esta correcto se aceptara la **Pull Request**, integrando los cambios.

### Integrantes
- Francisco Rovira
- Francisco Juarez
- Joaquin Pandolfi
- Martina Lozano
- Valentin Schneider
