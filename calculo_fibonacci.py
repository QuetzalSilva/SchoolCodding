# Definimos una función recursiva para calcular la secuencia de Fibonacci.
def calculo_fibonacci(n, secuencia=[0, 1]):
    # Con ayuda de un condicional, confirmaremos que el número ingresado sea positivo mayor a cero.
    if n <= 0:
        return "El número ingresado no cumple con los parámetros requeridos, intente de nuevo."
    
    # Si la longitud de la secuencia es igual a n, hemos terminado nuestro cálculo.
    if len(secuencia) >= n:
        return secuencia[:n]
    
    # Añadimos el siguiente número en la secuencia.
    secuencia.append(secuencia[-1] + secuencia[-2])
    return calculo_fibonacci(n, secuencia)

# Ingresaremos manualmente el número que queremos calcular.
numero = int(input("Ingresa un número positivo mayor a cero: "))
resultado = calculo_fibonacci(numero)

# Nos mostrará por pantalla el cálculo completo.
print(f"Secuencia de Fibonacci para {numero} términos: {resultado}")