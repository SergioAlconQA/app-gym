# Mi Gym

App de entrenamiento de gimnasio (PWA instalable en Android). Versión 1: datos guardados solo en el móvil.

- `src/app.html`: la app completa (HTML, CSS y JS).
- `python3 build.py`: genera `docs/index.html`, que es lo que publica GitHub Pages.
- `docs/`: carpeta publicada (manifest, service worker e iconos).

Tras cambiar `src/app.html`, ejecuta `build.py` y sube la versión de `CACHE` en `docs/sw.js`.
