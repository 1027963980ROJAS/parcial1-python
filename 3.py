#Escribe un programa que permita al usuario convertir una temperatura en grados centígrados a Fahrenheit o viceversa. El programa debe
#solicitar al usuario ingresar la temperatura y la unidad de medida (C para Celsius, F para Fahrenheit) y luego realizar la conversión
#correspondiente, el programa debe manejar un menú de opciones y solo detenerse cuando se presione la opción finalizar.
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    while True:
        print("1. Convertir de Celsius a Fahrenheit")
        print("2. Convertir de Fahrenheit a Celsius")
        print("3. Finalizar")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            celsius = float(input("Ingrese la temperatura en grados Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print("La temperatura en grados Fahrenheit es:", fahrenheit)
        elif opcion == "2":
            fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print("La temperatura en grados Celsius es:", celsius)
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()