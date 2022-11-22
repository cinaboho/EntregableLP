
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AMPERSAND ARRAY AS ASTERISCOIGUAL BARRAIGUAL BOOLEANO BREAK CADENA CASE CLASS COMA COMDOB COMENTARIO_LARGO COMENTARIO_UNA_LINEA COMPARE CONST CONTINUE CORCHDER CORCHIZQ COUNT CURRENT DEFAULT DEFINE DIVIDE DO DOBLEASTERISCOIGUAL DOSPUNTOS ECHO ELSE EMPTY END_SWITCH END_WHILE ENTERO ESPACIOENBLANCO EXPONENCIACION EXTENDS FIN FLOTANTE FOR FOREACH FUNCTION GLOBAL HEAP IF IGUAL INICIO LIST LLAVEDER LLAVEIZQ MAS MASIGUAL MAYORQUE MAYORQUEI MENORQUE MENORQUEI MENOS MENOSIGUAL MODULO MULTIPLICA NEW NOMBRE NULL OPEN_TAG_WITH_ECHO OPERACIONSUM OPERALOGICO_MAP OPERAMAPA OPERAPUT OPERASIG_ARRAY OPERCOMPARACION OPERLOGICO_AND OPERLOGICO_NOT OPERLOGICO_OR OPERLOGICO_OREXCLUSIVO OPERLOGICO_XOR PARENDER PARENIZQ PORCENTAJEIGUAL PRINT PRIVATE PROTECTED PUBLIC PUNTO PUNTOIGUAL PUNTOYCOMA RETURN RSORT SALTO_DE_LINEA SPLHEAP STATIC SWITCH TEXTOSENCILLO VARIABLE_PHP WHILEsentencias : operacionMatematica\n                  | operador\n                  | tipoDevalorNumerico\n                  | foreach\n                  | arraymaps\n                  | tipoDeDato\n                  | parametros\n                  | funcion\n                  | monticuloHEAP\n                  | comentarios\n                  | impresion\n                  | programabasico\n                  | for\n                  | SplHeap\n\n    operador : MAS\n                | MENOS\n                | MULTIPLICA\n                | DIVIDE\n                | MODULO\n                | EXPONENCIACION\n    operacionMatematica : VARIABLE_PHP IGUAL VARIABLE_PHP operador VARIABLE_PHP PUNTOYCOMA\n                            | VARIABLE_PHP IGUAL VARIABLE_PHP operador tipoDevalorNumerico PUNTOYCOMA\n                            | VARIABLE_PHP IGUAL tipoDevalorNumerico operador tipoDevalorNumerico PUNTOYCOMA\n                            | VARIABLE_PHP IGUAL tipoDevalorNumerico operador tipoDevalorNumerico operaciones PUNTOYCOMA\n                               operaciones : tipoDevalorNumerico operador tipoDevalorNumerico\n                            | tipoDevalorNumerico operador tipoDevalorNumerico operador tipoDevalorNumerico\n                            | PARENIZQ operaciones PARENDER\n                            | operador PARENIZQ operaciones PARENDER operaciones\n                            | PARENIZQ operaciones PARENDER operaciones\n                            | operador PARENIZQ operaciones PARENDER\n        tipoDevalorNumerico : ENTERO\n                           | FLOTANTE\n    tipoDeDato : ENTERO\n                  | FLOTANTE\n                  | CADENA\n                  | VARIABLE_PHP\n                  | BOOLEANO\n                  | NULL\n    parametros : tipoDeDato\n                  | tipoDeDato COMA parametros\n    foreach : FOREACH PARENIZQ VARIABLE_PHP AS AMPERSAND VARIABLE_PHP PARENDER LLAVEIZQ operacionMatematica LLAVEDER\n    arraymaps : OPERAMAPA PARENIZQ parametros PARENDER PUNTOYCOMA\n                 | VARIABLE_PHP IGUAL OPERAMAPA PARENIZQ parametros PARENDER PUNTOYCOMA\n    funcion : NEW NOMBRE PARENIZQ PARENDER PUNTOYCOMA\n    monticuloHEAP : HEAP IGUAL funcion\n  comentarios : COMENTARIO_UNA_LINEA\n                | COMENTARIO_LARGOimpresion : ECHO tipoDeDato PUNTOYCOMA\n        | PRINT tipoDeDato PUNTOYCOMA\n        | ECHO VARIABLE_PHP PUNTOYCOMA\n        | PRINT VARIABLE_PHP PUNTOYCOMAprogramabasico : INICIO operacionMatematica FIN\n    | INICIO operacionMatematica impresion FIN incdec : MAYORQUEI\n     | MENORQUEIincdecfor : MAS MAS\n     | MENOS MENOSfor : FOR PARENIZQ VARIABLE_PHP IGUAL ENTERO PUNTOYCOMA VARIABLE_PHP incdec ENTERO PUNTOYCOMA VARIABLE_PHP incdecfor PARENDER LLAVEIZQ impresion LLAVEDERSplHeap : CLASS NOMBRE EXTENDS SPLHEAP LLAVEIZQ PUBLIC FUNCTION COMPARE PARENIZQ parametros PARENDER LLAVEIZQ impresion LLAVEDER LLAVEDER '
    
