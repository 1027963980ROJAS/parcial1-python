#Escribe un programa en Python que permita calcular el pago de un producto en una tienda, tomando en cuenta que los productos se encuentran
#clasificados en cinco categorías: Ferretería, Aseo, Seguridad, Alimentos y Electrodomésticos. Cada categoría tiene un descuento diferente aplicado al
#precio del producto, el cual debe presentar un menú de opciones donde solo se termina el sistema con la opción “TERMINAR”.
#Descuentos por Categoría: Ferretería: 10% Aseo: 5% Seguridad: 15% Alimentos: 8% Electrodomésticos: 12%
#El programa debe solicitar al usuario ingresar la categoría y el precio de cada producto comprado, y luego calcular el precio final con el descuento
#aplicado. Al finalizar, debe mostrar la cantidad de productos comprados por cada categoría y el total recaudado.

# Definimos un diccionario que mapea cada categoría con su respectivo descuento
descuentos_por_categoria = {
    "Ferretería": 0.10,
    "Aseo": 0.05,
    "Seguridad": 0.15,
    "Alimentos": 0.08,
    "Electrodomésticos": 0.12
}

def calcular_descuento(categoria, precio):
    if categoria in descuentos_por_categoria:
        descuento = descuentos_por_categoria[categoria]
        return precio * (1 - descuento)
    else:
        return precio

def main():
    total_recaudado = 0
    cantidad_por_categoria = {categoria: 0 for categoria in descuentos_por_categoria}

    while True:
        print("Categorías disponibles:")
        for categoria in descuentos_por_categoria:
            print("-", categoria)
        print("TERMINAR")

        categoria = input("Ingrese la categoría del producto (o 'TERMINAR' para finalizar): ")

        if categoria == "TERMINAR":
            break

        if categoria in descuentos_por_categoria:
            precio = float(input("Ingrese el precio del producto: "))
            precio_con_descuento = calcular_descuento(categoria, precio)
            total_recaudado += precio_con_descuento
            cantidad_por_categoria[categoria] += 1
            print("El precio final con descuento es:", precio_con_descuento)
        else:
            print("Categoría inválida. Por favor, seleccione una categoría válida.")

    print("\nResumen de la compra:")
    for categoria, cantidad in cantidad_por_categoria.items():
        print("Cantidad de productos en", categoria + ":", cantidad)
    print("Total recaudado:", total_recaudado)

if __name__ == "__main__":
    main()