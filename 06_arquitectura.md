# Arquitectura del sistema

El programa funciona en una computadora y organiza sus funciones dentro de main.py.

```mermaid
flowchart TD
    U[Usuario] --> M[Menú de consola]
    M --> L[Registrar consultar actualizar y resumir]
    L --> G[Cargar y guardar datos]
    G <--> J[Archivo lotes.json]
    L --> M
```

El usuario selecciona una opción del menú. Las funciones procesan los datos y muestran el resultado. El archivo lotes.json conserva los lotes al cerrar el programa.
