# if __name__ == "__main__" and __package__ is None:
from cola import Cola
from nodos import Nodo_listaSE
from lse import Lista_SE
from lde import Lista_DE
from pila import Pila
from cp import ColaPrioridad
from jerarquicas.abin_obj import ArbolBinObj 
# else:
#     from bed.lineales.nodos import Nodo_listaSE
    
class Estudiante:
    def __init__(self, nombre:str, codigo) -> None:
        self.nombre = nombre
        self.codigo = codigo
    
    def __eq__(self, value: object, /) -> bool:
        return self.nombre == value.nombre or self.codigo == value.codigo

if __name__ == "__main__":
    arbolObj = ArbolBinObj()
    arbolObj.adicionar(Estudiante("Jose", 123), 1)
    arbolObj.adicionar(Estudiante("Josefina", 124), 2)
    arbolObj.adicionar(Estudiante("Pepe", 125), 3)
    arbolObj.adicionar(Estudiante("Luis", 126), 4)
    arbolObj.encontrar("Jose")
