from nodos import Nodo_pila

class Pila:
    """Clase que implementa el funcionamiento del TAD Pila
    """
    def __init__(self):
        self.__top = None
        

    def es_vacia(self):
        """Método que verifica si la pila se encuentra vacía
        Returns
        -------
        bool
        Retorna True si la pila es vacia. False en caso contrario
        """
        if not self.__top:
            return True
        else:
            return False
        
    def apilar(self, nuevo_dato):
        """Método que realiza la entrada de un nuevo dato a la pila.
        Realizar la validación de Homogeneidad para cada dato ingresado
        a la pila
        Parameters
        ----------
        nuevo_dato : object
        El nuevo dato a ser adicionado a la pila
        Returns
        -------
        bool
        True si nuevo_dato fue apilado. False en caso contrario
        """
        if not self.__top:
            self.__top = Nodo_pila(nuevo_dato)
            return True
        else:
            aux = self.__top
            if type(aux.dato) == type(nuevo_dato):
                nodo = Nodo_pila(nuevo_dato)
                self.__top = nodo
                nodo.sig = aux
                return True
            else:
                return False

    def desapilar(self):
        """Método que saca/quita el último nodo (elimina el nodo) de la pila
        y retorna su dato
        Returns
        -------
        object|None
        El dato del nodo desapilado y None cuando la pila no contenga
        nodos/datos
        """
        if self.__top:
            aux = self.__top
            self.__top = aux.sig
            return aux.dato

    def cima(self):
        """Método que retorna el dato del último nodo ingresado en la pila,
        sin quitarlo de la misma
        Returns
        -------
        object|None
        El dato del último nodo ingresado y None cuando la pila no
        contenga nodos/datos
        """
        if self.__top:
            aux = self.__top    
            return aux.dato

    def __len__(self):
        """Método que retorna el número de nodos que contiene la pila
        Returns
        -------
        int
        Tamaño de la pila
        """
        aux = self.__top
        cont = 0
        while aux:
            cont += 1
            aux = aux.sig
        return cont

    def __str__(self):
        """Método especial encargado de retornar una cadena con los datos
        actuales que se encuentran en la pila (sin desapilarlos)
        Returns
        -------
        str
        Una cadena que muestre todos los datos que actualmente almacena
        la pila, en el siguiente formato:
        “===(c)===
        (*[dato_n]*)
        ::
        (dato )₃
        ::
        (dato )₂
        ::
        (dato )” ₁
        Cuando hay un sólo dato:
        “===(c)===
        (*[dato_n]*)”
        Cuando no hay datos:
        “===(c)===”
        """
        resultado = "===(c)==="
        x = 0
        aux = self.__top
        if not aux:
            return resultado
        while x < len(self):
            resultado += f"\n({aux.dato})"
            if not aux.sig:
                return resultado
            else:
                resultado += "\n::"
            aux = aux.sig
            x += 1
        return resultado
        




