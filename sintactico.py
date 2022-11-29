import ply.yacc as yacc
import os
import time
from lexico import tokens

#----------------------- Inicio Johanna
arrayErrores=[]
log_sintactico_array=[]
#----------------------- Fin Johanna


#----------------------- Inicio Cindy
procedence = (
			  ('right', 'IGUAL'),
			  ('left','MENORQUE','MENORQUEI','MAYORQUE','MAYORQUEI'),
              ('left','ENTERO','DIVIDE'),
			  ('left', 'PARENIZQ', 'PARENDER'),
              ('left', 'LLAVEIZQ','LLAVEDER'),
              ('left', 'CORCHIZQ','CORCHDER')

)
#----------------------- Fin Cindy
nombres= {}

def p_sentencias(p):
    '''sentencias : final
                  | operacionMatematica
                  | operador
                  | tipoDevalorNumerico
                  | foreach
                  | arraymaps
                  | tipoDeDato
                  | parametros
                  | funcion
                  | monticuloHEAP
                  | comentarios
                  | impresion
                  | programabasico
                  | for
                  | SplHeap                  
                  | clases
                  | instrucciones
                  | insertheap
    '''

#----------------------- Inicio Cindy
def p_operador(p):
    '''operador : MAS
                | MENOS
                | MULTIPLICA
                | DIVIDE
                | MODULO
                | EXPONENCIACION
    '''

# #     $valor = $valor * $valor;
# #     $valor = $valor * 2;
# #     $valor = 2 * 2;

def p_operacionMatematica(p):
    '''operacionMatematica :  VARIABLE_PHP IGUAL VARIABLE_PHP        operador VARIABLE_PHP        PUNTOYCOMA
                            | VARIABLE_PHP IGUAL VARIABLE_PHP        operador tipoDevalorNumerico PUNTOYCOMA
                            | VARIABLE_PHP IGUAL tipoDevalorNumerico operador tipoDevalorNumerico PUNTOYCOMA
                            | VARIABLE_PHP IGUAL tipoDevalorNumerico operador tipoDevalorNumerico operaciones PUNTOYCOMA
                               '''
    

     #----------------------- Semantico Cindy


def p_operaciones(p):
    '''operaciones : tipoDevalorNumerico operador tipoDevalorNumerico
                            | tipoDevalorNumerico operador tipoDevalorNumerico operador tipoDevalorNumerico
                            | PARENIZQ operaciones PARENDER
                            | operador PARENIZQ operaciones PARENDER operaciones
                            | PARENIZQ operaciones PARENDER operaciones
                            | operador PARENIZQ operaciones PARENDER
        '''
def p_tipoDevalorNumerico(p):
    '''tipoDevalorNumerico : ENTERO
                           | FLOTANTE
    '''
    #----------------------- Semantico Cindy
    #p[0]=nombres[p[1],p[2]]

#tipoDeDato para poner dentro de una estructura ej: array{var1, var2, var3}
def p_tipoDeDato(p):
    '''tipoDeDato : ENTERO
                  | FLOTANTE
                  | CADENA
                  | VARIABLE_PHP
                  | BOOLEANO
                  | NULL
    '''
    #----------------------- Semantico Cindy

def p_parametros(p):
    '''parametros : tipoDeDato
                  | tipoDeDato COMA parametros
    '''

# foreach ($array as &$valor) {$valor = $valor * 2;}
def p_foreach(p):
    '''foreach : FOREACH PARENIZQ VARIABLE_PHP AS AMPERSAND VARIABLE_PHP PARENDER LLAVEIZQ operacionMatematica LLAVEDER
    '''
    log_sintactico_array.append("Foreach")
    #----------------------- Semantico Cindy
    p[0]=p[9]


# $b=array_map("cubo",$a);
# array_map("cubo",$a);
def p_arraymaps(p):
    '''arraymaps : OPERAMAPA PARENIZQ parametros PARENDER PUNTOYCOMA
                 | VARIABLE_PHP IGUAL OPERAMAPA PARENIZQ parametros PARENDER PUNTOYCOMA
    '''

#new jupilerLeague();
def p_funcion(p):
    '''funcion : NEW NOMBRE PARENIZQ parametros PARENDER PUNTOYCOMA
    | NEW NOMBRE PARENIZQ PARENDER
    | COUNT PARENIZQ parametros PARENDER PUNTOYCOMA
    | COUNT PARENIZQ VARIABLE_PHP COMA NOMBRE PARENDER PUNTOYCOMA
    | COUNT PARENIZQ VARIABLE_PHP PARENDER PUNTOYCOMA
    | NOMBRE PARENIZQ parametros PARENDER PUNTOYCOMA
    '''
    log_sintactico_array.append("Función")



