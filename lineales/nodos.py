class Nodo_listaSE():
    def __init__(self, dato) -> None:
        self.dato = dato
        self.sig = None

    def __str__(self):
        return f"{self.dato}"

class Nodo_listaDE:
    def __init__(self, dato) -> None:
        self.dato = dato
        self.sig = None
        self.ant = None
    
    def __str__(self):
        return f"{self.dato}"

class Nodo_listaCSE:
    def __init__(self, dato) -> None:
        self.dato = dato
        self.sig = None
        
class Nodo_pila:
    def __init__(self, dato) -> None:
        self.dato = dato
        self.sig = None
        
class Nodo_cola:
    def __init__(self, dato) -> None:
        self.dato = dato
        self.sig = None

class NodoPrioridad:
    def __init__(self, dato, prioridad) -> None:
        self.dato = dato
        self.prioridad = prioridad
        self.sig = None