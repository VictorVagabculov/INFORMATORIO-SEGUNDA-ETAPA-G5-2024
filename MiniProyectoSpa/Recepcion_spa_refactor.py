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
    if nombre_cliente.get() == "Nombre del Cliente":
        nombre_cliente.set("")


ingreso_cliente.bind("<Key>", limpiar_nombre)

# ----------------------------------------------------------------------------------------------------------------------------------------------
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


def limpiar_numero(event):
    if numero_box.get() == "Box n°":
        numero_box.set("")


ingreso_box.bind("<Key>", limpiar_numero)

def solo_numeros(char):
    return char.isdigit() or char == ""


validacion_numerica = ventana.register(solo_numeros)
ingreso_box.config(validate="key", validatecommand=(validacion_numerica, "%P"))

# ----------------------------------------------------------------------------------------------------------------------------------------------
# Boton de eliminar
def obtener_tiempo_servicio(nombre_servicio):
    for categoria, opciones in servicios.items():
        if nombre_servicio in opciones:
            return opciones[nombre_servicio]
    return 0

def eliminar_tarea():
    global tiempo_total
    if lista_servicios.curselection():
        seleccion = lista_servicios.curselection()
        servicio_eliminado = lista_servicios.get(seleccion)
        tiempo_a_restar = obtener_tiempo_servicio(servicio_eliminado) * 60
        tiempo_total -= tiempo_a_restar
        lista_servicios.delete(seleccion)
        actualizar_tiempo()  # Actualiza el temporizador después de eliminar
    elif lista_extras.curselection():
        seleccion = lista_extras.curselection()
        lista_extras.delete(seleccion)


boton_eliminar = tk.Button(
    ventana,
    text="Eliminar Seleccion",
    command=eliminar_tarea,
    font=("Arial", 10),
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

# ----------------------------------------------------------------------------------------------------------------------------------------------
# Hora de salida
label_hora_salida = tk.Label(
    ventana,
    text="Hora de salida: --:--:--",
    font=("Arial", 16, "bold"),
    bg="lightblue",
    fg="black",
)
label_hora_salida.place(x=700, y=450)


def calcular_hora_salida():
    tiempo_actual = time.time()
    tiempo_salida = tiempo_actual + tiempo_total
    hora_salida = time.strftime("%H:%M:%S", time.localtime(tiempo_salida))
    label_hora_salida.config(text=f"Hora de salida: {hora_salida}")

# ----------------------------------------------------------------------------------------------------------------------------------------------
# Boton de iniciar servicio
def iniciar_servicio():
    time.sleep(0.5)
    tiempo_servicio = tiempo_total
    cliente = nombre_cliente.get()
    box = numero_box.get()
    servicios_seleccionados = lista_servicios.get(0, tk.END)
    extras_seleccionados = lista_extras.get(0, tk.END)

    ventana_servicio = tk.Toplevel(ventana)
    ventana_servicio.title(f"Cliente: {cliente}, Box: {box}")
    ventana_servicio.geometry("400x500")
    ventana_servicio.configure(background="lightblue")

    label_cliente = tk.Label(
        ventana_servicio,
        text=f"Cliente: {cliente}",
        font=("Arial", 14, "bold"),
        bg="lightblue"
    )
    label_cliente.pack(pady=10)

    label_box = tk.Label(
        ventana_servicio,
        text=f"Box: {box}",
        font=("Arial", 14, "bold"),
        bg="lightblue"
    )
    label_box.pack(pady=10)

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

    label_tiempo_servicio = tk.Label(
        ventana_servicio,
        text="00:00:00",
        font=("Arial", 30, "bold"),
        bg="lightblue"
    )
    label_tiempo_servicio.pack(pady=10)

    label_hora_salida_servicio = tk.Label(
        ventana_servicio,
        text="Hora de salida: --:--:--",
        font=("Arial", 14, "bold"),
        bg="lightblue"
    )
    label_hora_salida_servicio.pack(pady=10)

    def actualizar_tiempo_servicio():
        nonlocal tiempo_servicio
        if tiempo_servicio > 0:
            tiempo_servicio -= 1
            horas, resto = divmod(tiempo_servicio, 3600)
            minutos, segundos = divmod(resto, 60)
            label_tiempo_servicio.config(text=f"{horas:02}:{minutos:02}:{segundos:02}")
            ventana_servicio.after(1000, actualizar_tiempo_servicio)
        else:
            label_tiempo_servicio.config(text="00:00:00")
            mostrar_popup_finalizacion()

    def calcular_hora_salida_servicio():
        tiempo_actual = time.time()
        tiempo_salida = tiempo_actual + tiempo_servicio
        hora_salida = time.strftime("%H:%M:%S", time.localtime(tiempo_salida))
        label_hora_salida_servicio.config(text=f"Hora de salida: {hora_salida}")

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

    calcular_hora_salida_servicio()
    actualizar_tiempo_servicio()

boton_iniciar = tk.Button(
    ventana,
    text="Iniciar Servicio",
    command=iniciar_servicio,
    font=("Arial", 20, "bold"),
    bg="lightblue",
    borderwidth=3
)
boton_iniciar.place(x=700, y=600)

# ----------------------------------------------------------------------------------------------------------------------------------------------
# Mostrar ventana principal
ventana.mainloop()
