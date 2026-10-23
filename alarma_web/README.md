- Creada por Deepseek 4.2 flash, superando a Claude Sonnet 5.5 y dejando muy atrás a GLM 5.3.
- Incluyo también la app que creó Claude con el mismo prompt.

# ⏰ Alarma Web

Una aplicación web de alarma ligera, sin dependencias y completamente funcional que funciona directamente en el navegador. Permite programar una alarma con hora, sonido, duración y volumen personalizados, con cuenta atrás en tiempo real y pantalla de aviso a pantalla completa.

> 🎵 Todos los sonidos se generan en tiempo real con la **Web Audio API** — no requiere archivos de audio externos ni conexión a internet.

---

## ✨ Características

### ⏱️ Reloj y fecha en vivo
- Reloj digital con segundos actualizándose en tiempo real.
- Fecha actual mostrada en español con formato completo (`viernes, 23 de octubre`).
- Tipografía con degradado y efecto de brillo.

### 🕰️ Programación de la alarma
- Selector de hora nativo (`<input type="time">`).
- Hora sugerida automáticamente: **un minuto después** de abrir la app.
- Detección inteligente: si la hora elegida ya pasó hoy, la alarma se programa para **el día siguiente**.
- Botón para cancelar la alarma activa en cualquier momento.

### 🔊 Seis sonidos distintos
Todos sintetizados con osciladores y envolventes:

| Sonido | Descripción |
|--------|-------------|
| **Beep clásico** | Cuatro pitidos cuadrados de 880 Hz |
| **Digital** | Tonos agudos alternados, estilo reloj digital |
| **Campana** | Acorde mayor con armónicos y caída larga |
| **Sirena** | Barrido ascendente y descendente tipo alarma |
| **Melodía** | Secuencia musical ascendente y descendente |
| **Despertar suave** | Acorde suave y lento, ideal para empezar el día |

Cada sonido tiene su propio **patrón y loop** para repetirse sin cortes.

### 🎚️ Control de duración y volumen
- Duración ajustable de **5 a 120 segundos** (pasos de 5 s).
- Volumen ajustable de **0 a 100 %** con actualización en vivo incluso mientras suena.
- Autoapagado exacto al cumplirse la duración configurada.

### ⏳ Cuenta atrás en tiempo real
- Tarjeta de estado que muestra la alarma programada.
- Cuenta regresiva formateada en **horas / minutos / segundos**.
- Indicador de "mañana" cuando la alarma corresponde al día siguiente.
- Botón de cancelar directamente en la tarjeta.

### 🔔 Pantalla completa al disparar
- Overlay con fondo difuminado.
- Icono de campana animado con efecto de vibración.
- Anillo pulsante de fondo.
- Hora de la alarma destacada.
- Botón grande **"Detener"** en tono rojo.
- Vibración del dispositivo (en móviles compatibles) mediante `navigator.vibrate`.

### 🔧 Detalles técnicos
- **Sin dependencias**: HTML, CSS y JavaScript puros.
- **Sin frameworks**: un único archivo `.html` autocontenido.
- **Web Audio API**: síntesis de sonido con `OscillatorNode` y `GainNode`.
- **Programación con lookahead**: los sonidos se agendan ligeramente en el futuro para evitar cortes.
- **Desbloqueo del audio** con el primer gesto del usuario (política de autoplay de los navegadores).
- **Reanudación automática** del contexto de audio tras cambios de pestaña.
- **Diseño responsive**: se adapta a móvil, tablet y escritorio.
- **Modo oscuro** integrado con paleta en degradados morado/azul.
- **Accesibilidad**: `color-scheme: dark` en inputs nativos, foco visible, tipografía clara.

---

## 🚀 Instalación y uso

### Opción 1 — Abrir directamente
1. Descarga el archivo `index.html`.
2. Haz doble clic para abrirlo en tu navegador.

> ⚠️ Algunos navegadores limitan la Web Audio API en archivos abiertos con `file://`. Si el sonido no funciona, usa la Opción 2.

### Opción 2 — Servidor local (recomendado)
```bash
# Con Python 3
python -m http.server 8000

# Con Node.js (npx)
npx serve
