grammar Types;

expr : unaryExpr | addExpr ;
funcCall : rangeCall | floorCall ;
rangeCall : RANGE '(' rangeArgs ')' ;
rangeArgs : rangeString | rangeNums ;
rangeString : STRING ;
rangeNums : NUM ',' NUM ;
floorCall : FLOOR '(' NUM ')' ;
array : '[' (expr (',' expr)*)? ']' ;
unaryExpr : ADD_OP NUM ;
addExpr : mulExpr | addExpr ADD_OP mulExpr ;
mulExpr : term | mulExpr MUL_OP term ;
term : num | string | funcCall | array | '(' expr ')' ;
num : NUM ;
string : STRING ;

STRING : '"' .*? '"' | '\'' .*? '\'' ;
NUM : [0-9]+ ('.' [0-9]+)? ;
ADD_OP : [\+\-] ;
MUL_OP : [\*\/] ;
RANGE : 'RANGE' ;
FLOOR : 'FLOOR' ;
WS : [ \r\t\n]+ -> skip ;

