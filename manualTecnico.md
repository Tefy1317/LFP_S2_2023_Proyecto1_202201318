# Manual Técnico - Proyecto 1
Universidad de San Carlos de Guatemala  
Lenguajes Formales y de Programación A+  
Estephanie Alejandra Ruiz Perez  
202201318  

## Introducción: 
El sistema esta diseñado con el objetivo de reconocer un lenguaje por medio de un analizador léxico. Por lo tanto, cuenta con diversas opciones que satisfacen las necesidades básicas para poder leer archivos con formato JSON, identificar errores y ejecutar instrucciones válidas para el lenguaje. Cuenta con una opción donde se pueden abrir y guardar archivos. Además, cuenta con una opción para analizar este archivo cargado. Finalmente, genera reportes que son representados por gráficas según las instrucciones del archivo.
## Requisitos del sistema
### Ejecución del sistema
Para la ejecución del sistema se requieren los siguientes elementos:
* Versión de python: Python 3.11.4
* Computadora
* Procesador mínimo: Core i5
* Memoria RAM: 8.00 GB
* Terminal para ejecutar el programa

### Desarrollo  del sistema
Para el desarrollo del sistema se requieren los siguientes elementos:
* IDE: Visual Studio Code
* Versión de python: Python 3.11.4
* Procesador mínimo: Core i5
* Memoria RAM: 8.00 GB

## Arquitectura del programa
### Diagrama de clases

![Diagrama de Clases](https://i.ibb.co/TvXKjgY/diagrama-Proyecto1-LFP.jpg)

### Estructura de archivos
Los archivos del programa son los siguientes:

![Estructura de archivos](https://i.ibb.co/VSgfQgh/estructura.jpg)

## Tecnologías y herramientas utilizadas
### Tecnologías
* Se utilizó la programación orientada a objetos, utilizando el lenguaje python.
* La versión python utilizada es: Python 3.11.4

### Herramientas
* Se utilizo el programa online Draw io para desarrollar el diagrama de clases. https://app.diagrams.net/
* Como interfaz de desarrollo se utilizó Visual Studio Code
* Como versionador de la aplicación se utilizó Github online
https://github.com/Tefy1317/LFP_S2_2023_Proyecto1_202201318

## Funcionalidades del programa
El programa cuenta con una interfaz programada con ayuda de la librería Tkinter en la que se puede ingresar texto para analizar.  

![Interfaz](https://i.ibb.co/GR3ckhj/Interfaz.jpg)  

![ClaseVentana](https://i.ibb.co/dsN1yY2/clase-Ventana.jpg)

El botón Analizar entrada crear los tokens para analizarlos y dar validaciones de aceptación según el lenguaje establecido.  

![BotonAnalizar](https://i.ibb.co/Sc3TdDH/analizar-entrada.jpg)  

Además, cuenta con el botón Ver Reporte, el cual muestra una gráfica con ayuda de Graphviz.  

![BotonVerReporte](https://i.ibb.co/10J8CrV/ver-Reporte.jpg)  

![Graphviz](https://i.ibb.co/GRsd2Mc/Graphviz.jpg)  

A través del botón Ver Errores, se genera un archivo Json con los caracteres que no son reconocidos por el sistema.  

![BotonVerErrores](https://i.ibb.co/fxcNfYv/ver-Errores.jpg)  

![Errores](https://i.ibb.co/3pzPw1d/Errores-Cod.jpg)