# Scraper de Ofertas Laborales

Este proyecto es un scraper de ofertas laborales que utiliza Selenium para extraer títulos y enlaces de trabajos desde la página de Computrabajo en Chile. Permite buscar trabajos que contengan una palabra clave específica ingresada por el usuario.

## Requisitos

- Python 3.x
- Selenium
- Chrome WebDriver (debe ser compatible con tu versión de Chrome)

## Instalación

1. Clona este repositorio o descarga los archivos.

2. Instala las dependencias requeridas:

       pip install selenium
3. Asegúrate de tener Chrome WebDriver instalado y que esté en tu PATH. 

## Uso

1. Abre una terminal y navega hasta el directorio del proyecto.

2. Ejecuta el script:

         python main.py
3. Cuando se te solicite, ingresa la palabra clave que deseas buscar en los títulos de trabajo.

4. El script navegará por las páginas de ofertas laborales y extraerá los trabajos que coincidan con tu búsqueda. Los resultados se guardarán en un archivo job_offers.json.

## Ejemplo

Si deseas buscar trabajos que contengan la palabra "Ventas", simplemente ingresa "Ventas" cuando se te solicite.

## Estructura de los Datos

Los datos extraídos se guardarán en un archivo JSON con la siguiente estructura:


        [
            {
                "title": "Ejecutivo de Ventas Part time de 10 a 16:30 hrs de lunes a viernes",
                "link": "https://cl.computrabajo.com/ofertas-de-trabajo/oferta-de-trabajo-de-ejecutivo-de-ventas-part-time-de-10-a-1630-hrs-de-lunes-a-viernes-en-santiago-centro-2DC9E14A19608C9661373E686DCF3405#lc=ListOffers-Score-0"
            },
            ...
        ]

## Notas

Asegúrate de que tu conexión a internet esté activa durante la ejecución del script.
El script puede tardar un tiempo en completarse, dependiendo de la cantidad de páginas de resultados.


