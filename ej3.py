num1 = int (input("ingrese un numero"))
num2 = int (input("ingrese otro numero"))

suma = num1 + num2
multiplicacion = num1 * num2

print("la suma es ", suma)
print("la multiplicacion es ", multiplicacion)

if num2 != 0:
    residuo = num1 % num2
    print("el residuo es ", residuo)

else:
    print("no se puede dividir entre 0")
    