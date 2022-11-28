
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AMPERSAND ARRAY AS ASTERISCOIGUAL BARRAIGUAL BOOLEANO BREAK CADENA CASE CLASS COMA COMDOB COMENTARIO_LARGO COMENTARIO_UNA_LINEA COMPARE CONST CONTINUE CORCHDER CORCHIZQ COUNT CURRENT DEFAULT DEFINE DIVIDE DO DOBLEASTERISCOIGUAL DOSPUNTOS ECHO ELSE EMPTY ENDSWITCH END_WHILE ENTERO ESPACIOENBLANCO EXPONENCIACION EXTENDS FIN FLOTANTE FOR FOREACH FUNCTION GLOBAL HEAP IF IGUAL IGUALIGUAL INICIO LIST LLAVEDER LLAVEIZQ MAS MASIGUAL MAYORIGUAL MAYORQUE MAYORQUEI MENORIGUAL MENORQUE MENORQUEI MENOS MENOSIGUAL MODULO MULTIPLICA NEW NOIGUAL NOMBRE NULL OPEN_TAG_WITH_ECHO OPERACIONSUM OPERALOGICO_MAP OPERAMAPA OPERAPUT OPERASIG_ARRAY OPERCOMPARACION OPERLOGICO_AND OPERLOGICO_NOT OPERLOGICO_OR OPERLOGICO_OREXCLUSIVO OPERLOGICO_XOR PARENDER PARENIZQ PORCENTAJEIGUAL PRINT PRIVATE PROTECTED PUBLIC PUNTO PUNTOIGUAL PUNTOYCOMA RETURN RSORT SALTO_DE_LINEA SPLHEAP STATIC SWITCH TEXTOSENCILLO VARIABLE_PHP WHILEsentencias : operacionMatematica\n                  | operador\n                  | tipoDevalorNumerico\n                  | foreach\n                  | arraymaps\n                  | tipoDeDato\n                  | parametros\n                  | funcion\n                  | monticuloHEAP\n                  | comentarios\n                  | impresion\n                  | programabasico\n                  | for\n                  | SplHeap\n                  | INICIO instrucciones FIN\n    operador : MAS\n                | MENOS\n                | MULTIPLICA\n                | DIVIDE\n                | MODULO\n                | EXPONENCIACION\n    operacionMatematica : VARIABLE_PHP IGUAL VARIABLE_PHP operador VARIABLE_PHP PUNTOYCOMA\n                            | VARIABLE_PHP IGUAL VARIABLE_PHP operador tipoDevalorNumerico PUNTOYCOMA\n                            | VARIABLE_PHP IGUAL tipoDevalorNumerico operador tipoDevalorNumerico PUNTOYCOMA\n                            | VARIABLE_PHP IGUAL tipoDevalorNumerico operador tipoDevalorNumerico operaciones PUNTOYCOMA\n    \n                               operaciones : tipoDevalorNumerico operador tipoDevalorNumerico\n                            | tipoDevalorNumerico operador tipoDevalorNumerico operador tipoDevalorNumerico\n                            | PARENIZQ operaciones PARENDER\n                            | operador PARENIZQ operaciones PARENDER operaciones\n                            | PARENIZQ operaciones PARENDER operaciones\n                            | operador PARENIZQ operaciones PARENDER\n        tipoDevalorNumerico : ENTERO\n                           | FLOTANTE\n    tipoDeDato : ENTERO\n                  | FLOTANTE\n                  | CADENA\n                  | VARIABLE_PHP\n                  | BOOLEANO\n                  | NULL\n    parametros : tipoDeDato\n                  | tipoDeDato COMA parametros\n    foreach : FOREACH PARENIZQ VARIABLE_PHP AS AMPERSAND VARIABLE_PHP PARENDER LLAVEIZQ operacionMatematica LLAVEDER\n    arraymaps : OPERAMAPA PARENIZQ parametros PARENDER PUNTOYCOMA\n                 | VARIABLE_PHP IGUAL OPERAMAPA PARENIZQ parametros PARENDER PUNTOYCOMA\n    funcion : NEW NOMBRE PARENIZQ PARENDER PUNTOYCOMA\n    monticuloHEAP : HEAP IGUAL funcion\n  instrucciones : instruccion instrucciones\n                     | instruccion\n                     instruccion : asignacion                     \n                    | echo\n                    | switchCase\n                     valores : ENTERO\n                  | FLOTANTE\n                  | CADENA\n                  | VARIABLE_PHP\n                  | BOOLEANO  \n                  | aritmetica\n                  | booleanos\n                  | NOMBRE PARENIZQ  PARENDER\n                  | NOMBRE PARENIZQ valores PARENDER  \n                  | crearArrayCorta                \n                  | crearArrayLarga\n     booleano : BOOLEANO                \n                | comparacion\n                | OPERLOGICO_NOT booleanos\n    booleanos : booleano\n                 | booleanos o_logicos booleanos\n    o_logicos : OPERLOGICO_AND\n                 | OPERLOGICO_OR comparacion : valores o_comparar valores o_comparar : IGUALIGUAL\n                  | NOIGUAL\n                  | MENORQUE\n                  | MAYORQUE\n                  | MAYORIGUAL\n                  | MENORIGUAL asignacion : VARIABLE_PHP IGUAL valores PUNTOYCOMA\n                    | VARIABLE_PHP IGUAL valores PUNTOYCOMA comentarios\n                    | VARIABLE_PHP difigual valores PUNTOYCOMA\n                    | VARIABLE_PHP difigual valores PUNTO valores PUNTOYCOMA comentarios\n                    | VARIABLE_PHP difigual valores PUNTO valores PUNTOYCOMA\n                    | asignacion\n                difigual : PUNTOIGUAL\n                      | MASIGUAL\n                      | MENOSIGUAL\n       operadores_aritmeticos : MAS\n                   | MENOS\n                   | MULTIPLICA\n                   | DIVIDE                   \n    aritmetica : valores operadores_aritmeticos valores\n                  | aritmetica operadores_aritmeticos valoresecho : ECHO CADENA PUNTOYCOMA\n            | ECHO VARIABLE_PHP PUNTOYCOMA\n            | ECHO aritmetica PUNTOYCOMA\n    crearArrayCorta :  CORCHIZQ valoresArray CORCHDER\n  crearArrayLarga :  ARRAY PARENIZQ valoresArray PARENDER\n  valoresArray : valores \n                | valores OPERASIG_ARRAY valores \n                | valores repite_valores\n                | valores OPERASIG_ARRAY valores  repite_claveValor\n                \n    repite_valores : COMA valores\n                  | COMA valores COMA\n                  | COMA valores repite_valores\n    repite_claveValor : COMA valores OPERASIG_ARRAY valores\n                        | COMA valores OPERASIG_ARRAY valores repite_claveValor\n    switchCase : SWITCH PARENIZQ valores PARENDER LLAVEIZQ casos_switch LLAVEDER                \n                | SWITCH PARENIZQ valores PARENDER LLAVEIZQ casos_switch DEFAULT DOSPUNTOS LLAVEIZQ instrucciones LLAVEDER LLAVEDER\n                | SWITCH PARENIZQ valores PARENDER DOSPUNTOS casos_switch ENDSWITCH PUNTOYCOMA\n  caso_switch : CASE valores DOSPUNTOS LLAVEIZQ instrucciones LLAVEDER\n                    | CASE valores DOSPUNTOS LLAVEIZQ instrucciones BREAK PUNTOYCOMA LLAVEDER\n                    | CASE valores DOSPUNTOS instrucciones\n                    | CASE valores DOSPUNTOS instrucciones BREAK PUNTOYCOMA\n    casos_switch : caso_switch casos_switch\n                    | caso_switch comentarios : COMENTARIO_UNA_LINEA\n                | COMENTARIO_LARGOimpresion : ECHO tipoDeDato PUNTOYCOMA\n        | PRINT tipoDeDato PUNTOYCOMA\n        | ECHO VARIABLE_PHP PUNTOYCOMA\n        | PRINT VARIABLE_PHP PUNTOYCOMAprogramabasico : INICIO operacionMatematica FIN\n    | INICIO operacionMatematica impresion FIN\n    | INICIO asignacion FINincdec : MAYORQUEI\n     | MENORQUEIincdecfor : MAS MAS\n     | MENOS MENOSfor : FOR PARENIZQ VARIABLE_PHP IGUAL ENTERO PUNTOYCOMA VARIABLE_PHP incdec ENTERO PUNTOYCOMA VARIABLE_PHP incdecfor PARENDER LLAVEIZQ impresion LLAVEDERSplHeap : CLASS NOMBRE EXTENDS SPLHEAP LLAVEIZQ PUBLIC FUNCTION COMPARE PARENIZQ parametros PARENDER LLAVEIZQ impresion LLAVEDER LLAVEDER '
    
