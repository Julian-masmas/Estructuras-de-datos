    # INTEGRANTES
#---------------------------------------------#
# JULIAN ALEJANDRO FLOREZ MORAN
# ANDRES FELIPE NOGUERA
#---------------------------------------------#
import re
from pila import Pila
from lse import Lista_SE
class Prefija:

    prioridad_expresion = {"+":1, "-":1, "*":2, "/":2, "^":3, ")":5, "(":-1 }
    prioridad_pila = {"+":1, "-":1, "*":2, "/":2, "^":4, ")":0, "(":-1 }

    def __init__(self, expresion_infija:str) -> None:
        self.expresion_infija = re.sub(r'([+\-*/()])', r' \1 ', expresion_infija)

    def infija(self):
        return str(re.sub(r'\s+', ' ', self.expresion_infija)).strip()
        
    def prefija(self):
        pila_exp = Pila()  # pila para la expresión invertida
        pila_operadores = Pila()  #pila para operadores
        resultado = Lista_SE()  #lista para la expresión prefija
        expresion_invertida = []
        partes = self.infija().split()  
        for parte in reversed(partes):
            if parte == '(':
                expresion_invertida.append(')')
            elif parte == ')':
                expresion_invertida.append('(')
            else:
                expresion_invertida.append(parte)
        for parte in expresion_invertida:
            if parte == ' ':  
                continue
            if parte.isdigit():  
                resultado.adicionar(parte)
            elif parte == '(':  
                pila_operadores.apilar(parte)
            elif parte == ')':  
                while not pila_operadores.es_vacia() and pila_operadores.cima() != '(':
                    resultado.adicionar(pila_operadores.desapilar())
                pila_operadores.desapilar() 
            else:  #si es un operador
                while (not pila_operadores.es_vacia() and
                       self.prioridad_expresion[parte] < self.prioridad_pila[pila_operadores.cima()]):
                    resultado.adicionar(pila_operadores.desapilar())
                pila_operadores.apilar(parte)

        while not pila_operadores.es_vacia():
            resultado.adicionar(pila_operadores.desapilar())

        prefija_resultado = ' '.join(reversed([nodo.dato for nodo in resultado]))
        return prefija_resultado

    def eval_expr_aritm(self):
            partes = self.prefija().split()
            pila = Pila()
            for parte in reversed(partes):
                if parte.isdigit():  
                    pila.apilar(int(parte))
                else: 
                    numero1 = pila.desapilar()
                    numero2 = pila.desapilar()
                    if parte == '+':
                        resultado = numero1 + numero2
                    elif parte == '-':
                        resultado = numero1 - numero2
                    elif parte == '*':
                        resultado = numero1 * numero2
                    elif parte == '/':
                        resultado = numero1 / numero2
                    elif parte == '^':
                        resultado = numero1 ** numero2
                    pila.apilar(resultado)
            return pila.desapilar()
