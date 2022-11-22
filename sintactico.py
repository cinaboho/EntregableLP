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

# foreach ($array as &$valor) {
#     $valor = $valor * 2;
# }
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
#...escribir su parte
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
    | INICIO operacionMatematica impresion FIN '''

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

linea = " "
codigo = open("source.txt")
for linea in codigo:
    print(str(linea))
    parser.parse(linea)
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
