import tkinter as tk
from PIL import ImageTk, Image
import time
from servicios import *
from extras import *

# Ventana principal
ventana = tk.Tk()
ventana.title("Recepción Spa")
ventana.geometry("1000x800")
ventana.configure(background="lightblue")
ventana.iconbitmap("MiniProyectoSpa\Imagenes\spalogonegro.ico")

# Imagen de fondo
logo = Image.open("MiniProyectoSpa\Imagenes\spalogo.png")
logo = logo.resize((1000, 800))
logo_fondo = ImageTk.PhotoImage(logo)
label_fondo = tk.Label(ventana, image=logo_fondo, bg="lightblue")
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

# Ingreso de cliente
nombre_cliente = tk.StringVar()
ingreso_cliente = tk.Entry(ventana, width=30, textvariable=nombre_cliente, font=("Arial", 14, "bold"), justify="center", background="lightblue", borderwidth=3)
ingreso_cliente.grid(row=0, column=0, columnspan=1, padx=10, pady=10)
nombre_cliente.set("Nombre del Cliente")

# Botón para agregar cliente
def agregar_cliente():
    tarea = ingreso_cliente.get()
    if tarea:
        lista_cliente.insert(tk.END, tarea)
    ingreso_cliente.delete(0, tk.END)

boton_agregar = tk.Button(ventana, text="✔", command=agregar_cliente, font=("Arial", 10), justify="center", background="lightblue", borderwidth=3, width=2, height=1)
boton_agregar.grid(row=0, column=1, columnspan=1, padx=10, pady=10)

lista_cliente = tk.Listbox(ventana, width=30, height=1, font=("Arial", 14, "bold"), justify="center", background="lightblue", borderwidth=3)
lista_cliente.grid(row=2, column=0, columnspan=1, padx=10, pady=200,sticky="s")

def eliminar_tarea():
    seleccion = lista_cliente.curselection()
    if seleccion:
        lista_cliente.delete(seleccion)

boton_eliminar = tk.Button(ventana, text='✖', command=eliminar_tarea, font=("Arial", 10,), justify="center", background="lightblue", borderwidth=3, width=2, height=1)
boton_eliminar.grid(row=2, column=1, columnspan=1, padx=10, pady=200,sticky="s")

# Reloj
reloj = tk.Label(ventana, font=('Arial', 45, "bold"), bg='lightblue', fg='black')

def hora():
    tiempo_actual = time.strftime('%H:%M:%S')
    reloj.config(text=tiempo_actual)
    ventana.after(1000, hora)

reloj.grid(row=0, column=3, columnspan=1, padx=200, pady=10,sticky="w")
hora()

# Temporizador
tiempo_total = 0
label_tiempo = tk.Label(ventana, text="00:00:00", font=("Arial", 45, "bold"), bg="lightblue",borderwidth=3)
# label_tiempo.grid(row=2, column=4, columnspan=1, padx=200, pady=300)
label_tiempo.grid(row=3, column=3, columnspan=1, padx=200, pady=0,sticky="ne")


# Función para actualizar el temporizador
def actualizar_tiempo():
    global tiempo_total
    if tiempo_total > 0:
        tiempo_total -= 1
        horas, resto = divmod(tiempo_total, 3600)  # Calcula horas y el resto en segundos
        minutos, segundos = divmod(resto, 60)     # Calcula minutos y segundos a partir del resto
        label_tiempo.config(text=f"{horas:02}:{minutos:02}:{segundos:02}")
        ventana.after(1000, actualizar_tiempo)
    else:
        label_tiempo.config(text="00:00:00")

# Función para iniciar el temporizador
def iniciar_temporizador():
    actualizar_tiempo()

# Botón para iniciar el temporizador
boton_iniciar = tk.Button(ventana, text="▶", command=iniciar_temporizador, font=("Arial", 26, "bold"), bg="lightblue", borderwidth=3)
# boton_iniciar.grid(row=2, column=2, columnspan=1, padx=0, pady=100)
boton_iniciar.grid(row=3, column=3, columnspan=1, padx=150, pady=0,sticky="nw")

# agregar tiempo al temporizador
def agregar_tiempo(valor):
    global tiempo_total
    tiempo_total +=(valor+5) * 60 
    horas, resto = divmod(tiempo_total, 3600)
    minutos, segundos = divmod(resto, 60)
    label_tiempo.config(text=f"{horas:02}:{minutos:02}:{segundos:02}")

# Menú desplegable de servicios
boton_menu = tk.Menubutton(ventana, text='Servicios Principales', relief=tk.RAISED, width=30, height=1, font=("Arial", 14, "bold"), justify="center", background="lightblue", borderwidth=3)
boton_menu.grid(row=1, column=0, padx=20, pady=20)

menu_principal = tk.Menu(boton_menu, tearoff=0, relief=tk.RAISED, font=("Arial", 14, "bold"), background="lightblue", borderwidth=3)
boton_menu.config(menu=menu_principal)

servicios = {'Manos': Manos, 'Pies': Pies, 'Cutis': Cutis, 'Masajes': Masajes}

for categoria, opciones in servicios.items():
    submenu = tk.Menu(menu_principal, tearoff=0, relief=tk.RAISED, font=("Arial", 14, "bold"), background="lightblue", borderwidth=3)
    menu_principal.add_cascade(label=categoria, menu=submenu)

    for llave, valor in opciones.items():
        submenu.add_command(label=f"{llave}: {valor} minutos", command=lambda valor=valor: agregar_tiempo(valor))

ventana.mainloop()