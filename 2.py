#Crea un programa que solicite al usuario ingresar un número entero positivo (N). El programa debe mostrar la tabla de
#multiplicar del número, teniendo en cuenta que se debe generar la tabla con los primeros 10 valores de dicha tabla.
numero = int(input('por favor, ingrese un numero entero positivo (n): '))
if numero > 0:
    for i in range(1, 11):
        print(f'{numero} x {i} = {numero * i}')
else:
    print("Debes ingresar un número entero positivo.")