#$heap = new JupilerLeague();
def p_monticuloHEAP(p):
  '''monticuloHEAP : HEAP IGUAL funcion
  '''
  log_sintactico_array.append("Monticulo Heap")
  p[0]=p[3]

#$heap->insert($value);
#$heap->insert(19);
def p_insertheap(p):
    '''insertheap : VARIABLE_PHP o_comparar INSERT PARENIZQ VARIABLE_PHP PARENDER PUNTOYCOMA
                   | VARIABLE_PHP o_comparar INSERT PARENIZQ     ENTERO   PARENDER PUNTOYCOMA
    '''
    log_sintactico_array.append("Insert Heap")
    p[0]=p[2]

#----------Fin Cindy
#----------------------- Inicio Johanna
def p_instrucciones(p):
    '''instrucciones : instruccion
                     | instrucciones instruccion
                     '''
def p_instruccion(p):
    '''instruccion : asignacion                     
                    | echo
                    | switchCase                    
                    | verificacion_if
                    | retornoValor
                    | comentarios
                    | define
                    | impresion
                    | for
                    | SplHeap
                    | function2
                    | final
                     '''
def p_valores(p):
    '''valores : ENTERO
                  | FLOTANTE
                  | CADENA
                  | VARIABLE_PHP
                  | BOOLEANO
                  | aritmetica
                  | booleanos
                  | NOMBRE PARENIZQ  PARENDER
                  | NOMBRE PARENIZQ valores PARENDER
                  | NOMBRE PARENIZQ valoresParametros PARENDER
                  | crearArrayCorta
                  | crearArrayLarga
     '''

def p_booleano(p):
    '''booleano : BOOLEANO
                | comparacion
                | OPERLOGICO_NOT booleanos
    '''

def p_booleanos(p):
    '''booleanos : booleano
                 | booleanos o_logicos booleanos
    '''

def p_o_logicos(p):
    '''o_logicos : OPERLOGICO_AND
                 | OPERLOGICO_OR'''

def p_comparacion(p):
    ''' comparacion : valores o_comparar valores
     '''

def p_o_comparar(p):
    '''o_comparar : IGUALIGUAL
                  | NOIGUAL
                  | MENORQUE
                  | MAYORQUE
                  | MAYORIGUAL
                  | MENORIGUAL
                  | OPERALOGICO_MAP
                  | OPERDCOMPARACION
                  | OPERCOMPARACION
                   '''

def p_asignacion(p):
    '''asignacion :   VARIABLE_PHP IGUAL valores PUNTOYCOMA
                    | VARIABLE_PHP IGUAL valores PUNTOYCOMA comentarios
                    | VARIABLE_PHP difigual valores PUNTOYCOMA
                    | VARIABLE_PHP difigual valores PUNTO valores PUNTOYCOMA comentarios
                    | VARIABLE_PHP difigual valores PUNTO valores PUNTOYCOMA
                    | VARIABLE_PHP IGUAL BOOLEANO PUNTOYCOMA
                    | VARIABLE_PHP IGUAL BOOLEANO PUNTOYCOMA comentarios
                    | VARIABLE_PHP IGUAL funcion PUNTOYCOMA
                    | VARIABLE_PHP IGUAL NULL PUNTOYCOMA
                    | VARIABLE_PHP IGUAL NOMBRE PARENIZQ VARIABLE_PHP PARENDER PUNTOYCOMA
                    | VARIABLE_PHP IGUAL NOMBRE PARENIZQ valores PARENDER PUNTOYCOMA
                    | VARIABLE_PHP IGUAL NOMBRE PARENIZQ PARENDER PUNTOYCOMA
                    | asignaSplheap
                    | VARIABLE_PHP IGUAL EXPLODE PARENIZQ CADENA COMA VARIABLE_PHP PARENDER PUNTOYCOMA
                    | VARIABLE_PHP IGUAL funcion
                    | VARIABLE_PHP o_comparar NOMBRE PUNTOYCOMA
                '''
    log_sintactico_array.append("asignacion")

def p_difigual(p):
    '''difigual : PUNTOIGUAL
                      | MASIGUAL
                      | MENOSIGUAL
       '''

def p_clases(p):
    '''clases : CLASS NOMBRE LLAVEIZQ LLAVEDER
        '''
    log_sintactico_array.append("clases")

def p_function(p):
    '''function2 : FUNCTION NOMBRE LLAVEIZQ LLAVEDER
                | FUNCTION NOMBRE PARENIZQ PARENDER LLAVEIZQ instrucciones LLAVEDER
                | PUBLIC FUNCTION COMPARE PARENIZQ parametros PARENDER LLAVEIZQ instrucciones LLAVEDER
                | FUNCTION NOMBRE PARENIZQ parametros PARENDER LLAVEIZQ instrucciones LLAVEDER
                | FUNCTION NOMBRE PARENIZQ valoresParametros PARENDER LLAVEIZQ instrucciones LLAVEDER
    '''
    log_sintactico_array.append("function")

