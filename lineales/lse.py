    # INTEGRANTES
#---------------------------------------------#
# JULIAN ALEJANDRO FLOREZ MORAN
# ANDRES FELIPE NOGUERA
#---------------------------------------------#
from nodos import Nodo_listaSE
if __name__ == "__main__" and __package__ is None:
    from nodos import Nodo_listaSE
# else:
#      from bed.lineales.nodos import Nodo_listaSE

class Lista_SE:
    """Metodo constructor de una lista simplemente enlazada 
    """
    def __init__(self):
        self.__cab = None # Atributo cabecera (oculto)

    

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
        """metodo que adiciona un elemento al final de la lista 
        comprobando que sean datos del mismo tipo

        Args:
            dato (object): dato a adicionar en la lista    

        Returns:
            bool: T/F dependiendo de si se pudo agregar a la lista
        """
        if self.es_vacia():
            self.__cab = Nodo_listaSE(dato)
        else:
            nodo = Nodo_listaSE(dato)
            actual = self.__cab
            if type(actual.dato) == type(nodo.dato):
                while actual.sig:
                    actual = actual.sig
                actual.sig = nodo
                return True
            return False

    def posicionar(self, nuevo_dato, pos):
        """Método que inserta un nuevo nodo en cualquier posición de la
        lista. Si la lista está vacía la única posición válida será
        cero. Si la lista ya contiene datos, serán válidas posiciones
        intermedias o la posición inmediatemente superior a la del último dato.

        Parameters
        ----------
        nuevo_dato : object
            El nuevo dato a ser añadido a la lista.
        pos : int, optional
            Posición a insertar en la lista, por defecto 0.

        Returns
        -------
        bool
            True cuando el dato es insertado en la lista. False en caso
            contrario.
        """
        if type(self.__cab.dato) == type(nuevo_dato):
            if pos > len(self):
                return False
            elif self.es_vacia() or pos == 0:
                self.adicionar(nuevo_dato)
                return True
            else:
                nuevo_nodo = Nodo_listaSE(nuevo_dato)
                actual = self.__cab
                cont = 0
                dif = cont - pos
                while cont != pos:
                    if dif == -1:
                        anterior = actual
                    actual = actual.sig
                    cont += 1
                    dif += 1
                if actual is None:
                    self.adicionar(nuevo_dato)
                    return True
                else:
                    anterior.sig = nuevo_nodo
                    nuevo_nodo.sig = actual
                    return True
        else:
            return False
    
    def recorrer(self):
        """Recorre la lista imprimiendo todos los datos, excepto cuando la lista es vacia
        """
        if self.es_vacia():
            print("La lista está vacía")
        else:
            actual = self.__cab
            while actual:
                print(actual)
                actual = actual.sig
                
    def encontrar(self, dato_encontrar):
        """metodo que busca un dato dado en la lista

        Parameters
        ----------
        dato_encontrar : object
            dato a encontrar

        Returns
        -------
        object  
            dato encontrado
        None
            no encuentra dato
        """
        if self.es_vacia():
            return False
        else:
            actual = self.__cab
            while actual:
                if actual.dato == dato_encontrar:
                    return actual.dato
                actual = actual.sig

    def ubicar(self, pos):
        """Método que realiza la búsqueda de un dato en la lista dependiendo
        de la posición ingresada.

        Parameters
        ----------
        pos : int
            Corresponde a la posición en la lista a ubicar el dato.

        Returns
        -------
        object|None
            object si el dato es ubicado en la lista, None en caso contrario.
        """
        if self.es_vacia():
            return False
        else:
            actual = self.__cab
            cont = 0
            while cont < pos:
                actual = actual.sig
                cont += 1
            return actual
                
    def remover(self, item, por_pos=True):
        """Método que permite remover un nodo de la lista ya sea por una
        posición o por el dato correspondiente. Si es por dato, deberá
        remover cada uno de los nodos que contenga dicho dato.

        Parameters
        ----------
        item : object|int
            Puede corresponder al valor del dato a ser removido de la lista
            o a la posición en la lista a remover el dato.
            En el caso de remover por dato, se buscará todas las coincidencias
            del dato a eliminar en la lista y serán quitadas.
        por_pos : bool, optional
            Si es True, el método intentará remover un dato por su posición,
            de lo contrario se intentará hacerlo por su valor, por defecto True.

        Returns
        -------
        bool
            True cuando el dato es removido de la lista. False en caso
            contrario.
        """
        if por_pos:
            return self.__remover_pos(item)
        else:
            # CONSULTA: remover por dato
            return self.__remover_dato(item)
    
    def __remover_pos(self, pos_elm):
        actual = self.__cab
        cont = 0
        dif = cont - pos_elm
        if pos_elm > 0:
            while cont != pos_elm:
                if dif == -1:
                    anterior = actual   
                actual = actual.sig
                cont += 1
                dif += 1
            anterior.sig = actual.sig
            return True 
        elif pos_elm == 0 and actual:
            self.__cab = actual.sig
            return True
        elif pos_elm > len(self):
            return False

    def __remover_dato(self, dato_elem):
        if self.es_vacia():
            return False
        actual = self.__cab
        anterior = None
        encontrado = False
        while actual is not None:
            if actual.dato == dato_elem:
                encontrado = True
                if actual == self.__cab:
                    self.__cab = actual.sig
                    actual = self.__cab  # Avanza al siguiente nodo
                else:
                    anterior.sig = actual.sig
                    actual = actual.sig  # Avanza al siguiente nodo
            else:
                anterior = actual
                actual = actual.sig  # Avanza al siguiente nodo
        return encontrado

    def __str__(self):
        """Método que devuelve una cadena con los datos de la lista, o una
        cadena vacía en el caso de que la lista sea vacía.

        Returns
        -------
        str
            Si la lista no es vacía retornará una cadena en el formato:
                "(dato_0) :>: (dato_1) :>: (dato_2) :>: ... :>: (dato_n)"
                "(7) :>: (8) :>: (5) :>: (5) :>: (9)"
            De lo contrario retornará una cadena vacía: ""
        """
        if self.es_vacia():
            return ""
        actual = self.__cab
        resultado = ""
        while actual is not None:
            if resultado:
                resultado += " :>: "
            resultado += f"({actual.dato})"
            actual = actual.sig
        return resultado
