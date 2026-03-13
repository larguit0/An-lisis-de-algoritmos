class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]

        Estrategia Greedy elegida
        Primero se ordenan los intervalos por start.
        Luego se recorren los intervalos una sola vez fusionando aquellos
        que se solapan.

        Si los intervalos están ordenados por start, cualquier solapamiento
        posible solo puede ocurrir con el intervalo anterior ya procesado.
        Por eso estaría bien comparar el final del último intervalo agregado
        con el inicio del intervalo actual.

        """
         # Se ordenan los intervalos por su punto de inicio
        # intervals.sort(key=lambda x: x[0])

        # esto permite recorrer los intervalos en orden y detectar fácilmente los solapamientos consecutivos

        # Ordenar n intervalos → O(n log n)

        # Luego se hace una sola pasada del arreglo para fusionar los intervalos que se solapan.
        # El for recorre todos los intervalos una vez → O(n)

        # En cada iteración:
        # comparar inicio con el final anterior → O(1)
        # actualizar el intervalo → O(1)

        # Complejidad total:
        # Ordenamiento → O(n log n)
        # Recorrido → O(n)

        # Big-O final → O(n log n)

        # Espacio:
        # Se usa una lista para guardar los intervalos fusionados
        # En el peor caso puede almacenar todos los intervalos

        # Espacio total → O(n)

        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])

        merged = [intervals[0]]

        for start, end in intervals[1:]:
            last_end = merged[-1][1]
            if start <= last_end:
                merged[-1][1] = max(last_end, end)
            else:
                merged.append([start, end])

        # Complejidad total:
        # Ordenamiento : O(n log n)
        # Recorrido : O(n)
        # Total :  O(n log n)

        # Espacio:
        # Se usa una lista para guardar los intervalos fusionados
        # En el peor caso puede almacenar todos los intervalos
        # Complejidad espacial : O(n)

        return merged