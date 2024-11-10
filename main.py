import tkinter as tk

from Function import Function

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

#Etiqueta 5
etiqueta5 = tk.Label(ventana,text=" xi :")
etiqueta5.pack()
etiqueta5.place(x = 50 , y = 190)
#Caja de Texto 5
cajatext5 = tk.Entry(ventana)
cajatext5.pack()
cajatext5.place(x=100 , y = 190)

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
    Xo = float(ObtenerTexto(cajatext2))
    Yo = float(ObtenerTexto(cajatext3))
    H = float(ObtenerTexto(cajatext4))
    f = Function(ObtenerTexto(cajatext1))
    xi = ObtenerTexto(cajatext5)
    x = Xo
    y = Yo
    respuesta = [(x, y)]
    while x < 2:
        k1 = H * f.evaluate(x, y)
        k2 = H * f.evaluate(x + H / 2, y + k1 / 2)
        k3 = H * f.evaluate(x + H / 2, y + k2 / 2)
        k4 = H * f.evaluate(x + H, y + k3)
        y = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x = x + H
        respuesta.append((x, y))
    for item in respuesta:
        print('printing point')
        print(f'x = {item[0]}')
        print(f'y = {item[1]}')

    ActualizarEtiqueta(etiqueta6,respuesta)
    return respuesta


#Boton Graficar
boton1 = tk.Button(ventana,text=" Graficar" , command = Graficar)
boton1.pack()
boton1.place(x=100,y= 600)

#Boton Resolver
boton2 = tk.Button(ventana,text=" Resolver" , command = Resolver)
boton2.pack()
boton2.place(x=100,y= 300)

etiqueta6 = tk.Label(ventana,text="")
etiqueta6.pack()
etiqueta6.place(x = 100 , y = 340)

def ActualizarEtiqueta(etiqueta,valor):
   etiqueta.config(text = "La funcion es : {valor}")

ventana.mainloop()