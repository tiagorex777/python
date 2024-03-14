lista_ingresada = input("ingrese cadena de numeros separados con espacio ")
lista = lista_ingresada.split(' ')

print(lista_ingresada)
cadena = ""

for element in lista:
    numero = int(element)
    if(numero % 3 == 0):
        continue
    else:
        cadena += element + " - "
print(cadena)

    