def p_define(p):
    '''define : DEFINE PARENIZQ CADENA COMA valores PARENDER PUNTOYCOMA'''
    log_sintactico_array.append("define")


#def p_paramclases(p):
 #   '''paramclases :           '''
def p_operadores_aritmeticos(p):
    '''operadores_aritmeticos : MAS
                   | MENOS
                   | MULTIPLICA
                   | DIVIDE
    '''

def p_aritmetica(p):
    '''aritmetica : valores operadores_aritmeticos valores
                  | aritmetica operadores_aritmeticos valores'''

def p_echo(p):
    '''echo : ECHO valores PUNTOYCOMA
            | ECHO NOMBRE PARENIZQ valores PARENDER PUNTOYCOMA
            | ECHO CADENA PUNTOYCOMA
            | ECHO VARIABLE_PHP PUNTOYCOMA
            | ECHO aritmetica PUNTOYCOMA
    '''
    log_sintactico_array.append("ECHO")

def p_crearArrayCorta(p):
  #'''crearArrayCorta :  VARIABLE_PHP IGUAL ARRAY PARENIZQ valoresArray PARENDER PUNTOYCOMA
  '''crearArrayCorta :  CORCHIZQ valoresArray CORCHDER
  '''
  log_sintactico_array.append("Crear Array Corta")

def p_crearArrayLarga(p):
  #'''crearArrayLarga :  VARIABLE_PHP IGUAL ARRAY PARENIZQ valoresArray PARENDER PUNTOYCOMA
  '''crearArrayLarga :  ARRAY PARENIZQ valoresArray PARENDER
  '''
  log_sintactico_array.append("Crear Array larga")


def p_valoresArray(p):
    '''valoresArray : valores 
                    | valores OPERASIG_ARRAY valores 
                    | valores repite_valores
                    | valores OPERASIG_ARRAY valores  repite_claveValor
                '''
  
def p_repite_valoresSeparadosComa(p):
    '''
    repite_valores : COMA valores
                  | COMA valores COMA
                  | COMA valores repite_valores
    '''
def p_repite_claveValorSeparadosComa(p):
    '''repite_claveValor : COMA valores OPERASIG_ARRAY valores
                        | COMA valores OPERASIG_ARRAY valores COMA
                        | COMA valores OPERASIG_ARRAY valores repite_claveValor
    '''
def p_switchCase(p):  
  '''switchCase : SWITCH PARENIZQ valores PARENDER LLAVEIZQ casos_switch LLAVEDER                
                | SWITCH PARENIZQ valores PARENDER LLAVEIZQ casos_switch DEFAULT DOSPUNTOS LLAVEIZQ instrucciones LLAVEDER LLAVEDER
                | SWITCH PARENIZQ valores PARENDER DOSPUNTOS casos_switch ENDSWITCH PUNTOYCOMA
  '''
  log_sintactico_array.append("Switch")

def p_caso_switch(p):
    '''caso_switch : CASE valores DOSPUNTOS LLAVEIZQ instrucciones LLAVEDER
                    | CASE valores DOSPUNTOS LLAVEIZQ instrucciones BREAK PUNTOYCOMA LLAVEDER
                    | CASE valores DOSPUNTOS instrucciones
                    | CASE valores DOSPUNTOS instrucciones BREAK PUNTOYCOMA
    '''
    log_sintactico_array.append("Caso Switch")

def p_casos_switch(p):
    '''casos_switch : caso_switch casos_switch
                    | caso_switch '''

def p_valoresParametros(p):
    '''valoresParametros : valores
                        | valores repite_valores_parametro
                        | VARIABLE_PHP IGUAL valores
                        | VARIABLE_PHP IGUAL valores repite_valores_parametro
    '''
  
def p_repite_valoresParametros(p):
    '''
    repite_valores_parametro : COMA valores
                            | COMA VARIABLE_PHP IGUAL valores
                            | COMA valores repite_valores_parametro
                            | COMA VARIABLE_PHP IGUAL valores repite_valores_parametro
    '''

