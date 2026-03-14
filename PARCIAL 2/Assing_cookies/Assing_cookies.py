class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
         

        Estrategia Greedy elegida:
        Se ordenan los niños por nivel de interes y las galletas por tamaño.
        Despues se intenta satisfacer primero al niño menos exigente con la
        galleta más pequeña que sea suficiente.

        Si se diera una galleta grande a un niño poco exigente, podría faltar
        para un niño más exigente después
        
        """

        # Se ordena la lista de niños por nivel de avaricia → O(n log n)
        # Se ordena la lista de galletas por tamaño → O(m log m)

        # Después del ordenamiento se usa un while que recorre ambas listas
        # cada una como máximo una vez.

        # i avanza por los niños → O(n)
        # j avanza por las galletas → O(m)

        # Total del recorrido → O(n + m)

        # Complejidad total:
        # O(n log n + m log m) por los ordenamientos
        # + O(n + m) por el recorrido
        # Big-O final → O(n log n + m log m)

        # Espacio:
        # Solo se usan variables auxiliares (i, j, contentos)
        # Espacio extra → O(1)

        g.sort()
        s.sort()

        i = 0  #  niños
        j = 0  #  galletas
        contentos = 0


        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                contentos += 1
                i += 1
                j += 1
            else:
                j += 1

        return contentos