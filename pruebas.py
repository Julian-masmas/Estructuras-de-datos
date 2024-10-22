# if __name__ == "__main__" and __package__ is None:
# from cola import Cola
# from nodos import Nodo_listaSE
# from lse import Lista_SE
# from lde import Lista_DE
# from pila import Pila
# from cp import ColaPrioridad
from jerarquicas.abin_obj import ArbolBinObj 
# else:
#     from bed.lineales.nodos import Nodo_listaSE
    
class Estudiante:
    def __init__(self, nombre:str, codigo) -> None:
        self.nombre = nombre
        self.codigo = codigo
    
    def __eq__(self, otro) -> bool:
        return self.nombre == otro.nombre

    def __str__(self) -> str:
        return f"{self.nombre}: {self.codigo}"

if __name__ == "__main__":
    arbolObj = ArbolBinObj()
    arbolObj.adicionar(Estudiante("Jose", 123), 8)
    arbolObj.adicionar(Estudiante("Pepe", 125), 14)
    arbolObj.adicionar(Estudiante("Josefina", 124), 7)
    arbolObj.adicionar(Estudiante("Daniela", 126), 10)
    arbolObj.adicionar(Estudiante("Luis", 126), 12)
    arbolObj.adicionar(Estudiante("Danna", 126), 11)
    # arbolObj.adicionar(Estudiante("Angela", 126), 7)
    # arbolObj.adicionar(Estudiante("Sara", 126), 1)
    print(arbolObj.altura())
