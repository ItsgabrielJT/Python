from distutils.command.config import config
from struct import pack
from symtable import SymbolTableFactory
import tkinter as tk
from tkinter.messagebox import QUESTION
from tkinter.tix import TEXT
from tkinter.ttk import Style
from turtle import left
from constantes import styles, config

class Home(tk.Frame):
    # Estructura de la ventana
    def __init__(self, parents, controller):
        super().__init__(parents)
        self.configure(background = styles.BACKGROUND)
        self.controller = controller   # Aqui se guardan los modos de juegos

        # Apariencia
        # Con StringVar colocamos donde poner ese titulo
        self.game_mode = tk.StringVar(self, value = "Normal") # self significa que pasamos el frame de Home
        self.initWidgets()

    def moveToGame(self):
        self.controller.mode = self.game_mode.get()
        self.controller.showFrame(Game)

    def moveToAdd(self):
        self.controller.mode = self.game_mode.get()
        self.controller.showFrame(Agree)

    def initWidgets(self):
        # Definimos el widget
        tk.Label(
            self, 
            text = "Yo Nunca: The GAme",
            justify = tk.CENTER,
            **styles.STYLE # Estamos trayendo todo nuestro diccionario            
        # Colocamos el widget
        ).pack (
            side = tk.TOP,
            fill = tk.BOTH,
            expand = True,
            padx = 22, # Margen Horizontal
            pady = 11 # Margen Vertical
        )

        tk.Button (
            self,
            text = "Agregar ideas",
            command = self.moveToAdd,
            **styles.STYLE,
            relief = tk.FLAT, #uitamos los margenes
            activebackground = styles.BACKGROUND,
            activeforeground = styles.TEXT,
        ).pack (
            side = tk.TOP,
            fill = tk.X,
            padx = 22,
            pady = 11,
        )

        # Agregamos un frame dentro del frame home
        optionsFrame = tk.Frame(self)
        optionsFrame.configure(background = styles.COMPONENT)
        optionsFrame.pack (
            side = tk.TOP,
            fill = tk.BOTH,
            expand = True,
            padx = 22,
            pady = 11
        )

        tk.Label (
            optionsFrame,
            text = "Elige tu modo de juego ",
            justify = tk.CENTER,
            **styles.STYLE
        ).pack (
            side = tk.TOP,
            fill = tk.X,
            padx = 22,
            pady = 11
        )

        for (key, value) in config.MODES.items():
            tk.Radiobutton (
                optionsFrame,
                text = key + ("!!!" if key == "ATREVIDO" else ""),
                variable = self.game_mode,
                value = value,
                # El active sirve para camabair la apariencia en cada click sobre el boton
                activebackground = styles.BACKGROUND,
                activeforeground = styles.TEXT,
                **styles.STYLE
            ).pack (
                side = tk.LEFT,
                fill = tk.BOTH,
                expand = True,
                padx = 5,
                pady = 5
            )

        tk.Button (
            self,
            text = "EMPEZAR",
            command = self.moveToGame, # Estamos psanado la funcion como un objeto, esto hace que se ejecute solo al applastar el boton
            #command = self.moveToGame() # Si hacemos eso la funcion se ejecuta sin necesidad de usar el bootn
            **styles.STYLE,
            relief = tk.FLAT, #uitamos los margenes
            activebackground = styles.BACKGROUND,
            activeforeground = styles.TEXT,
        ).pack (
            side = tk.TOP,
            fill = tk.X,
            padx = 22,
            pady = 11,
        )

