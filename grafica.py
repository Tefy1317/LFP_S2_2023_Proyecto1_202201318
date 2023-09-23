import graphviz
import time


class Arbol:
    def __init__(self):
        timestr = time.strftime("%Y%m%d-%H%M%S")
        self.dot = graphviz.Digraph(comment=f"Graph {timestr}")
        self.contador = 0

    def agregarConfiguracion(self, configuracion):
        self.dot.attr(
            'node',
            style="filled",
            fillcolor=configuracion["fondo"],
            fontcolor=configuracion["fuente"],
            shape=configuracion["forma"],
        )
        self.dot.attr(label=configuracion["texto"])

    def agregarNodo(self, valor):
        nombre = f"nodo{self.contador}"
        self.dot.node(nombre, valor)
        self.contador += 1
        return nombre

    def agregarArista(self, nodo1: str, nodo2: str):
        self.dot.edge(nodo1, nodo2)

    def generarGrafica(self):
        self.dot.render("Graficas/Arbol", view=True)
        self.dot.save("Graficas/Arbol.dot")

    def obtenerUltimoNodo(self):
        return f"nodo{self.contador - 1}"

arbol = Arbol()