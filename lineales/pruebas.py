# if __name__ == "__main__" and __package__ is None:
from cola import Cola
from nodos import Nodo_listaSE
from lse import Lista_SE
from lde import Lista_DE
from pila import Pila
from cp import ColaPrioridad
# else:
#     from bed.lineales.nodos import Nodo_listaSE
    


if __name__ == "__main__":
    cola_prioridad = ColaPrioridad()
    cola_prioridad.encolar("Pepe", 4)
    cola_prioridad.encolar("Diego", 2)
    cola_prioridad.encolar("Josefina", 5)
    cola_prioridad.encolar("Luis", 1)
    print(cola_prioridad)
