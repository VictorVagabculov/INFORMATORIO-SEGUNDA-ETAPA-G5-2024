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
ventana.iconbitmap("Imagenes/spalogonegro.ico")

# Imagen de fondo
logo = Image.open("Imagenes/spalogo.png")
logo = logo.resize((1000, 800))
logo_fondo = ImageTk.PhotoImage(logo)
label_fondo = tk.Label(ventana, image=logo_fondo, bg="lightblue")
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

# ----------------------------------------------------------------------------------------------------------------------------------------------
# Ingreso de cliente
nombre_cliente = tk.StringVar()
ingreso_cliente = tk.Entry(
    ventana,
    width=31,
    textvariable=nombre_cliente,
    font=("Arial", 14, "bold"),
    justify="center",
    background="lightblue",
    borderwidth=3,
)
ingreso_cliente.place(x=10, y=10)
nombre_cliente.set("Nombre del Cliente")


def limpiar_nombre(event):
    if nombre_cliente.get() == "Nombre del Cliente":  # Si el valor es el predeterminado
        nombre_cliente.set("")  # Limpiar el Entry


ingreso_cliente.bind("<Key>", limpiar_nombre)
# -----------------------------------------------------------------------------------------------------------------------------------------------
# Ingreso el numero de BOX

numero_box = tk.StringVar()
ingreso_box = tk.Entry(
    ventana,
    width=6,
    textvariable=numero_box,
    font=("Arial", 14, "bold"),
    justify="center",
    background="lightblue",
    borderwidth=3,
)
ingreso_box.place(x=400, y=10)
numero_box.set("Box n°")


# Función para limpiar el campo de entrada al escribir la primera vez
def limpiar_numero(event):
    if numero_box.get() == "Box n°":
        numero_box.set("")


ingreso_box.bind("<Key>", limpiar_numero)


# Función para validar que solo se ingresen números
def solo_numeros(char):
    return (
        char.isdigit() or char == ""
    )  # Permitir números y el vacío (cuando se borra el texto)


# Configurar la validación
validacion_numerica = ventana.register(solo_numeros)
ingreso_box.config(
    validate="key", validatecommand=(validacion_numerica, "%P")
)  # %P es el contenido actual del Entry después del cambio


# ----------------------------------------------------------------------------------------------------------------------------------------------
# Boton de eliminar
def eliminar_tarea():
    seleccion = (
        lista_servicios.curselection()
        or lista_extras.curselection()
    )
    if seleccion:
        lista_servicios.delete(
            seleccion
        ) or lista_extras.delete(seleccion)


boton_eliminar = tk.Button(
    ventana,
    text="Eliminar Seleccion",
    command=eliminar_tarea,
    font=(
        "Arial",
        10,
    ),
    justify="center",
    background="lightblue",
    borderwidth=3,
    width=18,
    height=1,
)
boton_eliminar.place(x=70, y=730)

# ----------------------------------------------------------------------------------------------------------------------------------------------
# Reloj
reloj = tk.Label(ventana, font=("Arial", 45, "bold"), bg="lightblue", fg="black")


def hora():
    tiempo_actual = time.strftime("%H:%M:%S")
    reloj.config(text=tiempo_actual)
    ventana.after(1000, hora)


reloj.place(x=700, y=10)
hora()

# ----------------------------------------------------------------------------------------------------------------------------------------------
# Temporizador
tiempo_total = 0
label_tiempo = tk.Label(
    ventana, text="00:00:00", font=("Arial", 40, "bold"), bg="lightblue", borderwidth=3
)
label_tiempo.place(x=700, y=530)


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
label_hora_salida = tk.Label(
    ventana,
    text="Hora de salida: --:--:--",
    font=("Arial", 16, "bold"),
    bg="lightblue",
    fg="black",
)
label_hora_salida.place(x=700, y=450)


# Función para calcular la hora de salida
def calcular_hora_salida():
    tiempo_actual = time.time()
    tiempo_salida = tiempo_actual + tiempo_total
    hora_salida = time.strftime("%H:%M:%S", time.localtime(tiempo_salida))
    label_hora_salida.config(text=f"Hora de salida: {hora_salida}")


# ------------------------------------------------------------------------------------------------------------------------------------------------
# Función para iniciar el servicio

def reiniciar_ventana():
    # Reiniciar los campos de texto
    nombre_cliente.set("Nombre del Cliente")
    numero_box.set("Box n°")

    # Limpiar las listas de servicios y extras seleccionados
    lista_servicios.delete(0, tk.END)
    lista_extras.delete(0, tk.END)

    # Reiniciar el temporizador
    global tiempo_total
    tiempo_total = 0
    label_tiempo.config(text="00:00:00")

    # Restablecer la hora de salida
    label_hora_salida.config(text="Hora de salida: --:--:--")

# Función para validar si ambos campos tienen texto y habilitar el botón
def validar_entradas(*args):
    cliente = nombre_cliente.get()
    box = numero_box.get()

    # Si ambos campos no están vacíos, habilitar el botón
    if cliente and cliente != "Nombre del Cliente" and box and box != "Box n°":
        boton_iniciar.config(state=tk.NORMAL)
    else:
        boton_iniciar.config(state=tk.DISABLED)

