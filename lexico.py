import ply.lex as lex

reserved = {
     #Viviana
    'if': 'IF',
    'else': 'ELSE',
    'do': 'DO',
    'while': 'WHILE',
    'end_while': 'END_WHILE',
    'for': 'FOR',
    'switch': 'SWITCH',
    'case': 'CASE',
    'endswitch': 'ENDSWITCH',
    'break': 'BREAK',
    'continue': 'CONTINUE',
    'default': 'DEFAULT',
	'echo' : 'ECHO',
    'define': 'DEFINE',
    'SplHeap': 'SPLHEAP',
    #Fin Viviana

    #Cindy
    'as': 'AS',
    'foreach': 'FOREACH',
    'rsort': 'RSORT',
    'count': 'COUNT',
    'array': 'ARRAY',
    'global': 'GLOBAL',
    'static': 'STATIC',
    'print': 'PRINT',
    'const': 'CONST',
    'function': 'FUNCTION',
    'return': 'RETURN',
    'class': 'CLASS',
    'new': 'NEW',
    #Fin Cindy

    #Johanna
    'extends': 'EXTENDS',
    #'int': 'INTEGER',
    #'string': 'STRING',
    #'float': 'FLOAT',
    'protected': 'PROTECTED',
    'public' :'PUBLIC',
    'private':'PRIVATE',
    'null': 'NULL',
    'compare': 'COMPARE',
    'current': 'CURRENT',
    'list': 'LIST',
    'empty': 'EMPTY'
    #Fin Johanna
    
}
tokens = [
     #Viviana
    'INICIO',
    'FIN',
    'OPEN_TAG_WITH_ECHO',
    'SALTO_DE_LINEA',
    'PUNTOYCOMA',
    'PUNTO',
    'COMA',
    'COMDOB',
    'DOSPUNTOS',
    'PARENIZQ',
    'PARENDER',
    'LLAVEIZQ',
    'LLAVEDER',
    'CORCHIZQ',
    'CORCHDER',
    'AMPERSAND',
    'IGUAL',
    'PUNTOIGUAL',
    'MAS',
    'MAYORQUEI',
    'MENORQUEI',
    #'STRING',
    #Fin Viviana

    #Cindy
    'MENOS',
    'MULTIPLICA',
    'DIVIDE',
    'MODULO',
    'EXPONENCIACION',
    'MASIGUAL',
    'MENOSIGUAL',
    'ASTERISCOIGUAL',
    'BARRAIGUAL',
    'PORCENTAJEIGUAL',
    'DOBLEASTERISCOIGUAL',
    'OPERCOMPARACION',
    'OPERLOGICO_OR',
    'OPERLOGICO_AND',
    'OPERLOGICO_XOR',
    'OPERLOGICO_OREXCLUSIVO',
    'OPERLOGICO_NOT',
    'OPERASIG_ARRAY',
    'HEAP',
    #Fin Cindy

    #Johanna
    'BOOLEANO',
    'IGUALIGUAL',
    'NOIGUAL', 
    'MAYORQUE',
    'MENORQUE',
    'MAYORIGUAL',
    'MENORIGUAL',
    'CADENA',
    'ENTERO',
    'FLOTANTE',
    'COMENTARIO_UNA_LINEA',
    'COMENTARIO_LARGO',
    'NOMBRE',
    'VARIABLE_PHP',
    'OPERAMAPA',
    'OPERALOGICO_MAP',
    'OPERACIONSUM',
    'OPERAPUT',
    'TEXTOSENCILLO',
    'ESPACIOENBLANCO'
    #Fin Johanna
 ] + list(reserved.values())

 #Viviana
t_PUNTOYCOMA = r';'
t_SALTO_DE_LINEA = r'\\n'
t_COMA = r','
t_COMDOB = r'\"'
t_DOSPUNTOS = r':'
t_PARENIZQ = r'\('
t_PARENDER = r'\)'
t_LLAVEIZQ = r'\{'
t_LLAVEDER = r'\}'
t_CORCHIZQ = r'\['
t_CORCHDER = r'\]'
t_AMPERSAND = r'\&'
t_PUNTOIGUAL = r'\.='
t_MAS = r'\+'
#Fin Viviana
    
 #Cindy
