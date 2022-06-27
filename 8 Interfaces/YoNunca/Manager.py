from importlib.machinery import SourcelessFileLoader
from logging import setLogRecordFactory
import tkinter as tk
from typing import Container
from constantes import styles
from screens import Home, Game, Agree

class Manager(tk.Tk):
    # Estructura de la app principal
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Yo nunca, The Game")
        #"container = tk.Frame(self)
        self.container = tk.Frame()
        self.mode = "Normal"
        self.container.pack (
            side = tk.TOP,
            fill = tk.BOTH,
            expand = True
        )
        self.container.configure(background = styles.BACKGROUND)
        self.container.grid_columnconfigure(0, weight = 1)
        self.container.grid_rowconfigure(0, weight = 1)

        self.frames = {}

        for F in (Home, Game, Agree):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = tk.NSEW)
        self.showFrame(Home)

    def showFrame(self, container):
        frame = self.frames[container]
        frame.tkraise()



    