# Asocia la función de validación a los cambios en los campos de entrada
nombre_cliente.trace_add("write", validar_entradas)
numero_box.trace_add("write", validar_entradas)


#Boton de iniciar servicio
boton_iniciar = tk.Button(
    ventana,
    text="Iniciar Servicio",
    command=lambda: (
        iniciar_servicio(),  # Ejecuta el servicio
        reiniciar_ventana(),
    ),
    font=("Arial", 20, "bold"),
    bg="lightblue",
    borderwidth=3,
)
boton_iniciar.place(x=700, y=650)


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
boton_menu_servicios = tk.Menubutton(
    ventana,
    text="Servicios Principales",
    relief=tk.RAISED,
    width=30,
    height=1,
    font=("Arial", 14, "bold"),
    justify="center",
    background="lightblue",
    borderwidth=3,
)
boton_menu_servicios.place(x=10, y=100)

menu_principal_servicios = tk.Menu(
    boton_menu_servicios,
    tearoff=0,
    relief=tk.RAISED,
    font=("Arial", 14, "bold"),
    background="lightblue",
    borderwidth=3,
)
boton_menu_servicios.config(menu=menu_principal_servicios)
# Creo un diccionario local de servicios (TEST está para probar tiempos cortos)
servicios = {"Manos": Manos, "Pies": Pies, "Cutis": Cutis, "Masajes": Masajes,"TEST": TEST} 

for categoria, opciones in servicios.items():
    submenu_servicios = tk.Menu(
        menu_principal_servicios,
        tearoff=0,
        relief=tk.RAISED,
        font=("Arial", 14, "bold"),
        background="lightblue",
        borderwidth=3,
    )
    menu_principal_servicios.add_cascade(label=categoria, menu=submenu_servicios)

    for llave, valor in opciones.items():
        submenu_servicios.add_command(
            label=f"{llave}: {valor} minutos",
            command=lambda valor=valor, llave=llave: (
                agregar_tiempo(valor),
                lista_servicios.insert(tk.END, llave),
            ),
        )

# ----------------------------------------------------------------------------------------------------------------------------------------------
# Menú desplegable de extras
boton_menu_extras = tk.Menubutton(
    ventana,
    text="Extras",
    relief=tk.RAISED,
    width=30,
    height=1,
    font=("Arial", 14, "bold"),
    justify="center",
    background="lightblue",
    borderwidth=3,
)
boton_menu_extras.place(x=410, y=100)

menu_principal_extras = tk.Menu(
    boton_menu_extras,
    tearoff=0,
    relief=tk.RAISED,
    font=("Arial", 14, "bold"),
    background="lightblue",
    borderwidth=3,
)
boton_menu_extras.config(menu=menu_principal_extras)

Extras = {"Masajeadores": Masajeadores, "Comida": Comida, "Bebida": Bebida}

for categoria, opciones in Extras.items():
    submenu_extras = tk.Menu(
        menu_principal_extras,
        tearoff=0,
        relief=tk.RAISED,
        font=("Arial", 14, "bold"),
        background="lightblue",
        borderwidth=3,
    )
    menu_principal_extras.add_cascade(label=categoria, menu=submenu_extras)

    for extra in opciones:
        submenu_extras.add_command(
            label=f"{extra}",
            command=lambda extra=extra: lista_extras.insert(tk.END, extra),
        )

# ----------------------------------------------------------------------------------------------------------------------------------------------
# Servicios seleccionados
frame_servicios = tk.Frame(ventana)
frame_servicios.place(x=10, y=470)

lista_servicios_label = tk.Label(
    text=("Servicios seleccionados"),
    width=22,
    height=1,
    font=("Arial", 14, "bold"),
    justify="center",
    background="lightblue",
    borderwidth=3,
)
lista_servicios_label.place(x=10, y=440)

scrollbar = tk.Scrollbar(frame_servicios, orient=tk.HORIZONTAL)
scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

lista_servicios = tk.Listbox(
    frame_servicios,
    selectmode=tk.SINGLE,
    width=24,
    height=10,
    font=("Arial", 14, "bold"),
    justify="center",
    background="lightblue",
    borderwidth=3,
)
lista_servicios.pack(side=tk.LEFT, fill=tk.BOTH)

lista_servicios.config(xscrollcommand=scrollbar.set)
scrollbar.config(command=lista_servicios.xview)

# Extras seleccionados

lista_extras_label = tk.Label(
    text=("Extras seleccionados"),
    width=18,
    height=1,
    font=("Arial", 14, "bold"),
    justify="center",
    background="lightblue",
    borderwidth=3,
)
lista_extras_label.place(x=300, y=440)

lista_extras = tk.Listbox(
    ventana,
    selectmode=tk.SINGLE,
    width=20,
    height=10,
    font=("Arial", 14, "bold"),
    justify="center",
    background="lightblue",
    borderwidth=3,
)
lista_extras.place(x=300, y=470)
# ----------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------

