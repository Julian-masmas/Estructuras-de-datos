# if __name__ == "__main__" and __package__ is None:
# from cola import Cola
# from nodos import Nodo_listaSE
# from lse import Lista_SE
# from lde import Lista_DE
# from pila import Pila
# from cp import ColaPrioridad
from jerarquicas.abin_obj import ArbolBinObj 
from jerarquicas.abin_bus import ArbolBinario_Bus
from jerarquicas.recorridos import pre_orden
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
    arbol = ArbolBinario_Bus()
    l = [4,9,2,5,7,10,1,12,13,45,123]
    for i in l:
        arbol.adicionar(i)
    print(arbol.encontrar_maximo())
