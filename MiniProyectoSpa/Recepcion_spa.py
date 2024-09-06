import tkinter as tk
from tkinter import PhotoImage
from PIL import ImageTk, Image
import time 
from servicios import *

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

#reloj

reloj = tk.Label(ventana, font= ('Arial', 45), bg = 'lightblue', fg ='black')

def hora():
         tiempo_actual = time.strftime('%H: %M: %S')
         reloj.config(text = tiempo_actual)
         ventana.after(1000, hora)
reloj.grid(row=0, column=4,columnspan=1, padx=300, pady=10)
hora()

# Menu desplegable de servicios

boton_menu = tk.Menubutton(ventana, text='Servicios Principales', relief=tk.RAISED, width=30,height=1, font=("Arial", 14, "bold"), justify="center", background="lightblue", borderwidth=3)
boton_menu.grid(row=1,column=0,padx=20, pady=20)

menu_principal = tk.Menu(boton_menu, tearoff=0,relief=tk.RAISED, font=("Arial", 14, "bold"), background="lightblue", borderwidth=3)
boton_menu.config(menu=menu_principal)

servicios = {'Manos': Manos, 'Pies': Pies, 'Cutis': Cutis, 'Masajes': Masajes}

for categoria, opciones in servicios.items():
    submenu = tk.Menu(menu_principal, tearoff=0,relief=tk.RAISED, font=("Arial", 14, "bold"), background="lightblue", borderwidth=3)
    menu_principal.add_cascade(label=categoria, menu=submenu,)
    
    for llave,valor in opciones.items():
        submenu.add_command(label=f"{llave}:  {valor} minutos.")

ventana.mainloop()

