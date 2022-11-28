txt = " "
cont = 0
def incrementarContador():
    global cont
    cont +=1
    return "%d" %cont

class Nodo(): 
    pass


# class p_sentencias(Nodo):
#     def __init__(self,name):
#         self.name = name

#     #def imprimir():

#     def traducir(self):
#         global txt
#         id = incrementarContador()

#         return id

class p_operador(Nodo):
    def __init__(self,name):
        self.name = name

    #def imprimir():

    def traducir(self):
        global txt
        id = incrementarContador()

        return id
class p_operacionMatematica(Nodo):
    def __init__(self,name):
        self.name = name

    #def imprimir():
        
    def traducir(self):
        global txt
        id = incrementarContador()

        return id
class p_operaciones(Nodo):
    def __init__(self,name):
        self.name = name

    #def imprimir():
        
    def traducir(self):
        global txt
        id = incrementarContador()

        return id
class p_tipoDevalorNumerico(Nodo):
    def __init__(self,name):
        self.name = name

    #def imprimir():
        
    def traducir(self):
        global txt
        id = incrementarContador()

        return id
class p_tipoDeDato(Nodo):
    def __init__(self,name):
        self.name = name

    #def imprimir():
        
    def traducir(self):
        global txt
        id = incrementarContador()

        return id
class p_parametros(Nodo):
    def __init__(self,name):
        self.name = name

    #def imprimir():
        
    def traducir(self):
        global txt
        id = incrementarContador()

        return id
class p_foreach(Nodo):
    def __init__(self,name):
        self.name = name

    #def imprimir():
        
    def traducir(self):
        global txt
        id = incrementarContador()

        return id
class p_arraymaps(Nodo):
    def __init__(self,name):
        self.name = name

    #def imprimir():
        
    def traducir(self):
        global txt
        id = incrementarContador()

        return id
class p_funcion(Nodo):
    def __init__(self,name):
        self.name = name

    #def imprimir():
        
    def traducir(self):
        global txt
        id = incrementarContador()

        return id
class p_monticuloHEAP(Nodo):
    def __init__(self,name):
        self.name = name

    #def imprimir():
        
    def traducir(self):
        global txt
        id = incrementarContador()

        return id
class p_instrucciones(Nodo):
    def __init__(self,name):
        self.name = name

    #def imprimir():
        
    def traducir(self):
        global txt
        id = incrementarContador()

        return id
class p_instruccion(Nodo):
    def __init__(self,name):
        self.name = name

    #def imprimir():
        
    def traducir(self):
        global txt
        id = incrementarContador()

        return id
class p_valores(Nodo):
    def __init__(self,name):
        self.name = name

    #def imprimir():
        
    def traducir(self):
        global txt
        id = incrementarContador()

        return id
class p_booleano(Nodo):
    def __init__(self,name):
        self.name = name

    #def imprimir():
        
    def traducir(self):
        global txt
        id = incrementarContador()

        return id
class p_booleanos(Nodo):
    def __init__(self,name):
        self.name = name

    #def imprimir():
        
    def traducir(self):
        global txt
        id = incrementarContador()

        return id
class p_o_logicos(Nodo):
    def __init__(self,name):
        self.name = name

    #def imprimir():
        
    def traducir(self):
        global txt
        id = incrementarContador()

        return id
class p_comparacion(Nodo):
    def __init__(self,name):
        self.name = name

    #def imprimir():

    def traducir(self):
        global txt
        id = incrementarContador()

        return id
class p_o_comparar(Nodo):
    def __init__(self,name):
        self.name = name

    #def imprimir():

    def traducir(self):
        global txt
        id = incrementarContador()

        return id
class p_asignacion(Nodo):
    def __init__(self,name):
        self.name = name

    #def imprimir():
        
    def traducir(self):
        global txt
        id = incrementarContador()

        return id
class p_difigual(Nodo):
    def __init__(self,name):
        self.name = name

    #def imprimir():
        
    def traducir(self):
        global txt
        id = incrementarContador()

        return id
class p_operadores_aritmeticos(Nodo):
    def __init__(self,name):
        self.name = name

    #def imprimir():
        
    def traducir(self):
        global txt
        id = incrementarContador()

        return id
class p_aritmetica(Nodo):
    def __init__(self,name):
        self.name = name

    #def imprimir():
        
    def traducir(self):
        global txt
        id = incrementarContador()

        return id
class p_crearArray(Nodo):
    def __init__(self,name):
        self.name = name

    #def imprimir():
        
    def traducir(self):
        global txt
        id = incrementarContador()

        return id
class p_valoresArray(Nodo):
    def __init__(self,name):
        self.name = name

    #def imprimir():
        
    def traducir(self):
        global txt
        id = incrementarContador()

        return id
class p_repite_valoresSeparadosComa(Nodo):
    def __init__(self,name):
        self.name = name

    #def imprimir():
        
    def traducir(self):
        global txt
        id = incrementarContador()

        return id
class p_repite_claveValorSeparadosComa(Nodo):
    def __init__(self,name):
        self.name = name

    #def imprimir():
        
    def traducir(self):
        global txt
        id = incrementarContador()

        return id
class p_switchCase(Nodo):
    def __init__(self,name):
        self.name = name

    #def imprimir():
        
    def traducir(self):
        global txt      
        id = incrementarContador()

        return id 

class p_caso_switch(Nodo):
    def __init__(self,name):
        self.name = name

    #def imprimir():
        
    def traducir(self):
        global txt
        id = incrementarContador()

        return id
class p_casos_switch(Nodo):
    def __init__(self,name):
        self.name = name

    #def imprimir():
        
    def traducir(self):
        global txt
        id = incrementarContador()

        return id
class p_comentarios(Nodo):
    def __init__(self,name):
        self.name = name

    #def imprimir():
        
    def traducir(self):
        global txt
        id = incrementarContador()

        return id
class p_impresion(Nodo):
    def __init__(self,name):
        self.name = name

    #def imprimir():
        
    def traducir(self):
        global txt
        id = incrementarContador()

        return id
class p_programabasico(Nodo):
    def __init__(self,name):
        self.name = name

    #def imprimir():
        
    def traducir(self):
        global txt
        id = incrementarContador()

        return id
class  p_incdec(Nodo):
    def __init__(self,name):
        self.name = name

    #def imprimir():
        
    def traducir(self):
        global txt
        id = incrementarContador()

        return id
class p_incdecfor(Nodo):
    def __init__(self,name):
        self.name = name

    #def imprimir():
        
    def traducir(self):
        global txt
        id = incrementarContador()

        return id
class  p_for(Nodo):
    def __init__(self,name):
        self.name = name

    #def imprimir():
        
    def traducir(self):
        global txt
        id = incrementarContador()

        return id
class p_SplHeap(Nodo):
    def __init__(self,name):
        self.name = name

    #def imprimir():
        
    def traducir(self):
        global txt
        id = incrementarContador()

        return id