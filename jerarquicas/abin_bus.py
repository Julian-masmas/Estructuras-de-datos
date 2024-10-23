from re import sub
from jerarquicas.abin import  ArbolBin
from jerarquicas.nodos import NodoArbol_Bin
from jerarquicas.excepciones import DuplicatedKeyError, HomogenetyError

class ArbolBinario_Bus(ArbolBin):
    def adicionar(self, nueva_clave) -> bool:
        self.raiz = self.__adicionar(self.raiz, nueva_clave)
        return True
    
    def __adicionar(self, sub_arbol, nueva_clave):
        # Validar homogeneidad (implementa tu lógica de validación aquí)
        if not sub_arbol:
            return NodoArbol_Bin(nueva_clave)
        elif nueva_clave < sub_arbol.clave:
            sub_arbol.izq = self.__adicionar(sub_arbol.izq, nueva_clave)
        elif nueva_clave > sub_arbol.clave:
            sub_arbol.der = self.__adicionar(sub_arbol.der, nueva_clave)
        else:
            raise DuplicatedKeyError(nueva_clave)
        
        return sub_arbol

    
    def encontrar(self, clave_encontrar) -> object:
        return self.__encontrar(self.raiz, clave_encontrar)
    
    def __encontrar(self, sub_arbol, clave_encontrar):
        if sub_arbol:
            if clave_encontrar == sub_arbol.clave:
                return sub_arbol.clave
            elif clave_encontrar < sub_arbol.clave: #<-🔍
                return self.__encontrar(sub_arbol.izq, clave_encontrar)
            else:
                return self.__encontrar(sub_arbol.der, clave_encontrar)
        return None
    
    def encontrar_minimo(self):
        return self.__minimo(self.raiz)

    def __minimo(self, sub_arbol):
        if sub_arbol:
            if sub_arbol.izq or sub_arbol.der:
                if sub_arbol.izq.clave < sub_arbol.clave:
                    return self.__minimo(sub_arbol.izq)
                return sub_arbol
            return sub_arbol
        return sub_arbol

    def encontrar_maximo(self):
        """Metodo que retorna la clave mas grande del arbol
        """
        return self.__maximo(self.raiz)

    def __maximo(self, sub_arbol):
        if sub_arbol:
            if sub_arbol.izq or sub_arbol.der:
                if sub_arbol.der.clave > sub_arbol.clave:
                    return self.__maximo(sub_arbol.der)
                return sub_arbol
            return sub_arbol
        return sub_arbol

    def remover(self, clave_remover, mayor=True):
        """Elimina el nodo donde se encuentra la clave sin eliminar los posibles
            hijos que este tenga.


        Parameters
        ----------
        clave_remover : _type_
            _description_
        mayor : bool, optional
            Cuando es True se elimina el nodo correspondiente y se deja
            como reemplazo el hijo MAYOR de los menores.
            Cuando es False se elimina el nodo y se deja como reemplazo
            el hijo MENOR de los mayores, by default True
        """
        pass

def pre_orden(arbol_bin):
    __pre_orden(arbol_bin.raiz)

def __pre_orden(sub_arbol):
    if sub_arbol:
        print(sub_arbol.clave)
        __pre_orden(sub_arbol.izq)
        __pre_orden(sub_arbol.der)
        return sub_arbol
def post_orden(arbol_bin):
    __post_orden(arbol_bin.raiz)

def __post_orden(sub_arbol):
    if sub_arbol:
        __pre_orden(sub_arbol.izq)
        __pre_orden(sub_arbol.der)
        print(sub_arbol.clave)
        return sub_arbol
    
def str_pre_orden(sub_arbol, sep="|"):
    pass
