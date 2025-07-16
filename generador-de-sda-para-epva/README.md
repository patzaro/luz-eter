# Generador de Situaciones de Aprendizaje para EPVA

Esta es una aplicación web de una sola página (SPA) diseñada para asistir a los docentes de Educación Plástica, Visual e Audiovisual (EPVA) en la creación de Situaciones de Aprendizaje.

La herramienta utiliza un modelo de lenguaje generativo (Gemini) para crear propuestas pedagógicas personalizadas, alineadas con el currículo oficial de Galicia, a partir de las especificaciones del profesorado.

## Características Principales

*   **Generación a Medida:** Permite introducir el curso, el tema, el contexto del grupo, las necesidades de atención a la diversidad y el número de sesiones.
*   **Narrativas Creativas:** La IA propone tres hilos conductores o narrativas para la Situación de Aprendizaje, fomentando un enfoque creativo.
*   **Desarrollo Sesión por Sesión:** Detalla una propuesta completa con actividades, recursos, instrumentos de evaluación y estrategias de atención a la diversidad para cada sesión.
*   **Integración Curricular Dinámica:** La aplicación carga los saberes básicos y criterios de evaluación directamente desde archivos Markdown, asegurando que las propuestas estén siempre alineadas con el currículo oficial.
*   **Exportación a PDF:** Genera un documento PDF profesional y bien formateado con la Situación de Aprendizaje completa, listo para ser utilizado.

## Cómo Funciona

La aplicación está construida enteramente en el lado del cliente (frontend) y sigue un flujo de trabajo claro:

1.  **Carga de Datos:** Al iniciar, la aplicación utiliza la `Fetch API` para cargar los currículos de 1º y 3º de la ESO desde los archivos Markdown del repositorio.
2.  **Entrada del Usuario:** El docente completa un formulario con los parámetros de la Situación de Aprendizaje deseada.
3.  **Llamada a la API:** Se construye un prompt detallado que incluye la entrada del usuario y el texto completo del currículo correspondiente. Este prompt se envía a la API de Google Gemini.
4.  **Procesamiento de la Respuesta:** La aplicación recibe una respuesta estructurada en formato JSON y la utiliza para renderizar las diferentes fases de la interfaz (selección de narrativa y desarrollo).
5.  **Generación del Documento:** Utiliza la librería `jsPDF` para crear un documento PDF a partir de los datos finales aprobados por el usuario.

## Fuente Curricular

La rigurosidad pedagógica de la herramienta se basa en el contenido de los siguientes archivos, que son cargados dinámicamente:

*   `currículo_epva_gal_2022_1er-curso.md`
*   `currículo_epva_gal_2022_3er-curso.md`

El contenido de estos archivos está adaptado del **DECRETO 156/2022, de 15 de septiembre**, por el que se establece la ordenación y el currículo de la Educación Secundaria Obligatoria en la Comunidad Autónoma de Galicia.

## Puesta en Marcha

1.  Clonar el repositorio.
2.  Abrir el archivo `index.html` en un navegador web moderno.

**Nota sobre la API Key:** En el código, la clave de la API de Google Gemini se ha dejado intencionadamente en blanco por motivos de seguridad (`const apiKey = "";`). Para que las llamadas a la API funcionen, se debe gestionar una clave válida de forma segura, preferiblemente a través de un backend o un proxy que evite exponer la clave en el código del cliente.

## Posibles Mejoras

*   Implementar un backend (ej. Node.js, Cloud Function) para gestionar las llamadas a la API de forma segura.
*   Añadir la capacidad de editar el texto generado por la IA antes de la exportación a PDF.
*   Ampliar la aplicación para incluir más cursos, materias o currículos de otras comunidades autónomas.

## Licencia

Este proyecto se distribuye bajo la licencia MIT.
