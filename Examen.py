import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as mBox
from tkinter import scrolledtext

def funcion_click1():
    x=0
    if option.get()==1:
        x=x+20
    if option_1.get()==1 or option_2.get()==1:
        if option_3.get()==0 and option_4.get()==0 and option_5.get()==0:
            x=x+20
    if option2.get()==1:
            x=x+20
    if p1.get()=="es un modelo matemático usado para aproximar la relación":
        x=x+20
    if p2.get()=="una de las distribuciones de probabilidad de variable continua":
        x=x+20
    mBox.showinfo("Calificacion","Tu calificacion es "+str(x))

ventana=tk.Tk()
ventana.title("Examen") #titulo
ventana.resizable(0,0) #dimension

barra_menu=Menu()
ventana.config(menu=barra_menu)

texto1=ttk.Label(ventana,text="¿Que es la regresion lineal?").grid(column=0,row=0)
p1=tk.StringVar()
Pnombre=ttk.Entry(ventana,width=60, textvariable=p1)
Pnombre.grid(column=1,row=0)

texto1=ttk.Label(ventana,text="¿Qué es una distribución normal?").grid(column=0,row=1)
p2=tk.StringVar()
Pnombre=ttk.Entry(ventana,width=60, textvariable=p2)
Pnombre.grid(column=1,row=1)

texto10=ttk.Label(ventana,text="¿En que consiste la estadística descriptiva?").grid(column=0,row=2)
option=tk.IntVar()
radio1=tk.Radiobutton(ventana,text="Tienen por objeto fundamental describir y analizar las características de un conjunto de datos", variable=option,value=1)
radio1.grid(column=0,row=3,sticky=tk.W)
radio2=tk.Radiobutton(ventana,text="Es una parte de la Estadística que comprende los métodos y procedimientos", variable=option,value=2)
radio2.grid(column=0,row=4,sticky=tk.W)
radio3=tk.Radiobutton(ventana,text="es una técnica estadística donde la puntuación de una variable Y se predice a partir de la puntuación de una segunda variable X", variable=option,value=3)
radio3.grid(column=0,row=5,sticky=tk.W)

texto10=ttk.Label(ventana,text="¿Es un metodo estadistico?").grid(column=0,row=6)
option2=tk.IntVar()
radio4=tk.Radiobutton(ventana,text="Niveles de medición", variable=option2,value=1)
radio4.grid(column=0,row=7,sticky=tk.W)
radio5=tk.Radiobutton(ventana,text="Técnicas de aproximacion", variable=option2,value=2)
radio5.grid(column=0,row=8,sticky=tk.W)
radio6=tk.Radiobutton(ventana,text="Experimentales", variable=option2,value=3)
radio6.grid(column=0,row=9,sticky=tk.W)

texto9=ttk.Label(ventana,text="¿Cual de las siguientes si son tipos de estadistica?").grid(column=0,row=10)
option_1=tk.IntVar()
casilla_1=tk.Checkbutton(ventana,text="Estadística descriptiva",variable=option_1).grid(column=0,row=11)
option_2=tk.IntVar()
casilla_2=tk.Checkbutton(ventana,text="Estadística inferencial",variable=option_2).grid(column=0,row=12)
option_3=tk.IntVar()
casilla_3=tk.Checkbutton(ventana,text="Estadistica modulae",variable=option_3).grid(column=0,row=13)
option_4=tk.IntVar()
casilla_4=tk.Checkbutton(ventana,text="Estadistica finita",variable=option_4).grid(column=0,row=14)
option_5=tk.IntVar()
casilla_5=tk.Checkbutton(ventana,text="Redes sociales",variable=option_5).grid(column=0,row=15)


ImprimirDP=ttk.Button(ventana, text="Imprimir Resultado",command=funcion_click1).grid(column=3, row=16)

ventana.mainloop()