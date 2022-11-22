import ply.yacc as yacc
import os
import time
from lexico import tokens


def p_sentencias(p):
    '''sentencias : operacionMatematica
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
                  | instrucciones
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
def p_operacionMatematica(p):
    '''operacionMatematica : VARIABLE_PHP IGUAL VARIABLE_PHP operador VARIABLE_PHP PUNTOYCOMA
                            | VARIABLE_PHP IGUAL VARIABLE_PHP operador tipoDevalorNumerico PUNTOYCOMA
                            | VARIABLE_PHP IGUAL tipoDevalorNumerico operador tipoDevalorNumerico PUNTOYCOMA
                            | VARIABLE_PHP IGUAL tipoDevalorNumerico operador tipoDevalorNumerico operaciones PUNTOYCOMA
                               '''
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

#tipoDeDato para poner dentro de una estructura ej: array{var1, var2, var3}
def p_tipoDeDato(p):
    '''tipoDeDato : ENTERO
                  | FLOTANTE
                  | CADENA
                  | VARIABLE_PHP
                  | BOOLEANO
                  | NULL
    '''


def p_parametros(p):
    '''parametros : tipoDeDato
                  | tipoDeDato COMA parametros
    '''

# foreach ($array as &$valor) {$valor = $valor * 2;}
def p_foreach(p):
    '''foreach : FOREACH PARENIZQ VARIABLE_PHP AS AMPERSAND VARIABLE_PHP PARENDER LLAVEIZQ operacionMatematica LLAVEDER
    '''

# $b=array_map("cubo",$a);
# array_map("cubo",$a);
def p_arraymaps(p):
    '''arraymaps : OPERAMAPA PARENIZQ parametros PARENDER PUNTOYCOMA
                 | VARIABLE_PHP IGUAL OPERAMAPA PARENIZQ parametros PARENDER PUNTOYCOMA
    '''

#new jupilerLeague();
def p_funcion(p):
    '''funcion : NEW NOMBRE PARENIZQ PARENDER PUNTOYCOMA
    '''

#$heap = new JupilerLeague();
def p_monticuloHEAP(p):
  '''monticuloHEAP : HEAP IGUAL funcion
  '''
#----------------------- Fin Cindy
#
#----------------------- Inicio Johanna
def p_instrucciones(p):
    '''instrucciones : instruccion instrucciones
                     | instruccion
                     '''
def p_instruccion(p):
    '''instruccion : asignacion                     
                    | switchCase
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
                  | crearArray
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
    ''' comparacion : valores o_comparar valores '''

def p_o_comparar(p):
    '''o_comparar : IGUALIGUAL
                  | NOIGUAL
                  | MENORQUE
                  | MAYORQUE
                  | MAYORIGUAL
                  | MENORIGUAL '''

def p_asignacion(p):
    '''asignacion : VARIABLE_PHP IGUAL valores PUNTOYCOMA
                    | VARIABLE_PHP IGUAL valores PUNTOYCOMA comentarios
                    | VARIABLE_PHP difigual valores PUNTOYCOMA
                    | VARIABLE_PHP difigual valores PUNTO valores PUNTOYCOMA comentarios
                    | VARIABLE_PHP difigual valores PUNTO valores PUNTOYCOMA
                    | asignacion
                '''
def p_difigual(p):
    '''difigual : PUNTOIGUAL
                      | MASIGUAL
                      | MENOSIGUAL
       '''
def p_operadores_aritmeticos(p):
    '''operadores_aritmeticos : MAS
                   | MENOS
                   | MULTIPLICA
                   | DIVIDE                   
    '''

def p_aritmetica(p):
    '''aritmetica : valores operadores_aritmeticos valores
                  | aritmetica operadores_aritmeticos valores'''
    


def p_crearArray(p):
  #'''crearArray :  VARIABLE_PHP IGUAL ARRAY PARENIZQ valoresArray PARENDER PUNTOYCOMA
  '''crearArray :  ARRAY PARENIZQ valoresArray PARENDER
  '''

def p_valoresArray(p):
    '''valoresArray : valores 
                | valores OPERASIG_ARRAY valores 
                | valores repite_valores
                | valores OPERASIG_ARRAY valores  repite_claveValor
                '''
  
def p_repite_valoresSeparadosComa(p):
    '''
    repite_valores : COMA valores
                  | COMA valores repite_valores
    '''
def p_repite_claveValorSeparadosComa(p):
    '''repite_claveValor : COMA valores OPERASIG_ARRAY valores
                        | COMA valores OPERASIG_ARRAY valores repite_claveValor
    '''
def p_switchCase(p):  
  '''switchCase : SWITCH PARENIZQ valores PARENDER LLAVEIZQ casos_switch LLAVEDER                
                | SWITCH PARENIZQ valores PARENDER LLAVEIZQ casos_switch DEFAULT DOSPUNTOS LLAVEIZQ instrucciones LLAVEDER LLAVEDER
                | SWITCH PARENIZQ valores PARENDER DOSPUNTOS casos_switch ENDSWITCH PUNTOYCOMA
  '''

def p_caso_switch(p):
    '''caso_switch : CASE valores DOSPUNTOS LLAVEIZQ instrucciones LLAVEDER
                    | CASE valores DOSPUNTOS LLAVEIZQ instrucciones BREAK PUNTOYCOMA LLAVEDER
                    | CASE valores DOSPUNTOS instrucciones
                    | CASE valores DOSPUNTOS instrucciones BREAK PUNTOYCOMA
    '''    

def p_casos_switch(p):
    '''casos_switch : caso_switch casos_switch
                    | caso_switch '''
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
        | PRINT VARIABLE_PHP PUNTOYCOMA'''
def p_programabasico(p):
    '''programabasico : INICIO operacionMatematica FIN
    | INICIO operacionMatematica impresion FIN
    | INICIO asignacion FIN'''

def  p_incdec(p):
    '''incdec : MAYORQUEI
     | MENORQUEI'''

def p_incdecfor(p):
    '''incdecfor : MAS MAS
     | MENOS MENOS'''

#for ($i = 1; $i <= 10; $i++) { echo $i; } por ahora solo sirve con impresion dentro
def  p_for(p):
    '''for : FOR PARENIZQ VARIABLE_PHP IGUAL ENTERO PUNTOYCOMA VARIABLE_PHP incdec ENTERO PUNTOYCOMA VARIABLE_PHP incdecfor PARENDER LLAVEIZQ impresion LLAVEDER'''

def p_SplHeap(p):
    '''SplHeap : CLASS NOMBRE EXTENDS SPLHEAP LLAVEIZQ PUBLIC FUNCTION COMPARE PARENIZQ parametros PARENDER LLAVEIZQ impresion LLAVEDER LLAVEDER '''

#class JupilerLeague extends SplHeap { public function compare($array1, $array2) { echo "a es mayor que b"; } }
#POR AHORA funciona solo con impresion dentro

#def p_newline(p):
#    'newline : \n+'


#----------------------- Fin Viviana
#
#----------------------- error
file = open("log.txt", "a")

def p_error(p):
  if p:
    print(
      f"Error de sintaxis - Token: {p.type}, Línea: {p.lineno}, Col: {p.lexpos}"
    )
    parser.errok()
  else:
    print("Error de sintaxis Fin de Linea")

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
  result = parser.parse(s)
  file.write("\n\n")
  file.write(s+os.linesep)
  file.write("FECHA Y HORA -> ")
  ahora = time.strftime("%c")
  file.write(ahora+ os.linesep)
  print(result)


while True:
  try:
    s = input('calc > ')
  except EOFError:
    break
  if not s: continue
  validaRegla(s)

file.close()
