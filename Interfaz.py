from tkinter import *
from tkinter import  messagebox
from tkinter import filedialog
root  = Tk()

def infoEstud():
    messagebox.showinfo("Estudiante","Victor Abdiel Lux Juracán\n201403946\nIPC2")
def infoProgram():
    messagebox.showinfo("Acerca de","Simulador de Ensamblaje \n V.4.0")
def salir():

    if messagebox.askquestion("Salir","Desea Salir?")=="yes":
        root.destroy()

root.title('Simulacion')
#root.resizable(0,0)#ancho, largo (boolean redimencion)
root.iconbitmap("ICO.ico") #icono
#root.geometry("650x350")#cambiar tama
barraMenu = Menu(root)
root.config(bg="sky blue", menu=barraMenu)#configuraciones

fr = Frame()
fr.pack()
fr.config(bg="white",width="650",height="350")
#Imagen = PhotoImage(file="image.png")
#label1 = Label(fr,image=Imagen) #para usar label variable
#label1.place(x="100",y="200")

Label(fr,text = "Label1",font=("Arial","18"),bg="white").grid(row="0",column="0")
texto = Entry(fr,font=("Arial","18"))
texto.grid(row="0", column="1")

archivoMenu = Menu(barraMenu,tearoff=0)
archivoMenu.add_command(label="Cargar Archivo Maquina")
archivoMenu.add_command(label="Cargar Archivo Simulacion")
archivoMenu.add_separator()

archivoMenu.add_command(label="Salir",command=salir)

archivoRepor = Menu(barraMenu,tearoff=0)
archivoRepor.add_command(label="Reporte Simulacion")
archivoRepor.add_command(label="Reporte Secuencia de Cola")

archivoAyuda= Menu(barraMenu,tearoff=0)
archivoAyuda.add_command(label="Estudiante",command=infoEstud)
archivoAyuda.add_command(label="Acerca de",command=infoProgram)

barraMenu.add_cascade(label="Archivo",menu=archivoMenu)
barraMenu.add_cascade(label="Repotes",menu=archivoRepor)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)


root.mainloop()


