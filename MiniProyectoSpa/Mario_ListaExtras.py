#Función para mostrar opciones de Extras en una ventana emergente
def mostrar_opciones(extra):
    def seleccionar_opcion(opcion):
        print(f"Seleccionado: {opcion}")  # Aquí puedes añadir lógica para manejar la selección
        top.destroy()  # Cierra la ventana emergente
    
    top = tk.Toplevel(ventana)
    top.title(f"{extra} Opciones")
    top.geometry("240x100")
    
    canvas = tk.Canvas(top, width=100, height=100, bg='lightblue')
    scrollbar = tk.Scrollbar(top, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    
    frame = tk.Frame(canvas, bg='lightblue')
    
    # Añadir los elementos del extra al Frame
    for item in Extras[extra]:
        tk.Button(frame, text=item, font=("Arial", 14, "bold"), bg='lightblue', command=lambda i=item: seleccionar_opcion(i)).pack(fill='x')

    # Configurar el Canvas y el Frame
    canvas.create_window((0, 0), window=frame, anchor='nw')
    frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Menu desplegable de Extras
Extras = {'Masajeadores': Masajeadores, 'Comida': Comida, 'Bebida': Bebida}

def on_select_extra(option):
    mostrar_opciones(option)

boton_Extras = tk.Menubutton(ventana, text='Extras', relief=tk.RAISED, width=30, height=1, font=("Arial", 14, "bold"), justify="center", background="lightblue", borderwidth=3)
boton_Extras.grid(row=1, column=1, padx=20, pady=20)

menu_Extras = tk.Menu(boton_Extras, tearoff=0, relief=tk.RAISED, font=("Arial", 14, "bold"), background="lightblue", borderwidth=3)
boton_Extras.config(menu=menu_Extras)

for nombre in Extras.keys():
    menu_Extras.add_command(label=nombre, command=lambda n=nombre: on_select_extra(n))

ventana.mainloop()

