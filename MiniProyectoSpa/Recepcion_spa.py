import tkinter as tk
from tkinter import PhotoImage
from PIL import ImageTk, Image


ventana = tk.Tk()

ventana.title("Recepción Spa")
ventana.geometry("1000x800")
ventana.configure(background="lightblue")

imagen_fondo = Image.open("Imagenes\spalogo.png")
imagen_fondo = imagen_fondo.resize((1000,800))
fondo = Image.new("RGBA", imagen_fondo.size, (173, 216, 230))
imagen_fondo_combinada = Image.alpha_composite(fondo, imagen_fondo)


img = ImageTk.PhotoImage(imagen_fondo_combinada)
etiqueta_fondo = tk.Label(ventana, image=img)
etiqueta_fondo.pack(fill="both", expand=True)

ventana.mainloop()

