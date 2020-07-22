from tkinter import *
from Base_de_Datos import *
from funciones import *
from PIL import Image, ImageTk

class Borrar():

    def __init__(self, imagen):
        self.__imagen = imagen

    def delete_function(self):
        self.top = Toplevel()
        self.top.title("Borrar Registro")
        self.top.iconbitmap(self.__imagen)
        self.top.config(width = 300, height = 350)
        objetoFun = Funciones(self.top)
        objetoBD = Conexion()

        # define id
        self.__miID = StringVar()
        self.__miNombre = StringVar()
        self.__miApellido = StringVar()
        self.__miNumero = StringVar()
        self.__miDireccion = StringVar()
        self.__TextoComentario = Text(self.top)
        #self.__TextoComentario.config(state = "disable")

        # search
        self.__validatecommand = self.top.register(objetoFun.is_valid_char)
        self.__idLabel = Label(self.top, text = "Ingrese id:")
        self.__idLabel.place(x=20, y=10, height=20, width=80)
        self.__cuadroID = Entry(self.top, textvariable = self.__miID, validate="key", validatecommand=(self.__validatecommand, "%S"))
        self.__cuadroID.config(fg = "red", justify = "right")
        self.__cuadroID.place(x=100, y=10, height=20, width=180)

        # search button
        self.botonLeer = Button(self.top, text = "Buscar", command = lambda:objetoBD.leer(self.__miID, self.__miNombre, self.__miApellido, self.__miNumero, self.__miDireccion, self.__TextoComentario))
        self.botonLeer.place(x=180, y = 40, height=30, width=60)

        # -------------------------------------------------- show fields
        # Cuadro Nombre
        self.nombreLabel = Label(self.top, text = "Nombre:")
        self.nombreLabel.place(x=-26, y=80, height=20, width=180)
        self.cuadroNombre = Entry(self.top, textvariable = self.__miNombre, state = 'disable')
        self.cuadroNombre.config(fg = "blue", justify = "left")
        self.cuadroNombre.place(x=100, y = 80, height=20, width=180)

        # Cuadro Apellido
        self.apellidoLabel = Label(self.top, text = "Apellido:")
        self.apellidoLabel.place(x=-26, y=110, height=20, width=180)
        self.cuadroApellido = Entry(self.top, textvariable = self.__miApellido, state = 'disable')
        self.cuadroApellido.config(fg = "blue", justify = "left")
        self.cuadroApellido.place(x=100, y = 110, height=20, width=180)

        # Cuadro Telefono
        self.passLabel = Label(self.top, text = "Telefono:")
        self.passLabel.place(x=-28, y=140, height=20, width=180)
        self.cuadroTelefono = Entry(self.top, textvariable = self.__miNumero, state = 'disable')
        self.cuadroTelefono.config(fg = "blue", justify = "left", validate="key", validatecommand=(self.__validatecommand, "%S"))
        self.cuadroTelefono.place(x=100, y = 140, height=20, width=180)

        # Cuadro Direccion
        self.passLabel = Label(self.top, text = "Direccion:")
        self.passLabel.place(x=-28, y=170, height=20, width=180)
        self.cuadroDireccion = Entry(self.top, textvariable = self.__miDireccion, state = 'disable')
        self.cuadroDireccion.config(fg = "blue", justify = "left")
        self.cuadroDireccion.place(x=100, y = 170, height=20, width=180)

        # Cuadro de Texto (Comentario)
        self.cuadroLabel = Label(self.top, text = "Observaciones:")
        self.cuadroLabel.place(x=-0, y=230, height=20, width=100)
        # Posicion del cuadro de texto
        self.__TextoComentario.place(x=100, y = 200, height=100, width=165)
        self.scrollVert = Scrollbar(self.top, command = self.__TextoComentario.yview)
        self.scrollVert.place(x=265, y = 200, height=100)
        self.__TextoComentario.config(yscrollcommand = self.scrollVert.set)

        # boton limpiar
        self.botonCrear = Button(self.top, text = "Limpiar", command = lambda:objetoFun.limpiarCampos(self.__miID, self.__miNombre, self.__miApellido, self.__miNumero, self.__miDireccion, self.__TextoComentario))
        self.botonCrear.place(x=100, y = 310, height=30, width=60)

        # boton Borrar
        self.botonEliminar = Button(self.top, text = "Eliminar", command = lambda : objetoBD.borrar(self.__miID, self.__miNombre, self.__miApellido, self.__miNumero, self.__miDireccion, self.__TextoComentario))
        self.botonEliminar.place(x=180, y = 310, height=30, width=60)