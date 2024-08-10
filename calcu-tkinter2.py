from tkinter import *
# Creamos la ventana inicial
ventana = Tk()
ventana.title("Calculadora Básica")
ventana.configure(background="thistle1")

# Entrada de texto
tx1 = Entry(ventana, font=("Calibri 20"), background="plum3", )
tx1.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Funciones de los botones al clikear
i = 0

# ingresa los numeros a la pantalla y la variable global es para que vayan agregandose
# de izquierda a derecha


def click(valor):
    global i
    tx1.insert(i, valor)
    i += 1


# Borra y vuelve a la posicion 0


def borrar():
    tx1.delete(0, END)
    i = 0


# con get ingresa los numeros y con eval realiza las operaciones, borra las operaciones en delete y
# muestra el resultado, luego vuelve a cero


def operaciones():
    pedido = tx1.get()
    resultado = eval(pedido)
    tx1.delete(0, END)
    tx1.insert(0, resultado)
    i = 0


# Botones
B1 = Button(ventana, text="1", width=5, height=2,
            background="pink", command=lambda: click(1))
B2 = Button(ventana, text="2", width=5, height=2,
            background="pink", command=lambda: click(2))
B3 = Button(ventana, text="3", width=5, height=2,
            background="pink", command=lambda: click(3))
B4 = Button(ventana, text="4", width=5, height=2,
            background="pink", command=lambda: click(4))
B5 = Button(ventana, text="5", width=5, height=2,
            background="pink", command=lambda: click(5))
B6 = Button(ventana, text="6", width=5, height=2,
            background="pink", command=lambda: click(6))
B7 = Button(ventana, text="7", width=5, height=2,
            background="pink", command=lambda: click(7))
B8 = Button(ventana, text="8", width=5, height=2,
            background="pink", command=lambda: click(8))
B9 = Button(ventana, text="9", width=5, height=2,
            background="pink", command=lambda: click(9))
B0 = Button(ventana, text="0", width=5, height=2,
            background="pink", command=lambda: click(0))

Bborrar = Button(ventana, text="AC", width=5, height=2,
                 background="plum4", command=lambda: borrar())
Bparentesis1 = Button(
    ventana, text="(", width=5, height=2, background="plum2", command=lambda: click("("))
Bparentesis2 = Button(ventana, text=")", width=5,
                      height=2, background="plum2", command=lambda: click(")"))
Bpunto = Button(ventana, text=".", width=5, height=2,
                background="plum2", command=lambda: click("."))

Bdiv = Button(ventana, text="/", width=5, height=2,
              background="violet", command=lambda: click("/"))
Bmulti = Button(ventana, text="*", width=5, height=2,
                background="violet", command=lambda: click("*"))
Bsuma = Button(ventana, text="+", width=5, height=2,
               background="violet", command=lambda: click("+"))
Bresta = Button(ventana, text="-", width=5, height=2,
                background="violet", command=lambda: click("-"))
Bigual = Button(ventana, text="=", width=5, height=2,
                background="plum4", command=lambda: operaciones())


# Ubicar los botones en pantalla
Bborrar.grid(row=1, column=0, padx=5, pady=5)
Bparentesis1.grid(row=1, column=1, padx=5, pady=5)
Bparentesis2.grid(row=1, column=2, padx=5, pady=5)
Bsuma.grid(row=1, column=3, padx=5, pady=5)

B1.grid(row=2, column=0, padx=5, pady=5)
B2.grid(row=2, column=1, padx=5, pady=5)
B3.grid(row=2, column=2, padx=5, pady=5)
Bresta.grid(row=2, column=3, padx=5, pady=5)

B4.grid(row=3, column=0, padx=5, pady=5)
B5.grid(row=3, column=1, padx=5, pady=5)
B6.grid(row=3, column=2, padx=5, pady=5)
Bmulti.grid(row=3, column=3, padx=5, pady=5)

B7.grid(row=4, column=0, padx=5, pady=5)
B8.grid(row=4, column=1, padx=5, pady=5)
B9.grid(row=4, column=2, padx=5, pady=5)
Bdiv.grid(row=4, column=3, padx=5, pady=5)

B0.grid(row=5, column=1, padx=5, pady=5)
Bpunto.grid(row=5, column=2, padx=5, pady=5)
Bigual.grid(row=5, column=3, padx=5, pady=5)


ventana.mainloop()
