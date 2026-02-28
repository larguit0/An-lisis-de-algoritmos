# Primer for recorre s → O(n)
# Segundo for recorre t → O(n)
# Total: O(n) + O(n) = O(2n)
# En Big O se eliminan constantes → O(n)

# Se usa un diccionario para contar letras.
# En el peor caso puede guardar n caracteres distintos.q
# Mejor caso:
# Si las longitudes son distintas → O(1)
# También puede terminar antes si detecta un conteo negativo.

# Peor caso:
# Cuando sí son anagramas.
# Recorre completamente ambos strings → O(n)

# Se usa un diccionario para el alojo de 
class Solution(object):
    def isAnagram(self, s, t):
        while (len(s) == len(t)):
            cuenta ={}
            for c in s:
                cuenta[c] = cuenta.get(c,0)+1

            for c in t:
                cuenta[c]=cuenta.get(c,0)-1
                if cuenta[c]<0:
                    return False
            return True
        return False



        
        