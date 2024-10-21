from jerarquicas.nodos import NodoArbol_Bin_Obj
if __name__ == "__main__" and __package__ is None:
   from nodos import NodoArbol_Bin_Obj
else:
    from jerarquicas.nodos import NodoArbol_Bin_Obj
class ArbolBinObj:
    def __init__(self) -> None:
        self.raiz = None

    def adicionar(self, nueva_clave, valor):
        return self.__adicionar(self.raiz, nueva_clave, valor)

    def __adicionar(self, sub_arbol, nueva_clave, valor):
        if not sub_arbol:
            sub_arbol = NodoArbol_Bin_Obj(nueva_clave, valor)
        elif valor < sub_arbol.orden:
            sub_arbol.izq = self.__adicionar(sub_arbol.izq, nueva_clave, valor)
        else:
            sub_arbol.der = self.__adicionar(sub_arbol.der, nueva_clave, valor)
        return sub_arbol

    def encontrar(self, clave_encontrar) -> object:
        return self.__encontrar(self.raiz, clave_encontrar)
    
    def __encontrar(self, sub_arbol, clave_encontrar):
        if sub_arbol:
            print(sub_arbol.clave, "<=>", clave_encontrar)
            print(("O" if sub_arbol.izq else "X") + " : " +
            ("O" if sub_arbol.der else "X"))
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

