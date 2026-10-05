# Sistema de control de producción de cerveza
Autor: Wilmer Emanuel Pazmiño Montoya. Proyecto académico.

## Problema y objetivo
Los registros dispersos dificultan consultar qué lotes se han elaborado y en qué etapa están. El programa permite registrar lotes, consultar sus datos, actualizar su estado y obtener un resumen de litros y cantidad de lotes.

## Entorno y ejecución
Python 3.10 o posterior, Visual Studio Code como editor y terminal de Windows. No requiere paquetes externos. Instala Python y abre la carpeta del proyecto en el editor.

En la terminal de esa carpeta ejecuta:
```sh
py -3 main.py
```
En Linux/macOS: `python3 main.py`. En Windows también puedes abrir `Iniciar_Windows.bat` después de instalar Python con su lanzador.
Primera versión: `py -3 paso1/avance_inicial.py`.

## Paso 1: inicio del desarrollo
- Entorno: Python, editor y terminal.
- Código inicial: `paso1/avance_inicial.py`, registro y consulta en memoria. Al salir pierde sus datos; esa limitación se resuelve en el paso 2.
- Diagramas: carpeta `diagramas`, en formato Markdown con Mermaid, que GitHub puede representar.
- Repositorio y video: seguir `ENTREGA_Y_VIDEOS.md`.

## Paso 2: desarrollo
`main.py` agrega actualización de estados, resumen y persistencia JSON. Los campos son código único, estilo, litros positivos, fecha y estado. Se admiten las etapas Elaboración, Fermentación, Maduración y Envasado; el usuario puede corregir el estado sin una secuencia obligatoria.

## Arquitectura
Aplicación de consola de un solo usuario. La entrada y salida están en el menú y las funciones interactivas; la lógica se organiza en registrar, consultar, actualizar y resumen; cargar y guardar administran un archivo JSON local. Se usa una lista de diccionarios, apropiada para este alcance inicial.

## Estructuras y relación con los diagramas
| Funcionalidad | Función | Estructuras | Diagrama |
|---|---|---|---|
| Navegación | main | while, if/elif/else | 01_menu.md |
| Registro | registrar | while, if, validación | 02_registrar.md |
| Consulta | consultar | if, for | 03_consultar.md |
| Cambio de estado | actualizar | for, if | 04_actualizar.md |
| Resumen | resumen | for y sum | 05_resumen.md |

## Datos y límites
`lotes.json` se crea al registrar el primer lote y se conserva al cerrar. Los ejemplos de los videos son ficticios. No subir registros reales de la empresa a GitHub. Es un prototipo académico: no incluye autenticación, conexión entre equipos ni control automático de fermentadores. Si el archivo de datos está dañado, el programa se detiene para evitar sobrescribirlo.

## Entregables pendientes de publicación
Este paquete contiene el código y los diagramas. El enlace de GitHub debe obtenerse al crear el repositorio real; los videos deben grabarse explicando y ejecutando el proyecto. No se han publicado ni grabado desde este paquete.
