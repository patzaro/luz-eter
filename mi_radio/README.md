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

- HLS (.m3u8): funciona en Safari de forma nativa y en el resto mediante hls.js, que se carga automáticamente desde un CDN (solo la primera vez que reproduces una emisora HLS).



