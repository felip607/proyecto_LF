
import requests
import re
from lxml import html
import json

def scraping_m():
    # URLs de las páginas
    urls = [
        "https://www.tiendafractalis.com/marca-fractalis",
        "https://www.tiendafractalis.com/marca-fractalis?page=2&count=24",
        "https://www.tiendafractalis.com/marca-fractalis?page=3&count=24"
    ]

    # Encabezado de la petición
    headers = {
        "user-agent": "https://explore.whatismybrowser.com/useragents/parse/?analyse-my-user-agent=yes"
    }

    # Lista para almacenar los productos extraídos
    productos = []

    # Bucle para iterar por cada URL
    for url in urls:
        # Obtener el contenido HTML de la página
        response = requests.get(url, headers=headers)
        datahtml = response.text

        # Convertir el HTML a un objeto lxml
        finder = html.fromstring(datahtml)

        # Extraer elementos con data-producto usando XPath
        data_productos = finder.xpath('//div[@itemtype="http://schema.org/Product"]/@data-producto')

        # Procesar cada elemento data-producto
        for data_producto in data_productos:
            # Convertir comillas simples a dobles
            data_producto_con_dobles = re.sub("'", '"', data_producto)

            # Decodificar el JSON
            producto = json.loads(data_producto_con_dobles)

            # Extraer y almacenar la información deseada
            nombre = producto["name"].split("(")[0]
            # ... Puedes extraer otras propiedades como id, precio, etc.

            # Agregar el producto a la lista de productos
            productos.append({
                "nombre": nombre,
                # ... Añade otras propiedades extraídas
            })

    # Imprimir los nombres de los productos extraídos
    
    return productos
        
