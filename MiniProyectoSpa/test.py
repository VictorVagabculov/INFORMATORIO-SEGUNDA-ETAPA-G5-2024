import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Recepción Spa")
ventana.geometry("1000x800")
ventana.configure(background="lightblue")

# Frame para contener el Listbox y la Scrollbar
frame = tk.Frame(ventana)
frame.place(x=10, y=450)

# Crear el Listbox
lista_extras = tk.Listbox(frame, selectmode=tk.SINGLE, width=60, height=15, background="lightblue", font=("Arial", 12))
lista_extras.pack(side=tk.TOP, fill=tk.BOTH)

# Crear la Scrollbar horizontal
scrollbar = tk.Scrollbar(frame, orient=tk.HORIZONTAL)
scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

# Asociar la Scrollbar con el Listbox horizontalmente
lista_extras.config(xscrollcommand=scrollbar.set)
scrollbar.config(command=lista_extras.xview)

# Menú desplegable de extras
boton_menu_extras = tk.Menubutton(ventana, text='Extras', relief=tk.RAISED, width=30, height=1, font=("Arial", 14, "bold"), justify="center", background="lightblue", borderwidth=3)
boton_menu_extras.place(x=410, y=100)

menu_principal_extras = tk.Menu(boton_menu_extras, tearoff=0, relief=tk.RAISED, font=("Arial", 14, "bold"), background="lightblue", borderwidth=3)
boton_menu_extras.config(menu=menu_principal_extras)

# Ejemplo de datos para Extras
Extras = {
    'Masajeadores': ["Masajeador A", "Masajeador B", "Masajeador C"],
    'Comida': ["Ensalada", "Sándwich", "Muffin"],
    'Bebida': ["Agua", "Jugo", "Té"]
}

for categoria, opciones in Extras.items():
    submenu_extras = tk.Menu(menu_principal_extras, tearoff=0, relief=tk.RAISED, font=("Arial", 14, "bold"), background="lightblue", borderwidth=3)
    menu_principal_extras.add_cascade(label=categoria, menu=submenu_extras)

    for extra in opciones:
        submenu_extras.add_command(label=f"{extra}", command=lambda extra=extra: lista_extras.insert(tk.END, extra))

ventana.mainloop()