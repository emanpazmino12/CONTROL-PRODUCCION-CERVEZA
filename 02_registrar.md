# 02 registrar

```mermaid
flowchart TD
 A([Registrar]) --> B[Leer código no vacío]
 B --> C{Código repetido?}
 C -- Sí --> D[Mostrar aviso] --> Z([Volver al menú])
 C -- No --> E[Leer estilo no vacío]
 E --> F[Leer litros]
 F --> G{Número finito y positivo?}
 G -- No --> F
 G -- Sí --> H[Leer fecha]
 H --> I{Fecha válida?}
 I -- No --> H
 I -- Sí --> J[Crear lote en Elaboración]
 J --> K[Guardar archivo y actualizar lista]
 K --> Z
```

En registro y actualización, un error de escritura muestra un aviso y vuelve al menú sin confirmar el cambio.
