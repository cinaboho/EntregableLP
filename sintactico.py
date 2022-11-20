import ply.yacc as yacc
from lexico import tokens

def p_sentencias(p):
    '''sentencias : operacionMatematica
                  | operador
                  | tipoDevalorNumerico
                  | foreach
                  | arraymaps
                  | tipoDeDato
                  | parametros 
    '''



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

# $b = array_map("cubo", $a);
# array_map("cubo", $a);

def p_arraymaps(p):
    '''arraymaps : OPERAMAPA PARENIZQ parametros PARENDER PUNTOYCOMA
                 | VARIABLE_PHP IGUAL OPERAMAPA PARENIZQ parametros PARENDER PUNTOYCOMA
    '''

def p_error(p):
  if p:
    print(
      f"Error de sintaxis - Token: {p.type}, Línea: {p.lineno}, Col: {p.lexpos}"
    )
    parser.errok()
  else:
    print("Error de sintaxis Fin de Linea")


# Build the parser
parser = yacc.yacc()


def validaRegla(s):
  result = parser.parse(s)
  print(result)


while True:
  try:
    s = input('calc > ')
  except EOFError:
    break
  if not s: continue
  validaRegla(s)