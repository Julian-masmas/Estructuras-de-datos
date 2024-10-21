    # INTEGRANTES
#---------------------------------------------#
# JULIAN ALEJANDRO FLOREZ MORAN
# ANDRES FELIPE NOGUERA
#---------------------------------------------#
from nodos import NodoPrioridad

class ColaPrioridad:
    """Clase que implementa una Cola con Prioridades en una única cola.
    La prioridad va de 1 (más alta) a 5 (más baja).
    """
    def __init__(self):
        self.__frente = None
        self.__final = None

    def es_vacia(self):
        """Método que verifica si la cola de prioridad está vacía
        Returns
        -------
        bool
        Retorna True si la cola está vacía. False en caso contrario
        """
        return self.__frente is None
        
    def encolar(self, nuevo_dato, prioridad):
        """Método que agrega un nuevo dato a la cola según su prioridad
        Parameters
        ----------
        nuevo_dato : object
        El nuevo dato a ser encolado
        prioridad : int
        Un entero entre 1 y 5 que representa la prioridad (1 es la más alta)
        Returns
        -------
        bool
        True si el nuevo_dato fue encolado correctamente. False si no.
        """
        if prioridad < 1 or prioridad > 6:
            return False  # Prioridad fuera de rango

        nuevo_nodo = NodoPrioridad(nuevo_dato, prioridad)

        # Si la cola está vacía, el nuevo nodo se convierte en el frente
        if self.es_vacia():
            self.__frente = nuevo_nodo
            self.__final = nuevo_nodo
        else:
            # Si el nuevo nodo tiene mayor prioridad que el frente actual
            if nuevo_nodo.prioridad < self.__frente.prioridad:
                nuevo_nodo.sig = self.__frente
                self.__frente = nuevo_nodo
            else:
                # Recorremos la cola hasta encontrar el lugar adecuado para la prioridad
                actual = self.__frente
                while actual.sig and actual.sig.prioridad <= nuevo_nodo.prioridad:
                    actual = actual.sig

                # Insertamos el nodo en la posición correcta
                nuevo_nodo.sig = actual.sig
                actual.sig = nuevo_nodo

                # Si insertamos al final, actualizamos el final de la cola
                if nuevo_nodo.sig is None:
                    self.__final = nuevo_nodo

        return True

    def desencolar(self):
        """Método que elimina el primer nodo de la cola y retorna su dato
        Returns
        -------
        object|None
        El dato del nodo desencolado o None si la cola está vacía
        """
        if self.es_vacia():
            return None
        aux = self.__frente
        self.__frente = aux.sig
        if self.__frente is None:  # Si la cola se vacía
            self.__final = None
        return aux.dato

    def frente(self):
        """Método que retorna el dato del nodo en el frente (con mayor prioridad)
        sin desencolar
        Returns
        -------
        object|None
        El dato del nodo en el frente o None si la cola está vacía
        """
        if self.es_vacia():
            return None
        return self.__frente.dato

    def __len__(self):
        """Método que retorna el número de nodos en la cola
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
        actuales que se encuentran en la cola (sin desencolarlos)
        Returns
        -------
        str
        Una cadena que muestre todos los datos con su prioridad
        """
        resultado = "Cola de Prioridades:\n"
        aux = self.__frente
        if not aux:
            return "Cola vacía"
        while aux:
            resultado += f"({aux.dato}, Prioridad: {aux.prioridad})"
            aux = aux.sig
            if aux:
                resultado += " -> "
        return resultado
