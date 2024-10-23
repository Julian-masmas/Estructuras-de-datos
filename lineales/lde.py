from nodos import Nodo_listaDE

class Lista_DE:
    def __init__(self) -> None:
        """Constructor de la lista doble
        """
        self.__cab = None
        self.__actual = None
        self.__inverso = False

    @property
    def inverso(self) -> bool:
        """Propiedad de la lista, activada la lista se recorre de revés 

        Returns
        -------
        bool
            _description_
        """
        return self.__inverso()
    
    @inverso.setter
    def inverso(self, valor: bool = False):
        self.__inverso = valor

    def __len__(self):
        """Método que calcula el tamaño de la lista.

        Returns
        -------
        int
            El número de nodos que tiene la lista.
        """        
        actual = self.__cab
        tamano = 0
        if self.es_vacia():
            return False
        else:
            while actual:
                actual = actual.sig
                tamano += 1
            return tamano

    def __iter__(self):
        """metodo que permite iterar sobre las listas

        Yields
        ------
        _type_
            _description_
        """
        actual = self.__cab
        while actual:
            yield actual
            actual = actual.sig

    def __str__(self) -> str:
        if self.es_vacia():
            return ""
        actual = self.__cab
        resultado = ""
        while actual is not None:
            if resultado:
                resultado += " <=> "
            resultado += f"({actual.dato})"
            actual = actual.sig
        return resultado

    def es_vacia(self):
        """Metodo que comprueba si una lista esta vacia

        Returns:
            Bool: True cuando la lista está vacia
        """
        if self.__cab is None:
            return True
        else:
            return False

    def adicionar(self, dato):
        nodo = Nodo_listaDE(dato)
        if self.es_vacia():
            self.__cab = nodo
        else:
            actual = self.__cab
            if type(actual.dato) == type(nodo.dato): #Comprueba que sean del mismo tipo de dato
                while actual.sig:
                    actual = actual.sig
                actual.sig = nodo
                nodo.ant = actual
                return True
            else:
                return False

    def posicionar(self, dato, pos):
        if self.es_vacia():
            self.__cab = Nodo_listaDE(dato)
        elif pos == 0:
            if type(dato) == type(self.__cab.dato):
                nodo = Nodo_listaDE(dato) 
                actual = self.__cab
                self.__cab = nodo
                nodo.sig = actual
                actual.ant = nodo
                return True
        else:
            if type(dato) == type(self.__cab.dato):
                nodo = Nodo_listaDE(dato)
                actual = self.__cab
                anterior = None
                cont = 0
                while cont != pos:
                    anterior = actual
                    actual = actual.sig
                    cont += 1
                anterior.sig = nodo
                nodo.ant = anterior
                nodo.sig = actual
                actual.ant = nodo
                return True
            else:
                return False
            
    def remover(self, dato, por_pos=True):
        """metodo que elimina de la lista un elemento

        Args:
            dato (object|int): el objeto a eliminar o la posicion del objeto a eliminar
            por_pos (bool, optional): _description_. Defaults to True.

        Returns:
            bool: True|False dependiendo si se pudo eliminar
        """
        if por_pos:
            return self.__remover_pos(dato)
        else:
            return self.__remover_dato(dato)
        
    def __remover_dato(self, dato):
        if self.es_vacia():
            return False
        elif self.__cab.dato == dato:
            self.__cab = self.__cab.sig
            if self.__cab:
                self.__cab.ant = None
            return True
        else:
            actual = self.__cab
            while actual:
                if actual.dato == dato:
                    actual.ant.sig = actual.sig
                    if actual.sig:
                        actual.sig.ant = actual.ant
                    return True
                actual = actual.sig
            return False
    
    def __remover_pos(self, pos):
        if self.es_vacia():
            return False
        elif pos > len(self):
            return False
        elif pos == 0:
            self.__cab = self.__cab.sig
            if self.__cab:
                self.__cab.ant = None
            return True
        actual = self.__cab
        anterior = None
        cont = 0
        while cont!= pos and actual.sig:
            anterior = actual
            actual = actual.sig
            cont += 1
        if not actual.sig:
            anterior.sig = None
            return True
        else:
            anterior.sig = actual.sig
            actual.sig.ant = anterior
            return True
        
    def encontrar(self, dato_buscar):
        if self.es_vacia():
            return None
        actual = self.__cab
        while actual.sig:
            if actual.dato == dato_buscar:
                return actual
            actual = actual.sig
        return None
    
    def ubicar(self, pos):
        if self.es_vacia() or pos > len(self):
            return None
        actual = self.__cab
        cont = 0
        while cont!= pos and actual.sig:
            actual = actual.sig
            cont += 1
        if not actual.sig:
            return None
        else:
            return actual.dato
        
    def adelante(self):
        if self.es_vacia():
            return None
        if self.__actual is None:
            self.__actual = self.__cab  # Inicia en la cabeza si no hay nodo actual

        if self.inverso:  # Si estamos en modo inverso, nos movemos hacia atrás
            if self.__actual.ant:
                self.__actual = self.__actual.ant
                return self.__actual
            else:
                return None
        else:  # Si estamos en modo normal, nos movemos hacia adelante
            if self.__actual.sig:
                self.__actual = self.__actual.sig
                return self.__actual
            else:
                return None

    def atras(self):
        if self.es_vacia():
            return None
        if self.__actual is None:
            self.__actual = self.__cab  # Inicia en la cabeza si no hay nodo actual

        if self.inverso:  # Si estamos en modo inverso, nos movemos hacia adelante
            if self.__actual.sig:
                self.__actual = self.__actual.sig
                return self.__actual
            else:
                return None
        else:  # Si estamos en modo normal, nos movemos hacia atrás
            if self.__actual.ant:
                self.__actual = self.__actual.ant
                return self.__actual
            else:
                return None
    
