import tkinter as tk
from tkinter import ttk
from Function import Function
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import sys
import os
from PIL import Image, ImageTk 
from numerica import Numerica as n
from Interpolation import Interpolation as interpolation
import sympy as sym


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
etiqueta = tk.Label(ventana,text= " dy/dx : ",bg='black',fg='white',font=("Helvetica", 10, "bold"))
etiqueta.pack()
etiqueta.place(x = 40 , y = 30)
#Caja de Texto
cajatext1 = tk.Entry(ventana,bg='black',fg='white')
cajatext1.pack()
cajatext1.place(x=100 , y = 30)

#Etiqueta 2
etiqueta2 = tk.Label(ventana,text=" Xo :",bg='black',fg='white',font=("Helvetica", 10, "bold"))
etiqueta2.pack()
etiqueta2.place(x = 50 , y = 70)
#Caja de Texto 2
cajatext2 = tk.Entry(ventana,bg='black',fg='white')
cajatext2.pack()
cajatext2.place(x=100 , y = 70)

#Etiqueta 3
etiqueta3 = tk.Label(ventana,text=" Yo :",bg='black',fg='white',font=("Helvetica", 10, "bold"))
etiqueta3.pack()
etiqueta3.place(x = 50 , y = 110)
#Caja de Texto 3
cajatext3 = tk.Entry(ventana,bg='black',fg='white')
cajatext3.pack()
cajatext3.place(x=100 , y = 110)

#Etiqueta 4
etiqueta4 = tk.Label(ventana,text=" H :",bg='black',fg='white',font=("Helvetica", 10, "bold"))
etiqueta4.pack()
etiqueta4.place(x = 50 , y = 150)
#Caja de Texto 4
cajatext4 = tk.Entry(ventana,bg='black',fg='white')
cajatext4.pack()
cajatext4.place(x=100 , y = 150)

#Etiqueta 5
etiqueta5 = tk.Label(ventana,text=" xi :",bg='black',fg='white',font=("Helvetica", 10, "bold"))
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
respuesta_frame = ttk.Frame(ventana, relief="sunken", borderwidth=1)
respuesta_frame.pack(pady=10, side=tk.BOTTOM, anchor=tk.CENTER)
respuesta_frame.place(x=50,y=300)
respuesta_frame.place_forget()

respuesta_label = ttk.Label(respuesta_frame, text="", wraplength=300, justify="left")
respuesta_label.pack(padx=40, pady=40)


# Función para obtener el epsilon de la máquina
def VerEpsilon():
    epsilon = numerica.obtener_epsilon()  # Usar método estático de la clase Numerica
    label_epsilon.config(text=f"Epsilon de la máquina: {epsilon:.16f}")
    label_epsilon.place(x=1150, y=30)  

manejo_errores_label = tk.Label(ventana, text="Manejo de errores:", font=("Helvetica", 14, "bold italic"), bg="black", fg="white")
manejo_errores_label.pack() 
manejo_errores_label.place(x=800, y=30)  

# Botón para ver el epsilon de la máquina
boton_epsilon = tk.Button(ventana, text="Ver Epsilon de la máquina", command=VerEpsilon,bg='black',fg='white')
boton_epsilon.pack()
boton_epsilon.place(x=995, y=30)

# Etiqueta para mostrar el valor del epsilon, colocada justo al lado del botón
label_epsilon = tk.Label(ventana, text="", font=("Helvetica", 12), fg="white" , bg='black')
label_epsilon.pack()
label_epsilon.place(x=1150, y=30)  
label_epsilon.place_forget()


# Etiqueta para introducir el valor real
etiqueta_real = tk.Label(ventana, text="Introducir Valor Real:",bg='black',fg='white')
etiqueta_real.pack()
etiqueta_real.place(x=800, y=80)

