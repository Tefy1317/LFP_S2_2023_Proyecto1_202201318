from Datos.expresion import *
import math 
from grafica import * 

class expresionTrigonometrica(Expresion):
    def __init__(self, tipoExpresion, valor1, linea, columna):
        self.tipo = tipoExpresion
        self.valor1 = valor1
        self.linea = linea
        self.columna = columna

    def interpreteExpresiones(self): 
        valor = self.valor1

        nodo = None

        if isinstance(self.valor1, Expresion):
            valor = self.valor1.interpreteExpresiones()
            nodo = arbol.obtenerUltimoNodo()
        else:
            valor = self.valor1
            nodo = arbol.agregarNodo(str(valor))

        print("-" * 20)
        print("tipo: ", self.tipo)
        print("valor: ", valor)
        resultado = None
        if self.tipo == "seno":
            resultado = math.sin(valor)
        elif self.tipo == "coseno":
            resultado = math.cos(valor)
        elif self.tipo == "tangente":
            resultado = math.tan(valor)
        elif self.tipo == "inverso":
            resultado = 1/valor
            
        
        raiz = arbol.agregarNodo(f"{self.tipo}\\n{str(round(resultado,2))}")
        arbol.agregarArista(raiz, nodo)

        return round(resultado, 2)