from jerarquicas.abin import  ArbolBin
from jerarquicas.nodos import NodoArbol_Bin
from jerarquicas.excepciones import DuplicatedKeyError, HomogenetyError

class ArbolBinario_Bus(ArbolBin):
    def adicionar(self, nueva_clave) -> bool:
        return self.__adicionar(self.raiz, nueva_clave)
    
    def __adicionar(self, sub_arbol, nueva_clave):
        #Validar homogeneidad raise HomogenetyError(nueva_clave)
        if not sub_arbol:
            sub_arbol = NodoArbol_Bin(nueva_clave)
        elif  nueva_clave < sub_arbol.clave:
            sub_arbol.izq = self.__adicionar(sub_arbol.izq, nueva_clave)
        elif  nueva_clave > sub_arbol.clave:
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
        """Metodo que retorna la clave mas pequeña del arbol
        """
        pass
    def encontrar_maximo(self):
        """Metodo que retorna la clave mas grande del arbol
        """
        pass
    def remover(self, clave_remover, mayor=True):
        """Elimina el nodo donde se encuentra la clave sin eliminar los posibles
        hijos que este tenga.

        Parameters
        ----------
        clave_remover : _type_
            Clave a eliminar del árbol
        mayor : bool, optional
            Si es True, reemplaza con el hijo mayor de los menores.
            Si es False, reemplaza con el hijo menor de los mayores, by default True.
        """
        self.raiz = self.__remover(self.raiz, clave_remover, mayor)
    
    def __remover(self, sub_arbol, clave_remover, mayor):
        if not sub_arbol:
            return sub_arbol

        if clave_remover < sub_arbol.clave:
            sub_arbol.izq = self.__remover(sub_arbol.izq, clave_remover, mayor)
        elif clave_remover > sub_arbol.clave:
            sub_arbol.der = self.__remover(sub_arbol.der, clave_remover, mayor)
        else:
            # Nodo con solo un hijo o sin hijos
            if not sub_arbol.izq:
                return sub_arbol.der
            elif not sub_arbol.der:
                return sub_arbol.izq

            # Nodo con dos hijos: obtenemos el sucesor (menor de los mayores) o el predecesor
            if mayor:
                temp = self.__encontrar_max(sub_arbol.izq)  # predecesor
                sub_arbol.clave = temp.clave
                sub_arbol.izq = self.__remover(sub_arbol.izq, temp.clave, mayor)
            else:
                temp = self.__encontrar_min(sub_arbol.der)  # sucesor
                sub_arbol.clave = temp.clave
                sub_arbol.der = self.__remover(sub_arbol.der, temp.clave, mayor)

        return sub_arbol

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