class Game(tk.Frame):    
    # Estructura de la ventana
    def __init__(self, parents, controller):
        super().__init__(parents)
        self.configure(background = styles.BACKGROUND)
        self.controller = controller
        self.current_question = tk.StringVar(self, value = "Preparaods, listos, Deleeeee")
        self.ficheros = None
        self.initWidgets()

    def updateQuestion(self):
        self.mode = self.controller.mode
        if (self.ficheros == None) or (self.controller.mode.lower() not in self.ficheros.name.lower()):
            self.ficheros = open(f'C:/Users/gabrieljt/Desktop/Python/8 Interfaces/YoNunca/ficheros/{self.mode}.txt', 'r', encoding = "utf-8")

        tmp = self.ficheros.readline()

        if tmp != "":
            self.current_question.set(tmp)
        else:
            self.current_question.set("Ya hemos leido todo elarchvio") # Hacemos esto por que usamos anteriormente StringVar
            self.ficheros.close()
            self.ficheros = open(f'C:/Users/gabrieljt/Desktop/Python/8 Interfaces/YoNunca/ficheros/{self.mode}.txt', 'r', encoding = "utf-8")
                                    
    def initWidgets(self):
        # Definimos el widget
        tk.Label(
            self, 
            text = "Yo Nunca: ---------------",
            justify = tk.CENTER,
            **styles.STYLE # Estamos trayendo todo nuestro diccionario            
        # Colocamos el widget
        ).pack (
            side = tk.TOP,
            fill = tk.BOTH,
            expand = True,
            padx = 22, # Margen Horizontal
            pady = 11 # Margen Vertical
        )
        
        tk.Label (
            self,
            text = "preparados, listos, Daleeeeee ",
            textvar = self.current_question, # Muestra en la label lo que guardeos
            justify = tk.CENTER,
            **styles.STYLE
        ).pack (
            side = tk.TOP,
            fill = tk.X,
            padx = 22,
            pady = 11
        )        

        tk.Button (
            self,
            text = "Siguiente -> ",
            command = self.updateQuestion,
            #command = self.moveToGame() # Si hacemos eso la funcion se ejecuta sin necesidad de usar el bootn
            **styles.STYLE,
            relief = tk.FLAT, #uitamos los margenes
            activebackground = styles.BACKGROUND,
            activeforeground = styles.TEXT,
        ).pack (
            side = tk.TOP,
            fill = tk.BOTH,
            expand = True,
            padx = 22,
            pady = 11,
        )

        tk.Button (
            self,
            text = " <- HOME ",
            command = lambda: self.controller.showFrame(Home),
            #command = self.moveToGame() # Si hacemos eso la funcion se ejecuta sin necesidad de usar el bootn
            **styles.STYLE,
            relief = tk.FLAT, #uitamos los margenes
            activebackground = styles.BACKGROUND,
            activeforeground = styles.TEXT,
        ).pack (
            side = tk.TOP,
            fill = tk.BOTH,
            expand = True,
            padx = 22,
            pady = 11,
        )

class Agree(tk.Frame):
    def __init__(self, parents, controller):
        super().__init__(parents)
        self.configure(background = styles.BACKGROUND)
        self.question = tk.StringVar(self, value = "")
        self.controller = controller
        self.ficheros = None
        self.initWidgets()

    def initWidgets(self):

        tk.Label (
            self,
            text = "Modo de juego",
            textvar = self.controller.mode,            
            justify = tk.CENTER,
            **styles.STYLE
        ).pack (
            side = tk.TOP,
            fill = tk.X,
            padx = 22,
            pady = 11
        )         

        # Definimos el widget
        tk.Label(
            self, 
            text = "Yo Nunca: ------------------------",
            justify = tk.CENTER,
            **styles.STYLE # Estamos trayendo todo nuestro diccionario            
        # Colocamos el widget
        ).pack (
            side = tk.TOP,
            fill = tk.BOTH,
            expand = True,
            padx = 22, # Margen Horizontal
            pady = 11 # Margen Vertical
        )

        tk.Entry (
            self,
            **styles.STYLE,
            justify = tk.CENTER,
            relief = tk.FLAT, #uitamos los margenes            
            textvariable = self.question.set(self.question)
        ).pack (
            side = tk.TOP,
            fill = tk.BOTH,
            expand = True,
            padx = 22,
            pady = 11,
        )     

        tk.Button (
            self,
            text = "Guardar -> ",
            command = self.saveQuestion,
            #command = self.moveToGame() # Si hacemos eso la funcion se ejecuta sin necesidad de usar el bootn
            **styles.STYLE,
            relief = tk.FLAT, #uitamos los margenes
            activebackground = styles.BACKGROUND,
            activeforeground = styles.TEXT,
        ).pack (
            side = tk.TOP,
            fill = tk.BOTH,
            expand = True,
            padx = 22,
            pady = 11,
        )

        tk.Button (
            self,
            text = " <- HOME ",
            command = lambda: self.controller.showFrame(Home),
            #command = self.moveToGame() # Si hacemos eso la funcion se ejecuta sin necesidad de usar el bootn
            **styles.STYLE,
            relief = tk.FLAT, #uitamos los margenes
            activebackground = styles.BACKGROUND,
            activeforeground = styles.TEXT,
        ).pack (
            side = tk.TOP,
            fill = tk.BOTH,
            expand = True,
            padx = 22,
            pady = 11,
        )        

    def saveQuestion(self):
        ...