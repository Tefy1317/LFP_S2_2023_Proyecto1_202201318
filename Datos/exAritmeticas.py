from Datos.expresion import *
from grafica import *
import math

class expresionAritmetica(Expresion):
    def __init__(self, tipoExpresion, valor1, valor2, linea, columna):
        self.tipo = tipoExpresion
        self.valor1 = valor1
        self.valor2 = valor2
        self.linea = linea
        self.columna = columna

    def interpreteExpresiones(self):
        global arbol

        valor1 = self.valor1
        valor2 = self.valor2

        nodo1 = None
        nodo2 = None

        if isinstance(self.valor1, Expresion):
            valor1 = self.valor1.interpreteExpresiones()
            nodo1 = arbol.obtenerUltimoNodo()
            print("RESULTADO: ", valor1)
        else:
            valor1 = self.valor1
            nodo1 = arbol.agregarNodo(str(valor1))
        if isinstance(self.valor2, Expresion):
            valor2 = self.valor2.interpreteExpresiones()
            nodo2 = arbol.obtenerUltimoNodo()
            print("RESULTADO: ", valor2)
        else:
            valor2 = self.valor2
            nodo2 = arbol.agregarNodo(str(valor2))

        print("OPERACIÓN: ", self.tipo)

        print("-" * 20)
        print("tipo: ", self.tipo)
        print("valor1: ", valor1)
        print("valor2: ", valor2)

        resultado = None
        if self.tipo == "suma":
            resultado = valor1 + valor2
        elif self.tipo == "resta":
            resultado = valor1 - valor2
        elif self.tipo == "multiplicacion":
            resultado = valor1 * valor2
        elif self.tipo == "division":
            resultado = valor1 / valor2
        elif self.tipo == "potencia":
            resultado = math.pow(valor1, valor2)
        elif self.tipo == "raiz":
            resultado = math.pow(valor1, 1 / valor2)
        elif self.tipo == "mod":
            resultado = valor1 % valor2


        if arbol == None:
            print("arbol vacío")

        raiz = arbol.agregarNodo(f"{self.tipo}\\n{str(round(resultado))}")
        arbol.agregarArista(raiz, nodo1)
        if self.valor2 != None:
            arbol.agregarArista(raiz, nodo2)

        return round(resultado,2)

 