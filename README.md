# Scraper de Liverpool

Debido a las protecciones anti-scraping implementadas por Liverpool mediante Akamai, no fue posible realizar el scraping utilizando peticiones HTTP tradicionales.
Por esta razón, se optó por una arquitectura híbrida en la que Playwright se utiliza para abrir un navegador real, renderizar el contenido y extraer el HTML final de las páginas, mientras que Scrapy se encarga posteriormente del parseo de dichos HTMLs y la extracción estructurada de la información.

## Requisitos Previos

- Python 3.8 o superior.
- Chromium.

## Ejecución

1. **Crear venv o env:**
   ```
   En Windows:
   python -m venv venv
   .\venv\Scripts\activate
   ```

   ```
   En Mac/Linux:
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instalar dependencias:**

   ```
   pip install -r requirements.txt
   ```

4. **Instalar navegadores de Playwright:**

   ```
   playwright install
   ```

## Ejecución

Para correr el scraper:

```bash
python run.py
```

## Resultados

El scraper generará un archivo de texto con los resultados en:

`scraper/output/laptops.txt`

## Nota

- El scraper está configurado para ejecutarse en modo "headful" (navegador visible) por defecto para evitar bloqueos por la página de Liverpool.
- Los archivos HTML temporales se descargan y luego se procesan localmente.
