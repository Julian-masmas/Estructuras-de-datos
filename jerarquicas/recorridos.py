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
