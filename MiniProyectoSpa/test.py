import tkinter as tk

# ----------------------------------------------------------------------------------------------------------------------------------------------
# Ventana principal
ventana = tk.Tk()
ventana.title("Recepción Spa")
ventana.geometry("500x400")
ventana.configure(background="lightblue")

# ----------------------------------------------------------------------------------------------------------------------------------------------
# Ingreso de cliente
nombre_cliente = tk.StringVar()

ingreso_cliente = tk.Entry(ventana, width=30, textvariable=nombre_cliente, font=("Arial", 14, "bold"), justify="center", background="lightblue", borderwidth=3)
ingreso_cliente.place(x=10, y=10)
nombre_cliente.set("Nombre del Cliente")

# ----------------------------------------------------------------------------------------------------------------------------------------------
# Botón para agregar cliente
def agregar_cliente():
    tarea = ingreso_cliente.get()
    if tarea:
        lista_cliente.insert(tk.END, tarea)
        ingreso_cliente.delete(0, tk.END)

boton_agregar = tk.Button(ventana, text="✔", command=agregar_cliente, font=("Arial", 10), justify="center", background="lightblue", borderwidth=3, width=2, height=1, state=tk.DISABLED)
boton_agregar.place(x=360, y=10)

# ----------------------------------------------------------------------------------------------------------------------------------------------
# Nombre del cliente
lista_cliente = tk.Listbox(ventana, width=30, height=1, font=("Arial", 14, "bold"), justify="center", background="lightblue", borderwidth=3)
lista_cliente.place(x=10, y=50)

# ----------------------------------------------------------------------------------------------------------------------------------------------
# Función para habilitar/deshabilitar el botón según el contenido del campo de entrada
def validar_entrada(*args):
    if nombre_cliente.get().strip():  # Si no está vacío, habilitar el botón
        boton_agregar.config(state=tk.NORMAL)
    else:  # Si está vacío, deshabilitar el botón
        boton_agregar.config(state=tk.DISABLED)

# Monitorea cambios en el campo de texto
nombre_cliente.trace_add("write", validar_entrada)

# ----------------------------------------------------------------------------------------------------------------------------------------------
ventana.mainloop()