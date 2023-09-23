import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from analizador import analizar
from analizador import archivoErrores

#Código para cuadro de texto
class ScrollText(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.text = tk.Text(
            self,
            bg="#ffcccc",  
            foreground="#ff1493",  
            insertbackground="#ff1493",  
            selectbackground="#ff69b4",  
            width=120,
            height=25,
            font=("Courier New", 13),
        )

        self.scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.text.yview)
        self.text.configure(yscrollcommand=self.scrollbar.set)

        self.numberLines = TextLineNumbers(self, width=40, bg="#dee2e6")
        self.numberLines.attach(self.text)

        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.numberLines.pack(side=tk.LEFT, fill=tk.Y, padx=(5, 0))
        self.text.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.text.bind("<Key>", self.onPressDelay)
        self.text.bind("<Button-1>", self.numberLines.redraw)
        self.scrollbar.bind("<Button-1>", self.onScrollPress)
        self.text.bind("<MouseWheel>", self.onPressDelay)

    def onScrollPress(self, *args):
        self.scrollbar.bind("<B1-Motion>", self.numberLines.redraw)

    def onScrollRelease(self, *args):
        self.scrollbar.unbind("<B1-Motion>", self.numberLines.redraw)

    def onPressDelay(self, *args):
        self.after(2, self.numberLines.redraw)

    def get(self, *args, **kwargs):
        return self.text.get(*args, **kwargs)

    def insert(self, *args, **kwargs):
        return self.text.insert(*args, **kwargs)

    def delete(self, *args, **kwargs):
        return self.text.delete(*args, **kwargs)

    def index(self, *args, **kwargs):
        return self.text.index(*args, **kwargs)

    def redraw(self):
        self.numberLines.redraw()

class TextLineNumbers(tk.Canvas):
    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs, highlightthickness=0)
        self.textwidget = None

    def attach(self, text_widget):
        self.textwidget = text_widget

    def redraw(self, *args):
        """redraw line numbers"""
        self.delete("all")

        i = self.textwidget.index("@0,0")
        while True:
            dline = self.textwidget.dlineinfo(i)
            if dline is None:
                break
            y = dline[1]
            linenum = str(i).split(".")[0]
            self.create_text(
                2,
                y,
                anchor="nw",
                text=linenum,
                fill="#868e96",
                font=("Courier New", 13, "bold"),
            )
            i = self.textwidget.index("%s+1line" % i)


class Ventana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Proyecto 1")
        self.geometry("1000x580")
        self.scroll = ScrollText(self)
        self.scroll.pack()
        self.after(200, self.scroll.redraw())

        self.menu = Menu(self)
        self.config(menu=self.menu)
        self.filemenu = Menu(self.menu)
        self.menu.add_cascade(label="Archivo", menu=self.filemenu)
        self.filemenu.add_command(label="Abrir", command=self.abrirArchivo)
        self.filemenu.add_command(label="Guardar", command=self.guardar)
        self.filemenu.add_command(label="Guardar como", command=self.guardarComo)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Salir", command=self.quit)

        #Frame para agregar los botones
        button_frame = tk.Frame(self)
        button_frame.pack(side=tk.TOP, pady=10)

        buttonAnalizar= Button(button_frame, text="Analizar entrada", command=self.analizarTexto, bg="#dee2e6", fg="black", font=("Courier New", 15))
        buttonAnalizar.pack(side=tk.LEFT, padx=10)

        buttonAnalizar= Button(button_frame, text="Ver Reporte", command=self.verReporte, bg="#dee2e6", fg="black", font=("Courier New", 15))
        buttonAnalizar.pack(side=tk.LEFT, padx=10)

        buttonErrores = Button(button_frame, text="Ver Errores", command=self.cargarJson, bg="#dee2e6", fg="black", font=("Courier New", 15))
        buttonErrores.pack(side=tk.RIGHT, padx=10)

    def abrirArchivo(self):
        global filepath
        filepath = askopenfilename(
            filetypes=[("JSON Files", "*.json"), ("All Files", "*.*")]
        )
        if not filepath:
            return
        
        self.scroll.delete(1.0,tk.END)
        with open(filepath, "r") as archivoCargado:
            text = archivoCargado.read()
            self.scroll.insert(tk.END, text)
        self.title(f"Proyecto 1 - {filepath}")

    def guardarComo(self):
        filepath = asksaveasfilename(
            defaultextension="json",
            filetypes=[("JSON Files", "*.json"), ("All Files", "*.*")],
        )
        if not filepath:
            return
        with open(filepath, "w") as output_file:
            text = self.scroll.get(1.0, tk.END)
            output_file.write(text)
        self.title(f"Proyecto 1 - {filepath}")
    
    def guardar(self):
        if not filepath:
            self.guardarComo()
        else:
            with open(filepath, "w") as output_file:
                text = self.scroll.get(1.0, tk.END)
                output_file.write(text)
            self.title(f"Proyecto 1 - {filepath}")

    def analizarTexto(self):
        global arbol
        text = self.scroll.get(1.0, tk.END) 
        if text.strip() == "": 
            messagebox.showinfo(message="No hay ningún texto para analizar", title="Error")
        else:
            messagebox.showinfo(message="Archivo analizado con éxito, ver detalles en consola", title="Mensaje")
            arbol = analizar(text)
            #arbol.dot.view()
        return arbol 
    
    def verReporte(self):
        arbol.dot.view()
  
    def cargarJson(self):
       archivoErrores()

    
app = Ventana()
app.mainloop()