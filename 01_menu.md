# 01 menu

```mermaid
flowchart TD
 A([Inicio]) --> B[Cargar lotes]
 B --> C{Carga correcta?}
 C -- No --> X[Mostrar error] --> Z([Fin])
 C -- Sí --> D[Mostrar menú y leer opción]
 D --> E{Opción}
 E -- 1 --> F[Registrar lote]
 E -- 2 --> G[Consultar lotes]
 E -- 3 --> H[Actualizar estado]
 E -- 4 --> I[Mostrar resumen]
 E -- 5 --> Z
 E -- Otra --> J[Mostrar opción inválida]
 F --> D
 G --> D
 H --> D
 I --> D
 J --> D
```

En registro y actualización, un error de escritura muestra un aviso y vuelve al menú sin confirmar el cambio.