t_MENOS = r'\-'
t_MULTIPLICA = r'\*'
t_DIVIDE = r'\/'
t_MODULO = r'%'
t_EXPONENCIACION = r'\*\*'
t_MASIGUAL = r'\+\='
t_MENOSIGUAL = r'\-\='
t_ASTERISCOIGUAL = r'\*\='
t_BARRAIGUAL = r'\/\='
t_PORCENTAJEIGUAL = r'\%\='
t_DOBLEASTERISCOIGUAL = r'\*\*\='
t_OPERCOMPARACION = r'=='
t_MAYORQUEI = r'<='
t_MENORQUEI= r'>='
t_IGUAL = r'='

 #Fin Cindy

 #Johanna
t_IGUALIGUAL = r'=='
t_NOIGUAL = r'!='
t_MAYORQUE=r'>'
t_MENORQUE = r'<'
t_MAYORIGUAL = r'>='
t_MENORIGUAL = r'<='
t_OPERALOGICO_MAP = r'\->'
t_OPERACIONSUM = r'sum\(\)'
t_OPERAPUT = r'put'
t_COMENTARIO_UNA_LINEA =r'//'+'.*'
t_COMENTARIO_LARGO = r'\/\*(.|\n)*?\*\/|\/\/([^?%\n]|[?%](?!>))*\n?|\#([^?%\n]|[?%](?!>))*\n?'
#Fin Johanna

 #Viviana
def t_INICIO(t):
    r'<[?%](([Pp][Hh][Pp][\r]?)|=)?'
    return t

def t_FIN(t):
    r'[?%]>\r?\n?'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
t_ignore  = ' \t'

#'OPEN_TAG_WITH_ECHO',
#Fin Viviana

 #Cindy

def t_OPERLOGICO_OR(t):
    r'or'
    return t
     
def t_OPERLOGICO_AND(t):
    r'and'
    return t
    
def t_OPERAMAPA(t):
    r'array\_map'
    return t

def t_OPERLOGICO_XOR(t):
    r'xor'
    return t
    
def t_OPERLOGICO_OREXCLUSIVO(t):
    r'\|\|'
    return t


def t_OPERLOGICO_NOT(t):
    r'!'
    return t
    
def t_OPERASIG_ARRAY(t):
    r'(\=){1}(\>){1}'
    return t

def t_HEAP(t):
    r'\$heap'
    return t
#Fin Cindy    


# Johanna
def t_BOOLEANO(t):
    r'True|False|true|false|TRUE|FALSE'
    return t


def t_CADENA(t):
    r'\"(.)+\" | \'(.)+\''
    return t

def t_FLOTANTE(t):
    #r'\d+\.\d+'
    r'[+|-]?[0-9]*\.[0-9]+'
    t.value = float(t.value)
    return t

def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_PUNTO = r'\.'

def t_NOMBRE(t):
    #r'[a-zA-Z_][a-zA-Z0-9_]*'
    r'[a-zA-Z][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, "NOMBRE")
    return t

def t_VARIABLE_PHP(t):  
    r'\$[A-Za-z_][\w_]*'
    return t


# Fin Johanna
#Cindy
resultados = []


def t_error(t):
    #lineae="Caracter no reconocido {t.value[0]} en línea {t.lineno}"
    print("Caracter no reconocido'%s'" % t.value[0])
    #print(lineae)
    #resultados.append(lineae)
    t.lexer.skip(1)

lexer = lex.lex()
#----para validar con source.txt

validador = lex.lex()
def getTokens(lex):
    while True:
        tok = lex.token()
        if not tok:
            break
        print(tok)
#validador = lex.lex()
#def getTokens(lex):
#    while True:
#        tok = lex.token()
#        if not tok:
#            break
#        print(tok)


linea = " "
codigo = open("source.txt")
for linea in codigo:
    validador.input(linea)
    getTokens(validador)
codigo.close()

print("Analisis Terminado: ")
#-----fin para validar con source.txt

#FinCindy

