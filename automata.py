import scraping
import json




productos=[]

def hacer_scraping():
    
    
    return scraping.scraping_m()
    

def guardar_json(productos):
    with open("productos.json", "w") as archivo:
        json.dump(productos, archivo, indent=4)


productos = hacer_scraping()
guardar_json(productos)

for producto in productos:
    print(producto["nombre"])
    
    
    
    
