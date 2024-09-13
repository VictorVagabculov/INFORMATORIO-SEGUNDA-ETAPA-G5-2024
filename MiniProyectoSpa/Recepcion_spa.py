import tkinter as tk
from PIL import ImageTk, Image
import time
from servicios import *
from extras import *

# ----------------------------------------------------------------------------------------------------------------------------------------------
# Ventana principal
ventana = tk.Tk()
ventana.title("Recepción Spa")
ventana.geometry("1000x800")
ventana.configure(background="lightblue")
ventana.iconbitmap("MiniProyectoSpa/Imagenes/spalogonegro.ico")

# Imagen de fondo
logo = Image.open("MiniProyectoSpa/Imagenes/spalogo.png")
logo = logo.resize((1000, 800))
logo_fondo = ImageTk.PhotoImage(logo)
label_fondo = tk.Label(ventana, image=logo_fondo, bg="lightblue")
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

# ----------------------------------------------------------------------------------------------------------------------------------------------
# Ingreso de cliente
nombre_cliente = tk.StringVar()
ingreso_cliente = tk.Entry(ventana, width=30, textvariable=nombre_cliente, font=("Arial", 14, "bold"), justify="center", background="lightblue", borderwidth=3)
ingreso_cliente.place(x=10, y=10)   
nombre_cliente.set("Nombre del Cliente")
# -----------------------------------------------------------------------------------------------------------------------------------------------
# Botón para agregar cliente
def agregar_cliente():
    tarea = ingreso_cliente.get()
    if tarea:
        lista_cliente.insert(tk.END, tarea)
    ingreso_cliente.delete(0, tk.END)

boton_agregar = tk.Button(ventana, text="✔", command=agregar_cliente, font=("Arial", 10), justify="center", background="lightblue", borderwidth=3, width=2, height=1)
boton_agregar.place(x=360, y=10)   
# ----------------------------------------------------------------------------------------------------------------------------------------------
# Nombre del cliente
lista_cliente = tk.Listbox(ventana, width=30, height=1, font=("Arial", 14, "bold"), justify="center", background="lightblue", borderwidth=3)
lista_cliente.place(x=10, y=400)   
# ----------------------------------------------------------------------------------------------------------------------------------------------
# Boton de eliminar
def eliminar_tarea():
    seleccion = lista_cliente.curselection() or lista_servicios.curselection() or lista_extras.curselection()
    if seleccion:
        lista_cliente.delete(seleccion) or lista_servicios.delete(seleccion) or lista_extras.delete(seleccion)

boton_eliminar = tk.Button(ventana, text='✖', command=eliminar_tarea, font=("Arial", 10,), justify="center", background="lightblue", borderwidth=3, width=2, height=1)
boton_eliminar.place(x=360, y=400)   

# ----------------------------------------------------------------------------------------------------------------------------------------------
# Reloj
reloj = tk.Label(ventana, font=('Arial', 45, "bold"), bg='lightblue', fg='black')

def hora():
    tiempo_actual = time.strftime('%H:%M:%S')
    reloj.config(text=tiempo_actual)
    ventana.after(1000, hora)

reloj.place(x=700, y=10)   
hora()

# ----------------------------------------------------------------------------------------------------------------------------------------------
# Temporizador
tiempo_total = 0
label_tiempo = tk.Label(ventana, text="00:00:00", font=("Arial", 45, "bold"), bg="lightblue", borderwidth=3)
label_tiempo.place(x=700, y=500)   

# Función para actualizar el temporizador
def actualizar_tiempo():
    global tiempo_total
    if tiempo_total > 0:
        tiempo_total -= 1
        horas, resto = divmod(tiempo_total, 3600) 
        minutos, segundos = divmod(resto, 60)    
        label_tiempo.config(text=f"{horas:02}:{minutos:02}:{segundos:02}")
        ventana.after(1000, actualizar_tiempo)
    else:
        label_tiempo.config(text="00:00:00")
# -----------------------------------------------------------------------------------------------------------------------------------------------
# Hora de salida
# Etiqueta para la hora de salida
label_hora_salida = tk.Label(ventana, text="Hora de salida: --:--:--", font=("Arial", 23, "bold"), bg="lightblue", fg='black')
label_hora_salida.place(x=645, y=450)   

# Función para calcular la hora de salida
def calcular_hora_salida():
    tiempo_actual = time.time() 
    tiempo_salida = tiempo_actual + tiempo_total 
    hora_salida = time.strftime('%H:%M:%S', time.localtime(tiempo_salida)) 
    label_hora_salida.config(text=f"Hora de salida: {hora_salida}")
# ------------------------------------------------------------------------------------------------------------------------------------------------
# Función para iniciar el temporizador
def iniciar_temporizador():
    calcular_hora_salida() 
    actualizar_tiempo()
    boton_iniciar.config(state=tk.DISABLED)

