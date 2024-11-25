import tkinter as tk
from tkinter import ttk
from Function import Function
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import sys
import os
from PIL import Image, ImageTk 
from numerica import Numerica as n



ventana = tk.Tk()
ventana.title("Interfaz")

ruta_imagen = os.path.join(os.getcwd(), "Image", "X2.jpg")

try:
    img = Image.open(ruta_imagen)
    photo = ImageTk.PhotoImage(img)
    label = tk.Label(ventana, image=photo)
    label.pack()
except Exception as e:
    print(f"Error: {e}")

#Etiqueta
etiqueta = tk.Label(ventana,text= " dx/dy : ",bg='black',fg='white')
etiqueta.pack()
etiqueta.place(x = 50 , y = 30)
#Caja de Texto
cajatext1 = tk.Entry(ventana,bg='black',fg='white')
cajatext1.pack()
cajatext1.place(x=100 , y = 30)

#Etiqueta 2
etiqueta2 = tk.Label(ventana,text=" Xo :",bg='black',fg='white')
etiqueta2.pack()
etiqueta2.place(x = 50 , y = 70)
#Caja de Texto 2
cajatext2 = tk.Entry(ventana,bg='black',fg='white')
cajatext2.pack()
cajatext2.place(x=100 , y = 70)

#Etiqueta 3
etiqueta3 = tk.Label(ventana,text=" Yo :",bg='black',fg='white')
etiqueta3.pack()
etiqueta3.place(x = 50 , y = 110)
#Caja de Texto 3
cajatext3 = tk.Entry(ventana,bg='black',fg='white')
cajatext3.pack()
cajatext3.place(x=100 , y = 110)

#Etiqueta 4
etiqueta4 = tk.Label(ventana,text=" H :",bg='black',fg='white')
etiqueta4.pack()
etiqueta4.place(x = 50 , y = 150)
#Caja de Texto 4
cajatext4 = tk.Entry(ventana,bg='black',fg='white')
cajatext4.pack()
cajatext4.place(x=100 , y = 150)

#Etiqueta 5
etiqueta5 = tk.Label(ventana,text=" xi :",bg='black',fg='white')
etiqueta5.pack()
etiqueta5.place(x = 50 , y = 190)
#Caja de Texto 5
cajatext5 = tk.Entry(ventana , bg='black',fg='white')
cajatext5.pack()
cajatext5.place(x=100 , y = 190)

#Posible mensaje de Error
label_error = tk.Label(ventana, text="", fg="red") 
label_error.pack() 

# Crea un Label para la respuesta
respuesta_frame = ttk.Frame(ventana, relief="sunken", borderwidth=2)
respuesta_frame.pack(pady=10, side=tk.BOTTOM, anchor=tk.CENTER)
respuesta_frame.place(x=60,y=360)

respuesta_label = ttk.Label(respuesta_frame, text="", wraplength=300, justify="left")
respuesta_label.pack(padx=70, pady=70)


# Función para obtener el epsilon de la máquina
def VerEpsilon():
    epsilon = sys.float_info.epsilon
    label_epsilon.config(text=f"Epsilon de la máquina: {epsilon:.16f}")

# Botón para ver el epsilon de la máquina
boton_epsilon = tk.Button(ventana, text="Ver Epsilon de la máquina", command=VerEpsilon,bg='black',fg='white')
boton_epsilon.pack()
boton_epsilon.place(x=50, y=250)

# Etiqueta para mostrar el valor del epsilon, colocada justo al lado del botón
label_epsilon = tk.Label(ventana, text="", font=("Helvetica", 12), fg="white" , bg='black')
label_epsilon.pack()
label_epsilon.place(x=250, y=250)  # Ajusta la posición para que esté al lado del botón

# ELEMENTOS NUMERICA CALCULAR ERROR
# Etiqueta para introducir el valor real
etiqueta_real = tk.Label(ventana, text="Introducir Valor Real:",bg='black',fg='white')
etiqueta_real.pack()
etiqueta_real.place(x=50, y=290)

# Caja de texto para el valor real
cajatext_real = tk.Entry(ventana,bg='black',fg='white')
cajatext_real.pack()
cajatext_real.place(x=200, y=290)

# Botón para calcular el error
def CalcularError():
    try:
        valor_real = float(cajatext_real.get())  # Obtener el valor exacto
        if respuesta_label["text"]:  # Asegurarse de que ya hay una solución
            texto_respuesta = respuesta_label["text"]
            y_aprox = float(texto_respuesta.split("y = ")[1])  # Extraer y
            error_absoluto = abs(valor_real - y_aprox)  # Calcular error absoluto
            error_relativo = (error_absoluto / abs(valor_real)) * 100  # Calcular error relativo
            label_error_absoluto.config(text=f"{error_absoluto:.4f}")
            label_error_relativo.config(text=f"{error_relativo:.2f}%")
        else:
            label_error.config(text="Primero resuelva la EDO para calcular los errores.")
    except ValueError:
        label_error.config(text="Ingrese un valor numérico válido para el valor real.")

boton_calcular_error = tk.Button(ventana, text="Calcular Error", command=CalcularError,bg='black',fg='white')
boton_calcular_error.pack()
boton_calcular_error.place(x=420, y=290)

# Etiquetas para los errores
etiqueta_error_relativo = tk.Label(ventana, text="Error Relativo en Porcentaje:",bg='black',fg='white')
etiqueta_error_relativo.pack()
etiqueta_error_relativo.place(x=420, y=330)

label_error_relativo = tk.Label(ventana, text="",bg='black',fg='white')
label_error_relativo.pack()
label_error_relativo.place(x=580, y=330)

etiqueta_error_absoluto = tk.Label(ventana, text="Error Absoluto:",bg='black',fg='white')
etiqueta_error_absoluto.pack()
etiqueta_error_absoluto.place(x=420, y=360)

label_error_absoluto = tk.Label(ventana, text="",bg='black',fg='white')
label_error_absoluto.pack()
label_error_absoluto.place(x=510, y=360)
# ** FIN DE LOS ELEMENTOS NUEVOS **


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
            k2 = H * f.evaluate(n.suma_numerica(x, H / 2), n.suma_numerica(y, k1 / 2))
            k3 = H * f.evaluate(n.suma_numerica(x, H / 2), n.suma_numerica(y, k2 / 2))
            k4 = H * f.evaluate(n.suma_numerica(x, H), n.suma_numerica(y, k3))
            y = n.suma_numerica(y, n.suma_numerica(k1, 2 * k2, 2 * k3, k4) / 6)
            x = n.suma_numerica(x + H)
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
boton1 = tk.Button(ventana,text=" Graficar" , command = Graficar,bg='black',fg='white')
boton1.pack()
boton1.place(x=100,y= 600)

#Boton Resolver
boton2 = tk.Button(ventana,text=" Resolver" , command = Resolver,bg='black',fg='white')
boton2.pack()
boton2.place(x=100,y= 325)

ventana.mainloop()