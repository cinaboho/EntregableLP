import ply.lex as lex

reserved = {
    #Cindy
    'as': 'AS',
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
    'int': 'INTEGER',
    'string': 'STRING',
    'bool': 'BOOLEAN',
    'float': 'FLOAT',
    'null': 'NULL',
    'true': 'TRUE',
    'false': 'FALSE',
    'compare': 'COMPARE',
    'current': 'CURRENT',
    'list': 'LIST',
    'empty': 'EMPTY'
    #Fin Johanna
    
}
tokens = [
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
    #Fin Cindy

    #Johanna
    'BOOLEANO',
    'MAYORQUE',
    'MENORQUE',
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
    'ECHO',
    'PUBLIC',
    'PROTECTED',
    'PRIVATE',
    'TEXTOSENCILLO',
    'ESPACIOENBLANCO'
    #Fin Johanna
 ] + list(reserved.values())
 
 #Cindy
t_MENOS = r'\-'
t_MULTIPLICA = r'\*'
t_DIVIDE = r'/'
t_MODULO = r'%'
t_EXPONENCIACION = r'\*\*'
t_MASIGUAL = r'\+\='
t_MENOSIGUAL = r'\-\='
t_ASTERISCOIGUAL = r'\*\='
t_BARRAIGUAL = r'\/\='
t_PORCENTAJEIGUAL = r'\%\='
t_DOBLEASTERISCOIGUAL = r'\*\*\='
t_OPERCOMPARACION = r'=='

def t_OPERLOGICO_OR(t):
    r'or'
    return t
    
def t_OPERLOGICO_AND(t):
    r'and'
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

#Fin Cindy             
        
#Cindy
resultados = []


def t_error(t):
    lineae="Caracter no reconocido {t.value[0]} en línea {t.lineno}"
    print(lineae)
    resultados.append(lineae)
    t.lexer.skip(1)


validador = lex.lex()
def getTokens(lex):
    while True:
        tok = lex.token()
        if not tok:
            break
        print(tok)


linea = " "
codigo = open("source.txt")
for linea in codigo:
    validador.input(linea)
    getTokens(validador)
codigo.close()

print("Analisis Terminado: ")

#FinCindy
