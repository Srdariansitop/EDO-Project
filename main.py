import tkinter as tk
from tkinter import ttk
from Function import Function
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import sys


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


# Función para obtener el epsilon de la máquina
def VerEpsilon():
    epsilon = sys.float_info.epsilon
    label_epsilon.config(text=f"Epsilon de la máquina: {epsilon:.16f}")

# Botón para ver el epsilon de la máquina
boton_epsilon = tk.Button(ventana, text="Ver Epsilon de la máquina", command=VerEpsilon)
boton_epsilon.pack()
boton_epsilon.place(x=100, y=250)

# Etiqueta para mostrar el valor del epsilon, colocada justo al lado del botón
label_epsilon = tk.Label(ventana, text="", font=("Helvetica", 12), fg="blue")
label_epsilon.pack()
label_epsilon.place(x=250, y=250)  # Ajusta la posición para que esté al lado del botón


#Obtener Texto
def ObtenerTexto(cajatext):
    text = cajatext.get()
    return text

def Graficar():
    try:
        # Obtener datos de la interfaz (asumiendo que tienes funciones para obtenerlos)
        f = Function(ObtenerTexto(cajatext1)) # Asegúrate que la función f está definida y que el texto se parsea correctamente
        h = float(ObtenerTexto(cajatext4)) # Paso de Runge-Kutta
        puntos_rk = Resolver() # Obtener puntos de Runge Kutta desde la función Resolver()
        if puntos_rk is None:
            return # Manejar el caso donde Resolver() falla

        x_vals, y_vals = zip(*puntos_rk)
        xi, xf = min(x_vals), max(x_vals)
        yi, yf = min(y_vals), max(y_vals)

        margen = 0.2
        expansion_isoclinas = 5

        rango_x = xf - xi
        rango_y = yf - yi
        xi -= rango_x * margen
        xf += rango_x * margen
        yi -= rango_y * margen
        yf += rango_y * margen

        xi -= expansion_isoclinas
        xf += expansion_isoclinas
        yi -= expansion_isoclinas
        yf += expansion_isoclinas

        x = np.arange(xi, xf + h, h)
        y = np.arange(yi, yf + h, h)
        X, Y = np.meshgrid(x, y)

        U = 1
        V = np.array([f.evaluate(X[i,j],Y[i,j]) for i in range(X.shape[0]) for j in range(X.shape[1])]).reshape(X.shape)
        U2, V2 = U / np.sqrt(U**2 + V**2), V / np.sqrt(U**2 + V**2)

        fig = Figure(figsize=(7, 6), dpi=100)
        ax = fig.add_subplot(111)

        ax.quiver(X, Y, U2, V2, color='gray', alpha=0.6)
        ax.plot(x_vals, y_vals, color='blue', label='Solución Runge-Kutta', marker='o')
        ax.set_title(r'Campo de direcciones y Solución Runge-Kutta')
        ax.set_xlim(xi, xf)
        ax.set_ylim(yi, yf)
        ax.grid(True)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.axhline(0, color='black', linewidth=0.5, ls='--')
        ax.axvline(0, color='black', linewidth=0.5, ls='--')
        ax.legend()

        canvas = FigureCanvasTkAgg(fig, master=ventana)
        canvas.draw()
        canvas.get_tk_widget().place(x=800, y=70)

    except Exception as e:
        label_error.config(text=f"Error al graficar: {e}")

    


 

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
    except Exception as e:  
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