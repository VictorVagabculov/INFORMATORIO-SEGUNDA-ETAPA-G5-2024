
import tkinter as tk

lista_de_servicios = ["Manos", "Pies", "Rostro", "Masajes"]
lista_de_tiempos = [45, 45, 90, 60]


def obtener_duracion(servicio):
    indice = lista_de_servicios.index(servicio)  # Busca en la lista de servicios
    tiempo = lista_de_tiempos[indice]  # Obtiene el indice de la lista de tiempos
    return (f"Duración: {tiempo} minutos")

#Para poder usar la función anterior como label
def mostrar_duracion(servicio):
    duracion = obtener_duracion(servicio)
    etiqueta.config(text=duracion)


ventana =tk.Tk()
ventana.title('Menu de Servicios')
ventana.geometry('400x200')

menu_servicio = tk.Menu(ventana)
ventana.config(menu = menu_servicio)

#Menu principal
menu_principal = tk.Menu(menu_servicio)
menu_servicio.add_cascade(label = 'Servicios', menu= menu_principal)

#Despliegue de servicios ofrecidos que a su vez despliega la duraciín de cada uno.

for servicio in lista_de_servicios:
    submenu = tk.Menu(menu_principal)
    menu_principal.add_cascade(label=servicio, menu=submenu)
    
    submenu.add_command(label=obtener_duracion(servicio))


ventana.mainloop()