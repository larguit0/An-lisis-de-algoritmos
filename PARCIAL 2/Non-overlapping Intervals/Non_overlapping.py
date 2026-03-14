class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int

        Estrategia Greedy elegida
        Ordenar los intervalos por su tiempo de finalización y mantener siempre
        el intervalo que termina primero. Esto porque al elegir el intervalo que termina antes deja más espacio 
        disponible para los siguientes intervalos, reduciendo la probabilidad de futuros
        solapamientos
        """

        # Se ordenan los intervalos por su tiempo de finalización
        # intervals.sort(key=lambda x: x[1])
        # Este ordenamiento permite aplicar la estrategia greedy elegir siempre el intervalo que termina primero.

        # Ordenar n intervalos → O(n log n)

        # Después del ordenamiento se hace un solo recorrido del arreglo  para verificar solapamientos.

        # El for recorre la lista una vez → O(n)

        # Complejidad total:
        # Ordenamiento → O(n log n)
        # Recorrido → O(n)

        # Big-O final → O(n log n)

        # Espacio:
        # Solo variables auxiliares (prev_end, removals)
        # Espacio extra → O(1)

        if len(intervals) <= 1:
            return 0

        intervals.sort(key=lambda x: x[1])

        prev_end = intervals[0][1]

        # contador de intervalos a eliminar
        removals = 0

        for i in range(1, len(intervals)):

            start, end = intervals[i]

            if start < prev_end:
                removals += 1

            else:
                prev_end = end
        return removals