# Caja de texto para el valor real
cajatext_real = tk.Entry(ventana,bg='black',fg='white')
cajatext_real.pack()
cajatext_real.place(x=920, y=80)

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
            label_error_relativo.place(x=960, y=165)
            label_error_absoluto.place(x=890, y=195)
        else:
            label_error.config(text="Primero resuelva la EDO para calcular los errores.")
    except ValueError:
        label_error.config(text="Ingrese un valor numérico válido para el valor real.")

# Botón para calcular el error
boton_calcular_error = tk.Button(ventana, text="Calcular Error", command=CalcularErrorDesdeInterfaz, bg='black',fg='white',font=("Helvetica", 12, "bold"))
boton_calcular_error.pack()
boton_calcular_error.place(x=800, y=125)

# Etiquetas para los errores
etiqueta_error_relativo = tk.Label(ventana, text="Error Relativo en Porcentaje:",bg='black',fg='white')
etiqueta_error_relativo.pack()
etiqueta_error_relativo.place(x=800, y=165)

label_error_relativo = tk.Label(ventana, text="",bg='black',fg='white')
label_error_relativo.pack()
label_error_relativo.place(x=960, y=165)
label_error_relativo.place_forget()

etiqueta_error_absoluto = tk.Label(ventana, text="Error Absoluto:",bg='black',fg='white')
etiqueta_error_absoluto.pack()
etiqueta_error_absoluto.place(x=800, y=195)

label_error_absoluto = tk.Label(ventana, text="",bg='black',fg='white')
label_error_absoluto.pack()
label_error_absoluto.place(x=890, y=195)
label_error_absoluto.place_forget()

etiqueta_e = tk.Label(ventana, text="Introducir Intervalo e:",bg='black',fg='white')
etiqueta_e.pack()
etiqueta_e.place(x=800, y=330)

cajatext_e = tk.Entry(ventana)
cajatext_e.pack()
cajatext_e.place(x=925, y=330)

explicacion_label = tk.Label(
    ventana,
    text="El programa calcula el valor más cercano a un objetivo conocido (x) \n"
         "con el menor error relativo dentro del rango definido por un margen de error (e).\n"
         "Introduce el margen de error (e) a continuación.",
    font=("Helvetica", 10),
    fg="black"
)
explicacion_label.pack()
explicacion_label.place(x=850, y=250)

resultado_lower_error_label = tk.Label(
    ventana, 
    text="Resultado: --- (valor más cercano con menor error relativo a x)", 
    font=("Helvetica", 12), 
    fg="blue"
)
resultado_lower_error_label.pack()
resultado_lower_error_label.place(x=500, y=436)
resultado_lower_error_label.place(x=970, y=370)

# Función para calcular el valor con el menor error relativo desde la GUI
def CalcularLowerError():
    try:
        a = Resolver()
        # print(f"a: {a}")
        x = a[len(a) - 1][1]  # Obtener el valor de x desde cajatext2
        # print(f"x: {x}")
        e = float(cajatext_e.get())  # Obtener el valor de e desde cajatext_e
        mejor_aproximado = numerica.lower_error(x, e)  # Llamar a la función `lower_error` de Numerica
        resultado_lower_error_label.config(text=f"Valor con menor error: {mejor_aproximado:.4f}")
    except ValueError:
        label_error.config(text="Ingrese valores válidos para x y e.")

