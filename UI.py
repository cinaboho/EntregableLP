from tkinter import  *
from sintactico import validaRegla as validacion
raiz=Tk()
raiz.title("Intérpete PHP - Grupo 2")
raiz.resizable(True,False)
raiz.iconbitmap("cat2.ico")
raiz.geometry("1100x550")

miFrame= Frame(raiz,width=1000,height=500)
miFrame.pack()

label1= Label(miFrame,text="Ingrese su código PHP",font=("Times", "24", "bold italic"))
label1.grid(row=0,column=0,pady=10)

#texto=StringVar()
#cuadro=Entry(miFrame,textvariable=texto)
#cuadro.grid(row=2,column=2,padx=10,pady=10)

codigo=Text(miFrame)
codigo.grid(row=1,column=0,padx=5,pady=10)
scroll=Scrollbar(miFrame,command=codigo.yview)
scroll.grid(row=1,column=1,sticky="nsw")
codigo.config(yscrollcommand=scroll.set)



texto=StringVar()
cuadro=Entry(miFrame,textvariable=texto)
cuadro.grid(row=1,column=2,padx=10,ipadx=100,ipady=200)



def boton():
    input=codigo.get("1.0",'end-1c')
    texto.set("")
    validacion(input.rstrip('\n'))
    texto.set("prueba")
    print(input)


boton=Button(raiz,text="Analizar",command=boton)
boton.pack()


#resultado= Label(miFrame,text="Resultado: ",font=("Times", "18"))
#resultado.grid(row=3,column=0,pady=10)
#texto=StringVar(resultado)


raiz.mainloop()