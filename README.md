# Cosmic IDE — BlueJ Support (plantilla de repositorio)

**ESTO TODAVÍA NO ES UN PLUGIN INSTALABLE.** El código fuente incluido es un prototipo, no hay `plugin.apk` ni acciones integradas con Cosmic IDE. Por eso `plugins.json` empieza como `[]`: mostrar una extensión que no funciona sería engañoso.

## Qué contiene
- `source/bluej-support/`: fuentes Kotlin, manifiesto y herramienta de terminal para compilar/ejecutar Java sin Gradle.
- `publish.py`: crea el índice y calcula el SHA-256 **solo cuando se aporte un ZIP real y compilado**.
- `artifacts/`: carpeta para el ZIP compilado.

## Cómo publicar después de compilar
1. Implementa y compila el plugin con las APIs Android `plugin-api` e `ide-api` de Cosmic IDE; verifica que registra acciones de compilar/ejecutar Java.
2. Empaqueta `manifest.json` y `plugin.apk` en `artifacts/bluej-support-1.0.0.zip`.
3. Ejecuta `python3 publish.py TU_USUARIO artifacts/bluej-support-1.0.0.zip`.
4. Sube el contenido de esta carpeta (no el ZIP que la contiene) a la rama `main` de un repositorio público llamado `cosmic-bluej-marketplace`.
5. En Cosmic IDE, configura `https://raw.githubusercontent.com/TU_USUARIO/cosmic-bluej-marketplace/main/plugins.json`.

**Nota:** el validador de `publish.py` comprueba la estructura, no garantiza que el APK compile o se active. La app valida también la compatibilidad y carga del plugin.

Documentación: https://github.com/Cosmic-Ide/Cosmic-IDE/blob/main/docs/plugin-architecture.md
