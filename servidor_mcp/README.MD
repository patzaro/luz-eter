# Proyecto: Servidor MCP con FastAPI

Creado por Copilot con mi inestimable ayuda.

## Lo que hemos construido

Hasta este punto, se ha desarrollado un servidor MCP funcional que utiliza FastAPI y permite interactuar con un archivo CSV como fuente de datos externa. El servidor expone dos endpoints clave:

### 1. `GET /usuario_csv/nombre`
Consulta datos específicos desde el archivo `usuarios.csv`. Busca por nombre y devuelve edad y ciudad asociadas.

### 2. `POST /agregar_usuario`
Permite agregar nuevos registros al archivo CSV. Recibe los datos en formato JSON, los valida y los añade al archivo, creando el archivo si aún no existe.

---

## Para qué sirve

Este servidor MCP sirve como puente entre modelos de inteligencia artificial y datos reales. Puede ser utilizado para:

- Consultar y modificar fuentes externas de datos sin tener que acceder directamente a ellas.
- Crear una capa de abstracción entre el modelo IA y el sistema operativo o la base de datos.
- Desarrollar un asistente digital personalizado que interactúe con información local o de terceros.
- Extender sus capacidades para conectar con APIs públicas, calendarios, bases de datos o sistemas de archivos.

---

## Cómo se prueba el servidor

### 1. Ejecutar el servidor

Desde una terminal en la carpeta del proyecto, lanza el servidor con el siguiente comando:

```bash
py -m uvicorn main:app --reload
```

Esto iniciará el servidor en la dirección local `http://127.0.0.1:8000`.

### 2. Acceder a la interfaz de pruebas (Swagger UI)

Abre tu navegador y entra en:

```
http://127.0.0.1:8000/docs
```

Desde esta interfaz podrás probar los endpoints interactivos:

- Selecciona `GET /usuario_csv/{nombre}` → escribe un nombre y ejecuta para ver los datos que devuelve.
- Selecciona `POST /agregar_usuario` → escribe un JSON con los datos del nuevo usuario y ejecuta para agregarlo.

### 3. Validar los resultados

- Puedes comprobar los cambios en el archivo `usuarios.csv` desde la terminal o abriéndolo con cualquier editor de texto.
- También puedes usar herramientas como `curl`, Postman o escribir scripts en Python para enviar peticiones HTTP al servidor.

---

## Siguientes pasos posibles

- Endpoint `GET /usuarios` para listar todos los registros.
- `PUT` o `PATCH` para editar datos existentes.
- `DELETE` para eliminar registros específicos.
- Integración directa con IA vía clientes MCP como LangChain o Semantic Kernel.