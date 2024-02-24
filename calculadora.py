def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir por cero."

def calculadora():
    print("Bienvenido a la calculadora")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    opcion = input("Por favor, elige una opción (1:Sumar/2:Restar/3:Multiplicacio/4Division: ")

    if opcion in ['1', '2', '3', '4']:
        number1 = float(input("Ingrese el primer número: "))
        number2 = float(input("Ingrese el segundo número: "))

        if opcion == '1':
            print("El resultado de la suma es:", suma(number1, number2))
        elif opcion == '2':
            print("El resultado de la resta es:", resta(number1, number2))
        elif opcion == '3':
            print("El resultado de la multiplicación es:", multiplicacion(number1, number2))
        elif opcion == '4':
            print("El resultado de la división es:", division(number1, number2))
    else:
        print("Opción inválida")

calculadora()