def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n_terms = int(input("Ingrese el número de términos de la secuencia de Fibonacci que desea generar: "))

if n_terms <= 0:
    print("Ingrese un número entero positivo.")
else:
    print("La secuencia de Fibonacci es:")
    for i in range(n_terms):
        print(fibonacci(i))
