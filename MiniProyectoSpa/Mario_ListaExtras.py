import tkinter as tk
ventana = tk.Tk()
ventana.title('Servicios')
ventana.geometry('400x200')
barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)
menu_principal = tk.Menu(barra_menu)
barra_menu.add_cascade(label =
'Extras', menu=menu_principal)
submenu0 = tk.Menu(menu_principal)
menu_principal.add_cascade(label =
'Masajista', menu=submenu0)
submenu0.add_command(label = 'Femenino')
submenu0.add_command(label = 'Masculino')
submenu1 = tk.Menu(menu_principal)
menu_principal.add_cascade(label =
'Comida', menu=submenu1)
submenu1.add_command(label = 'Barra de Cereal')
submenu1.add_command(label =  'Mix frutos secos')
submenu2 = tk.Menu(menu_principal)
submenu2 = tk.Menu(menu_principal)
menu_principal.add_cascade(label =
'Bebida', menu=submenu2)
submenu2.add_command(label = 'Jamaica')
submenu2.add_command(label = 'Tamarindo')
ventana.mainloop()