# Botón para calcular el valor con el menor error relativo
boton_lower_error = tk.Button(ventana, text="Calcular Menor Error Relativo:", command=CalcularLowerError, bg='black',fg='white', font=("Helvetica", 12, "bold"))
boton_lower_error.pack()
boton_lower_error.place(x=715, y=370)



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
        # Limpia posibles mensajes de error y oculta el frame de la respuesta
        label_error.config(text="")
        respuesta_label.config(text="")
        respuesta_frame.place_forget()

        # Obtén los valores ingresados en la interfaz
        Xo = float(ObtenerTexto(cajatext2))
        Yo = float(ObtenerTexto(cajatext3))
        H = float(ObtenerTexto(cajatext4))
        f = Function(ObtenerTexto(cajatext1))
        xi = float(ObtenerTexto(cajatext5))

        respuesta = n.runge_kutta_4(f, Xo, Yo, H, xi)



        # Muestra el último punto de la solución en respuesta_label
        ultimo_punto = respuesta[-1]
        texto_respuesta = f"""Solución por el método Runge-Kutta:
x = {ultimo_punto[0]:.2f}
y = {ultimo_punto[1]:.2f}"""
        respuesta_label.config(text=texto_respuesta, font=("Helvetica", 18))  # Letra más grande

        # Ajusta dinámicamente el tamaño del frame al texto
        respuesta_label.update_idletasks()  # Asegura que el tamaño requerido se calcule
        width = respuesta_label.winfo_reqwidth() + 100
        height = respuesta_label.winfo_reqheight() + 100
        respuesta_frame.config(width=width, height=height)

        # Muestra el frame de respuesta
        respuesta_frame.place(x=50, y=300)

        return respuesta

    except ValueError:
        label_error.config(text="Error: Ingrese valores numéricos válidos.")
        return None
    except Exception as e:
        label_error.config(text=f"Ocurrió un error: {e}")
        return None


#Boton Graficar
boton1 = tk.Button(ventana,text=" Graficar" , command = Graficar,bg='black',fg='white',font=("Helvetica", 12, "bold"))
boton1.pack()
boton1.place(x=150,y= 250)

#Boton Resolver
boton2 = tk.Button(ventana,text=" Resolver" , command = Resolver,bg='black',fg='white',font=("Helvetica", 12, "bold"))
boton2.pack()
boton2.place(x=50,y= 250)

manejo_errores_label = tk.Label(ventana, text="INTERPOLACION:", font=("Helvetica", 14, "bold italic"), bg="black", fg="white")
manejo_errores_label.pack() 
manejo_errores_label.place(x=800, y=430)  

# Recuadros Interpolacion

#Etiqueta xi
etiquetaxi = tk.Label(ventana,text=" Xi",bg='black',fg='white', font=("Helvetica", 10, "bold"))
etiquetaxi.pack()
etiquetaxi.place(x = 773 , y = 477)
#Etiqueta f(xi)
etiquetaFxi = tk.Label(ventana,text=" f(Xi)",bg='black',fg='white', font=("Helvetica", 10, "bold"))
etiquetaFxi.pack()
etiquetaFxi.place(x = 760 , y = 522)

# Primer recuadro x1
txtBox1 = tk.Text(ventana, width=4, height=2, bg='white', fg='black')
txtBox1.pack()
txtBox1.place(x=800, y=470)

# Segundo recuadro x2
txtBox2 = tk.Text(ventana, width=4, height=2, bg='white', fg='black')
txtBox2.pack()
txtBox2.place(x=840, y=470)

# Tercer recuadro x3
txtBox3 = tk.Text(ventana, width=4, height=2, bg='white', fg='black')
txtBox3.pack()
txtBox3.place(x=880, y=470)

# Cuarto recuadro x4
txtBox4 = tk.Text(ventana, width=4, height=2, bg='white', fg='black')
txtBox4.pack()
txtBox4.place(x=920, y=470)

# Quinto recuadro x5
txtBox5 = tk.Text(ventana, width=4, height=2, bg='white', fg='black')
txtBox5.pack()
txtBox5.place(x=960, y=470)

# Primer recuadro f1
txtBoxF1 = tk.Text(ventana, width=4, height=2, bg='white', fg='black')
txtBoxF1.pack()
txtBoxF1.place(x=800, y=515)

# Segundo recuadro f2
txtBoxF2 = tk.Text(ventana, width=4, height=2, bg='white', fg='black')
txtBoxF2.pack()
txtBoxF2.place(x=840, y=515)

