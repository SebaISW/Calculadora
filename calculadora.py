from tkinter import *

ventana = Tk()
ventana.title("Calculadora")
entrada = 0
#Entrada
e_text = Entry(ventana, font = ("Calibri 20"))
e_text.grid(row = 0, column = 0, columnspan = 4, padx = 50,pady = 5)

#Funciones
def click_boton(valor):
    global entrada
    e_text.insert(entrada,valor)
    entrada += 1
def borra():
    e_text.delete(0,END)
def calculo():
    ecuacion = e_text.get()
    resultado = eval(ecuacion)
    e_text.delete(0,END)
    e_text.insert(0,resultado)

#Botones
boton1 = Button(ventana, text = "1", width = 5, height = 2, command = lambda: click_boton(1))
boton2 = Button(ventana, text = "2", width = 5, height = 2, command = lambda: click_boton(2))
boton3 = Button(ventana, text = "3", width = 5, height = 2, command = lambda: click_boton(3))
boton4 = Button(ventana, text = "4", width = 5, height = 2, command = lambda: click_boton(4))
boton5 = Button(ventana, text = "5", width = 5, height = 2, command = lambda: click_boton(5))
boton6 = Button(ventana, text = "6", width = 5, height = 2, command = lambda: click_boton(6))
boton7 = Button(ventana, text = "7", width = 5, height = 2, command = lambda: click_boton(7))
boton8 = Button(ventana, text = "8", width = 5, height = 2, command = lambda: click_boton(8))
boton9 = Button(ventana, text = "9", width = 5, height = 2, command = lambda: click_boton(9))
boton0 = Button(ventana, text = "0", width = 19, height = 2, command = lambda: click_boton(0))

boton_borrar = Button(ventana, text = "AC", width = 5, height = 2, command = lambda: borra())
boton_parentesis1 = Button(ventana, text = "(",width = 5, height = 2, command = lambda: click_boton("("))
boton_parentesis2 = Button(ventana, text = ")",width = 5, height = 2, command = lambda: click_boton(")"))
boton_punto = Button(ventana, text = ".",width = 5, height = 2, command = lambda: click_boton("."))

boton_div = Button(ventana, text = "/",width = 5, height = 2, command = lambda: click_boton("/"))
boton_mult = Button(ventana, text = "x",width = 5, height = 2, command = lambda: click_boton("*"))
boton_sum = Button(ventana, text = "+",width = 5, height = 2, command = lambda: click_boton("+"))
boton_rest = Button(ventana, text = "-",width = 5, height = 2, command = lambda: click_boton("-"))
boton_igual = Button(ventana, text = "=",width = 5, height = 2, command = lambda: calculo())




#Agregar botones en pantalla 
boton_borrar.grid(row= 1, column = 0, padx = 5, pady= 5)
boton_parentesis1.grid(row= 1 , column = 1, padx = 5, pady= 5)
boton_parentesis2.grid(row= 1, column = 2, padx = 5, pady= 5)
boton_div.grid(row= 1, column = 3, padx = 5, pady= 5)
boton7.grid(row= 2, column = 0, padx = 5, pady= 5)
boton8.grid(row= 2, column = 1, padx = 5, pady= 5)
boton9.grid(row= 2, column = 2, padx = 5, pady= 5)
boton_mult.grid(row= 2, column = 3, padx = 5, pady= 5)


boton4.grid(row= 3, column = 0, padx = 5, pady= 5)
boton5.grid(row= 3, column = 1, padx = 5, pady= 5)
boton6.grid(row= 3, column = 2, padx = 5, pady= 5)
boton_sum.grid(row = 3, column = 3, padx = 5, pady = 5)

boton1.grid(row= 4, column = 0, padx = 5, pady= 5)
boton2.grid(row= 4, column = 1, padx = 5, pady= 5)
boton3.grid(row= 4, column = 2, padx = 5, pady= 5)
boton_rest.grid(row = 4, column = 3, padx = 5, pady = 5)

boton0.grid(row = 5, column = 0, columnspan = 2, padx = 5, pady = 5)
boton_punto.grid(row = 5, column = 2, padx = 5, pady = 5)
boton_igual.grid(row = 5, column = 3, padx = 5, pady = 5)




ventana.mainloop()
