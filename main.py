import tkinter as tk

ventana = tk.Tk()
ventana.title("Interfaz")
#Etiqueta
etiqueta = tk.Label(ventana,text=" Escriba una ecuacion diferencial : ")
etiqueta.pack()

#Caja de Texto
cajatext = tk.Entry(ventana)
cajatext.pack()

#Obtener Texto
def ObtenerTexto():
    text = cajatext.get()
    return text

#Funcion de Alina
def Graficar():
   ObtenerTexto()
  

#Funcion de Dario
def Resolver():
   ObtenerTexto()

#Boton Graficar
boton1 = tk.Button(ventana,text="Graficar" , command= Graficar)
boton1.pack()
boton1.place(x=100,y= 50)

#Boton Resolver
boton2 = tk.Button(ventana,text="Resolver" , command= Resolver)
boton2.pack()
boton2.place(x=1200,y= 50)




ventana.mainloop()