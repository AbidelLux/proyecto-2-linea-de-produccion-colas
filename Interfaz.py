from tkinter import *
root  = Tk()
root.title('Simulacion')
#root.resizable(0,0)#ancho, largo (boolean redimencion)
root.iconbitmap("ICO.ico") #icono
#root.geometry("650x350")#cambiar tama
root.config(bg="sky blue")#configuraciones

fr = Frame()
fr.pack()
fr.config(bg="white",width="650",height="350")
#Imagen = PhotoImage(file="image.png")
#label1 = Label(fr,image=Imagen) #para usar label variable
#label1.place(x="100",y="200")

Label(fr,text = "Label1",font=("Arial","18"),bg="white").grid(row="0",column="0")
texto = Entry(fr,font=("Arial","18"))
texto.grid(row="0", column="1")
root.mainloop()