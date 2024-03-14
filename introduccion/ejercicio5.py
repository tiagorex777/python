entrada_usuario = input("ingrese lista de numeros separado con , ")
lista = entrada_usuario.split(',')

for element in lista:
    numero = int(element) #cambio el tipo de dato de string a entero
    if(numero < 0):
        break
    print(element)

