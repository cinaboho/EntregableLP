import ply.yacc as yacc
from lexico import tokens
from colorama import init, Fore, Back, Style

def p_sentencias(p):
    '''sentencias : operacionMatematica
                  | operador
                  | tipoDevalorNumerico
                  | foreach
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

# foreach ($array as &$valor) {
#     $valor = $valor * 2;
# }
def p_foreach(p):
    '''foreach : FOREACH PARENIZQ VARIABLE_PHP AS AMPERSAND VARIABLE_PHP PARENDER LLAVEIZQ operacionMatematica LLAVEDER
    '''

def p_error(p):
  if p:
    print(
      f"Error de sintaxis - Token: {p.type}, Línea: {p.lineno}, Col: {p.lexpos}"
    )
    parser.errok()
  else:
    print("\033[4;35m"+"Error de sintaxis Fin de Linea"+Back.RESET)


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