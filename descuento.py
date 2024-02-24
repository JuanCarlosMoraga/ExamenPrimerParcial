def calcDescuento(precio):
    if precio > 500:
        descuento = precio * 0.10
        precioDescuento = precio - descuento
        return precioDescuento
    else:
        return precio

def main():
    print("Bienvenido a la aplicación que cálcula su descuento")

    precio = float(input("Ingrese el precio del producto: "))

    precio_final = calcDescuento(precio)

    print("El precio final del producto es:", precio_final)

if __name__ == "__main__":
    main()
