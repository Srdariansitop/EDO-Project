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
from Interpolation import Interpolation as interpolation


#Intancia de la Clase Numerica
numerica = n()

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
    epsilon = numerica.obtener_epsilon()  # Usar método estático de la clase Numerica
    label_epsilon.config(text=f"Epsilon de la máquina: {epsilon:.16f}")


# Botón para ver el epsilon de la máquina
boton_epsilon = tk.Button(ventana, text="Ver Epsilon de la máquina", command=VerEpsilon,bg='black',fg='white')
boton_epsilon.pack()
boton_epsilon.place(x=50, y=600)

# Etiqueta para mostrar el valor del epsilon, colocada justo al lado del botón
label_epsilon = tk.Label(ventana, text="", font=("Helvetica", 12), fg="white" , bg='black')
label_epsilon.pack()
label_epsilon.place(x=250, y=600)  # Ajusta la posición para que esté al lado del botón


# Etiqueta para introducir el valor real
etiqueta_real = tk.Label(ventana, text="Introducir Valor Real:",bg='black',fg='white')
etiqueta_real.pack()
etiqueta_real.place(x=50, y=290)

# Caja de texto para el valor real
cajatext_real = tk.Entry(ventana,bg='black',fg='white')
cajatext_real.pack()
cajatext_real.place(x=200, y=290)

# Botón para calcular el error
# Función para calcular el error
def CalcularErrorDesdeInterfaz():
    try:
        valor_real = float(cajatext_real.get())  # Obtener el valor exacto desde la interfaz
        if respuesta_label["text"]:  # Asegurarse de que ya hay una solución
            texto_respuesta = respuesta_label["text"]
            error_absoluto, error_relativo = numerica.calcular_error(valor_real, texto_respuesta)  # Usar el método de la clase Numerica
            label_error_absoluto.config(text=f"{error_absoluto:.4f}")
            label_error_relativo.config(text=f"{error_relativo:.2f}%")
        else:
            label_error.config(text="Primero resuelva la EDO para calcular los errores.")
    except ValueError:
        label_error.config(text="Ingrese un valor numérico válido para el valor real.")

# Botón para calcular el error
boton_calcular_error = tk.Button(ventana, text="Calcular Error", command=CalcularErrorDesdeInterfaz)
boton_calcular_error.pack()
boton_calcular_error.place(x=425, y=290)

# Etiquetas para los errores
etiqueta_error_relativo = tk.Label(ventana, text="Error Relativo en Porcentaje:",bg='black',fg='white')
etiqueta_error_relativo.pack()
etiqueta_error_relativo.place(x=425, y=330)

label_error_relativo = tk.Label(ventana, text="",bg='black',fg='white')
label_error_relativo.pack()
label_error_relativo.place(x=585, y=330)

etiqueta_error_absoluto = tk.Label(ventana, text="Error Absoluto:",bg='black',fg='white')
etiqueta_error_absoluto.pack()
etiqueta_error_absoluto.place(x=425, y=360)

label_error_absoluto = tk.Label(ventana, text="",bg='black',fg='white')
label_error_absoluto.pack()
label_error_absoluto.place(x=515, y=360)

etiqueta_e = tk.Label(ventana, text="Introducir Intervalo e:")
etiqueta_e.pack()
etiqueta_e.place(x=425, y=470)

cajatext_e = tk.Entry(ventana)
cajatext_e.pack()
cajatext_e.place(x=548, y=470)

explicacion_label = tk.Label(
    ventana,
    text="El programa calcula el valor más cercano a un objetivo conocido (x) \n"
         "con el menor error relativo dentro del rango definido por un margen de error (e).\n"
         "Introduce el margen de error (e) a continuación.",
    font=("Helvetica", 10),
    fg="black"
)
explicacion_label.pack()
explicacion_label.place(x=500, y=400)

resultado_lower_error_label = tk.Label(
    ventana, 
    text="Resultado: --- (valor más cercano con menor error relativo a x)", 
    font=("Helvetica", 12), 
    fg="blue"
)
resultado_lower_error_label.pack()
resultado_lower_error_label.place(x=500, y=436)
resultado_lower_error_label.place(x=600, y=510)

# Función para calcular el valor con el menor error relativo desde la GUI
def CalcularLowerError():
    try:
        x = float(cajatext2.get())  # Obtener el valor de x desde cajatext2
        e = float(cajatext_e.get())  # Obtener el valor de e desde cajatext_e
        mejor_aproximado = numerica.lower_error(x, e)  # Llamar a la función `lower_error` de Numerica
        resultado_lower_error_label.config(text=f"Valor con menor error: {mejor_aproximado:.4f}")
    except ValueError:
        label_error.config(text="Ingrese valores válidos para x y e.")

# Botón para calcular el valor con el menor error relativo
boton_lower_error = tk.Button(ventana, text="Calcular Menor Error Relativo", command=CalcularLowerError)
boton_lower_error.pack()
boton_lower_error.place(x=425, y=510)