def p_verificacion_if(p):
    '''
    verificacion_if : IF PARENIZQ valores PARENDER LLAVEIZQ instrucciones LLAVEDER
                      | IF PARENIZQ valores PARENDER instruccion
                      | IF PARENIZQ valores PARENDER LLAVEIZQ instrucciones LLAVEDER ELSE LLAVEIZQ instrucciones LLAVEDER
                      | IF PARENIZQ valores PARENDER instruccion ELSE instrucciones
                      | IF PARENIZQ comparaciones o_comparar comparaciones PARENDER instrucciones
                      | IF PARENIZQ comparaciones o_comparar comparaciones PARENDER LLAVEIZQ instrucciones LLAVEDER
    '''
    log_sintactico_array.append("IF")

def p_comparaciones(p):
    '''comparaciones : VARIABLE_PHP CORCHIZQ ENTERO CORCHDER
    '''

def p_retornoValor(p):
    '''retornoValor : RETURN valores PUNTOYCOMA
    | RETURN comparaciones o_comparar comparaciones PUNTOYCOMA
    | RETURN comparaciones o_comparar comparaciones INTE ENTERO DOSPUNTOS ENTERO PUNTOYCOMA
    '''
    log_sintactico_array.append("RETURN")

#----------------------- Fin Johanna
#
#----------------------- Inicio Viviana
def p_comentarios(p):
    '''comentarios : COMENTARIO_UNA_LINEA
                | COMENTARIO_LARGO'''
def p_impresion(p):
    '''impresion : ECHO tipoDeDato PUNTOYCOMA
        | PRINT tipoDeDato PUNTOYCOMA
        | ECHO VARIABLE_PHP PUNTOYCOMA
        | PRINT VARIABLE_PHP PUNTOYCOMA
        | ECHO comparaciones PUNTOYCOMA
        | ECHO funcion
        | ECHO VARIABLE_PHP PUNTO CADENA PUNTOYCOMA'''
    log_sintactico_array.append("imprimir")

def p_programabasico(p):
    '''programabasico : INICIO operacionMatematica FIN
                      | INICIO operacionMatematica impresion FIN
                      | INICIO asignacion FIN'''


def p_final(p):
    'final : INICIO instrucciones FIN'
def  p_incdec(p):
    '''incdec : MAYORIGUAL
     | MENORIGUAL'''

def p_incdecfor(p):
    '''incdecfor : MAS MAS
     | MENOS MENOS'''

#for ($i = 1; $i <= 10; $i++) { echo $i; } por ahora solo sirve con impresion dentro
def  p_for(p):
    '''for : FOR PARENIZQ VARIABLE_PHP IGUAL ENTERO PUNTOYCOMA VARIABLE_PHP incdec ENTERO PUNTOYCOMA VARIABLE_PHP incdecfor PARENDER LLAVEIZQ instrucciones LLAVEDER'''
    log_sintactico_array.append("bucle for")

def p_SplHeap(p):
    '''SplHeap : CLASS NOMBRE EXTENDS SPLHEAP LLAVEIZQ function2 LLAVEDER '''
    log_sintactico_array.append("Splheap")


#class JupilerLeague extends SplHeap { public function compare($array1, $array2) { echo "a es mayor que b"; } }
#POR AHORA funciona solo con impresion dentro

def p_asignaSplheap(p):
    '''asignaSplheap : VARIABLE_PHP o_comparar INSERT PARENIZQ ARRAY PARENIZQ CADENA OPERASIG_ARRAY valores PARENDER PARENDER PUNTOYCOMA '''
    log_sintactico_array.append("asignaSplheap")
#def p_newline(p):
#    'newline : \n+'
#----------------------- Fin Viviana
#-----------------------Cindy




#----------------------- error

def p_error(p):
  if p:
    res=f"Error de sintaxis - Token: {p.type}, Línea: {p.lineno}, Col: {p.lexpos}"
    arrayErrores.append(res)
    print(res
      
    )
    parser.errok()
  else:
    res="Error de sintaxis Fin de Linea"
    print(res)
    arrayErrores.append(res)
#----------------------- Build the parser
parser = yacc.yacc()

programa=""
linea = " "
codigo = open("source.txt")
for linea in codigo:
    programa += linea.rstrip('\n')
print(programa)
resultado=parser.parse(programa)
print(resultado)
codigo.close()

def validaRegla(s):
  arrayErrores.clear()
  log_sintactico_array.clear()
  file = open("log.txt", "a")
  result = parser.parse(s)
  file.write("\n\n")
  file.write(s+os.linesep)
  file.write("FECHA Y HORA -> ")
  ahora = time.strftime("%c")
  file.write(ahora+ os.linesep)
  file.close()
  #---Semantico
  #result.imprimir(" ")
  #print result.traducir()

  #graphfile = open('graphviztrhee.vz','w')
  #graphfile.write(result.traducir())
  #graphFile.close()

  print(result)


#while True:
  #try:
    #s = input('calc > ')
  #except EOFError:
    #break
  #if not s: continue
  #validaRegla(s)