# Función para iniciar el servicio
def iniciar_servicio():
    time.sleep(0.5)
    
    # Obtener el tiempo total del servicio actual
    tiempo_servicio = tiempo_total  # Copiar el tiempo total actual a una variable local para esta ventana
    
    # Obtener el texto del Entry de nombre de cliente
    cliente = nombre_cliente.get()

    # Obtener el texto del Entry del número de box
    box = numero_box.get()

    # Obtener los servicios y extras seleccionados
    servicios_seleccionados = lista_servicios.get(0, tk.END)
    extras_seleccionados = lista_extras.get(0, tk.END)

    # Crear nueva ventana
    ventana_servicio = tk.Toplevel(ventana)
    ventana_servicio.title(f"Cliente: {cliente}, Box: {box}")
    ventana_servicio.geometry("400x500")
    ventana_servicio.configure(background="lightblue")

    # Mostrar el nombre del cliente
    label_cliente = tk.Label(
        ventana_servicio,
        text=f"Cliente: {cliente}",
        font=("Arial", 14, "bold"),
        bg="lightblue"
    )
    label_cliente.pack(pady=10)

    # Mostrar el número de box
    label_box = tk.Label(
        ventana_servicio,
        text=f"Box: {box}",
        font=("Arial", 14, "bold"),
        bg="lightblue"
    )
    label_box.pack(pady=10)

    # Mostrar servicios seleccionados
    label_servicios = tk.Label(
        ventana_servicio,
        text="Servicios seleccionados:",
        font=("Arial", 14, "bold"),
        bg="lightblue"
    )
    label_servicios.pack(pady=10)

    for servicio in servicios_seleccionados:
        tk.Label(
            ventana_servicio,
            text=servicio,
            font=("Arial", 12),
            bg="lightblue"
        ).pack()

    # Mostrar extras seleccionados
    label_extras = tk.Label(
        ventana_servicio,
        text="Extras seleccionados:",
        font=("Arial", 14, "bold"),
        bg="lightblue"
    )
    label_extras.pack(pady=10)

    for extra in extras_seleccionados:
        tk.Label(
            ventana_servicio,
            text=extra,
            font=("Arial", 12),
            bg="lightblue"
        ).pack()

    # Temporizador en la nueva ventana
    label_tiempo_servicio = tk.Label(
        ventana_servicio, 
        text="00:00:00", 
        font=("Arial", 30, "bold"), 
        bg="lightblue"
    )
    label_tiempo_servicio.pack(pady=10)

    # Hora de salida
    label_hora_salida_servicio = tk.Label(
        ventana_servicio,
        text="Hora de salida: --:--:--",
        font=("Arial", 14, "bold"),
        bg="lightblue"
    )
    label_hora_salida_servicio.pack(pady=10)

    # Función para actualizar el temporizador en la nueva ventana
    def actualizar_tiempo_servicio():
        nonlocal tiempo_servicio  # Usar la variable local tiempo_servicio en lugar de la global tiempo_total
        if tiempo_servicio > 0:
            tiempo_servicio -= 1
            horas, resto = divmod(tiempo_servicio, 3600)
            minutos, segundos = divmod(resto, 60)
            label_tiempo_servicio.config(text=f"{horas:02}:{minutos:02}:{segundos:02}")
            ventana_servicio.after(1000, actualizar_tiempo_servicio)
        else:
            label_tiempo_servicio.config(text="00:00:00")
         # Mostrar el popup cuando el temporizador finalice
            mostrar_popup_finalizacion()

    # Función para calcular la hora de salida y mostrarla
    def calcular_hora_salida_servicio():
        tiempo_actual = time.time()
        tiempo_salida = tiempo_actual + tiempo_servicio
        hora_salida = time.strftime("%H:%M:%S", time.localtime(tiempo_salida))
        label_hora_salida_servicio.config(text=f"Hora de salida: {hora_salida}")

    # Iniciar el temporizador y calcular la hora de salida
    calcular_hora_salida_servicio()
    actualizar_tiempo_servicio()

    # Popup de finalizacion.
    def mostrar_popup_finalizacion():
        popup = tk.Toplevel(ventana_servicio)
        popup.title("Servicio Finalizado")
        popup.geometry("400x150")
        popup.configure(background="lightblue")
    
        label_popup = tk.Label(
            popup,
            text=f"¡{cliente}, en la box: {box} ha finalizado!",
        
            font=("Arial", 14, "bold"),
            bg="lightblue"
        )
        label_popup.pack(pady=30)

        boton_ok = tk.Button(
            popup,
            text="OK",
            command=popup.destroy,
            font=("Arial", 12, "bold"),
            bg="lightblue",
            borderwidth=3
    )
        boton_ok.pack(pady=10)

reiniciar_ventana() #Si no reinicio la ventan ni bien la abro, no se me deshabilita el boton de iniciar 🤷‍♂️
ventana.mainloop()
