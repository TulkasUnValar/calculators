import tkinter as tk
from tkinter import ttk
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from random import uniform

# --------------------------------------------BackEnd-------------------------------------
def calculate_integral():
    # Usuario ingresa valores
    funtion = funtion_input.get()
    a = float(a_input.get())
    b = float(b_input.get())
    n = int(n_input.get())

    integral_value_answer.delete(0, tk.END)
    error_answer.delete(0, tk.END)    

    # Definir el símbolo x y la función f(x)
    x = sp.symbols('x')
    f_x = sp.sympify(funtion)

    try:
        # Calcular el ancho de cada partición
        delta_x = (b - a) / n

        # Calcular la integral por Simpson 1/3
        simpson_result = 0
        for i in range(n):
            x_left = a + i * delta_x
            x_right = a + (i + 1) * delta_x
            x_middle = a + (i + 0.5) * delta_x
            simpson_result += (delta_x / 6) * (sp.integrate(f_x.subs(x, x_left), (x, x_left, x_right)) + 4 * sp.integrate(f_x.subs(x, x_middle), (x, x_left, x_right)) + sp.integrate(f_x.subs(x, x_right), (x, x_left, x_right)))

        # Calcular error
        h = (b - a) / 2
        fourth_derivative = sp.diff(f_x, x, 4)
        random_num = a + uniform(a, b) * (b - a)
        error_result = - ((h**5) / 90) * fourth_derivative * random_num
       
        # Mostrar resultado en la interfaz gráfica
        integral_value_answer.insert(tk.INSERT, string=simpson_result)
        error_answer.insert(tk.INSERT, string=error_result)

        # Crear gráfica de la función en el intervalo dado
        x_vals = np.linspace(a, b, 400)
        f = sp.lambdify(x, f_x, 'numpy')
        y_vals = f(x_vals)

        plt.figure(figsize=(8, 6))
        plt.plot(x_vals, y_vals, label=f'f(x) = {funtion}')
        plt.fill_between(x_vals, y_vals, alpha=0.3)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.grid(True)
        plt.show()

    except ValueError:
        error = tk.Label(frame, text="Input error", font=('Candara', 8))
        error.grid(row=3, column=0, padx=10, pady=5)

# Función clear_results, se ejecuta con botton Clear
def clear_display():
    funtion_input.delete(0, tk.END)
    a_input.delete(0, tk.END)
    b_input.delete(0, tk.END)
    n_input.delete(0, tk.END)
    integral_value_answer.delete(0, tk.END)
    error_answer.delete(0, tk.END)

# --------------------------------------------------------FrontEnd------------------------------------------------------
# Configurar ventana tkinter
window = tk.Tk()
window.title("Interation by Simpson 1/3")
#window.geometry("800x600")
frame = tk.Frame(window)
frame.pack()

# Marco usuario
user_input_frame = tk.LabelFrame(frame, text="User input")
user_input_frame.grid(row=0, column=0, padx=20, pady=20)

# Imprime Funtion f(x):
label_funtion = tk.Label(user_input_frame, text="Funtion f(x):")
label_funtion.grid(row=0, column=0, padx=10, pady=5)
# Entrada función de usuario
funtion_input = tk.Entry(user_input_frame)
funtion_input.grid(row=0, column=1, padx=10, pady=5)

# Imprime leftmost (a):
label_a = tk.Label(user_input_frame, text="Leftmost value (a):")
label_a.grid(row=1, column=0, padx=10, pady=5)
# Entrada usuario leftmost (a)
a_input = tk.Entry(user_input_frame)
a_input.grid(row=1, column=1, padx=10, pady=5)

# Imprime Rightmost value (b):
label_b = tk.Label(user_input_frame, text="Rightmost value (b):")
label_b.grid(row=2, column=0, padx=10, pady=5)
# Entrada de usuario Rightmost (b)
b_input = tk.Entry(user_input_frame)
b_input.grid(row=2, column=1, padx=10, pady=5)

# Imprime Num of partitions (n):
label_n = tk.Label(user_input_frame, text="Num of partitions (n):")
label_n.grid(row=3, column=0, padx=10, pady=5)
# Entrada de usuario Num of partitions (n)
n_input = tk.Entry(user_input_frame)
n_input.grid(row=3, column=1, padx=10, pady=5)

# Marco respuestas
answer_frame = tk.LabelFrame(frame, text="Answers")
answer_frame.grid(row=1, column=0, padx=10, pady=5)

# Imprime en ventana "Integral"
integral_label = tk.Label(answer_frame, text="Integral = ######")
integral_label.grid(row=0, column=0, padx=10, pady=5)

# Imprime en ventana "Integral value"
integral_value_label = tk.Label(answer_frame, text="Integral value")
integral_value_label.grid(row=1, column=0, padx=10, pady=5)
# Respuesta Binario
integral_value_answer = tk.Entry(answer_frame, width=30)
integral_value_answer.grid(row=1, column=1, padx=10, pady=5)

# Imprime en ventana "Error"
error_label = tk.Label(answer_frame, text="Error")
error_label.grid(row=2, column=0, padx=10, pady=5)
# Respuesta Error
error_answer = tk.Entry(answer_frame, width=30)
error_answer.grid(row=2, column=1, padx=10, pady=5)

# Marco opciones
options_frame = tk.LabelFrame(frame, text="Options")
options_frame.grid(row=2, column=0, padx=10, pady=5)
# Botón covertir, función submit
convert_button = tk.Button(options_frame, text="Convert", command=calculate_integral, font=('Candara', 12, 'bold'), state=tk.ACTIVE)
convert_button.grid(row=0, column=0, padx=10, pady=5)
# Boton borrar
clear_button = tk.Button(options_frame, text="Clear", command=lambda: clear_display(), font=('Candara', 12, 'bold'), state=tk.ACTIVE)
clear_button.grid(row=0,column=1,padx=10,pady=5)
# Boton exit
exit_button = tk.Button(options_frame, text="Exit", command=frame.quit, font=('Candara', 12, 'bold'), state=tk.ACTIVE)
exit_button.grid(row=0, column=2, padx=10, pady=5)
# Ejecutar la aplicación

window.mainloop()