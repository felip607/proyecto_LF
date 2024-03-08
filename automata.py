import re
import scraping
import json



categorias=[[],[],[],[],[],[],[]]
productos=[]

def hacer_scraping():
    
    
    return scraping.scraping_m()
    

def guardar_json(productos):
    with open("productos.json", "w") as archivo:
        json.dump(productos, archivo, indent=4)
    
    with open("Hoodie.json", "w") as archivo:
        json.dump(categorias[0], archivo, indent=4)
    
    with open("Chaqueta.json", "w") as archivo:
        json.dump(categorias[1], archivo, indent=4)
    
    with open("Cardigan.json", "w") as archivo:
        json.dump(categorias[2], archivo, indent=4)
    
    with open("Camisas_camibusos.json", "w") as archivo:
        json.dump(categorias[3], archivo, indent=4)
        
    with open("Pantalones.json", "w") as archivo:
        json.dump(categorias[4], archivo, indent=4)
    
    with open("Joggers.json", "w") as archivo:
        json.dump(categorias[5], archivo, indent=4)
        
    with open("otros.json", "w") as archivo:
        json.dump(categorias[6], archivo, indent=4)
        
   
    
    
    
def clasificar():
    for producto in productos:
        if re.match(r'^.*Hoodie.*$', str(producto['nombre'])):
            categorias[0].append(producto)
           
        elif re.match(r'^(?!.*Hoodie).*Chaqueta.*$', str(producto['nombre'])):
            categorias[1].append(producto)
            
        elif re.match(r'^.*Cardigan.*$', str(producto['nombre'])) or re.match(r'^.*Cárdigan.*$', str(producto['nombre'])):
            categorias[2].append(producto)
            
        elif re.match(r'^.*Cami.*$', str(producto['nombre'])):
            categorias[3].append(producto)
           
        elif re.match(r'^.*Pantalon.*$', str(producto['nombre'])):
            categorias[4].append(producto)
            
        elif re.match(r'^.*Jogger.*$', str(producto['nombre'])):
            categorias[5].append(producto)
            
        else :
            categorias[6].append(producto)
            

def menu():
    op=True
    while(op):
        
        print("selecione una opcion")
        print("1) hacer scraping")
        print("2) salir")
        opcion = input()
        if opcion == '1':
            op2=True
            while (op2) :
                clasificar()
                print("seleccione una opcion")
                print("1) ver productos")
                print("2) ver productos clasificados")
                print("3) guardar en json")
                opcion2 = input()
                if opcion2 == '1':
                    print("PRODUCTOS")
                    print("------------------------")
                    for prod in productos:
                        print(prod['nombre'])
                    print("------------------------")
                elif opcion2 =='2':
                    
                    print("RESULTADOS")
                    print("------------------------")
                    print("hoodies")
                    for prod in categorias[0]:
                        print(prod['nombre'])
                    print("------------------------")
                    print("chaquetas")
                    for prod in categorias[1]:
                        print(prod['nombre'])
                    print("------------------------")
                    print("cardigan")
                    for prod in categorias[2]:
                        print(prod['nombre'])
                    print("------------------------")
                    print("camisas_camibusos")
                    for prod in categorias[3]:
                        print(prod['nombre'])
                    print("------------------------")
                    print("pantalones")
                    for prod in categorias[4]:
                        print(prod['nombre'])
                    print("------------------------")
                    print("joggers")
                    for prod in categorias[5]:
                        print(prod['nombre'])
                    print("------------------------")
                    print("otros")
                    for prod in categorias[6]:
                        print(prod['nombre'])
                    print("------------------------")
                elif opcion2=='3':
                    print("jsons guardados")
                    guardar_json(productos)
                else:
                    op2=False
                    print("atras")
                
        else:    
            print("salientdo")
            break

productos = hacer_scraping()
menu()





    
    
    
