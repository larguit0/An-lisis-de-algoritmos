# El ciclo recorre el string una sola vez.
# Cada comparación es O(1).
# Total → O(n)

# Solo se usa una variable contador.
# No se crean estructuras adicionales.

# Espacio total → O(1)

# Mejor caso-Peor caso::
# Siempre debe recorrer todo el string.
# → O(n)

# Es una solución lineal eficiente.
# No es fuerza bruta porque no compara
# todos contra todos.

# Se usa un string (similar a arreglo).
# Acceder a s[i] → O(1)
# Recorrer completo → O(n)

# No se necesita set ni diccionario
# porque solo se comparan vecinos.

n = int(input())
s = input().strip()

contador = 0
for i in range(1, n):
    if s[i] == s[i - 1]:
        contador += 1

print(contador)
