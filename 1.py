#Crea un programa que solicite al usuario ingresar valores y este debe verificar cuando se ingresa una vocal, el programa
#debe contar y mostrar la cantidad de vocales (a, e, i, o, u) ingresadas cuantas, de cada una y la cantidad total, importante
#tener en cuenta que la aplicación se detiene con una opción de menú llamada finalizar.
def contar_vocales(cadena):
    # Inicializamos el contador de cada vocal a 0
    contador_a = contador_e = contador_i = contador_o = contador_u = 0
    
    # Convertimos la cadena a minúsculas para hacer la comparación más simple
    cadena = cadena.lower()
    
    # Recorremos cada carácter de la cadena
    for caracter in cadena:
        if caracter == 'a':
            contador_a += 1
        elif caracter == 'e':
            contador_e += 1
        elif caracter == 'i':
            contador_i += 1
        elif caracter == 'o':
            contador_o += 1
        elif caracter == 'u':
            contador_u += 1
    
    # Calculamos el total de vocales
    total_vocales = contador_a + contador_e + contador_i + contador_o + contador_u
    
    # Mostramos los resultados
    print("Cantidad de vocales 'a':", contador_a)
    print("Cantidad de vocales 'e':", contador_e)
    print("Cantidad de vocales 'i':", contador_i)
    print("Cantidad de vocales 'o':", contador_o)
    print("Cantidad de vocales 'u':", contador_u)
    print("Total de vocales:", total_vocales)

def main():
    while True:
        print("1. Ingresar una cadena")
        print("2. Finalizar")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            cadena = input("Ingrese una cadena de texto: ")
            contar_vocales(cadena)
        elif opcion == "2":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()