_lr_action_items = {'VARIABLE_PHP':([0,17,18,19,20,21,22,34,35,36,39,40,41,42,53,73,76,78,89,103,116,126,130,],[16,-15,-16,-17,-18,-19,-20,46,50,52,57,58,63,57,74,58,85,57,102,111,52,57,132,]),'MAS':([0,58,59,61,62,87,96,100,106,113,115,122,132,135,],[17,17,17,-31,-32,17,17,17,17,17,17,17,135,139,]),'MENOS':([0,58,59,61,62,87,96,100,106,113,115,122,132,136,],[18,18,18,-31,-32,18,18,18,18,18,18,18,136,140,]),'MULTIPLICA':([0,58,59,61,62,87,96,100,106,113,115,122,],[19,19,19,-31,-32,19,19,19,19,19,19,19,]),'DIVIDE':([0,58,59,61,62,87,96,100,106,113,115,122,],[20,20,20,-31,-32,20,20,20,20,20,20,20,]),'MODULO':([0,58,59,61,62,87,96,100,106,113,115,122,],[21,21,21,-31,-32,21,21,21,21,21,21,21,]),'EXPONENCIACION':([0,58,59,61,62,87,96,100,106,113,115,122,],[22,22,22,-31,-32,22,22,22,22,22,22,22,]),'ENTERO':([0,17,18,19,20,21,22,34,35,39,40,42,61,62,73,76,77,78,83,87,100,105,106,115,117,118,119,121,122,126,],[23,-15,-16,-17,-18,-19,-20,47,47,47,61,47,-31,-32,61,61,61,47,92,61,61,61,61,61,125,-54,-55,61,61,47,]),'FLOTANTE':([0,17,18,19,20,21,22,34,35,39,40,42,61,62,73,76,77,78,87,100,105,106,115,121,122,126,],[24,-15,-16,-17,-18,-19,-20,48,48,48,62,48,-31,-32,62,62,62,48,62,62,62,62,62,62,62,48,]),'FOREACH':([0,],[25,]),'OPERAMAPA':([0,40,],[26,60,]),'CADENA':([0,34,35,39,42,78,126,],[27,27,27,27,27,27,27,]),'BOOLEANO':([0,34,35,39,42,78,126,],[28,28,28,28,28,28,28,]),'NULL':([0,34,35,39,42,78,126,],[29,29,29,29,29,29,29,]),'NEW':([0,44,],[30,30,]),'HEAP':([0,],[31,]),'COMENTARIO_UNA_LINEA':([0,],[32,]),'COMENTARIO_LARGO':([0,],[33,]),'ECHO':([0,51,94,95,98,107,137,142,],[34,34,-21,-22,-23,-24,34,34,]),'PRINT':([0,51,94,95,98,107,137,142,],[35,35,-21,-22,-23,-24,35,35,]),'INICIO':([0,],[36,]),'FOR':([0,],[37,]),'CLASS':([0,],[38,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,27,28,29,32,33,47,48,55,56,57,66,67,68,69,70,71,82,90,91,94,95,98,107,109,129,145,146,],[0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-36,-15,-16,-17,-18,-19,-20,-31,-32,-35,-37,-38,-46,-47,-33,-34,-39,-40,-36,-45,-48,-50,-49,-51,-52,-53,-42,-44,-21,-22,-23,-24,-43,-41,-59,-58,]),'COMA':([7,16,23,24,27,28,29,47,48,55,57,],[39,-36,-33,-34,-35,-37,-38,-33,-34,39,-36,]),'IGUAL':([16,31,52,74,],[40,44,73,83,]),'PARENIZQ':([17,18,19,20,21,22,25,26,37,43,60,61,62,87,97,100,106,115,120,122,],[-15,-16,-17,-18,-19,-20,41,42,53,65,78,-31,-32,100,106,100,100,100,126,100,]),'PUNTOYCOMA':([27,28,29,45,46,47,48,49,50,61,62,80,81,85,86,87,92,99,101,113,115,122,123,125,127,128,],[-35,-37,-38,67,68,-33,-34,69,70,-31,-32,90,91,94,95,98,103,107,109,-25,-27,-30,-29,130,-26,-28,]),'PARENDER':([27,28,29,47,48,55,56,57,61,62,64,65,88,102,108,113,114,115,122,123,127,128,131,134,139,140,],[-35,-37,-38,-33,-34,-39,-40,-36,-31,-32,80,81,101,110,115,-25,122,-27,-30,-29,-26,-28,133,138,-56,-57,]),'NOMBRE':([30,38,],[43,54,]),'FIN':([51,67,68,69,70,72,94,95,98,107,],[71,-48,-50,-49,-51,82,-21,-22,-23,-24,]),'EXTENDS':([54,],[75,]),'AS':([63,],[79,]),'LLAVEDER':([67,68,69,70,94,95,98,107,124,141,143,144,],[-48,-50,-49,-51,-21,-22,-23,-24,129,143,145,146,]),'SPLHEAP':([75,],[84,]),'AMPERSAND':([79,],[89,]),'LLAVEIZQ':([84,110,133,138,],[93,116,137,142,]),'PUBLIC':([93,],[104,]),'FUNCTION':([104,],[112,]),'MAYORQUEI':([111,],[118,]),'MENORQUEI':([111,],[119,]),'COMPARE':([112,],[120,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'sentencias':([0,],[1,]),'operacionMatematica':([0,36,116,],[2,51,124,]),'operador':([0,58,59,87,96,100,106,113,115,122,],[3,76,77,97,105,97,97,121,97,97,]),'tipoDevalorNumerico':([0,40,73,76,77,87,100,105,106,115,121,122,],[4,59,59,86,87,96,96,113,96,96,127,96,]),'foreach':([0,],[5,]),'arraymaps':([0,],[6,]),'tipoDeDato':([0,34,35,39,42,78,126,],[7,45,49,55,55,55,55,]),'parametros':([0,39,42,78,126,],[8,56,64,88,131,]),'funcion':([0,44,],[9,66,]),'monticuloHEAP':([0,],[10,]),'comentarios':([0,],[11,]),'impresion':([0,51,137,142,],[12,72,141,144,]),'programabasico':([0,],[13,]),'for':([0,],[14,]),'SplHeap':([0,],[15,]),'operaciones':([87,100,106,115,122,],[99,108,114,123,128,]),'incdec':([111,],[117,]),'incdecfor':([132,],[134,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> sentencias","S'",1,None,None,None),
  ('sentencias -> operacionMatematica','sentencias',1,'p_sentencias','sintactico.py',8),
  ('sentencias -> operador','sentencias',1,'p_sentencias','sintactico.py',9),
  ('sentencias -> tipoDevalorNumerico','sentencias',1,'p_sentencias','sintactico.py',10),
  ('sentencias -> foreach','sentencias',1,'p_sentencias','sintactico.py',11),
  ('sentencias -> arraymaps','sentencias',1,'p_sentencias','sintactico.py',12),
  ('sentencias -> tipoDeDato','sentencias',1,'p_sentencias','sintactico.py',13),
  ('sentencias -> parametros','sentencias',1,'p_sentencias','sintactico.py',14),
  ('sentencias -> funcion','sentencias',1,'p_sentencias','sintactico.py',15),
  ('sentencias -> monticuloHEAP','sentencias',1,'p_sentencias','sintactico.py',16),
  ('sentencias -> comentarios','sentencias',1,'p_sentencias','sintactico.py',17),
  ('sentencias -> impresion','sentencias',1,'p_sentencias','sintactico.py',18),
  ('sentencias -> programabasico','sentencias',1,'p_sentencias','sintactico.py',19),
  ('sentencias -> for','sentencias',1,'p_sentencias','sintactico.py',20),
  ('sentencias -> SplHeap','sentencias',1,'p_sentencias','sintactico.py',21),
  ('operador -> MAS','operador',1,'p_operador','sintactico.py',27),
  ('operador -> MENOS','operador',1,'p_operador','sintactico.py',28),
  ('operador -> MULTIPLICA','operador',1,'p_operador','sintactico.py',29),
  ('operador -> DIVIDE','operador',1,'p_operador','sintactico.py',30),
  ('operador -> MODULO','operador',1,'p_operador','sintactico.py',31),
  ('operador -> EXPONENCIACION','operador',1,'p_operador','sintactico.py',32),
  ('operacionMatematica -> VARIABLE_PHP IGUAL VARIABLE_PHP operador VARIABLE_PHP PUNTOYCOMA','operacionMatematica',6,'p_operacionMatematica','sintactico.py',38),
  ('operacionMatematica -> VARIABLE_PHP IGUAL VARIABLE_PHP operador tipoDevalorNumerico PUNTOYCOMA','operacionMatematica',6,'p_operacionMatematica','sintactico.py',39),
  ('operacionMatematica -> VARIABLE_PHP IGUAL tipoDevalorNumerico operador tipoDevalorNumerico PUNTOYCOMA','operacionMatematica',6,'p_operacionMatematica','sintactico.py',40),
  ('operacionMatematica -> VARIABLE_PHP IGUAL tipoDevalorNumerico operador tipoDevalorNumerico operaciones PUNTOYCOMA','operacionMatematica',7,'p_operacionMatematica','sintactico.py',41),
  ('operaciones -> tipoDevalorNumerico operador tipoDevalorNumerico','operaciones',3,'p_operaciones','sintactico.py',44),
  ('operaciones -> tipoDevalorNumerico operador tipoDevalorNumerico operador tipoDevalorNumerico','operaciones',5,'p_operaciones','sintactico.py',45),
  ('operaciones -> PARENIZQ operaciones PARENDER','operaciones',3,'p_operaciones','sintactico.py',46),
  ('operaciones -> operador PARENIZQ operaciones PARENDER operaciones','operaciones',5,'p_operaciones','sintactico.py',47),
  ('operaciones -> PARENIZQ operaciones PARENDER operaciones','operaciones',4,'p_operaciones','sintactico.py',48),
  ('operaciones -> operador PARENIZQ operaciones PARENDER','operaciones',4,'p_operaciones','sintactico.py',49),
  ('tipoDevalorNumerico -> ENTERO','tipoDevalorNumerico',1,'p_tipoDevalorNumerico','sintactico.py',52),
  ('tipoDevalorNumerico -> FLOTANTE','tipoDevalorNumerico',1,'p_tipoDevalorNumerico','sintactico.py',53),
  ('tipoDeDato -> ENTERO','tipoDeDato',1,'p_tipoDeDato','sintactico.py',58),
  ('tipoDeDato -> FLOTANTE','tipoDeDato',1,'p_tipoDeDato','sintactico.py',59),
  ('tipoDeDato -> CADENA','tipoDeDato',1,'p_tipoDeDato','sintactico.py',60),
  ('tipoDeDato -> VARIABLE_PHP','tipoDeDato',1,'p_tipoDeDato','sintactico.py',61),
  ('tipoDeDato -> BOOLEANO','tipoDeDato',1,'p_tipoDeDato','sintactico.py',62),
  ('tipoDeDato -> NULL','tipoDeDato',1,'p_tipoDeDato','sintactico.py',63),
  ('parametros -> tipoDeDato','parametros',1,'p_parametros','sintactico.py',68),
  ('parametros -> tipoDeDato COMA parametros','parametros',3,'p_parametros','sintactico.py',69),
  ('foreach -> FOREACH PARENIZQ VARIABLE_PHP AS AMPERSAND VARIABLE_PHP PARENDER LLAVEIZQ operacionMatematica LLAVEDER','foreach',10,'p_foreach','sintactico.py',76),
  ('arraymaps -> OPERAMAPA PARENIZQ parametros PARENDER PUNTOYCOMA','arraymaps',5,'p_arraymaps','sintactico.py',82),
  ('arraymaps -> VARIABLE_PHP IGUAL OPERAMAPA PARENIZQ parametros PARENDER PUNTOYCOMA','arraymaps',7,'p_arraymaps','sintactico.py',83),
  ('funcion -> NEW NOMBRE PARENIZQ PARENDER PUNTOYCOMA','funcion',5,'p_funcion','sintactico.py',88),
  ('monticuloHEAP -> HEAP IGUAL funcion','monticuloHEAP',3,'p_monticuloHEAP','sintactico.py',93),
  ('comentarios -> COMENTARIO_UNA_LINEA','comentarios',1,'p_comentarios','sintactico.py',103),
  ('comentarios -> COMENTARIO_LARGO','comentarios',1,'p_comentarios','sintactico.py',104),
  ('impresion -> ECHO tipoDeDato PUNTOYCOMA','impresion',3,'p_impresion','sintactico.py',106),
  ('impresion -> PRINT tipoDeDato PUNTOYCOMA','impresion',3,'p_impresion','sintactico.py',107),
  ('impresion -> ECHO VARIABLE_PHP PUNTOYCOMA','impresion',3,'p_impresion','sintactico.py',108),
  ('impresion -> PRINT VARIABLE_PHP PUNTOYCOMA','impresion',3,'p_impresion','sintactico.py',109),
  ('programabasico -> INICIO operacionMatematica FIN','programabasico',3,'p_programabasico','sintactico.py',111),
  ('programabasico -> INICIO operacionMatematica impresion FIN','programabasico',4,'p_programabasico','sintactico.py',112),
  ('incdec -> MAYORQUEI','incdec',1,'p_incdec','sintactico.py',115),
  ('incdec -> MENORQUEI','incdec',1,'p_incdec','sintactico.py',116),
  ('incdecfor -> MAS MAS','incdecfor',2,'p_incdecfor','sintactico.py',119),
  ('incdecfor -> MENOS MENOS','incdecfor',2,'p_incdecfor','sintactico.py',120),
  ('for -> FOR PARENIZQ VARIABLE_PHP IGUAL ENTERO PUNTOYCOMA VARIABLE_PHP incdec ENTERO PUNTOYCOMA VARIABLE_PHP incdecfor PARENDER LLAVEIZQ impresion LLAVEDER','for',16,'p_for','sintactico.py',124),
  ('SplHeap -> CLASS NOMBRE EXTENDS SPLHEAP LLAVEIZQ PUBLIC FUNCTION COMPARE PARENIZQ parametros PARENDER LLAVEIZQ impresion LLAVEDER LLAVEDER','SplHeap',15,'p_SplHeap','sintactico.py',127),
]