_lr_action_items = {'INICIO':([0,],[16,]),'VARIABLE_PHP':([0,16,18,19,20,21,22,23,33,34,35,36,39,42,43,45,46,47,49,50,51,60,70,72,73,74,75,76,89,92,93,110,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,141,146,148,154,155,156,164,166,173,178,195,197,199,200,204,214,216,224,229,231,232,239,241,242,246,248,264,],[17,44,-16,-17,-18,-19,-20,-21,-115,-116,55,59,64,-49,71,-50,-51,78,94,99,64,107,-49,111,117,-83,-84,-85,117,117,117,117,-92,-93,-94,117,-86,-87,-88,-89,117,117,-71,-72,-73,-74,-75,-76,117,-68,-69,117,117,169,64,-77,-79,117,117,117,194,-78,212,-81,117,117,117,-80,-106,236,117,71,-108,64,71,71,94,254,-107,]),'MAS':([0,77,78,79,80,81,82,83,84,86,87,88,91,94,95,97,98,111,112,113,114,115,116,117,118,140,142,143,144,145,157,158,159,160,161,162,163,171,179,180,181,182,183,188,192,207,215,219,221,223,234,240,254,261,],[18,-54,-55,123,123,-52,-53,-56,-58,-61,-62,-66,-64,18,18,-32,-33,18,123,-32,-33,-54,123,-55,123,123,-58,-56,123,123,123,123,123,-58,-59,123,-95,18,123,-60,123,123,-96,18,18,18,123,123,18,18,18,123,261,267,]),'MENOS':([0,77,78,79,80,81,82,83,84,86,87,88,91,94,95,97,98,111,112,113,114,115,116,117,118,140,142,143,144,145,157,158,159,160,161,162,163,171,179,180,181,182,183,188,192,207,215,219,221,223,234,240,254,262,],[19,-54,-55,124,124,-52,-53,-56,-58,-61,-62,-66,-64,19,19,-32,-33,19,124,-32,-33,-54,124,-55,124,124,-58,-56,124,124,124,124,124,-58,-59,124,-95,19,124,-60,124,124,-96,19,19,19,124,124,19,19,19,124,262,268,]),'MULTIPLICA':([0,77,78,79,80,81,82,83,84,86,87,88,91,94,95,97,98,111,112,113,114,115,116,117,118,140,142,143,144,145,157,158,159,160,161,162,163,171,179,180,181,182,183,188,192,207,215,219,221,223,234,240,],[20,-54,-55,125,125,-52,-53,-56,-58,-61,-62,-66,-64,20,20,-32,-33,20,125,-32,-33,-54,125,-55,125,125,-58,-56,125,125,125,125,125,-58,-59,125,-95,20,125,-60,125,125,-96,20,20,20,125,125,20,20,20,125,]),'DIVIDE':([0,77,78,79,80,81,82,83,84,86,87,88,91,94,95,97,98,111,112,113,114,115,116,117,118,140,142,143,144,145,157,158,159,160,161,162,163,171,179,180,181,182,183,188,192,207,215,219,221,223,234,240,],[21,-54,-55,126,126,-52,-53,-56,-58,-61,-62,-66,-64,21,21,-32,-33,21,126,-32,-33,-54,126,-55,126,126,-58,-56,126,126,126,126,126,-58,-59,126,-95,21,126,-60,126,126,-96,21,21,21,126,126,21,21,21,126,]),'MODULO':([0,94,95,97,98,111,113,114,171,188,192,207,221,223,234,],[22,22,22,-32,-33,22,-32,-33,22,22,22,22,22,22,22,]),'EXPONENCIACION':([0,94,95,97,98,111,113,114,171,188,192,207,221,223,234,],[23,23,23,-32,-33,23,-32,-33,23,23,23,23,23,23,23,]),'ENTERO':([0,18,19,20,21,22,23,35,36,39,47,49,51,72,73,74,75,76,89,92,93,97,98,110,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,141,146,147,148,152,156,164,166,171,192,199,200,204,206,207,223,225,226,227,229,233,234,239,246,],[24,-16,-17,-18,-19,-20,-21,56,56,56,81,97,56,113,81,-83,-84,-85,81,81,81,-32,-33,81,81,-86,-87,-88,-89,81,81,-71,-72,-73,-74,-75,-76,81,-68,-69,81,81,97,97,56,176,81,81,81,97,97,81,81,81,97,97,97,238,-124,-125,81,97,97,56,97,]),'FLOTANTE':([0,18,19,20,21,22,23,35,36,39,47,49,51,72,73,74,75,76,89,92,93,97,98,110,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,141,146,147,148,156,164,166,171,192,199,200,204,206,207,223,229,233,234,239,246,],[25,-16,-17,-18,-19,-20,-21,57,57,57,82,98,57,114,82,-83,-84,-85,82,82,82,-32,-33,82,82,-86,-87,-88,-89,82,82,-71,-72,-73,-74,-75,-76,82,-68,-69,82,82,98,98,57,82,82,82,98,98,82,82,82,98,98,98,82,98,98,57,98,]),'FOREACH':([0,],[26,]),'OPERAMAPA':([0,49,],[27,96,]),'CADENA':([0,35,36,39,47,51,72,73,74,75,76,89,92,93,110,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,141,148,156,164,166,199,200,204,229,239,],[28,28,28,28,77,28,115,115,-83,-84,-85,115,115,115,115,115,-86,-87,-88,-89,115,115,-71,-72,-73,-74,-75,-76,115,-68,-69,115,115,28,115,115,115,115,115,115,115,28,]),'BOOLEANO':([0,35,36,39,47,51,72,73,74,75,76,89,92,93,110,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,141,148,156,164,166,199,200,204,229,239,],[29,29,29,29,83,29,83,83,-83,-84,-85,83,143,83,83,83,-86,-87,-88,-89,83,83,-71,-72,-73,-74,-75,-76,143,-68,-69,83,83,29,83,83,83,83,83,83,83,29,]),'NULL':([0,35,36,39,51,148,239,],[30,30,30,30,30,30,30,]),'NEW':([0,53,],[31,31,]),'HEAP':([0,],[32,]),'COMENTARIO_UNA_LINEA':([0,154,197,],[33,33,33,]),'COMENTARIO_LARGO':([0,154,197,],[34,34,34,]),'ECHO':([0,16,33,34,41,42,43,45,46,70,119,120,121,154,155,178,186,187,190,197,208,214,216,231,232,241,242,263,264,271,],[35,47,-115,-116,35,-49,47,-50,-51,-49,-92,-93,-94,-77,-79,-78,-22,-23,-24,-81,-25,-80,-106,47,-108,47,47,35,-107,35,]),'PRINT':([0,41,186,187,190,208,263,271,],[36,36,-22,-23,-24,-25,36,36,]),'FOR':([0,],[37,]),'CLASS':([0,],[38,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,19,20,21,22,23,24,25,28,29,30,33,34,56,57,62,63,64,65,66,68,102,103,104,105,106,109,174,175,186,187,190,208,210,247,274,275,],[0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-37,-16,-17,-18,-19,-20,-21,-32,-33,-36,-38,-39,-115,-116,-34,-35,-40,-41,-37,-15,-121,-123,-46,-117,-119,-118,-120,-122,-43,-45,-22,-23,-24,-25,-44,-42,-129,-128,]),'COMA':([7,17,24,25,28,29,30,56,57,62,64,81,82,83,84,86,87,88,91,115,116,117,140,142,143,157,158,159,160,161,163,180,181,182,183,240,],[39,-37,-34,-35,-36,-38,-39,-34,-35,39,-37,-52,-53,-56,-58,-61,-62,-66,-64,-54,-57,-55,166,-65,-63,-91,-90,-70,-67,-59,-95,-60,199,200,-96,199,]),'SWITCH':([16,33,34,42,43,45,46,70,119,120,121,154,155,178,197,214,216,231,232,241,242,264,],[48,-115,-116,-49,48,-50,-51,-49,-92,-93,-94,-77,-79,-78,-81,-80,-106,48,-108,48,48,-107,]),'IGUAL':([17,32,44,71,107,236,],[49,53,72,110,152,246,]),'PARENIZQ':([18,19,20,21,22,23,26,27,37,48,52,85,90,96,97,98,171,189,192,207,223,228,234,],[-16,-17,-18,-19,-20,-21,50,51,60,93,101,138,141,148,-32,-33,192,207,192,192,192,239,192,]),'PUNTOYCOMA':([28,29,30,54,55,56,57,58,59,77,78,79,81,82,83,84,86,87,88,91,97,98,111,112,113,114,115,116,117,118,142,143,150,151,157,158,159,160,161,163,169,170,171,176,179,180,183,191,193,220,221,223,234,235,238,244,245,253,258,],[-36,-38,-39,103,104,-34,-35,105,106,119,120,121,-52,-53,-56,-58,-61,-62,-66,-64,-32,-33,-55,154,-52,-53,-54,-57,-55,155,-65,-63,174,175,-91,-90,-70,-67,-59,-95,186,187,190,195,197,-60,-96,208,210,232,-26,-28,-31,-30,248,-27,-29,259,265,]),'PARENDER':([28,29,30,56,57,62,63,64,81,82,83,84,86,87,88,91,97,98,100,101,115,116,117,138,140,142,143,145,157,158,159,160,161,162,163,165,167,172,180,181,182,183,194,198,200,201,209,221,222,223,234,235,240,244,245,249,250,260,267,268,],[-36,-38,-39,-34,-35,-40,-41,-37,-52,-53,-56,-58,-61,-62,-66,-64,-32,-33,150,151,-54,-57,-55,161,-97,-65,-63,168,-91,-90,-70,-67,-59,180,-95,-99,183,193,-60,-98,-101,-96,211,-100,-102,-103,223,-26,234,-28,-31,-30,-104,-27,-29,255,-105,266,-126,-127,]),'NOMBRE':([31,38,47,72,73,74,75,76,89,92,93,110,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,141,156,164,166,199,200,204,229,],[52,61,85,85,85,-83,-84,-85,85,85,85,85,85,-86,-87,-88,-89,85,85,-71,-72,-73,-74,-75,-76,85,-68,-69,85,85,85,85,85,85,85,85,85,]),'FIN':([33,34,40,41,42,43,45,46,67,69,70,103,104,105,106,119,120,121,154,155,178,186,187,190,197,208,214,216,232,264,],[-115,-116,65,66,68,-48,-50,-51,109,-47,-49,-117,-119,-118,-120,-92,-93,-94,-77,-79,-78,-22,-23,-24,-81,-25,-80,-106,-108,-107,]),'BREAK':([33,34,43,45,46,69,70,119,120,121,154,155,178,197,214,216,232,243,252,264,],[-115,-116,-48,-50,-51,-47,-49,-92,-93,-94,-77,-79,-78,-81,-80,-106,-108,253,258,-107,]),'CASE':([33,34,43,45,46,69,70,119,120,121,154,155,178,184,185,197,203,214,216,232,243,257,259,264,270,],[-115,-116,-48,-50,-51,-47,-49,-92,-93,-94,-77,-79,-78,204,204,-81,204,-80,-106,-108,-111,-109,-112,-107,-110,]),'LLAVEDER':([33,34,43,45,46,69,70,103,104,105,106,119,120,121,154,155,178,186,187,190,197,202,203,208,214,216,218,232,237,243,251,252,256,257,259,264,265,269,270,272,273,],[-115,-116,-48,-50,-51,-47,-49,-117,-119,-118,-120,-92,-93,-94,-77,-79,-78,-22,-23,-24,-81,216,-114,-25,-80,-106,-113,-108,247,-111,256,257,264,-109,-112,-107,270,272,-110,274,275,]),'DEFAULT':([33,34,43,45,46,69,70,119,120,121,154,155,178,197,202,203,214,216,218,232,243,257,259,264,270,],[-115,-116,-48,-50,-51,-47,-49,-92,-93,-94,-77,-79,-78,-81,217,-114,-80,-106,-113,-108,-111,-109,-112,-107,-110,]),'ENDSWITCH':([33,34,43,45,46,69,70,119,120,121,154,155,178,197,203,205,214,216,218,232,243,257,259,264,270,],[-115,-116,-48,-50,-51,-47,-49,-92,-93,-94,-77,-79,-78,-81,-114,220,-80,-106,-113,-108,-111,-109,-112,-107,-110,]),'PUNTOIGUAL':([44,71,],[74,74,]),'MASIGUAL':([44,71,],[75,75,]),'MENOSIGUAL':([44,71,],[76,76,]),'CORCHIZQ':([47,72,73,74,75,76,89,92,93,110,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,141,156,164,166,199,200,204,229,],[89,89,89,-83,-84,-85,89,89,89,89,89,-86,-87,-88,-89,89,89,-71,-72,-73,-74,-75,-76,89,-68,-69,89,89,89,89,89,89,89,89,89,]),'ARRAY':([47,72,73,74,75,76,89,92,93,110,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,141,156,164,166,199,200,204,229,],[90,90,90,-83,-84,-85,90,90,90,90,90,-86,-87,-88,-89,90,90,-71,-72,-73,-74,-75,-76,90,-68,-69,90,90,90,90,90,90,90,90,90,]),'OPERLOGICO_NOT':([47,72,73,74,75,76,89,92,93,110,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,141,156,164,166,199,200,204,229,],[92,92,92,-83,-84,-85,92,92,92,92,92,-86,-87,-88,-89,92,92,-71,-72,-73,-74,-75,-76,92,-68,-69,92,92,92,92,92,92,92,92,92,]),'EXTENDS':([61,],[108,]),'IGUALIGUAL':([77,78,79,80,81,82,83,84,86,87,88,91,111,112,113,114,115,116,117,118,140,142,143,144,145,157,158,159,160,161,162,163,179,180,181,182,183,215,219,240,],[-54,-55,-57,129,-52,-53,-56,-58,-61,-62,-66,-64,-55,129,-52,-53,-54,-57,-55,129,129,-58,-56,129,129,129,129,129,-58,-59,129,-95,129,-60,129,129,-96,129,129,129,]),'NOIGUAL':([77,78,79,80,81,82,83,84,86,87,88,91,111,112,113,114,115,116,117,118,140,142,143,144,145,157,158,159,160,161,162,163,179,180,181,182,183,215,219,240,],[-54,-55,-57,130,-52,-53,-56,-58,-61,-62,-66,-64,-55,130,-52,-53,-54,-57,-55,130,130,-58,-56,130,130,130,130,130,-58,-59,130,-95,130,-60,130,130,-96,130,130,130,]),'MENORQUE':([77,78,79,80,81,82,83,84,86,87,88,91,111,112,113,114,115,116,117,118,140,142,143,144,145,157,158,159,160,161,162,163,179,180,181,182,183,215,219,240,],[-54,-55,-57,131,-52,-53,-56,-58,-61,-62,-66,-64,-55,131,-52,-53,-54,-57,-55,131,131,-58,-56,131,131,131,131,131,-58,-59,131,-95,131,-60,131,131,-96,131,131,131,]),'MAYORQUE':([77,78,79,80,81,82,83,84,86,87,88,91,111,112,113,114,115,116,117,118,140,142,143,144,145,157,158,159,160,161,162,163,179,180,181,182,183,215,219,240,],[-54,-55,-57,132,-52,-53,-56,-58,-61,-62,-66,-64,-55,132,-52,-53,-54,-57,-55,132,132,-58,-56,132,132,132,132,132,-58,-59,132,-95,132,-60,132,132,-96,132,132,132,]),'MAYORIGUAL':([77,78,79,80,81,82,83,84,86,87,88,91,111,112,113,114,115,116,117,118,140,142,143,144,145,157,158,159,160,161,162,163,179,180,181,182,183,215,219,240,],[-54,-55,-57,133,-52,-53,-56,-58,-61,-62,-66,-64,-55,133,-52,-53,-54,-57,-55,133,133,-58,-56,133,133,133,133,133,-58,-59,133,-95,133,-60,133,133,-96,133,133,133,]),'MENORIGUAL':([77,78,79,80,81,82,83,84,86,87,88,91,111,112,113,114,115,116,117,118,140,142,143,144,145,157,158,159,160,161,162,163,179,180,181,182,183,215,219,240,],[-54,-55,-57,134,-52,-53,-56,-58,-61,-62,-66,-64,-55,134,-52,-53,-54,-57,-55,134,134,-58,-56,134,134,134,134,134,-58,-59,134,-95,134,-60,134,134,-96,134,134,134,]),'PUNTO':([81,82,83,84,86,87,88,91,115,116,117,118,142,143,157,158,159,160,161,163,180,183,],[-52,-53,-56,-58,-61,-62,-66,-64,-54,-57,-55,156,-65,-63,-91,-90,-70,-67,-59,-95,-60,-96,]),'OPERASIG_ARRAY':([81,82,83,84,86,87,88,91,115,116,117,140,142,143,157,158,159,160,161,163,180,183,215,],[-52,-53,-56,-58,-61,-62,-66,-64,-54,-57,-55,164,-65,-63,-91,-90,-70,-67,-59,-95,-60,-96,229,]),'CORCHDER':([81,82,83,84,86,87,88,91,115,116,117,139,140,142,143,157,158,159,160,161,163,165,180,181,182,183,198,200,201,240,250,],[-52,-53,-56,-58,-61,-62,-66,-64,-54,-57,-55,163,-97,-65,-63,-91,-90,-70,-67,-59,-95,-99,-60,-98,-101,-96,-100,-102,-103,-104,-105,]),'OPERLOGICO_AND':([81,82,83,84,86,87,88,91,115,116,117,142,143,157,158,159,160,161,163,180,183,],[-52,-53,-56,136,-61,-62,-66,-64,-54,-57,-55,136,-63,-91,-90,-70,136,-59,-95,-60,-96,]),'OPERLOGICO_OR':([81,82,83,84,86,87,88,91,115,116,117,142,143,157,158,159,160,161,163,180,183,],[-52,-53,-56,137,-61,-62,-66,-64,-54,-57,-55,137,-63,-91,-90,-70,137,-59,-95,-60,-96,]),'DOSPUNTOS':([81,82,83,84,86,87,88,91,115,116,117,142,143,157,158,159,160,161,163,168,180,183,217,219,],[-52,-53,-56,-58,-61,-62,-66,-64,-54,-57,-55,-65,-63,-91,-90,-70,-67,-59,-95,185,-60,-96,230,231,]),'AS':([99,],[149,]),'SPLHEAP':([108,],[153,]),'AMPERSAND':([149,],[173,]),'LLAVEIZQ':([153,168,211,230,231,255,266,],[177,184,224,241,242,263,271,]),'PUBLIC':([177,],[196,]),'FUNCTION':([196,],[213,]),'MAYORQUEI':([212,],[226,]),'MENORQUEI':([212,],[227,]),'COMPARE':([213,],[228,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'sentencias':([0,],[1,]),'operacionMatematica':([0,16,224,],[2,41,237,]),'operador':([0,94,95,111,171,188,192,207,221,223,234,],[3,146,147,146,189,206,189,189,233,189,189,]),'tipoDevalorNumerico':([0,49,72,146,147,171,192,206,207,223,233,234,246,],[4,95,95,170,171,188,188,221,188,188,244,188,95,]),'foreach':([0,],[5,]),'arraymaps':([0,],[6,]),'tipoDeDato':([0,35,36,39,51,148,239,],[7,54,58,62,62,62,62,]),'parametros':([0,39,51,148,239,],[8,63,100,172,249,]),'funcion':([0,53,],[9,102,]),'monticuloHEAP':([0,],[10,]),'comentarios':([0,154,197,],[11,178,214,]),'impresion':([0,41,263,271,],[12,67,269,273,]),'programabasico':([0,],[13,]),'for':([0,],[14,]),'SplHeap':([0,],[15,]),'instrucciones':([16,43,231,241,242,],[40,69,243,251,252,]),'asignacion':([16,43,231,241,242,],[42,70,70,70,70,]),'instruccion':([16,43,231,241,242,],[43,43,43,43,43,]),'echo':([16,43,231,241,242,],[45,45,45,45,45,]),'switchCase':([16,43,231,241,242,],[46,46,46,46,46,]),'difigual':([44,71,],[73,73,]),'aritmetica':([47,72,73,89,92,93,110,122,127,128,135,138,141,156,164,166,199,200,204,229,],[79,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,]),'valores':([47,72,73,89,92,93,110,122,127,128,135,138,141,156,164,166,199,200,204,229,],[80,112,118,140,144,145,112,157,158,159,144,162,140,179,181,182,215,182,219,240,]),'booleanos':([47,72,73,89,92,93,110,122,127,128,135,138,141,156,164,166,199,200,204,229,],[84,84,84,84,142,84,84,84,84,84,160,84,84,84,84,84,84,84,84,84,]),'crearArrayCorta':([47,72,73,89,92,93,110,122,127,128,135,138,141,156,164,166,199,200,204,229,],[86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,]),'crearArrayLarga':([47,72,73,89,92,93,110,122,127,128,135,138,141,156,164,166,199,200,204,229,],[87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,]),'booleano':([47,72,73,89,92,93,110,122,127,128,135,138,141,156,164,166,199,200,204,229,],[88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,]),'comparacion':([47,72,73,89,92,93,110,122,127,128,135,138,141,156,164,166,199,200,204,229,],[91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,]),'operadores_aritmeticos':([79,80,112,116,118,140,144,145,157,158,159,162,179,181,182,215,219,240,],[122,127,127,122,127,127,127,127,127,127,127,127,127,127,127,127,127,127,]),'o_comparar':([80,112,118,140,144,145,157,158,159,162,179,181,182,215,219,240,],[128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,]),'o_logicos':([84,142,160,],[135,135,135,]),'valoresArray':([89,141,],[139,167,]),'repite_valores':([140,182,],[165,201,]),'operaciones':([171,192,207,223,234,],[191,209,222,235,245,]),'repite_claveValor':([181,240,],[198,250,]),'casos_switch':([184,185,203,],[202,205,218,]),'caso_switch':([184,185,203,],[203,203,203,]),'incdec':([212,],[225,]),'incdecfor':([254,],[260,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> sentencias","S'",1,None,None,None),
  ('sentencias -> operacionMatematica','sentencias',1,'p_sentencias','sintactico.py',26),
  ('sentencias -> operador','sentencias',1,'p_sentencias','sintactico.py',27),
  ('sentencias -> tipoDevalorNumerico','sentencias',1,'p_sentencias','sintactico.py',28),
  ('sentencias -> foreach','sentencias',1,'p_sentencias','sintactico.py',29),
  ('sentencias -> arraymaps','sentencias',1,'p_sentencias','sintactico.py',30),
  ('sentencias -> tipoDeDato','sentencias',1,'p_sentencias','sintactico.py',31),
  ('sentencias -> parametros','sentencias',1,'p_sentencias','sintactico.py',32),
  ('sentencias -> funcion','sentencias',1,'p_sentencias','sintactico.py',33),
  ('sentencias -> monticuloHEAP','sentencias',1,'p_sentencias','sintactico.py',34),
  ('sentencias -> comentarios','sentencias',1,'p_sentencias','sintactico.py',35),
  ('sentencias -> impresion','sentencias',1,'p_sentencias','sintactico.py',36),
  ('sentencias -> programabasico','sentencias',1,'p_sentencias','sintactico.py',37),
  ('sentencias -> for','sentencias',1,'p_sentencias','sintactico.py',38),
  ('sentencias -> SplHeap','sentencias',1,'p_sentencias','sintactico.py',39),
  ('sentencias -> INICIO instrucciones FIN','sentencias',3,'p_sentencias','sintactico.py',40),
  ('operador -> MAS','operador',1,'p_operador','sintactico.py',45),
  ('operador -> MENOS','operador',1,'p_operador','sintactico.py',46),
  ('operador -> MULTIPLICA','operador',1,'p_operador','sintactico.py',47),
  ('operador -> DIVIDE','operador',1,'p_operador','sintactico.py',48),
  ('operador -> MODULO','operador',1,'p_operador','sintactico.py',49),
  ('operador -> EXPONENCIACION','operador',1,'p_operador','sintactico.py',50),
  ('operacionMatematica -> VARIABLE_PHP IGUAL VARIABLE_PHP operador VARIABLE_PHP PUNTOYCOMA','operacionMatematica',6,'p_operacionMatematica','sintactico.py',58),
  ('operacionMatematica -> VARIABLE_PHP IGUAL VARIABLE_PHP operador tipoDevalorNumerico PUNTOYCOMA','operacionMatematica',6,'p_operacionMatematica','sintactico.py',59),
  ('operacionMatematica -> VARIABLE_PHP IGUAL tipoDevalorNumerico operador tipoDevalorNumerico PUNTOYCOMA','operacionMatematica',6,'p_operacionMatematica','sintactico.py',60),
  ('operacionMatematica -> VARIABLE_PHP IGUAL tipoDevalorNumerico operador tipoDevalorNumerico operaciones PUNTOYCOMA','operacionMatematica',7,'p_operacionMatematica','sintactico.py',61),
  ('operaciones -> tipoDevalorNumerico operador tipoDevalorNumerico','operaciones',3,'p_operaciones','sintactico.py',65),
  ('operaciones -> tipoDevalorNumerico operador tipoDevalorNumerico operador tipoDevalorNumerico','operaciones',5,'p_operaciones','sintactico.py',66),
  ('operaciones -> PARENIZQ operaciones PARENDER','operaciones',3,'p_operaciones','sintactico.py',67),
  ('operaciones -> operador PARENIZQ operaciones PARENDER operaciones','operaciones',5,'p_operaciones','sintactico.py',68),
  ('operaciones -> PARENIZQ operaciones PARENDER operaciones','operaciones',4,'p_operaciones','sintactico.py',69),
  ('operaciones -> operador PARENIZQ operaciones PARENDER','operaciones',4,'p_operaciones','sintactico.py',70),
  ('tipoDevalorNumerico -> ENTERO','tipoDevalorNumerico',1,'p_tipoDevalorNumerico','sintactico.py',73),
  ('tipoDevalorNumerico -> FLOTANTE','tipoDevalorNumerico',1,'p_tipoDevalorNumerico','sintactico.py',74),
  ('tipoDeDato -> ENTERO','tipoDeDato',1,'p_tipoDeDato','sintactico.py',81),
  ('tipoDeDato -> FLOTANTE','tipoDeDato',1,'p_tipoDeDato','sintactico.py',82),
  ('tipoDeDato -> CADENA','tipoDeDato',1,'p_tipoDeDato','sintactico.py',83),
  ('tipoDeDato -> VARIABLE_PHP','tipoDeDato',1,'p_tipoDeDato','sintactico.py',84),
  ('tipoDeDato -> BOOLEANO','tipoDeDato',1,'p_tipoDeDato','sintactico.py',85),
  ('tipoDeDato -> NULL','tipoDeDato',1,'p_tipoDeDato','sintactico.py',86),
  ('parametros -> tipoDeDato','parametros',1,'p_parametros','sintactico.py',92),
  ('parametros -> tipoDeDato COMA parametros','parametros',3,'p_parametros','sintactico.py',93),
  ('foreach -> FOREACH PARENIZQ VARIABLE_PHP AS AMPERSAND VARIABLE_PHP PARENDER LLAVEIZQ operacionMatematica LLAVEDER','foreach',10,'p_foreach','sintactico.py',98),
  ('arraymaps -> OPERAMAPA PARENIZQ parametros PARENDER PUNTOYCOMA','arraymaps',5,'p_arraymaps','sintactico.py',107),
  ('arraymaps -> VARIABLE_PHP IGUAL OPERAMAPA PARENIZQ parametros PARENDER PUNTOYCOMA','arraymaps',7,'p_arraymaps','sintactico.py',108),
  ('funcion -> NEW NOMBRE PARENIZQ PARENDER PUNTOYCOMA','funcion',5,'p_funcion','sintactico.py',115),
  ('monticuloHEAP -> HEAP IGUAL funcion','monticuloHEAP',3,'p_monticuloHEAP','sintactico.py',120),
  ('instrucciones -> instruccion instrucciones','instrucciones',2,'p_instrucciones','sintactico.py',128),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones','sintactico.py',129),
  ('instruccion -> asignacion','instruccion',1,'p_instruccion','sintactico.py',132),
  ('instruccion -> echo','instruccion',1,'p_instruccion','sintactico.py',133),
  ('instruccion -> switchCase','instruccion',1,'p_instruccion','sintactico.py',134),
  ('valores -> ENTERO','valores',1,'p_valores','sintactico.py',137),
  ('valores -> FLOTANTE','valores',1,'p_valores','sintactico.py',138),
  ('valores -> CADENA','valores',1,'p_valores','sintactico.py',139),
  ('valores -> VARIABLE_PHP','valores',1,'p_valores','sintactico.py',140),
  ('valores -> BOOLEANO','valores',1,'p_valores','sintactico.py',141),
  ('valores -> aritmetica','valores',1,'p_valores','sintactico.py',142),
  ('valores -> booleanos','valores',1,'p_valores','sintactico.py',143),
  ('valores -> NOMBRE PARENIZQ PARENDER','valores',3,'p_valores','sintactico.py',144),
  ('valores -> NOMBRE PARENIZQ valores PARENDER','valores',4,'p_valores','sintactico.py',145),
  ('valores -> crearArrayCorta','valores',1,'p_valores','sintactico.py',146),
  ('valores -> crearArrayLarga','valores',1,'p_valores','sintactico.py',147),
  ('booleano -> BOOLEANO','booleano',1,'p_booleano','sintactico.py',151),
  ('booleano -> comparacion','booleano',1,'p_booleano','sintactico.py',152),
  ('booleano -> OPERLOGICO_NOT booleanos','booleano',2,'p_booleano','sintactico.py',153),
  ('booleanos -> booleano','booleanos',1,'p_booleanos','sintactico.py',157),
  ('booleanos -> booleanos o_logicos booleanos','booleanos',3,'p_booleanos','sintactico.py',158),
  ('o_logicos -> OPERLOGICO_AND','o_logicos',1,'p_o_logicos','sintactico.py',162),
  ('o_logicos -> OPERLOGICO_OR','o_logicos',1,'p_o_logicos','sintactico.py',163),
  ('comparacion -> valores o_comparar valores','comparacion',3,'p_comparacion','sintactico.py',166),
  ('o_comparar -> IGUALIGUAL','o_comparar',1,'p_o_comparar','sintactico.py',169),
  ('o_comparar -> NOIGUAL','o_comparar',1,'p_o_comparar','sintactico.py',170),
  ('o_comparar -> MENORQUE','o_comparar',1,'p_o_comparar','sintactico.py',171),
  ('o_comparar -> MAYORQUE','o_comparar',1,'p_o_comparar','sintactico.py',172),
  ('o_comparar -> MAYORIGUAL','o_comparar',1,'p_o_comparar','sintactico.py',173),
  ('o_comparar -> MENORIGUAL','o_comparar',1,'p_o_comparar','sintactico.py',174),
  ('asignacion -> VARIABLE_PHP IGUAL valores PUNTOYCOMA','asignacion',4,'p_asignacion','sintactico.py',177),
  ('asignacion -> VARIABLE_PHP IGUAL valores PUNTOYCOMA comentarios','asignacion',5,'p_asignacion','sintactico.py',178),
  ('asignacion -> VARIABLE_PHP difigual valores PUNTOYCOMA','asignacion',4,'p_asignacion','sintactico.py',179),
  ('asignacion -> VARIABLE_PHP difigual valores PUNTO valores PUNTOYCOMA comentarios','asignacion',7,'p_asignacion','sintactico.py',180),
  ('asignacion -> VARIABLE_PHP difigual valores PUNTO valores PUNTOYCOMA','asignacion',6,'p_asignacion','sintactico.py',181),
  ('asignacion -> asignacion','asignacion',1,'p_asignacion','sintactico.py',182),
  ('difigual -> PUNTOIGUAL','difigual',1,'p_difigual','sintactico.py',187),
  ('difigual -> MASIGUAL','difigual',1,'p_difigual','sintactico.py',188),
  ('difigual -> MENOSIGUAL','difigual',1,'p_difigual','sintactico.py',189),
  ('operadores_aritmeticos -> MAS','operadores_aritmeticos',1,'p_operadores_aritmeticos','sintactico.py',192),
  ('operadores_aritmeticos -> MENOS','operadores_aritmeticos',1,'p_operadores_aritmeticos','sintactico.py',193),
  ('operadores_aritmeticos -> MULTIPLICA','operadores_aritmeticos',1,'p_operadores_aritmeticos','sintactico.py',194),
  ('operadores_aritmeticos -> DIVIDE','operadores_aritmeticos',1,'p_operadores_aritmeticos','sintactico.py',195),
  ('aritmetica -> valores operadores_aritmeticos valores','aritmetica',3,'p_aritmetica','sintactico.py',199),
  ('aritmetica -> aritmetica operadores_aritmeticos valores','aritmetica',3,'p_aritmetica','sintactico.py',200),
  ('echo -> ECHO CADENA PUNTOYCOMA','echo',3,'p_echo','sintactico.py',203),
  ('echo -> ECHO VARIABLE_PHP PUNTOYCOMA','echo',3,'p_echo','sintactico.py',204),
  ('echo -> ECHO aritmetica PUNTOYCOMA','echo',3,'p_echo','sintactico.py',205),
  ('crearArrayCorta -> CORCHIZQ valoresArray CORCHDER','crearArrayCorta',3,'p_crearArrayCorta','sintactico.py',210),
  ('crearArrayLarga -> ARRAY PARENIZQ valoresArray PARENDER','crearArrayLarga',4,'p_crearArrayLarga','sintactico.py',215),
  ('valoresArray -> valores','valoresArray',1,'p_valoresArray','sintactico.py',221),
  ('valoresArray -> valores OPERASIG_ARRAY valores','valoresArray',3,'p_valoresArray','sintactico.py',222),
  ('valoresArray -> valores repite_valores','valoresArray',2,'p_valoresArray','sintactico.py',223),
  ('valoresArray -> valores OPERASIG_ARRAY valores repite_claveValor','valoresArray',4,'p_valoresArray','sintactico.py',224),
  ('repite_valores -> COMA valores','repite_valores',2,'p_repite_valoresSeparadosComa','sintactico.py',229),
  ('repite_valores -> COMA valores COMA','repite_valores',3,'p_repite_valoresSeparadosComa','sintactico.py',230),
  ('repite_valores -> COMA valores repite_valores','repite_valores',3,'p_repite_valoresSeparadosComa','sintactico.py',231),
  ('repite_claveValor -> COMA valores OPERASIG_ARRAY valores','repite_claveValor',4,'p_repite_claveValorSeparadosComa','sintactico.py',234),
  ('repite_claveValor -> COMA valores OPERASIG_ARRAY valores repite_claveValor','repite_claveValor',5,'p_repite_claveValorSeparadosComa','sintactico.py',235),
  ('switchCase -> SWITCH PARENIZQ valores PARENDER LLAVEIZQ casos_switch LLAVEDER','switchCase',7,'p_switchCase','sintactico.py',238),
  ('switchCase -> SWITCH PARENIZQ valores PARENDER LLAVEIZQ casos_switch DEFAULT DOSPUNTOS LLAVEIZQ instrucciones LLAVEDER LLAVEDER','switchCase',12,'p_switchCase','sintactico.py',239),
  ('switchCase -> SWITCH PARENIZQ valores PARENDER DOSPUNTOS casos_switch ENDSWITCH PUNTOYCOMA','switchCase',8,'p_switchCase','sintactico.py',240),
  ('caso_switch -> CASE valores DOSPUNTOS LLAVEIZQ instrucciones LLAVEDER','caso_switch',6,'p_caso_switch','sintactico.py',245),
  ('caso_switch -> CASE valores DOSPUNTOS LLAVEIZQ instrucciones BREAK PUNTOYCOMA LLAVEDER','caso_switch',8,'p_caso_switch','sintactico.py',246),
  ('caso_switch -> CASE valores DOSPUNTOS instrucciones','caso_switch',4,'p_caso_switch','sintactico.py',247),
  ('caso_switch -> CASE valores DOSPUNTOS instrucciones BREAK PUNTOYCOMA','caso_switch',6,'p_caso_switch','sintactico.py',248),
  ('casos_switch -> caso_switch casos_switch','casos_switch',2,'p_casos_switch','sintactico.py',252),
  ('casos_switch -> caso_switch','casos_switch',1,'p_casos_switch','sintactico.py',253),
  ('comentarios -> COMENTARIO_UNA_LINEA','comentarios',1,'p_comentarios','sintactico.py',258),
  ('comentarios -> COMENTARIO_LARGO','comentarios',1,'p_comentarios','sintactico.py',259),
  ('impresion -> ECHO tipoDeDato PUNTOYCOMA','impresion',3,'p_impresion','sintactico.py',261),
  ('impresion -> PRINT tipoDeDato PUNTOYCOMA','impresion',3,'p_impresion','sintactico.py',262),
  ('impresion -> ECHO VARIABLE_PHP PUNTOYCOMA','impresion',3,'p_impresion','sintactico.py',263),
  ('impresion -> PRINT VARIABLE_PHP PUNTOYCOMA','impresion',3,'p_impresion','sintactico.py',264),
  ('programabasico -> INICIO operacionMatematica FIN','programabasico',3,'p_programabasico','sintactico.py',266),
  ('programabasico -> INICIO operacionMatematica impresion FIN','programabasico',4,'p_programabasico','sintactico.py',267),
  ('programabasico -> INICIO asignacion FIN','programabasico',3,'p_programabasico','sintactico.py',268),
  ('incdec -> MAYORQUEI','incdec',1,'p_incdec','sintactico.py',271),
  ('incdec -> MENORQUEI','incdec',1,'p_incdec','sintactico.py',272),
  ('incdecfor -> MAS MAS','incdecfor',2,'p_incdecfor','sintactico.py',275),
  ('incdecfor -> MENOS MENOS','incdecfor',2,'p_incdecfor','sintactico.py',276),
  ('for -> FOR PARENIZQ VARIABLE_PHP IGUAL ENTERO PUNTOYCOMA VARIABLE_PHP incdec ENTERO PUNTOYCOMA VARIABLE_PHP incdecfor PARENDER LLAVEIZQ impresion LLAVEDER','for',16,'p_for','sintactico.py',280),
  ('SplHeap -> CLASS NOMBRE EXTENDS SPLHEAP LLAVEIZQ PUBLIC FUNCTION COMPARE PARENIZQ parametros PARENDER LLAVEIZQ impresion LLAVEDER LLAVEDER','SplHeap',15,'p_SplHeap','sintactico.py',283),
]
