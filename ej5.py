nota = int(input("ingrese su nota"))

if nota < 0 or nota > 100:
    print("la nota no es valida")
elif nota <= 50:
    print("reprobado con ", nota)
else:
    print("aprobado con ", nota)