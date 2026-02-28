# Recorre la lista una sola vez → O(n)
# Buscar en un set → O(1) promedio
# Insertar en un set → O(1) promedio
# Total → O(n)

# Se usa un set para guardar los elementos vistos.
# En el peor caso guarda todos los elementos.

# Espacio total → O(n)

# Mejor caso:
# El primer duplicado aparece temprano.
# Termina antes de recorrer todo.

# Peor caso:
# No hay duplicados o están al final.
# Recorre toda la lista → O(n)

# No es fuerza bruta.
# Fuerza bruta sería comparar cada elemento
# con todos los demás → O(n²).

# Aquí se usa un set para detectar duplicados
# en tiempo constante.

# Lista:
# Buscar un elemento → O(n)

# Set no permite duplicados
# Buscar e insertar → O(1) promedio

# Gracias al set se reduce de O(n²) a O(n).

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        viewed = set()
        for i in nums:
            if i in viewed:
                return True
            viewed.add(i)
        return False