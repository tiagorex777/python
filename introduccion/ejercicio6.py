list = [1,2,3,4,5,6,7,8,9,10]
par = ""
impar = ""
for elemento in list:
    numero = str(elemento)
    if(elemento % 2 == 0):
        par += numero + " "
    else:
        impar += numero + " "
print(f"lista par :{par}")
print(f"lista impar:{impar}")
    