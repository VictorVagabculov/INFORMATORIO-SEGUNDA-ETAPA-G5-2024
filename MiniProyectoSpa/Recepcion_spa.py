import tkinter as tk
from tkinter import PhotoImage
#from PIL import ImageTk, Image
from  tkinter import  ttk,Frame
import time
from servicios import *

# ------------------- ventana-----------
ventana = tk.Tk()
ventana.title("Recepción Spa")
ventana.geometry("1000x800")
ventana.configure(background="lightblue")
hola_servicio=""




#-------------/  FRAME1 |---------------------------------------

frame1=Frame(ventana,bg="lightblue")
frame1.pack(expand=True,fill="both")


frame3=Frame(ventana,bg="lightblue")
frame3.pack(expand=True,fill="both")


#-------------/FRAME 2 |----------------------------------------------

frame2=Frame(ventana,bg="lightblue")
frame2.pack(expand=True,fill="both")









# imagen de fondo
#logo = Image.open("MiniProyectoSpa\Imagenes\spalogo.png")
#logo = logo.resize((1000, 800))
#logo_fondo = ImageTk.PhotoImage(logo)
#va eso   image=logo_fondo,

#---------------------------VARIABLES------------------------------------
servicios = {'Manos': Manos, 'Pies': Pies, 'Cutis': Cutis, 'Masajes': Masajes}

#--------------------------------logica -----------------------------------
#----------for anidado----------------------------------------------------
#----------Agregar-------------------

#-----------------AGREAGAR LISTA-----------------------------

#------------------------------agregar cliente ----------------------------

def agregarCliente():
    labe.config(text=nombre_cliente.get())
    nombre_cliente.set("")
#---------------------------------eliminar-------------------------------------
def eliminar_tarea():
    varSeleccionado = tablaa.selection()
    if varSeleccionado:
        tablaa.delete(varSeleccionado)


#--------------------------------RELOJ---------------------------------------

def hora():
    tiempo_actual = time.strftime('%H: %M: %S')
    reloj.config(text=tiempo_actual)
    ventana.after(1000, hora)

#-------------------------||||||||||||||||------------------------------------

#***************************************************************************

#-------------MENU----------------------------------------------------------



#----------------BOTONES ------------------------------------------------------


# boton salir
boton_salir = tk.Button(frame3, text="salir", command=quit)
boton_salir.grid(row=1, column=4, columnspan=1, padx=300, pady=10)
# codigo Noemi

#----------------agregar-------------------------------------------------------
boton_agregar = tk.Button(frame3, text="✔", command=agregarCliente, font=("Arial", 10),
                          background="lightblue", borderwidth=3, width=2, height=1)
boton_agregar.grid(row=3, column=0, columnspan=1, padx=10, pady=10)
#---------------agregar cliente---------------------------------------------------

#----------------eliminar-----------------------------------------------------
boton_eliminar = tk.Button(frame2, text="✖", command=eliminar_tarea, font=("Arial", 10),
                          background="lightblue", borderwidth=3, width=2, height=1)
boton_eliminar.grid(row=6, column=0, columnspan=1, padx=10, pady=10)

#***********************************************************************************************
labe=tk.Label(frame3,font="consolas 15 bold",width=30)
labe.grid(row=4, column=0)
#----------------menu--------------------------------------------------------
boton_menu = tk.Menubutton(frame3, text='Servicios Principales', relief=tk.RAISED, width=30, height=1,
                           font=("Arial", 14, "bold"), justify="center", background="lightblue", borderwidth=3)
boton_menu.grid(row=1, column=0, padx=20, pady=20)

menu_principal = tk.Menu(boton_menu, tearoff=0, relief=tk.RAISED, font=("Arial", 14, "bold"), background="lightblue",
                         borderwidth=3)
boton_menu.config(menu=menu_principal)

for categoria, opciones in servicios.items():
    submenu = tk.Menu(menu_principal, tearoff=0, relief=tk.RAISED, font=("Arial", 14, "bold"), background="lightblue",
                      borderwidth=3)
    menu_principal.add_cascade(label=categoria, menu=submenu, )

    for llave, valor in opciones.items():
        submenu.add_command(label=f"{llave}:{valor} minutos.",command=lambda valor=llave:tablaa.insert("","0", values=(valor,"")))

#--------------Tabla----------------------------------------------------------
tablaa=ttk.Treeview(frame2,columns=("co2","co3"),show="headings")
tablaa.grid(row=1,column=0)
tablaa.heading("co3",text="extras")
tablaa.heading("co2",text="servicios")

#-----------------nombre-------------------------------------------------------------

nombre_cliente = tk.StringVar()
ingreso_cliente = tk.Entry(frame1, width=30, textvariable=nombre_cliente, font=("Arial", 14, "bold"),background="lightblue")
ingreso_cliente.grid(row=0, column=0, columnspan=1, padx=10, pady=10)
nombre_cliente.set("Nombre ")

#---------------RELOJ-------------------------------------------------------------------------

reloj = tk.Label(frame1, font=('Arial', 45), bg='lightblue', fg='black')
reloj.grid(row=0, column=1, columnspan=1, padx=100, pady=10)
hora()


#---------Scroll var---------
barra_despalce=ttk.Scrollbar(frame2,orient="vertical",command=tablaa.yview)
tablaa.config(yscrollcommand=barra_despalce.set)
barra_despalce.grid(row=1,column=2,sticky="ns")
barra_despalce.config(command=tablaa.yview)


ventana.mainloop()
