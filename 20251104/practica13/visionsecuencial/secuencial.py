import math
import statistics

# ========================
# Datos iniciales
# ========================
a = 10
b = 5
lista = [1, 2, 3, 4, 4, 5]

# ========================
# Operaciones Básicas
# ========================
print("=== Operaciones Básicas ===")
suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b if b != 0 else "Error: división por cero"

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")

# ========================
# Estadísticas
# ========================
print("\n=== Estadísticas Básicas ===")
media = statistics.mean(lista)
mediana = statistics.median(lista)
moda = statistics.mode(lista)

print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")

# ========================
# Operaciones Especiales
# ========================
print("\n=== Operaciones Especiales ===")
potencia = a ** b
raiz = math.sqrt(a) if a >= 0 else "Error: raíz de número negativo"
logaritmo = math.log(a) if a > 0 else "Error: logaritmo indefinido"
exponencial = math.exp(b)

print(f"Potencia ({a}^{b}): {potencia}")
print(f"Raíz cuadrada de {a}: {raiz}")
print(f"Logaritmo de {a} base e: {logaritmo}")
print(f"Exponencial de {b}: {exponencial}")
