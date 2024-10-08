# Funci�n iterativa para sumar los d�gitos de un n�mero
def suma_iterativa(n):
    suma = 0
    while n > 9:
        suma += n % 10
        n //= 10
    return suma + n

# Funci�n recursiva para sumar los d�gitos de un n�mero
def suma_recursiva(n):
    if n <= 9:
        return n
    else:
        return suma_recursiva(n // 10) + n % 10

# Programa principal
numero = int(input("Ingrese un numero: "))

# Llamando a la funcion iterativa
print(f"Suma de los digitos (iterativa): {suma_iterativa(numero)}")

# Llamando a la funcion recursiva
print(f"Suma de los digitos (recursiva): {suma_recursiva(numero)}")