
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AMPERSAND ARRAY AS ASTERISCOIGUAL BARRAIGUAL BOOLEANO BREAK CADENA CASE CLASS COMA COMDOB COMENTARIO_LARGO COMENTARIO_UNA_LINEA COMPARE CONST CONTINUE CORCHDER CORCHIZQ COUNT CURRENT DEFAULT DIVIDE DO DOBLEASTERISCOIGUAL DOSPUNTOS ECHO ELSE EMPTY END_SWITCH END_WHILE ENTERO ESPACIOENBLANCO EXPONENCIACION EXTENDS FIN FLOAT FLOTANTE FOR FOREACH FUNCTION GLOBAL HEAP IF IGUAL INICIO INTEGER LIST LLAVEDER LLAVEIZQ MAS MASIGUAL MAYORQUE MENORQUE MENOS MENOSIGUAL MODULO MULTIPLICA NEW NOMBRE NULL OPEN_TAG_WITH_ECHO OPERACIONSUM OPERALOGICO_MAP OPERAMAPA OPERAPUT OPERASIG_ARRAY OPERCOMPARACION OPERLOGICO_AND OPERLOGICO_NOT OPERLOGICO_OR OPERLOGICO_OREXCLUSIVO OPERLOGICO_XOR PARENDER PARENIZQ PORCENTAJEIGUAL PRINT PRIVATE PROTECTED PUBLIC PUNTO PUNTOIGUAL PUNTOYCOMA RETURN RSORT SALTO_DE_LINEA STATIC STRING SWITCH TEXTOSENCILLO VARIABLE_PHP WHILEsentencias : operacionMatematica\n                  | operador\n                  | tipoDevalorNumerico\n                  | foreach\n                  | arraymaps\n                  | tipoDeDato\n                  | parametros\n                  | funcion\n                  | monticuloHEAP\n    operador : MAS\n                | MENOS\n                | MULTIPLICA\n                | DIVIDE\n                | MODULO\n                | EXPONENCIACION\n    operacionMatematica : VARIABLE_PHP IGUAL VARIABLE_PHP operador VARIABLE_PHP PUNTOYCOMA\n                            | VARIABLE_PHP IGUAL VARIABLE_PHP operador tipoDevalorNumerico PUNTOYCOMA\n    tipoDevalorNumerico : ENTERO\n                           | FLOTANTE\n    tipoDeDato : ENTERO\n                  | FLOTANTE\n                  | CADENA\n                  | VARIABLE_PHP\n                  | BOOLEANO\n                  | NULL\n    parametros : tipoDeDato\n                  | tipoDeDato COMA parametros\n    foreach : FOREACH PARENIZQ VARIABLE_PHP AS AMPERSAND VARIABLE_PHP PARENDER LLAVEIZQ operacionMatematica LLAVEDER\n    arraymaps : OPERAMAPA PARENIZQ parametros PARENDER PUNTOYCOMA\n                 | VARIABLE_PHP IGUAL OPERAMAPA PARENIZQ parametros PARENDER PUNTOYCOMA\n    funcion : NEW NOMBRE PARENIZQ PARENDER PUNTOYCOMA\n    monticuloHEAP : HEAP IGUAL funcion\n  '
    
