import tkinter as tk

ventana = tk.Tk()
ventana.title("Interfaz")
#Etiqueta
etiqueta = tk.Label(ventana,text= " dx/dy : ")
etiqueta.pack()
etiqueta.place(x = 50 , y = 30)
#Caja de Texto
cajatext1 = tk.Entry(ventana)
cajatext1.pack()
cajatext1.place(x=100 , y = 30)

#Etiqueta 2
etiqueta2 = tk.Label(ventana,text=" Xo :")
etiqueta2.pack()
etiqueta2.place(x = 50 , y = 70)
#Caja de Texto 2
cajatext2 = tk.Entry(ventana)
cajatext2.pack()
cajatext2.place(x=100 , y = 70)

#Etiqueta 3
etiqueta3 = tk.Label(ventana,text=" Yo :")
etiqueta3.pack()
etiqueta3.place(x = 50 , y = 110)
#Caja de Texto 3
cajatext3 = tk.Entry(ventana)
cajatext3.pack()
cajatext3.place(x=100 , y = 110)

#Etiqueta 4
etiqueta4 = tk.Label(ventana,text=" H :")
etiqueta4.pack()
etiqueta4.place(x = 50 , y = 150)
#Caja de Texto 4
cajatext4 = tk.Entry(ventana)
cajatext4.pack()
cajatext4.place(x=100 , y = 150)

#Obtener Texto
def ObtenerTexto(cajatext):
    text = cajatext.get()
    return text

#Funcion de Alina
def Graficar():
 dxdy = ObtenerTexto(cajatext1)
 Xo = ObtenerTexto(cajatext2)
 Yo = ObtenerTexto(cajatext3)
 H = ObtenerTexto(cajatext4)
 
  

#Funcion de Dario
def Resolver():
  dxdy = ObtenerTexto(cajatext1)
  Xo = ObtenerTexto(cajatext2)
  Yo = ObtenerTexto(cajatext3)
  H = ObtenerTexto(cajatext4)

#Boton Graficar
boton1 = tk.Button(ventana,text="Graficar" , command= Graficar)
boton1.pack()
boton1.place(x=100,y= 300)

#Boton Resolver
boton2 = tk.Button(ventana,text="Resolver" , command= Resolver)
boton2.pack()
boton2.place(x=100,y= 600)




ventana.mainloop()