import random
numero=random.randint(1,10)
intentos=0
while True:
    valor = input("ingrese su numero")
    if valor==numero:
        print("has acertado")
        break
    else:
        print("has fallado")
        intentos+=1
        if intentos>5:
            print("gameOver")


# print(random.randint(3,9))
# print(random.choices([2,4,7,9,0,3]))