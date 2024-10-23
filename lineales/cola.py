from nodos import Nodo_cola

class Cola:
    """Clase que implementa el funcionamiento del TAD Cola
    """
    def __init__(self):
        self.__frente = None
        self.__final = None  # Atributo para controlar la homogeneidad
        
    def es_vacia(self):
        """Método que verifica si la cola se encuentra vacía
        Returns
        -------
        bool
        Retorna True si la cola es vacía. False en caso contrario
        """
        return self.__frente is None
        
    def encolar(self, nuevo_dato):
        """Método que realiza la entrada de un nuevo dato a la cola.
        Realiza la validación de Homogeneidad para cada dato ingresado
        Parameters
        ----------
        nuevo_dato : object
        El nuevo dato a ser adicionado a la cola
        Returns
        -------
        bool
        True si el nuevo_dato fue encolado. False en caso contrario
        """
        nuevo_nodo = Nodo_cola(nuevo_dato)
        if self.es_vacia():
            self.__frente = nuevo_nodo
            self.__final = nuevo_nodo
            return True
        else:
            if type(self.__frente.dato) == type(nuevo_dato):
                self.__final.sig = nuevo_nodo
                self.__final = nuevo_nodo
                return True
            else:
                return False

    def desencolar(self):
        """Método que quita el primer nodo de la cola y retorna su dato
        Returns
        -------
        object|None
        El dato del nodo desencolado o None si la cola está vacía
        """
        if not self.es_vacia():
            aux = self.__frente
            self.__frente = aux.sig
            if self.__frente is None:  # Si la cola se queda vacía
                self.__final = None
            return aux.dato

    def frente(self):
        """Método que retorna el dato del primer nodo ingresado en la cola,
        sin quitarlo de la misma
        Returns
        -------
        object|None
        El dato del primer nodo ingresado o None si la cola está vacía
        """
        if not self.es_vacia():
            return self.__frente.dato

    def __len__(self):
        """Método que retorna el número de nodos que contiene la cola
        Returns
        -------
        int
        Tamaño de la cola
        """
        aux = self.__frente
        cont = 0
        while aux:
            cont += 1
            aux = aux.sig
        return cont

    def __str__(self):
        """Método especial encargado de retornar una cadena con los datos
        actuales que se encuentran en la cola
        Returns
        -------
        str
        Una cadena que muestre todos los datos que actualmente almacena
        la cola, en el siguiente formato:
        “@|<-{dato₁ }<-[dato₂ ]<-[dato₃ ]<-[dato_n]”   
        Cuando hay un sólo dato:
        “@|<-{dato₁}”
        Cuando no hay datos:
        “@|”
        """
        if self.es_vacia():
            return "@|"
        
        resultado = "@|<-"
        aux = self.__frente
        while aux:
            resultado += f"{{{aux.dato}}}"
            if aux.sig:
                resultado += "<-"
            aux = aux.sig
        return resultado
