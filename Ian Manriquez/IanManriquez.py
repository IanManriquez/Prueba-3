import json
import os
import time

while True:
    
    print ("")  
    print ("MUNDO LIBRO")
    print ("")
    print ("[1] - Menu de categorias")
    print ("[2] - Reportes")
    print ("[3] - Salir")
    opciones = int(input("Ingrese una opcion: "))

    if opciones == 1:
        while True:
            print ("")
            print ("MENU DE CATEGORIAS")
            print ("")
            print ("[1] - Agregar Categoria")
            print ("[2] - Editar Categoria")
            print ("[3] - Eliminar Categoria")
            print ("[4] - Buscar Categoria")
            print ("[5] - Volver")

            opcionesDos = int(input("Ingrese una opcion: "))

            if opcionesDos == 1:
                
                with open ("categoria.json", mode = "r") as LeerJson:
                lecturaJson = json.load(LeerJson)

                nuevaCategoria = {"Id": len("categoriaId.json") +1, "Nombre": nombre}

                lecturaJson["Categoria"].append(nuevaCategoria)

                with open ("categoria.json", mode = "w") as escribirJson:
                escrituraJson = json.dump(escribirJson, lecturaJson, indent = 4)


    elif opciones == 2:
        open #"Reportes_biblioteca_mundo_libro"
    
    else:
        print ("Que tenga un buen dia")
        exit()