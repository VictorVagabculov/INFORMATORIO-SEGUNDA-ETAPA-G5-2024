import tkinter as tk
from tkinter import PhotoImage
from PIL import ImageTk, Image
import time
#ventana
ventana = tk.Tk()

ventana.title("Recepción Spa")
ventana.geometry("1000x800")
ventana.configure(background="lightblue")

#imagen de fondo
logo = Image.open("MiniProyectoSpa\Imagenes\spalogo.png")
logo = logo.resize((1000, 800))  
logo_fondo = ImageTk.PhotoImage(logo)


label_fondo = tk.Label(ventana, image=logo_fondo, bg="lightblue")
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

#ingreso de cliente

nombre_cliente = tk.StringVar()
ingreso_cliente = tk.Entry(ventana, width=30, textvariable=nombre_cliente, font=("Arial", 14, "bold"), justify="center", background="lightblue", borderwidth=3)

ingreso_cliente.grid(row=0, column=0, columnspan=1, padx=10, pady=10)

nombre_cliente.set("Nombre del Cliente")



#boton de agregar cliente
def agregar_cliente():
    tarea = ingreso_cliente.get()
    if tarea:
        lista_cliente.insert(tk.END, tarea)
    ingreso_cliente.delete(0, tk.END)
boton_agregar = tk.Button(ventana, text = "✔", command = agregar_cliente,font=("Arial", 10), justify="center", background="lightblue", borderwidth=3,width=2,height=1)
boton_agregar.grid(row=0, column=1, columnspan=1, padx=10, pady=10)

lista_cliente = tk.Listbox(ventana,width=30,height=1, font=("Arial", 14, "bold"), justify="center", background="lightblue", borderwidth=3)
lista_cliente.grid(row=2, column=0, columnspan=1, padx=10, pady=400)

def eliminar_tarea():
    seleccion = lista_cliente.curselection()
    if seleccion:
        lista_cliente.delete(seleccion)

boton_eliminar = tk.Button(ventana, text = '✖', command = eliminar_tarea,font=("Arial", 10), justify="center", background="lightblue", borderwidth=3,width=2,height=1)
boton_eliminar.grid(row=2, column=1, columnspan=1, padx=10, pady=10)

#cronometro

def cronometro():
    minutos = 0
    segundos = 0

    try:
        while True:
            print(f"{minutos:02}:{segundos:02}")  # Formato mm:ss
            time.sleep(1)  # Espera 1 segundo
            segundos += 1

            if segundos == 60:  # Si los segundos llegan a 60, reinicia y suma un minuto
                segundos = 0
                minutos += 1

    except KeyboardInterrupt:
        print("\nCronómetro detenido.")

# Ejecutar el cronómetro
# cronometro()
    


ventana.mainloop()
    
















