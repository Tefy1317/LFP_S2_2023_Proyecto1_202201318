import os 
os.system('cls')
from Datos.exAritmeticas import *
from Datos.exTrigonometricas import *
from grafica import*
from collections import namedtuple
import json
import tkinter as tk
from os import remove

Token = namedtuple("Token", ["valor", "linea", "columna"])

linea = 1
columna = 1

tokens=[]

configuracion = {
    "texto": None,
    "fondo": None,
    "fuente": None,
    "forma": None,
}
errores = [] 
erroresSinRepetir = []
estructuraJson = []

def reconocerString(strInicial, digito):
    token = ""
    for caracter in strInicial: 
        if caracter == '"':
            return [token, digito]
        token += caracter
        digito += 1
    print("Error: string no cerrado")

def reconocerNumero(strInicial, digito):
    token = ""
    dec = False
    for caracter in strInicial:
        if caracter.isdigit(): 
            token += caracter
            digito +=1
        elif caracter == "." and not dec:
            token += caracter
            digito += 1
            dec = True 
        else: 
            break
    if dec: 
        return [float(token), digito]
    return [int(token), digito]

def crearTokens(strInicial):
    estructuraJson.clear()
    erroresSinRepetir.clear()
    errores.clear()
    global linea, columna, tokens
    digito = 0 
    contadorErrores = 0 
    while digito <len(strInicial):
        caracter = strInicial[digito]
        if caracter.isspace():
            if caracter == "\n":
                linea +=1
                columna = 1
            elif caracter == "\t":
                columna +=4
            else: 
                columna +=1
            digito +=1
        elif caracter == '"': 
            str, posicion = reconocerString(strInicial[digito+1:], digito)
            columna += len(str) + 1
            digito = posicion + 2
            token = Token(str, linea, columna)
            tokens.append(token)
        elif caracter in ["{", "}", "[", "]", ",", ":"]:
            columna += 1
            digito += 1
            token = Token(caracter, linea, columna)
            tokens.append(token)
        elif caracter.isdigit():
            num, posicion = reconocerNumero(strInicial[digito:], digito)
            columna += posicion - digito
            digito = posicion
            token = Token(num, linea, columna)
            tokens.append(token)
        else: 
            contadorErrores +=1
            print("Caracter no reconocido: ", caracter," en línea: ",linea," columna: ",columna)
            errorInfo = {
                "lexema": caracter,
                "tipo": "error lexico",
                "fila": linea,
                "columna": columna
            }

            errores.append(errorInfo) 

            digito +=1
            columna += 1

    for elemento in errores:
        if elemento not in erroresSinRepetir:
            erroresSinRepetir.append(elemento)

    for i, error in enumerate(erroresSinRepetir, start=1):
        estructuraJson.append({
            "No": i,
            "descripcion": error
    })
    linea = 1
    columna = 1
         

def encontrarInstruction():
    global tokens
    operacion = None
    valor1 = None
    valor2 = None
    while tokens:
        token = tokens.pop(0)
        print("Valor: ", token)
        if token.valor == "operacion":
            tokens.pop(0)
            operacion = tokens.pop(0).valor
        elif token.valor == "valor1":
            tokens.pop(0)
            valor1 = tokens.pop(0).valor
            if valor1 == "[":
                valor1 = encontrarInstruction()
        elif token.valor == "valor2":
            tokens.pop(0)
            valor2 = tokens.pop(0).valor
            if valor2 == "[":
                valor2 = encontrarInstruction()
        elif token.valor in ["texto", "fondo", "fuente", "forma"]:
            tokens.pop(0)
            configuracion[token.valor] = tokens.pop(0).valor
        else:
            pass
    
        if operacion and valor1 and valor2:
            return expresionAritmetica(operacion, valor1, valor2, 0, 0)
        if operacion and operacion in ["seno", "coseno", "inverso", "tangente"] and valor1:
            return expresionTrigonometrica(operacion, valor1, 0, 0)
    return None

def mostrarInstrucciones():
    global tokens 
    global arbol
    instrucciones = []

    while tokens: 
        instruccion = encontrarInstruction() 
        if instruccion: 
            instrucciones.append(instruccion)
    arbol.agregarConfiguracion(configuracion)
    return instrucciones


def analizar(entrada): 
    arbol.dot.clear()
    crearTokens(entrada)
    arbol.agregarConfiguracion(configuracion)
    instrucciones = mostrarInstrucciones()
    for i in instrucciones:
        print("RESULTADO INSTRUCCION: ", i.interpreteExpresiones())
    return arbol

def archivoErrores():
    try:
        remove("RESULTADOS_202201318.json")
    except FileNotFoundError:
        print(" ")

    with open("RESULTADOS_202201318.json", "w") as archivo_json:
        json.dump(estructuraJson, archivo_json, indent=4)
    archivo_json.close()
    
    ventanaNueva = tk.Tk()
    ventanaNueva.title(f"Errores JSON - {'RESULTADOS_202201318.json'}")
    ventanaNueva.geometry("500x500")
    ventanaNueva.configure(bg="#ffcccc")

    with open("RESULTADOS_202201318.json", "r") as archivo_json:
        datos_json = json.load(archivo_json)

    texto_json = json.dumps(datos_json, indent=4)
    resultado_text = tk.Text(
        ventanaNueva,
        bg="#ffcccc",  
        fg="#ff1493",  
        insertbackground="#ff1493",  
        selectbackground="#ff69b4",  
        width=120,
        height=25,
        font=("Courier New", 13),
    )
    resultado_text.insert("1.0", texto_json)
    resultado_text.pack(fill="both", expand=True)

