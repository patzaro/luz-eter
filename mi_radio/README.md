## ¿Para qué es esta app?

Una app para guardar y escuchar emisoras de radio. Funciona en un solo archivo, guarda todo en el navegador y soporta streams directos (MP3, AAC, OGG) y también HLS (.m3u8).

Los datos se guardan en localStorage, así que no se pierden al cerrar. Puedes exportar tus emisoras a un .json para hacer copia de seguridad o pasarlas a otro dispositivo con Exportar.

## Dónde conseguir las URLs de las emisoras
Necesitas la URL directa del stream, no la web de la radio. Se suele ver así:

https://stream.emisora.com:8000/live.mp3

https://servidor.com/radio.aac

https://servidor.com/hls/radio.m3u8

### Sitios donde encontrarlas

- radio-browser.info — base de datos pública y gratuita, con buscador por nombre y país. Es la mejor opción.

- La web de la emisora → botón derecho → inspeccionar, o "Escuchar en VLC/Winamp" que a veces muestra la URL.

- streamurl.link o foros de radio.

## Limitaciones importantes a tener en cuenta
- HTTPS obligatorio: si publicas la app en GitHub Pages (que va por HTTPS), los streams deben ser también https://. Un stream http:// será bloqueado por el navegador y no sonará.

- CORS: algunos servidores bloquean la reproducción desde otra web. Si una emisora no suena, prueba a abrir su URL directamente en el navegador. Si ahí sí suena pero en la app no, es CORS y no hay solución desde el HTML.

## ¿Cómo fue creada la app?
Con DeepSeek, a la primera. https://chat.deepseek.com/share/7oc4tzg8b48h65sdl7

## Futuras mejoras
¿Quieres que le añada algo más? Por ejemplo:

- Lista de emisoras preinstaladas (podría meter unas cuantas españolas de ejemplo).
- Buscador integrado que consulte la API de radio-browser y te deje añadir con un clic.
- Modo favoritos o categorías por género.
- Botón de "aleatorio" para saltar entre emisoras.



 
