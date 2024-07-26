def suma(a, b):
    mini_suma = a + b
    return mini_suma

def resta(a, b):
    mini_resta = a - b
    return mini_resta

def multiplicacion (a, b):
    mini_multiplicacion = a * b
    return mini_multiplicacion

def division (a, b):
    mini_division = a / b
    return mini_division

def potenciacion(a, b):
    mini_potenciacion = a ** b
    return mini_potenciacion

def radicacion(a, b):
    mini_potenciacion = pow(a, (1/b))
    return mini_potenciacion

def superindice(n):
    superindices = {
        0: '⁰', 1: '¹', 2: '²', 3: '³', 4: '⁴', 5: '⁵', 6: '⁶', 7: '⁷', 8: '⁸', 9: '⁹'
    }
    return ''.join(superindices.get(int(d), '') for d in str(n))
def mostrar_potenciacion(base, exponente):
    return f'{base}{superindice(exponente)}'
def mostrar_radicacion(base, raiz):
    return f'{superindice(raiz)}√{base}'

print("CALCULADORA VIRTUAL DE ENTEROS - BY: JIMMY ALEXANDER HUERTA VASQUEZ")
num_a = int(input("Ingrese el primer número: "))
num_b = int(input("Ingrese el segundo número: "))

# Llamada a la función y almacenamiento del resultado
resultado_suma = suma(num_a, num_b)
resultado_resta = resta(num_a, num_b)
resultado_multiplicacion = multiplicacion(num_a, num_b)
resultado_division = division(num_a, num_b)
resultado_potenciacion = potenciacion(num_a, num_b)
resultado_radicacion = radicacion(num_a, num_b)

# Imprimir el resultado
print(f'OPERACIÓN SUMA:\n{num_a} + {num_b} = {resultado_suma}')
print(f'OPERACIÓN RESTA:\n{num_a} - {num_b} = {resultado_resta}')
print(f'OPERACIÓN MULTIPLICACIÓN:\n{num_a} * {num_b} = {resultado_multiplicacion}')
print(f'OPERACIÓN DIVISIÓN:\n{num_a} / {num_b} = {resultado_division}')
print(f'OPERACIÓN POTENCIACIÓN:\n {mostrar_potenciacion(num_a, num_b)}= {resultado_potenciacion}')
print(f'OPERACIÓN RADICACIÓN:\n{mostrar_radicacion(num_a, num_b)} = {resultado_radicacion}')
