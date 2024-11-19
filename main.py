import tkinter as tk
from tkinter import ttk
from Function import Function
from grafico import graficar_campo_isoclinas_y_solucion

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

#Posible mensaje de Error
label_error = tk.Label(ventana, text="", fg="red") 
label_error.pack() 

# Crea un Label para la respuesta
respuesta_frame = ttk.Frame(ventana, relief="sunken", borderwidth=2)
respuesta_frame.pack(pady=10, side=tk.BOTTOM, anchor=tk.CENTER)
respuesta_frame.place(x=60,y=350)

respuesta_label = ttk.Label(respuesta_frame, text="", wraplength=300, justify="left")
respuesta_label.pack(padx=70, pady=70)


#Obtener Texto
def ObtenerTexto(cajatext):
    text = cajatext.get()
    return text

def Graficar():
 f = ObtenerTexto(cajatext1)
 H = ObtenerTexto(cajatext4)
 #graficar_campo_isoclinas_y_solucion(f,H,Resolver())
 

def Resolver():
    try:
        label_error.config(text="")
        respuesta_label.config(text="")
        Xo = float(ObtenerTexto(cajatext2))
        Yo = float(ObtenerTexto(cajatext3))
        H = float(ObtenerTexto(cajatext4))
        f = Function(ObtenerTexto(cajatext1))
        xi = float(ObtenerTexto(cajatext5))
        x = Xo
        y = Yo
        respuesta = [(x, y)]
        while x < xi:
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
        ultimo_punto = respuesta[-1] 
        texto_respuesta = f"""Solución por el método Runge-Kutta:
                        x = {ultimo_punto[0]:.2f}
                        y = {ultimo_punto[1]:.2f}"""
        respuesta_label.config(text=texto_respuesta,font=("Helvetica", 14))
        return respuesta
    except ValueError:
        label_error.config(text="Error: Ingrese valores numéricos válidos.")
        return None
    except Exception as e:  # Captura otras posibles excepciones
        label_error.config(text=f"Ocurrió un error: {e}")
        return None



#Boton Graficar
boton1 = tk.Button(ventana,text=" Graficar" , command = Graficar)
boton1.pack()
boton1.place(x=100,y= 600)

#Boton Resolver
boton2 = tk.Button(ventana,text=" Resolver" , command = Resolver)
boton2.pack()
boton2.place(x=100,y= 300)



ventana.mainloop()