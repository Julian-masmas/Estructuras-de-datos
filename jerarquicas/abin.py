from random import random
# from nodos import NodoArbol_Bin
if __name__ == "__main__" and __package__ is None:
   from nodos import NodoArbol_Bin
else:
    from jerarquicas.nodos import NodoArbol_Bin
    
class ArbolBin:
    def __init__(self) -> None:
        self.raiz = None

    def adicionar(self, nueva_clave) -> bool:
        self.raiz = self.__adicionar(self.raiz, nueva_clave)

    def __adicionar(self, sub_arbol, nueva_clave):      
        if not sub_arbol:
            sub_arbol = NodoArbol_Bin(nueva_clave)
        elif random() <= 0.5: #adicionar por izquierda
            nodo_izq = self.__adicionar(sub_arbol.izq, nueva_clave)
            sub_arbol.izq = nodo_izq
        else: #adicionar por derecha
            # nodo_der = self.__adicionar(sub_arbol.der, nueva_clave)    
            sub_arbol.der = self.__adicionar(sub_arbol.der, nueva_clave)           
        return sub_arbol
    
    def encontrar(self, clave_encontrar) -> object:
        return self.__encontrar(self.raiz, clave_encontrar)
    
    def __encontrar(self, sub_arbol, clave_encontrar):
        if sub_arbol:
            # print(sub_arbol.clave, "<=>", clave_encontrar)
            # print(("O" if sub_arbol.izq else "X") + " : " +
            # ("O" if sub_arbol.der else "X"))
            if sub_arbol.clave == clave_encontrar:
                return sub_arbol.clave
            else:
                clave_izq = self.__encontrar(sub_arbol.izq, clave_encontrar)
                if clave_izq:
                    return clave_izq
                clave_der = self.__encontrar(sub_arbol.der, clave_encontrar)
                if clave_der:
                    return clave_der   
        return None

    def __len__(self):
        return self.__cantidad_nodos(self.raiz)
    
    def __cantidad_nodos(self, sub_arbol):
        if sub_arbol:
            return (1 + 
                    self.__cantidad_nodos(sub_arbol.izq) +
                    self.__cantidad_nodos(sub_arbol.der)
                    )
        return 0

    def hojas(self): #Retorna la cantidad de hojas
        pass

    def internos(self): #
        pass

    def altura(self): #
        pass

if __name__ == "__main__":
    arbol = ArbolBin()
    arbol.adicionar(4)
    arbol.adicionar(5)
    arbol.adicionar(8)
    print(arbol.encontrar(80))
    print(len(arbol))