#Obtener Texto
def ObtenerTexto(cajatext):
    text = cajatext.get()
    return text

def Graficar():
    try:
         # Obtener datos de la interfaz
        f = Function(ObtenerTexto(cajatext1))  # Asegúrate de que la función f está definida correctamente
        h = float(ObtenerTexto(cajatext4))  # Paso de Runge-Kutta
        puntos_rk = Resolver()  # Obtener puntos de Runge-Kutta desde la función Resolver
        if puntos_rk is None:
            return  # Manejar el caso donde Resolver() falla

        # Preparar datos para la gráfica
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
        V = np.array([f.evaluate(X[i, j], Y[i, j]) for i in range(X.shape[0]) for j in range(X.shape[1])]).reshape(X.shape)
        U2, V2 = U / np.sqrt(U**2 + V**2), V / np.sqrt(U**2 + V**2)

        # Crear la nueva ventana para la gráfica
        ventana_grafica = tk.Toplevel(ventana)
        ventana_grafica.title("Gráfica")
        ventana_grafica.geometry("800x700")

        # Crear la figura de matplotlib
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

        # Integrar la figura en la nueva ventana
        canvas = FigureCanvasTkAgg(fig, master=ventana_grafica)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

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
            print(f"debugging {n}")
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
boton1.place(x=120,y= 250)

#Boton Resolver
boton2 = tk.Button(ventana,text=" Resolver" , command = Resolver,bg='black',fg='white')
boton2.pack()
boton2.place(x=50,y= 250)

# Recuadros Interpolacion
# Primer recuadro x1
txtBox1 = tk.Text(ventana, width=4, height=2, bg='white', fg='black')
txtBox1.pack()
txtBox1.place(x=1020, y=20)

# Segundo recuadro x2
txtBox2 = tk.Text(ventana, width=4, height=2, bg='white', fg='black')
txtBox2.pack()
txtBox2.place(x=1060, y=20)

# Tercer recuadro x3
txtBox3 = tk.Text(ventana, width=4, height=2, bg='white', fg='black')
txtBox3.pack()
txtBox3.place(x=1100, y=20)

# Cuarto recuadro x4
txtBox4 = tk.Text(ventana, width=4, height=2, bg='white', fg='black')
txtBox4.pack()
txtBox4.place(x=1140, y=20)

# Quinto recuadro x5
txtBox5 = tk.Text(ventana, width=4, height=2, bg='white', fg='black')
txtBox5.pack()
txtBox5.place(x=1180, y=20)

# Primer recuadro f1
txtBoxF1 = tk.Text(ventana, width=4, height=2, bg='white', fg='black')
txtBoxF1.pack()
txtBoxF1.place(x=1020, y=70)

# Segundo recuadro f2
txtBoxF2 = tk.Text(ventana, width=4, height=2, bg='white', fg='black')
txtBoxF2.pack()
txtBoxF2.place(x=1060, y=70)

# Tercer recuadro f3
txtBoxF3 = tk.Text(ventana, width=4, height=2, bg='white', fg='black')
txtBoxF3.pack()
txtBoxF3.place(x=1100, y=70)

# Cuarto recuadro f4
txtBoxF4 = tk.Text(ventana, width=4, height=2, bg='white', fg='black')
txtBoxF4.pack()
txtBoxF4.place(x=1140, y=70)

# Quinto recuadro f5
txtBoxF5 = tk.Text(ventana, width=4, height=2, bg='white', fg='black')
txtBoxF5.pack()
txtBoxF5.place(x=1180, y=70)

# Función para obtener los valores de los recuadros x1, x2, x3, x4, x5 y f1, f2, f3, f4, f5
def obtener_valores_recuadros():
    valores_x = []
    valores_f = []

    # Lista de los recuadros de texto x1, x2, x3, x4, x5
    for txtBox in [txtBox1, txtBox2, txtBox3, txtBox4, txtBox5]:
        texto = txtBox.get("1.0", "end-1c").strip()  
        try:
            valores_x.append(int(texto))
        except ValueError:
            valores_x.append(0)  

    # Lista de los recuadros de texto f1, f2, f3, f4, f5
    for txtBox in [txtBoxF1, txtBoxF2, txtBoxF3, txtBoxF4, txtBoxF5]:
        texto = txtBox.get("1.0", "end-1c").strip()  
        try:
            valores_f.append(int(texto))
        except ValueError:
            valores_f.append(0) 

    return valores_x, valores_f

xi, fi = obtener_valores_recuadros()

# Función de interpolación 
def interpolar():
    xi, fi = obtener_valores_recuadros()
    print("Valores de xi:", xi)
    print("Valores de fi:", fi)
    
    polynomial = interpolation.calculate_newton_method(xi, fi)
    
    print("Polinomio de interpolación:", polynomial)


# Botón para realizar la interpolación
btnInterpolar = tk.Button(ventana, text="Interpolar", command=interpolar)
btnInterpolar.pack()
btnInterpolar.place(x=1240, y=25)

ventana.mainloop()