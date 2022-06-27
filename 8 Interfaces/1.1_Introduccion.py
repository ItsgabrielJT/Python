from cgitb import text
import tkinter as tk

# 1.- Concepto de tkinter
# Funciona mediante widgets

# 2.- Que son widgets
# Son elementos predefinidos que podemos incrustar en nuestra apicacion 
# Ejemplos: un boton, una entrda de texto, etc.

app = tk.Tk() # Crenado la ventana principal

# Estamos creando objetos de la clase StringVar
palabra = tk.StringVar(app)
entrada = tk.StringVar(app)

# 3.- Aspectos de la ventana
app.geometry("600x300") # Dimensiones: Ancho x Alto
app.configure(background="black")
#tk.Wm.wm_title(app, "Hola Roberto")
app.title("Juego del Hola")

# 4.- Botones
def saludar():
    print("Hola bro")

def cambiarPalabra():
    palabra.set("entrate" + entrada.get())

tk.Button (
    app, # Aqui colocamos donde queremos agregar este boton
    text = "Hola aplasta,e",
    font = ("Courier", 14),
    bg = "#00a8e8", # Fondo de color del boton
    fg = "white", # Color de las letras  

    # 4.1.- Acciones de los botones
    # COn ayuda del command podemos realizar acciones,
    # En este caso estamos actiualizando e imprimiendo los valores de palabra y entrada

    #command = saludar, # Pasamos la funcion como una variable  
    command = lambda: print("Hola de nuevo " + entrada.get()), 
    #command = ..., # Se deja con esos puntos para dejar en blnaco l accion
    #command = cambiarPalabra, # Estamos actualizando el valor de palabra

).pack (
    fill = tk.BOTH, # Aqui estamos colocando el boton en la app 
    expand = True, # Se ajusta e auerdo al tamaño de la ventana
)

# 5.- Etiquetas
# Aplica las mimas reglas que el boton
tk.Label (
    app,
    text = "Souy un oesado",
    # Estamos imprimiendo lo que se guardo en la varible palabra
    textvariable = palabra, # Lo que esta en la variable palabra superpone al texto anterior
    bg = "black",
    fg = "white",
    justify = "center",
).pack (
    fill = tk.BOTH,
    expand = True,
)

# 6.- Entrada de texto
# Todos los datos que introduzcamos podemos pasarlos al boton o a laetiqueta
tk.Entry (
    bg = "black",
    fg = "white",
    justify = "center",
    textvariable = entrada # Mapeamos todas nuestros datos leidos a la variable entrada
).pack (
    fill = tk.BOTH,
    expand = True,
)

app.mainloop() # Ayuda refrescar la ventana en cada cambio que hagamos


