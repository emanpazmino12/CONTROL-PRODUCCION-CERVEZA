# Sistema de control de producción de cerveza

## Integrante
Wilmer Emanuel Pazmiño Montoya  
Universidad Internacional del Ecuador  
Ingeniería en Ciencia de Datos

## Fecha
10 de octubre de 2026

## Proyecto integrador
El impacto de las nuevas tecnologías en la sociedad: desarrollo y proyección de soluciones informáticas.

## Problema
Cuando los registros de producción están dispersos, resulta difícil consultar los lotes elaborados, sus cantidades y la etapa en la que se encuentran.

## Objetivo
Organizar los registros de producción de cerveza mediante un programa que permita registrar lotes, consultar sus datos, actualizar su estado y obtener un resumen.

## Funcionalidades
- Registrar código, estilo, litros y fecha de elaboración.
- Consultar los lotes registrados.
- Actualizar el estado a Elaboración, Fermentación, Maduración o Envasado.
- Mostrar la cantidad de lotes y el total de litros registrados.
- Conservar los datos en un archivo local llamado lotes.json.

## Herramientas
- Python 3.10 o posterior.
- Visual Studio Code.
- GitHub para mantener el historial de versiones.
- Mermaid para los diagramas.

No requiere instalar paquetes externos.

## Ejecución
Descargar el repositorio y descomprimirlo. Abrir una terminal en la carpeta que contiene main.py.

En Windows:

```powershell
py main.py
```

En Linux o macOS:

```bash
python3 main.py
```

Seleccionar una opción del menú y seguir las indicaciones.

## Archivos del repositorio
- main.py: programa completo.
- avance_inicial.py: primera versión de registro y consulta.
- 01_menu.md: flujo del menú.
- 02_registrar.md: registro de lotes.
- 03_consultar.md: consulta de lotes.
- 04_actualizar.md: actualización de estados.
- 05_resumen.md: resumen de producción.
- 06_arquitectura.md: organización del sistema.

## Estructuras de programación
El programa utiliza condicionales if, elif y else para seleccionar acciones y validar datos. Los ciclos while mantienen el menú y permiten repetir entradas incorrectas. Los ciclos for recorren los lotes y los estados.

El código está organizado en funciones para registrar, consultar, actualizar, resumir, cargar y guardar datos.

## Pruebas de funcionamiento
Durante la prueba en Windows se consultó un lote de 950 litros y se registró otro de 500 litros. El resumen mostró dos lotes y 1450 litros. Se actualizó el segundo lote a Fermentación y se comprobó que los datos permanecían al cerrar y volver a abrir el programa.

## Impacto tecnológico
El sistema muestra cómo un programa sencillo puede ayudar a organizar información en una actividad productiva. Permite consultar los registros y obtener totales sin sumar cada lote manualmente.

## Alcance y limitaciones
Es un prototipo académico de consola para un usuario. Los datos se ingresan manualmente. No controla fermentadores, temperaturas ni equipos, y no incluye inventario, costos o acceso desde varias computadoras.

Los litros del resumen corresponden al volumen registrado de los lotes; no representan necesariamente cerveza terminada o disponible para vender.
