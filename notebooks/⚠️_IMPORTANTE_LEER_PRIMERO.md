# Antes de empezar: uso responsable de notebooks

Este curso usa Jupyter porque combina explicación, código y resultados. Un
notebook es adecuado para enseñanza, exploración, prototipos y análisis
reproducibles cuando se controla su estado y su entorno.

## Riesgos que debes gestionar

| Riesgo | Control recomendado |
| --- | --- |
| Ejecución fuera de orden | Reinicia el kernel y ejecuta de principio a fin |
| Estado oculto | Define todas las entradas y evita depender de variables previas |
| Diffs JSON difíciles | Haz cambios pequeños y revisa metadata y outputs |
| Secretos en celdas | Usa variables de entorno y limpia outputs antes de compartir |
| Dependencias implícitas | Usa los locks o grupos declarados por el repositorio |
| Resultado no reproducible | Fija semillas, versiones, datos de entrada y parámetros |

## Del experimento al componente operable

```text
notebook exploratorio
        ↓ evidencia y contrato
función o módulo en scripts/
        ↓ pruebas automatizadas
pipeline empaquetado
        ↓ CI, configuración y observabilidad
despliegue operado
```

No existe una conversión automática: antes de operar un prototipo debes definir
interfaces, errores, idempotencia, seguridad, recursos, monitoreo y recuperación.
El repositorio ilustra esa separación mediante `notebooks/`, `scripts/`,
`tests/`, Docker y GitHub Actions.

## Lista de comprobación

- [ ] El notebook ejecuta desde un kernel limpio.
- [ ] Todas las fuentes, versiones y supuestos están documentados.
- [ ] No contiene claves, PII ni credenciales en inputs, outputs o metadata.
- [ ] Las funciones reutilizables se trasladaron a módulos probados.
- [ ] Los fallos externos tienen timeout, reintentos acotados y mensajes útiles.
- [ ] El despliegue no depende de ejecutar manualmente una celda.

Consulta la [guía de instalación](../docs/guia_instalacion.md), la
[arquitectura](../docs/arquitectura.md) y la
[guía de contribución](../CONTRIBUTING.md).
