def suma(a, b):
    mini_suma = a + b
    return mini_suma
def resta(a, b):
    mini_resta = a - b
    return mini_resta

print("CALCULADORA VIRTUAL")
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

# Llamada a la función y almacenamiento del resultado
resultado_suma = suma(a, b)
resultado_resta = resta(a, b)

# Imprimir el resultado
print(f'OPERACIÓN SUMA:\n{a} + {b} = {resultado_suma}')
print(f'OPERACIÓN RESTA:\n{a} - {b} = {resultado_resta}')