_lr_action_items = {'VARIABLE_PHP':([0,12,13,14,15,16,17,27,28,29,30,44,45,54,63,66,],[11,-10,-11,-12,-13,-14,-15,37,38,40,37,49,37,60,64,38,]),'MAS':([0,38,],[12,12,]),'MENOS':([0,38,],[13,13,]),'MULTIPLICA':([0,38,],[14,14,]),'DIVIDE':([0,38,],[15,15,]),'MODULO':([0,38,],[16,16,]),'EXPONENCIACION':([0,38,],[17,17,]),'ENTERO':([0,12,13,14,15,16,17,27,30,44,45,],[18,-10,-11,-12,-13,-14,-15,35,35,51,35,]),'FLOTANTE':([0,12,13,14,15,16,17,27,30,44,45,],[19,-10,-11,-12,-13,-14,-15,36,36,52,36,]),'FOREACH':([0,],[20,]),'OPERAMAPA':([0,28,],[21,39,]),'CADENA':([0,27,30,45,],[22,22,22,22,]),'BOOLEANO':([0,27,30,45,],[23,23,23,23,]),'NULL':([0,27,30,45,],[24,24,24,24,]),'NEW':([0,32,],[25,25,]),'HEAP':([0,],[26,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,22,23,24,33,34,35,36,37,43,55,56,57,58,61,67,],[0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-23,-10,-11,-12,-13,-14,-15,-18,-19,-22,-24,-25,-26,-27,-20,-21,-23,-32,-29,-31,-16,-17,-30,-28,]),'COMA':([7,11,18,19,22,23,24,33,35,36,37,],[27,-23,-20,-21,-22,-24,-25,27,-20,-21,-23,]),'IGUAL':([11,26,64,],[28,32,66,]),'PARENIZQ':([20,21,31,39,],[29,30,42,45,]),'PARENDER':([22,23,24,33,34,35,36,37,41,42,53,60,],[-22,-24,-25,-26,-27,-20,-21,-23,47,48,59,62,]),'NOMBRE':([25,],[31,]),'AS':([40,],[46,]),'AMPERSAND':([46,],[54,]),'PUNTOYCOMA':([47,48,49,50,51,52,59,],[55,56,57,58,-18,-19,61,]),'LLAVEDER':([57,58,65,],[-16,-17,67,]),'LLAVEIZQ':([62,],[63,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'sentencias':([0,],[1,]),'operacionMatematica':([0,63,],[2,65,]),'operador':([0,38,],[3,44,]),'tipoDevalorNumerico':([0,44,],[4,50,]),'foreach':([0,],[5,]),'arraymaps':([0,],[6,]),'tipoDeDato':([0,27,30,45,],[7,33,33,33,]),'parametros':([0,27,30,45,],[8,34,41,53,]),'funcion':([0,32,],[9,43,]),'monticuloHEAP':([0,],[10,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> sentencias","S'",1,None,None,None),
  ('sentencias -> operacionMatematica','sentencias',1,'p_sentencias','sintactico.py',5),
  ('sentencias -> operador','sentencias',1,'p_sentencias','sintactico.py',6),
  ('sentencias -> tipoDevalorNumerico','sentencias',1,'p_sentencias','sintactico.py',7),
  ('sentencias -> foreach','sentencias',1,'p_sentencias','sintactico.py',8),
  ('sentencias -> arraymaps','sentencias',1,'p_sentencias','sintactico.py',9),
  ('sentencias -> tipoDeDato','sentencias',1,'p_sentencias','sintactico.py',10),
  ('sentencias -> parametros','sentencias',1,'p_sentencias','sintactico.py',11),
  ('sentencias -> funcion','sentencias',1,'p_sentencias','sintactico.py',12),
  ('sentencias -> monticuloHEAP','sentencias',1,'p_sentencias','sintactico.py',13),
  ('operador -> MAS','operador',1,'p_operador','sintactico.py',18),
  ('operador -> MENOS','operador',1,'p_operador','sintactico.py',19),
  ('operador -> MULTIPLICA','operador',1,'p_operador','sintactico.py',20),
  ('operador -> DIVIDE','operador',1,'p_operador','sintactico.py',21),
  ('operador -> MODULO','operador',1,'p_operador','sintactico.py',22),
  ('operador -> EXPONENCIACION','operador',1,'p_operador','sintactico.py',23),
  ('operacionMatematica -> VARIABLE_PHP IGUAL VARIABLE_PHP operador VARIABLE_PHP PUNTOYCOMA','operacionMatematica',6,'p_operacionMatematica','sintactico.py',29),
  ('operacionMatematica -> VARIABLE_PHP IGUAL VARIABLE_PHP operador tipoDevalorNumerico PUNTOYCOMA','operacionMatematica',6,'p_operacionMatematica','sintactico.py',30),
  ('tipoDevalorNumerico -> ENTERO','tipoDevalorNumerico',1,'p_tipoDevalorNumerico','sintactico.py',34),
  ('tipoDevalorNumerico -> FLOTANTE','tipoDevalorNumerico',1,'p_tipoDevalorNumerico','sintactico.py',35),
  ('tipoDeDato -> ENTERO','tipoDeDato',1,'p_tipoDeDato','sintactico.py',40),
  ('tipoDeDato -> FLOTANTE','tipoDeDato',1,'p_tipoDeDato','sintactico.py',41),
  ('tipoDeDato -> CADENA','tipoDeDato',1,'p_tipoDeDato','sintactico.py',42),
  ('tipoDeDato -> VARIABLE_PHP','tipoDeDato',1,'p_tipoDeDato','sintactico.py',43),
  ('tipoDeDato -> BOOLEANO','tipoDeDato',1,'p_tipoDeDato','sintactico.py',44),
  ('tipoDeDato -> NULL','tipoDeDato',1,'p_tipoDeDato','sintactico.py',45),
  ('parametros -> tipoDeDato','parametros',1,'p_parametros','sintactico.py',50),
  ('parametros -> tipoDeDato COMA parametros','parametros',3,'p_parametros','sintactico.py',51),
  ('foreach -> FOREACH PARENIZQ VARIABLE_PHP AS AMPERSAND VARIABLE_PHP PARENDER LLAVEIZQ operacionMatematica LLAVEDER','foreach',10,'p_foreach','sintactico.py',58),
  ('arraymaps -> OPERAMAPA PARENIZQ parametros PARENDER PUNTOYCOMA','arraymaps',5,'p_arraymaps','sintactico.py',64),
  ('arraymaps -> VARIABLE_PHP IGUAL OPERAMAPA PARENIZQ parametros PARENDER PUNTOYCOMA','arraymaps',7,'p_arraymaps','sintactico.py',65),
  ('funcion -> NEW NOMBRE PARENIZQ PARENDER PUNTOYCOMA','funcion',5,'p_funcion','sintactico.py',70),
  ('monticuloHEAP -> HEAP IGUAL funcion','monticuloHEAP',3,'p_monticuloHEAP','sintactico.py',75),
]
