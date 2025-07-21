while True:
    print("\n--- Menú Principal ---")
    print("1. Ver estudiantes")
    print("2. Añadir estudiante")
    print("3. Salir")
    opcion = input("Selecciona una opción: ")
    match opcion:
        case 1:
            def factorial(n):
                if n == 0:
                    return 1
                else:
                    print(n)
                return n * factorial(n - 1)
            n = int(input("Ingrese un número entero positivo: "))
            print(factorial(n))
        case 2:
            def suma_numeros(n):
                if n == 1:
                    return 1
                else:
                    return n + suma_numeros(n - 1)
            try:
                n = int(input("Ingresa un número entero positivo: "))
                if n > 0:
                    resultado = suma_numeros(n)
                    print(f"La suma de los primeros {n} números naturales es: {resultado}")
                else:
                    print("Por favor ingresa un número mayor que cero.")
            except ValueError:
                print("Entrada no válida. Debes ingresar un número entero.")
        case 3:
            def Fibonacci(n):
                if n < 0:
                    return 0
                elif n == 1:
                    return 1
                else:
                    return n + Fibonacci(n - 1) + Fibonacci(n - 2)
                    n = int(input("Ingrese un numero entero positivo: "))
                if n > 0:
                    resultado = Fibonacci(n)
                    print(f"La suma de {n}: {resultado}")
                else:
                    print("Intente de nuevo")
        case 4:
            def
        case 5:
        case 6:
            def potencia(base,exponente):
                if exponente==0:
                    return 1
                else:
                    print(n)
                    return base*potencia(base,exponente-1)
            base=int(input("ingrese una base: "))
            exponente=int(input("ingrese un exponente: "))
            print(potencia(base,exponente))
        case 7:
            print("Saliendo del programa...")
            break