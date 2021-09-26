from tkinter import *
from tkinter import  messagebox
from tkinter import filedialog
from tkinter import ttk
root  = Tk()
#------------------------------------------------------------------------------------------------------------------------
def infoEstud():
    messagebox.showinfo("Estudiante","Victor Abdiel Lux Juracán\n201403946\nIPC2")
def infoProgram():
    messagebox.showinfo("Acerca de","Simulador de Ensamblaje \n V.4.0")
def salir():

    if messagebox.askquestion("Salir","Desea Salir?")=="yes":
        root.destroy()
def abrirXMLmaq():
    ruta = filedialog.askopenfilename(title="Abrir",filetypes=(("archivos XML","*.xml"),("todos los Archivos","*.*")))
    print(ruta)

def abrirXMLsim():
    ruta = filedialog.askopenfilename(title="Abrir",filetypes=(("archivos XML","*.xml"),("todos los Archivos","*.*")))
    print(ruta)
#----------------------------------------------------------------------------------------------------------------------- raiz de interfaz
root.title('Simulacion')
#root.resizable(0,0)#ancho, largo (boolean redimencion)
root.iconbitmap("ICO.ico") #icono
#root.geometry("650x350")#cambiar tama
barraMenu = Menu(root)
root.config(bg="sky blue", menu=barraMenu)#configuraciones
#------------------------------------------------------------------------------------------------------------------------ Frame
fr = Frame()
fr.pack()
fr.config(bg="white",width="650",height="350")
#Imagen = PhotoImage(file="image.png")
#label1 = Label(fr,image=Imagen) #para usar label variable
#label1.place(x="100",y="200")
#-----------------------------------------------------------------------------------------------------------------------componentes frame
Label(fr,text = "Tiempo de Simulacion",font=("Arial","12"),bg="white").grid(row=4,column=2)
texto = Entry(fr,font=("Arial","12"))
texto.grid(row=4, column=4)


Label(fr,text="Productos Disponibles para simulacion",font=("Arial Black","14"),bg="white").grid(row=0,column=0)
combo = ttk.Combobox(fr,values=["prod2","prod1"],state="readonly")
combo.grid(row=1,column=0)
combo.bind("<<ComboboxSelected>>")

Label(fr,text="Componentes Necesarios",font = ("Arial Black","14"),bg="white").grid(row=2,column=0)
Componentes = Text(fr)
Componentes.grid(row=3,column=0)
scroll1 = Scrollbar(fr,command=Componentes.yview)
scroll1.grid(row=3,column=1,sticky="nsew")
Componentes.config(width=45,height=10,padx=10,pady=10,yscrollcommand=scroll1.set)

Label(fr,text="Tabla de Resultados de Simulacion",font=("Arial Black","14"),bg="white").grid(row=2,column=2)
table = Text(fr)
table.grid(row=3,column=2)
scroll2 = Scrollbar(fr,command=table.yview)
scroll2.grid(row=3,column=3,sticky="nsew")
table.config(width=45,height=10,padx=10,pady=10,yscrollcommand=scroll2.set)

barraprogreso = ttk.Progressbar(fr,mode="indeterminate")
barraprogreso.grid(row=4,column=0)
barraprogreso.start(5)


#-----------------------------------------------------------------------------------------------------------------------MEnu
archivoMenu = Menu(barraMenu,tearoff=0)
archivoMenu.add_command(label="Cargar Archivo Maquina",command=abrirXMLmaq)
archivoMenu.add_command(label="Cargar Archivo Simulacion",command=abrirXMLsim)
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


