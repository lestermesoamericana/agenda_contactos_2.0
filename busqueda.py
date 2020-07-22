from tkinter import *
from Base_de_Datos import *
from funciones import *
from PIL import Image, ImageTk

class Busqueda():

    def __init__(self, imagen):
        self.__imagen = imagen

    def open(self):
        self.top = Toplevel()
        self.top.title("Busqueda")
        self.top.iconbitmap(self.__imagen)
        self.top.config(width = 500, height = 350)
        objetoFun = Funciones(self.top)

        # define id
        self.__miID = StringVar()
        

        # ------------------------------------------------- search
        self.__validatecommand = self.top.register(objetoFun.is_valid_char)
        self.__idLabel = Label(self.top, text = "Ingrese id:")
        self.__idLabel.place(x=20, y=10, height=20, width=80)
        self.__cuadroID = Entry(self.top, textvariable = self.__miID, validate="key", validatecommand=(self.__validatecommand, "%S"))
        self.__cuadroID.config(fg = "red", justify = "right")
        self.__cuadroID.place(x=100, y=10, height=20, width=180)

        # Search button
        self.botonLeer = Button(self.top, text = "Buscar")
        self.botonLeer.place(x=90, y = 40, height=30, width=60)


