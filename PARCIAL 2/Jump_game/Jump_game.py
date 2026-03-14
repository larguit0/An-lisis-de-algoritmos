class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        Estrategia Greedy elegida:
        Se mantiene el índice más lejano que se puede alcanzar, 
        mientras se recorre  el arreglo, actualizamos ese alcance máximo usando
        el salto disponible en cada posición.

        Si en algún punto el índice actual es mayor que el alcance máximo
        alcanzable, significa que no se puede llegar a esa posición, por lo
        tanto es imposible llegar al final del arreglo
        """

        # Se recorre la lista una sola vez usando un for
        # Cada operación dentro del for es O(1)

        # Actualizar max_reach → O(1)
        # Comparaciones → O(1)

        # Total del recorrido → O(n)
        # manteniendo el alcance máximo alcanzable.

        # Espacio:
        # Solo se usa una variable (max_reach)
        # Espacio total → O(1)

        max_reach = 0

        # En el peor caso se recorren todos los elementos → O(n)
        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
            if max_reach >= len(nums) - 1:
                return True
        return True