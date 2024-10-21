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

class NodoArbol_Bin_Obj:
    def __init__(self, clave, orden:int) -> None:
        """Constructor de la clase nodo para arboles de busqueda

        Parameters
        ----------
        clave : object
            cualquier objeto
        orden : int
            valor mediante el cual se ordenará el arbol
        """
        self.clave = clave
        self.izq = None
        self.der = None
        self.orden = orden

    def tiene_hijos(self) -> bool:
        if not self.izq and not self.der:
            return False
        return True

    def __str__(self) -> str:
        return f"{self.clave}" 

    def __eq__(self, value: object, /) -> bool:
        return self.orden == value.orden and self.clave == value.clave