# Botón para iniciar el temporizador
boton_iniciar = tk.Button(ventana, text="▶", command=iniciar_temporizador, font=("Arial", 28, "bold"), bg="lightblue", borderwidth=3)
boton_iniciar.place(x=645, y=500)   

# Agregar tiempo al temporizador
def agregar_tiempo(valor):
    global tiempo_total
    tiempo_total += (valor + 5) * 60 
    horas, resto = divmod(tiempo_total, 3600)
    minutos, segundos = divmod(resto, 60)
    label_tiempo.config(text=f"{horas:02}:{minutos:02}:{segundos:02}")
    calcular_hora_salida()

# ----------------------------------------------------------------------------------------------------------------------------------------------
# Menú desplegable de servicios
boton_menu_servicios = tk.Menubutton(ventana, text='Servicios Principales', relief=tk.RAISED, width=30, height=1, font=("Arial", 14, "bold"), justify="center", background="lightblue", borderwidth=3)
boton_menu_servicios.place(x=10, y=100)   

menu_principal_servicios = tk.Menu(boton_menu_servicios, tearoff=0, relief=tk.RAISED, font=("Arial", 14, "bold"), background="lightblue", borderwidth=3)
boton_menu_servicios.config(menu=menu_principal_servicios)

servicios = {'Manos': Manos, 'Pies': Pies, 'Cutis': Cutis, 'Masajes': Masajes}

for categoria, opciones in servicios.items():
    submenu_servicios = tk.Menu(menu_principal_servicios, tearoff=0, relief=tk.RAISED, font=("Arial", 14, "bold"), background="lightblue", borderwidth=3)
    menu_principal_servicios.add_cascade(label=categoria, menu=submenu_servicios)

    for llave, valor in opciones.items():
        submenu_servicios.add_command(label=f"{llave}: {valor} minutos", command=lambda valor=valor, llave=llave: (agregar_tiempo(valor), lista_servicios.insert(tk.END, llave)))

# ----------------------------------------------------------------------------------------------------------------------------------------------
# Menú desplegable de extras
boton_menu_extras = tk.Menubutton(ventana, text='Extras', relief=tk.RAISED, width=30, height=1, font=("Arial", 14, "bold"), justify="center", background="lightblue", borderwidth=3)
boton_menu_extras.place(x=410, y=100)

menu_principal_extras = tk.Menu(boton_menu_extras, tearoff=0, relief=tk.RAISED, font=("Arial", 14, "bold"), background="lightblue", borderwidth=3)
boton_menu_extras.config(menu=menu_principal_extras)

Extras = {'Masajeadores': Masajeadores, 'Comida': Comida, 'Bebida': Bebida}

for categoria, opciones in Extras.items():
    submenu_extras = tk.Menu(menu_principal_extras, tearoff=0, relief=tk.RAISED, font=("Arial", 14, "bold"), background="lightblue", borderwidth=3)
    menu_principal_extras.add_cascade(label=categoria, menu=submenu_extras)

    for extra in opciones:
        submenu_extras.add_command(label=f"{extra}",command=lambda extra=extra: lista_extras.insert(tk.END,extra))

# ----------------------------------------------------------------------------------------------------------------------------------------------
# Servicios seleccionados
frame_servicios = tk.Frame(ventana)
frame_servicios.place(x=10, y=470)

lista_servicios_label= tk.Label(text=("Servicios seleccionados"),width=22, height=1,font=("Arial", 14, "bold"), justify="center", background="lightblue", borderwidth=3)
lista_servicios_label.place(x=10, y=440)

scrollbar = tk.Scrollbar(frame_servicios,orient=tk.HORIZONTAL)
scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

lista_servicios = tk.Listbox(frame_servicios,selectmode=tk.SINGLE, width=24, height=10,font=("Arial", 14, "bold"), justify="center", background="lightblue", borderwidth=3)
lista_servicios.pack(side=tk.LEFT, fill=tk.BOTH)

lista_servicios.config(xscrollcommand=scrollbar.set)
scrollbar.config(command=lista_servicios.xview)

# Extras seleccionados

lista_extras_label= tk.Label(text=("Extras seleccionados"),width=18, height=1,font=("Arial", 14, "bold"), justify="center", background="lightblue", borderwidth=3)
lista_extras_label.place(x=300, y=440)

lista_extras = tk.Listbox(ventana,selectmode=tk.SINGLE, width=20, height=10,font=("Arial", 14, "bold"), justify="center", background="lightblue", borderwidth=3)
lista_extras.place(x=300, y=470)


ventana.mainloop()


# colocar nombre a las etiquetas de servicio seleccionado y extras seleccionados.
# temporizador, hora de salida, servicios seleccionados y extras seleccionados van en otra ventana despues de ejecutar el play.