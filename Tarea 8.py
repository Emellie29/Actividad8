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
n=int(input("Ingrese un numero entero para la suma: "))
print(suma(n))
########################
print("FIBONACCI")
def fibonacci(n):
    if n<0:
        return 1
    elif n==1:
        return 0
    else:
        print(n)
        return n+fibonacci(n-1)
n=int(input("Ingrese un numero entero n: "))
print(fibonacci(n))
######################
print("NO. LETRAS EN LA PALABRA")
def letra(n):
    if n == 0:
        return 0
    else:
        print(n)
        return n+letra(n-1)
n=input("Ingrese la frase que desea evaluar: ")
print(letra(n))
