class NodoArbol_Bin:
    def __init__(self, clave) -> None:
        self.clave = clave
        self.izq = None
        self.der = None

    def tiene_hijos(self) -> bool:
        if not self.izq and not self.der:
            return False
        return True

    def __str__(self) -> str:
        return f"{self.clave}" 