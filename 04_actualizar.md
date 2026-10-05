# 04 actualizar

```mermaid
flowchart TD
 A([Actualizar]) --> B[Leer código]
 B --> C[Buscar lote con for]
 C --> D{Encontrado?}
 D -- No --> E[Mostrar aviso] --> Z([Volver al menú])
 D -- Sí --> F[Mostrar estados y leer opción]
 F --> G{Opción válida?}
 G -- No --> H[Mostrar error] --> Z
 G -- Sí --> I[Guardar nuevo estado y actualizar lista] --> Z
```

En registro y actualización, un error de escritura muestra un aviso y vuelve al menú sin confirmar el cambio.
