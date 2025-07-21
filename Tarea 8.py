#while True
print("FACTORIAL")
def factorial(n):
   if n == 0:
      return 1
   else:
    print(n)
    return n * factorial(n - 1)
n = int(input("Ingrese un número entero positivo: "))
print(factorial(n))
#############################
print("SUMA")
def suma(n):
    if n == 0:
        return 0
    else:
        print(n)
        return n + suma(n-1)
n=int(input("Ingrese numero entero positivo: "))
print(suma(n))
########################
print("FIBONACCI")
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
######################
print("NO. LETRAS EN LA PALABRA")
#######################
print("INVERTIR UNA CADENA DE TEXTOS")
#######################
print("CALCULAR UNA POTENCIA")
def potencia(base,exponente):
    if exponente==0:
        return 1
    else:
        print(n)
        return base*potencia(base,exponente-1)
base=int(input("ingrese una base: "))
exponente=int(input("ingrese un exponente: "))
print(potencia(base,exponente))