def saludar():
    print ("Reciba Un Cordial Saludo")

saludar() # llama la funcion e imprime su contenido

# ingresar a menu para seleccionar opciones

#*** def calcular(cantidad,valor):
#     return cantidad*valor

# print("ingrese cantidad de productos ")
# cantidad=input()

# print("ingrese valor de producto ")
# valor=input()

# total=calcular(cantidad,valor)

# print(f"el total de los productos es $ {total})") ****


def calcular(c,v):
    return c*v
subtotal=0
cantidad=1

while cantidad!=0:
    print("ingrese cantidad de productos ")
    cantidad=float(input())
    if cantidad ==0:
        break
    print("ingrese valor de producto ")
    valor=float (input())
    total=calcular(cantidad, valor)

print(f"el total de los productos es $ {calcular})")