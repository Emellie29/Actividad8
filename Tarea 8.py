while True:
    print("\n♥♥♥♥♥♥♥♥MENÚ♥♥♥♥♥♥♥♥")
    print("1. Factorial")
    print("2. Suma")
    print("3. Fibonacci")
    print("4. Contar una letra en una palabra")
    print("5. Invertir cadena de texto")
    print("6. Potencia")
    print("7. Salir")
    opcion = input("Selecciona una opción: ")
    match opcion:
        case "1":
            def factorial(n):
                if n == 0:
                    return 1
                else:
                    print(n)
                    return n * factorial(n - 1)
            n = int(input("Ingrese un número entero positivo: "))
            print(factorial(n))
        case "2":
            def suma_numeros(n):
                if n == 1:
                    return 1
                else:
                    return n + suma_numeros(n - 1)
            try:
                n = int(input("Ingresa un número entero positivo: "))
                if n > 0:
                    resultado = suma_numeros(n)
                    print(f"La suma de los primeros {n} números es: {resultado}")
                else:
                    print("Por favor ingresa un número mayor que cero.")
            except ValueError:
                print("Entrada no válida. Debes ingresar un número entero.")
        case "3":
            def Fibonacci(n):
                if n<=1:
                    return n
                else:
                    return Fibonacci(n-1) + Fibonacci(n-2)
            n=int(input("Ingrese un número entero positivo: "))
            print(f"Fibonacci({n}): {Fibonacci(n)}")
        case "4":
            def contar(palabra,letra,indice=0):
                if indice == len(palabra):
                    return 0
                if palabra[indice].lower()== letra.lower():
                    return contar(palabra,letra,indice+1)+1
                else:
                    return contar(palabra,letra,indice+1)
            palabra=input("Ingrese una palabra: ")
            letra=input("Ingrese una letra para contar: ")
            if len(letra)!=1:
                print("Por favor ingresa una letra: ")
            else:
                cantidad=contar(palabra,letra)
                print(f"la letra {letra} aparece {cantidad} veces en la palabra.")
        case "5":
            def cadena_Invertida(Cadena):
                if len(Cadena)==0:
                    return ""
                else:
                    return Cadena[-1]+cadena_Invertida(Cadena[:-1])
            texto=input("Ingrese una cadena de texto: ")
            invertir=cadena_Invertida(texto)
            print(f"Cadena de texto invertida: {invertir}")
        case "6":
            def potencia(base,exponente):
                if exponente==0:
                    return 1
                else:
                    return base*potencia(base,exponente-1)
            base=int(input("ingrese una base: "))
            exponente=int(input("ingrese un exponente: "))
            print(potencia(base,exponente))
        case "7":
            print("Saliendo del programa.")
            break
        case _:
            print("Opcion no valida. Intente de nuevo.")