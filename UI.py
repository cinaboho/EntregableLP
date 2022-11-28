from tkinter import  *
from sintactico import validaRegla as validacion,arrayErrores,log_sintactico_array
from lexico import validaReglaLexico,log_lexico_array


raiz=Tk()
raiz.title("Intérpete PHP - Grupo 2")
raiz.resizable(True,False)
raiz.iconbitmap("cat2.ico")
raiz.geometry("1400x550")

miFrame= Frame(raiz,width=1400,height=500)
miFrame.pack()

label1= Label(miFrame,text="Ingrese su código PHP",font=("Times", "24", "bold italic"))
label1.grid(row=0,column=0,pady=10)

#texto=StringVar()
#cuadro=Entry(miFrame,textvariable=texto)
#cuadro.grid(row=2,column=2,padx=10,pady=10)


codigo=Text(miFrame)
codigo.grid(row=1,column=0,padx=5,ipadx=2,pady=1)
scroll=Scrollbar(miFrame,command=codigo.yview)
scroll.grid(row=1,column=1,sticky="nsw")
codigo.config(yscrollcommand=scroll.set)





#texto=StringVar()
#cuadro=Entry(miFrame,textvariable=texto)
#cuadro.grid(row=1,column=2,padx=1,ipadx=100,ipady=200)
texto=Text(miFrame)
texto.grid(row=1,column=2,padx=5,ipadx=2,ipady=1)



def botonLexico():
    input=codigo.get("1.0",'end-1c')
    texto.delete("1.0", "end")
    validaReglaLexico(input.rstrip('\n'))
    textoError=""
    for x in log_lexico_array:
       textoError=textoError+x+" \n"       
    texto.insert(END,textoError)
    print(input)

def boton():
    input=codigo.get("1.0",'end-1c')
    texto.delete("1.0", "end")
    validacion(input.rstrip('\n'))
    textoError=""
    
    for x in log_sintactico_array:
       textoError=textoError+x+" \n"               
    for x in arrayErrores:
       textoError=textoError+x+" \n"       
    texto.insert(END,textoError)
    print(input)


botonLexico=Button(raiz,text="LEXICO",command=botonLexico)
botonLexico.pack()
boton2=Button(raiz,text="SINTACTICO",command=boton)
boton2.pack()



#resultado= Label(miFrame,text="Resultado: ",font=("Times", "18"))
#resultado.grid(row=3,column=0,pady=10)
#texto=StringVar(resultado)


raiz.mainloop()