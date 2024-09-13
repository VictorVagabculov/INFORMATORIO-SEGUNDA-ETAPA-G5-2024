import tkinter as tk

# ----------------------------------------------------------------------------------------------------------------------------------------------
# Ventana principal
ventana = tk.Tk()
ventana.title("Recepción Spa")
ventana.geometry("500x400")
ventana.configure(background="lightblue")

# ----------------------------------------------------------------------------------------------------------------------------------------------
# Ingreso de número (solo números permitidos)
numero_box = tk.StringVar()  # Utiliza StringVar para mayor flexibilidad en la validación
ingreso_box = tk.Entry(ventana, width=6, textvariable=numero_box, font=("Arial", 14, "bold"), justify="center", background="lightblue", borderwidth=3)
ingreso_box.place(x=400, y=10)   
numero_box.set("Box n°")

# Función para validar que solo se ingresen números
def solo_numeros(char):
    return char.isdigit() or char == ""  # Permitir números y el vacío (cuando se borra el texto)

# Configurar la validación
validacion_numerica = ventana.register(solo_numeros)
ingreso_box.config(validate="key", validatecommand=(validacion_numerica, '%P'))  # %P es el contenido actual del Entry después del cambio

# ----------------------------------------------------------------------------------------------------------------------------------------------
ventana.mainloop()