# Tercer recuadro f3
txtBoxF3 = tk.Text(ventana, width=4, height=2, bg='white', fg='black')
txtBoxF3.pack()
txtBoxF3.place(x=880, y=515)

# Cuarto recuadro f4
txtBoxF4 = tk.Text(ventana, width=4, height=2, bg='white', fg='black')
txtBoxF4.pack()
txtBoxF4.place(x=920, y=515)

# Quinto recuadro f5
txtBoxF5 = tk.Text(ventana, width=4, height=2, bg='white', fg='black')
txtBoxF5.pack()
txtBoxF5.place(x=960, y=515)

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

# Variable global para almacenar el polinomio como función evaluable
funcion_polinomio = None  # Esto será una función lambda evaluable
xi, fi = [], []  # Variables para los puntos originales

# Función de interpolación 
def interpolar():
    global funcion_polinomio, xi, fi
    try:
        # Obtener valores de los recuadros de entrada
        xi, fi = obtener_valores_recuadros()
               
        # Calcular el polinomio de interpolación
        polinomio_simbolico = interpolation.calculate_newton_method(xi, fi)
        
        # Convertir el polinomio simbólico a una función evaluable
        x = sym.Symbol('x')
        funcion_polinomio = sym.lambdify(x, polinomio_simbolico, "numpy")
        
        # Mostrar el polinomio en el Label
        label_polinomio.config(
            text=f"Polinomio de interpolación:\n{polinomio_simbolico}", 
            font=("Helvetica", 12),
            fg="black"
        )
        label_polinomio.place(x=800, y=555)  # Mostrar el Label
    except Exception as e:
        label_polinomio.config(
            text=f"Error: {e}",
            font=("Helvetica", 12),
            fg="red"
        )
        label_polinomio.place(x=800, y=555)  # Mostrar el error

# Función para graficar el polinomio en una ventana aparte
def graficar_polinomio():
    global funcion_polinomio, xi, fi
    try:
        # Validar si el polinomio fue calculado
        if funcion_polinomio is None:
            raise ValueError("Primero debes calcular el polinomio de interpolación.")
        
        # Generar puntos para graficar el polinomio
        x_vals = np.linspace(min(xi)-5, max(xi)+5, 1000)  # Valores equidistantes entre los puntos originales
        y_vals = funcion_polinomio(x_vals)  # Evaluar el polinomio en estos puntos
        
        # Crear una nueva ventana para la gráfica
        plt.figure("Gráfico del Polinomio de Interpolación", figsize=(8, 6))
        plt.plot(x_vals, y_vals, label="Polinomio de Interpolación", color="blue")
        plt.scatter(xi, fi, color="red", label="Puntos originales")  # Los puntos dados
        plt.title("Polinomio de Interpolación")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.grid(True)
        plt.legend()
        plt.show()

    except Exception as e:
        # Manejo de errores en la gráfica
        label_polinomio.config(
            text=f"Error al graficar: {e}",
            font=("Helvetica", 12),
            fg="red"
        )
        label_polinomio.place(x=800, y=555)

# Label para mostrar el resultado del polinomio
label_polinomio = tk.Label( ventana, text="", font=("Helvetica", 12), bg="white", fg="black",  wraplength=300, justify="left")
label_polinomio.pack()
label_polinomio.place_forget()  # Ocultar inicialmente

# Botón para realizar la interpolación
btnInterpolar = tk.Button(ventana, text="Interpolar", command=interpolar, bg='black', fg='white',font=("Helvetica", 12, "bold"))
btnInterpolar.pack()
btnInterpolar.place(x=1010, y=475)

# Botón para graficar la interpolación
btnGraficarInter = tk.Button(ventana, text="Graficar", command=graficar_polinomio,  bg='black', fg='white',font=("Helvetica", 12, "bold"))
btnGraficarInter.pack()
btnGraficarInter.place(x=1105, y=475)

ventana.mainloop()