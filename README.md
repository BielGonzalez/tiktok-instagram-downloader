# 🎥 Descargador de Videos - TikTok e Instagram

Herramienta automatizada para descargar videos de TikTok e Instagram basándose en términos de búsqueda o hashtags.

## ✨ Características

- 🔍 Búsqueda de videos por descripción/hashtags
- 📥 Descarga automática desde TikTok
- 📥 Descarga automática desde Instagram
- 🖥️ Interfaz de línea de comandos simple e intuitiva
- 📁 Organización automática de descargas por búsqueda

## 📋 Requisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## 🚀 Instalación

1. Clona este repositorio:
```bash
git clone https://github.com/BielGonzalez/tiktok-instagram-downloader.git
cd tiktok-instagram-downloader
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

3. (Opcional) Configura tus credenciales de Instagram en `.env`:
```bash
cp .env.example .env
# Edita .env con tus credenciales
```

## 💻 Uso

### Modo Básico

Ejecuta el programa principal:
```bash
python main.py
```

Luego ingresa tu término de búsqueda cuando se te solicite:
```
📝 Ingresa la descripción de búsqueda: memes clash royale
```

El programa buscará y descargará videos relacionados con ese término tanto de TikTok como de Instagram.

### Modo Avanzado (yt-dlp)

Para descargar videos específicos por URL:
```bash
python main_ytdlp.py
```

## 📂 Estructura del Proyecto

```
tiktok-instagram-downloader/
├── main.py                 # Archivo principal
├── main_ytdlp.py          # Versión alternativa con yt-dlp
├── downloaders/
│   ├── __init__.py
│   ├── tiktok.py          # Descargador de TikTok
│   └── instagram.py       # Descargador de Instagram
├── requirements.txt        # Dependencias del proyecto
├── .env.example           # Ejemplo de configuración
├── .gitignore            # Archivos ignorados por git
├── downloads/            # Carpeta donde se guardan los videos
└── README.md             # Este archivo
```

## ⚙️ Configuración

Puedes personalizar el comportamiento editando el archivo `.env`:

```env
# Número máximo de videos a descargar por plataforma
MAX_VIDEOS=10

# Credenciales de Instagram (opcional)
INSTAGRAM_USERNAME=tu_usuario
INSTAGRAM_PASSWORD=tu_contraseña
```

## 📝 Ejemplo de Uso

```bash
$ python main.py

==================================================
DESCARGADOR DE VIDEOS - TIKTOK E INSTAGRAM
==================================================

📝 Ingresa la descripción de búsqueda: memes clash royale

🔍 Buscando videos de: 'memes clash royale'
📁 Los videos se guardarán en: downloads/memes_clash_royale

==================================================
🎵 BUSCANDO EN TIKTOK...
==================================================
✅ Se encontraron 10 videos en TikTok
⬇️  Descargando: tiktok_1_123456789.mp4
⬇️  Descargando: tiktok_2_987654321.mp4
...

==================================================
📸 BUSCANDO EN INSTAGRAM...
==================================================
🔍 Buscando hashtag: #memesclashroyale
⬇️  Descargando: instagram_1_AbCdEf
✅ Se descargaron 8 videos de Instagram

✅ ¡Descarga completada!
📂 Revisa la carpeta: downloads/memes_clash_royale
```

## ⚠️ Advertencias Importantes

1. **Términos de Servicio**: Asegúrate de cumplir con los términos de servicio de TikTok e Instagram
2. **Limitaciones de API**: Las APIs no oficiales pueden tener límites de uso
3. **Autenticación**: Instagram puede requerir autenticación para búsquedas amplias
4. **Cambios en APIs**: Las plataformas pueden cambiar sus APIs sin previo aviso

## 🐛 Solución de Problemas

### Error de autenticación en Instagram
```bash
# Asegúrate de configurar tus credenciales en .env
INSTAGRAM_USERNAME=tu_usuario
INSTAGRAM_PASSWORD=tu_contraseña
```

### Error al instalar dependencias
```bash
# Intenta actualizar pip primero
pip install --upgrade pip
pip install -r requirements.txt
```

### Videos no se descargan
- Verifica tu conexión a internet
- Comprueba que el hashtag/término existe en la plataforma
- Revisa los logs para mensajes de error específicos

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Haz fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la Licencia MIT.

## 👨‍💻 Autor

**BielGonzalez**

## 🙏 Agradecimientos

- TikTokApi
- Instaloader
- yt-dlp
- Comunidad de código abierto

---

⭐ Si este proyecto te fue útil, considera darle una estrella en GitHub!