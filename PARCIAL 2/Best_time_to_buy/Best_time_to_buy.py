class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int

        Estrategia Greedy:
        Cuando el precio del día actual es mayor que el del día anterior,
        se suma esa diferencia como ganancia. Esto equivale a comprar en el
        día anterior y vender en el día actual

        Si el precio sube de un día a otro, siempre es beneficioso aprovechar
        esa subida

        Esto funciona porque varias transacciones pequeñas equivalen a una
        sola transacción grande entre el valle y el pico.

        """
        # No se ordena el arreglo de precios porque el orden de los días es importante.

        # Se recorre la lista una sola vez comparando el precio actual con el del día anterior.

        # El for recorre n elementos → O(n)

        # Cada operación dentro del for es O(1)
        # comparación de precios → O(1)
        # suma de ganancia → O(1)

        # Total → O(n)

        # Espacio:
        # Solo se usa una variable (profit)
        # Espacio total → O(1)

        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]

        # Complejidad total:
        # Recorrido del arreglo → O(n)

        # Espacio:
        # Solo se usa una variable adicional (profit)
        # Complejidad espacial → O(1)

        return profit