# Recorre la lista una sola vez.
# Cada operación dentro del for es O(1).
# Total → O(n)

# Solo usa dos variables (minPrice y mejorGanancia).
# No crea estructuras nuevas.
# Espacio total → O(1)

# Mejor caso:
# Lista vacía o un solo elemento → O(1)
# Peor caso:
# Recorre toda la lista → O(n)

# No es fuerza bruta.
# Fuerza bruta sería probar todas las combinaciones
# de compra y venta → O(n²).

# se usa una solucion lineal eficiente:
# Se mantiene el precio minimo visto hasta ahora
# y se calcula la mejor ganancia en cada paso.

# Se usa un arreglo (lista).
# Acceder a un elemento → O(1)
# Recorrerlo completo → O(n)

# No se necesita hash map ni set
# porque solo se requiere comparar valores.
class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        
        minPrice = prices[0]
        mejorGanancia = 0

        for p in prices[1:]:
            ganancia = p -minPrice
            if ganancia > mejorGanancia:
                mejorGanancia = ganancia
            if p < minPrice:
                minPrice = p
        return mejorGanancia



        