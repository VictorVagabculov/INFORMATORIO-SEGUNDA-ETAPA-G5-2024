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

#--------------------------------logica -----------------------------------
#----------for anidado----------------------------------------------------
#----------Agregar-------------------

def guardado_datos_clientes():
    nombra="| "+manos.get()+" | "+pies.get()+" | "+cutis.get()+" | "+masaje.get()+"| "
    but =nombre_cliente.get()
    buta=""
    vari=(but,nombra, buta)
    nombre_cliente.set("")
    manos.set("")
    pies.set("")
    cutis.set("")
    masaje.set("")
    return vari
#-----------------AGREAGAR LISTA-----------------------------

def agregar():

    tablaa.insert("","0", values=(guardado_datos_clientes()))

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

#***************************************************************************

#-------------MENU----------------------------------------------------------



#----------------BOTONES ------------------------------------------------------

#----------------agregar-------------------------------------------------------
boton_agregar = tk.Button(frame3, text="✔", command=agregar, font=("Arial", 10),
                          background="lightblue", borderwidth=3, width=2, height=1)
boton_agregar.grid(row=3, column=0, columnspan=1, padx=10, pady=10)

#----------------eliminar-----------------------------------------------------
boton_eliminar = tk.Button(frame2, text="✖", command=eliminar_tarea, font=("Arial", 10),
                          background="lightblue", borderwidth=3, width=2, height=1)
boton_eliminar.grid(row=6, column=0, columnspan=1, padx=10, pady=10)

#***********************************************************************************************

#----------------menu--------------------------------------------------------
boton_menu = tk.Menubutton(frame3, text='Servicios Principales', relief=tk.RAISED, width=30, height=1,
                           font=("Arial", 14, "bold"), justify="center", background="lightblue", borderwidth=3)
boton_menu.grid(row=0, column=0,)
#---------------menu extras----------------------------------------------------
extras_menu = tk.Menubutton(frame3, text='extras', relief=tk.RAISED, width=30, height=1,
                           font=("Arial", 14, "bold"), justify="center", background="lightblue", borderwidth=3)
extras_menu.grid(row=2, column=0, padx=10, pady=10)

#********************************************************************************************************************

#------------------ cajas -------------------------------------------------------
manos=ttk.Combobox(frame3,values=Manos,state="readonly")
manos.grid(row=0,column=1)
#------------------  -------------------------------------------------------
pies=ttk.Combobox(frame3,values=Pies,state="readonly")
pies.grid(row=0,column=2)
#------------------  -------------------------------------------------------
cutis=ttk.Combobox(frame3,values=Cutis,state="readonly")
cutis.grid(row=0,column=3)
#------------------  -------------------------------------------------------
masaje=ttk.Combobox(frame3,values=Masajes,state="readonly")
masaje.grid(row=0,column=4)
#------------------------------------------------------------------------------
"""
codigo a restructurar 
"""
barra_menu = tk.Menu(ventana )
ventana.config(menu=barra_menu)
menu_principal = tk.Menu(barra_menu)
barra_menu.add_cascade(label ='Extras', menu=menu_principal)
submenu0 = tk.Menu(menu_principal)
menu_principal.add_cascade(label ='Masajista', menu=submenu0)
submenu0.add_command(label = 'Femenino')
submenu0.add_command(label = 'Masculino')

submenu1 = tk.Menu(menu_principal)
menu_principal.add_cascade(label ='Comida', menu=submenu1)
submenu1.add_command(label = 'Barra de Cereal')
submenu1.add_command(label =  'Mix frutos secos')
submenu2 = tk.Menu(menu_principal)
submenu2 = tk.Menu(menu_principal)
menu_principal.add_cascade(label =
'Bebida', menu=submenu2)
submenu2.add_command(label = 'Jamaica')
submenu2.add_command(label = 'Tamarindo')
#--------------------------------------------------------------------------------------



#------------------------------------------------------------------------


#-----------------------------------------------------------------------------
#--------------Tabla----------------------------------------------------------
tablaa=ttk.Treeview(frame2,columns=("co1","co2","co3"),show="headings")
tablaa.grid(row=0,column=0)
tablaa.heading("co3",text="extras")
tablaa.heading("co1",text="nombre")
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
barra_despalce.grid(row=0,column=2,sticky="ns")
barra_despalce.config(command=tablaa.yview)





ventana.mainloop()
