# cliente={"Nombre":"Jairo", "Apellido":"Torres","edad":"45","telefono":"3203142869","saldo":"6543789"}
# cliente={
    # "nombre":"Jairo",
    # "apellido":"Torres",
    # "edad":"45",
    # "telefono":"3203142869",
    # "saldo":"6543789"
    # }
    
# print(cliente)
# valor=cliente.get("nombre") # trae valor
# print(valor)
# cliente["profesion"]= "desarrollador" # ingresa valores
# cliente["ocupacion"]="designer"
# print(cliente["telefono"]) # imprime valor
# del cliente["telefono"] # borra valores

# print(cliente)
# print(cliente.keys())
# print(cliente.values())
# cajero={
#     "nombre":"juanito",
#     "apellido":"marquez",  
# }
# cliente.update(cajero) #une los diccionarios


redes = []  #define lista vacia
while True: #genera un clclo infinito
    print("opcion 1 agregar red") #imprime en pantalla
    print("opcion 2 ver redes") #imprime en pantalla
    print("opcion 0 para salir") #imprime en pantalla
    opcion = int(input("ingrese una opcion")) #imprime en pantalla
    if opcion == 1: #compara la opcion con el valor entero 1 y ejecuta bloque de codigo
        red = {} #define diccionario vacio
        print("ingrese la red") #imprime en pantalla
        nombre = input() #ingresa datos del teclado a la variable
        red["nombre"] = nombre  #guarda el dato del input en el diccionario clave nombre
        print("ingrese la contraseña")  #imprime en pantalla
        clave=input()  #ingresa datos del teclado a la variable
        red["clave"] = clave #guarda el dato del input en el diccionario clave clave
        redes.append(red) #agrega diccionario a la lista
    elif opcion == 2:  #compara la opcion con el valor entero 1 y ejecuta bloque de codigo
        for i in range(len(redes)): #repite el bloque segun el tamaño de la lista redes( metodo len)
            print(redes[i]) #imprime en pantalla