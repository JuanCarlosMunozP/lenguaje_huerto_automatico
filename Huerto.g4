grammar Huerto;

program: (declaration | routine)+ EOF;

declaration: 'cultivo' ID ';';

routine: 'tarea' ID '(' ')' '{' statement+ '}' ;

statement
    : control
    | action
    | call
    ;

control: 'si' condition ':' statement ('sino' ':' statement)? # ifControl ;

action
    : ('regar' | 'abonar' | 'podar' ) ID ';'     # cultivoAction
    | 'esperar' NUMBER 'dias' ';'     # esperarAction
    ;

call: ID '(' ')' ';' ;

condition: ID comparator NUMBER;

comparator: '<' | '>' | '==' ;

ID: [a-zA-Z_][a-zA-Z_0-9]*;
NUMBER: [0-9]+;
WS: [ \t\r\n]+ -> skip;