# 03 consultar

```mermaid
flowchart TD
 A([Consultar]) --> B{Hay lotes?}
 B -- No --> C[Mostrar lista vacía] --> Z([Volver al menú])
 B -- Sí --> D[Recorrer lista con for]
 D --> E[Mostrar datos de cada lote]
 E --> F{Quedan lotes?}
 F -- Sí --> D
 F -- No --> Z
```

En registro y actualización, un error de escritura muestra un aviso y vuelve al menú sin confirmar el cambio.
