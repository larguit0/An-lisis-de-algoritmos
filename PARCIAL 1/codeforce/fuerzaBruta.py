##no dA

def min_remove_bruteforce(s: str) -> int:
    n = len(s)
    minimo = n  # peor caso: eliminar todas

    def es_valida(cadena):
        for i in range(1, len(cadena)):
            if cadena[i] == cadena[i - 1]:
                return False
        return True

    def backtrack(index, construida):
        nonlocal minimo

        if index == n:
            if es_valida(construida):
                eliminadas = n - len(construida)
                minimo = min(minimo, eliminadas)
            return

        # Opción 1: NO eliminar
        backtrack(index + 1, construida + s[index])

        # Opción 2: eliminar
        backtrack(index + 1, construida)

    backtrack(0, "")
    return minimo