# para la base de datos
import sqlite3
from tkinter import *
from tkinter import messagebox
from funciones import *

# Crear Conexion
class Conexion():
    def __init__(self):
        self.__miConexion = sqlite3.connect("Usuarios")
        self.__miCursor = self.__miConexion.cursor()

    def crearConexion(self):
        try:
            self.__miCursor.execute(
                '''
                CREATE TABLE DATOSUSUARIOS(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE_USUARIO VARCHAR(50),
                APELLIDO VARCHAR(50),
                TELEFONO VARCHAR(25),
                DIRECCION VARCHAR(50),
                COMENTARIOS VARCHAR(200)
                )
                '''
            )

            messagebox.showinfo("BBDD", "BBDD Creada con éxito")
        except sqlite3.OperationalError:
            messagebox.showwarning("Atencion", "La BBDD ya existe")
    
    # -------------------------------------------- USO DEL CRUD ----------------------------------------------
    # CREATE
    def crear(self, campo1, campo2, campo3, campo4, textoCom):
        self.__idusuario = int()
        if campo1.get() == "" or campo2.get() == "" or campo3.get() == "" or campo4.get() == "":
            messagebox.showerror("Error","No hay datos para ingresar")
        else:
            self.__idusuario =self.__miCursor.execute(
                "INSERT INTO DATOSUSUARIOS VALUES(NULL, '" + campo1.get() +
                "','" + campo2.get() +
                "','" + campo3.get() +
                "','" + campo4.get() +
                "','" + textoCom.get("1.0",END) + "')"
                ).lastrowid
            self.__miConexion.commit()

            messagebox.showinfo("BBDD", "Registro insertado con exito. Su ID es: " + str(self.__idusuario))
            self.__miConexion.commit()
            self.__miConexion.close()

            campo1.set("")
            campo2.set("")
            campo3.set("")
            campo4.set("")
            textoCom.delete(1.0, END)
    
    # READ
    def leer(self, campoID, campo1, campo2, campo3, campo4, textoCom):
        try:
            textoCom.config(state = "disable")
            self.__miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID="+ campoID.get())
            usuarios = self.__miCursor.fetchall()

            textoCom.config(state = "normal")
            for usuario in usuarios:
                campoID.set(usuario[0])
                campo1.set(usuario[1])
                campo2.set(usuario[2])
                campo3.set(usuario[3])
                campo4.set(usuario[4])
                textoCom.insert(1.0, usuario[5])
            textoCom.config(state = "disable")
            self.__miConexion.commit()
        except:
            messagebox.showwarning("Sin Resultados", "No existen registros asociados a esa ID")

    # UPDATE
    def actualizar(self, campoID, campo1, campo2, campo3, campo4, textoCom):
        if campo1.get() == "" or campo2.get() == "" or campo3.get() == "" or campo4.get() == "":
            messagebox.showerror("Error","No hay datos para ingresar")
        else:
            self.__valor = messagebox.askquestion("Salir","Desea actualizar este registro?")

            if self.__valor == "yes":
                self.__info = (campo1.get(), campo2.get(), campo3.get(), campo4.get(), textoCom.get("1.0",END))

                # Actualizar
                self.__miCursor.execute(
                    "UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO=?, APELLIDO=?, TELEFONO=?, DIRECCION=?, COMENTARIOS=?"+
                    "WHERE ID=" + campoID.get(), self.__info)
                self.__miConexion.commit()

                messagebox.showinfo("BBDD", "Registro actualizado con exito")
                campoID.set("")
                campo1.set("")
                campo2.set("")
                campo3.set("")
                campo4.set("")
                textoCom.delete(1.0, END)
                
    
    # DELETE
    def borrar(self, campoID, campo1, campo2, campo3, campo4, textoCom):
        if campoID.get() == "":
            messagebox.showerror("Error", "Debe escribir un dato entero en ID")
        else:
            self.__valor = messagebox.askquestion("Salir","Desea borrar este registro?")

            if self.__valor == "yes":
                self.__miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID="+ campoID.get())
                self.__miConexion.commit()
                messagebox.showinfo("BBDD", "Registro borrado con exito")

                campoID.set("")
                campo1.set("")
                campo2.set("")
                campo3.set("")
                campo4.set("")
                textoCom.delete(1.0, END)

