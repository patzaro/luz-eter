Integra Gemini en tu Aplicación Web con una Clave API Gratuita.

## 1. Obtención de la Clave API de Gemini

Dentro de Google AI Studio, busca la opción para "Get API key" o "Crear clave de API". Es posible que esté en la sección de "API access" o "API keys". Sigue las instrucciones para generar una nueva clave.

## 2. Configuración del Backend Seguro con Google Apps Script

Google Apps Script te permite crear un backend ligero y seguro para gestionar tus peticiones a Gemini.

Pasos para configurar Google Apps Script:

1. Crea un nuevo proyecto de Apps Script:

- Ve a Google Apps Script.

- Haz clic en "Nuevo proyecto" o "New project". Se abrirá un nuevo editor de código.

2. Guarda tu clave API de forma segura:

- En el editor de Apps Script, ve a "Archivo" > "Propiedades del proyecto" > "Propiedades de secuencia de comandos" (o "Project properties" > "Script properties").

- Haz clic en "Añadir propiedad".

- En el campo "Propiedad", escribe API_KEY.

- En el campo "Valor", pega la clave API que obtuviste de Google AI Studio.

- Haz clic en "Guardar".

3. Implementa la función doPost(e):

- Esta función manejará las peticiones POST desde tu frontend, llamará a la API de Gemini y devolverá la respuesta.

4. Despliega tu proyecto de Apps Script como una aplicación web:

- En el editor de Apps Script, haz clic en "Implementar" > "Nueva implementación" (o "Deploy" > "New deployment").

- Selecciona "Tipo" como "Aplicación web".

- Configura el "Acceso" a "Cualquier usuario" (o "Anyone") para que tu frontend pueda acceder. ¡Importante! Si tu aplicación es privada, considera restringir el acceso.

- Haz clic en "Implementar".

- Una vez desplegado, se te proporcionará una "URL de la aplicación web". Guarda esta URL, la necesitarás para hacer las peticiones desde tu frontend.

## 3. Llamada desde el Frontend
Ahora que tu backend está configurado y desplegado, puedes realizar peticiones desde tu aplicación web para interactuar con Gemini.

El fichero `index.html` es un ejemplo básico que muestra un campo de entrada para la pregunta del usuario y un área para mostrar la respuesta.

### Pasos para usar el código frontend:

1. Copia el código: Guarda el código HTML anterior en un archivo index.html en tu computadora.

2. Reemplaza TU_URL_DE_APPS_SCRIPT_AQUÍ' en el código JavaScript con la URL de la aplicación web que obtuviste en el paso 2.4.

3. Abre el archivo: Abre el archivo `index.html` en tu navegador. Podrás ver la interfaz y probar la interacción con Gemini.

## Prompt para Gemini

Actúa como un asistente experto en desarrollo. Tu objetivo es guiarme paso a paso para integrar el modelo de IA gemini-2.5-flash-lite en mi aplicación web.

El proceso debe cubrir los siguientes puntos de forma clara y con ejemplos de código:

- Obtención de la clave de API: Explica cómo generar una nueva clave de API desde la web de Google AI Studio.
- Configuración del backend seguro con Google Apps Script:
Indica cómo crear un nuevo proyecto en Google Apps Script.
Muestra cómo guardar la clave de API de forma segura en las "Propiedades del secuencia de comandos".
- Proporciona el código completo para una función doPost(e) que reciba una pregunta desde el frontend, llame a la API de Gemini con la clave guardada y devuelva la respuesta del modelo.
- Llamada desde el frontend:
Proporciona un ejemplo de código HTML y JavaScript que muestre cómo enviar una pregunta del usuario al backend de Google Apps Script mediante una petición fetch.
- Muestra cómo recibir la respuesta y mostrarla en la página.