# Proyecto: Servidor MCP con FastAPI

Creado por por Copilot con mi inestimable ayuda.

## Lo que hemos construido

Hasta ahora, hemos desarrollado un servidor MCP básico en Python usando FastAPI, que expone una API local con dos grandes capacidades:

### 1. Lectura de datos desde archivo CSV
- Creamos un archivo `usuarios.csv` como fuente de datos estructurada.
- Implementamos el endpoint `GET /usuario_csv/{nombre}` que permite consultar los datos de un usuario específico desde el CSV.
- El servidor filtra por nombre (ignorando mayúsculas) y devuelve los datos en formato JSON.

### 2. Agregado dinámico de datos al CSV
- Implementamos el endpoint `POST /agregar_usuario` para insertar nuevos registros en el archivo `usuarios.csv`.
- La entrada se valida mediante un modelo `Usuario` que exige nombre, edad y ciudad.
- Si el archivo no existe, se crea con encabezado; si existe, se añade el nuevo dato al final.

## Para qué sirve este sistema

Este servidor MCP es una base funcional para conectar fuentes de datos simples a sistemas de inteligencia artificial, herramientas externas o dashboards. Sus utilidades incluyen:

- Integración con modelos de lenguaje (LLM) para brindar respuestas con datos reales.
- Simulación de un CRM ligero para gestionar usuarios.
- Base para agregar nuevas funcionalidades como filtros, búsqueda avanzada, edición o eliminación de datos.
- Punto de conexión para APIs, bases de datos u otros servicios que permitan enriquecer las capacidades de una IA.

## Próximos pasos sugeridos

Podríamos continuar el proyecto con opciones como:

- Crear el endpoint `GET /usuarios` para listar todos los registros.
- Implementar edición y borrado de registros por nombre o ID.
- Integrar el servidor con una IA usando LangChain u otro cliente MCP.
- Conectar el servidor con APIs externas o bases de datos reales.
