import ply.yacc as yacc
from lexer_classes import tokens  

def p_class(p):
    '''
    class : CLASS IDENTIFIER LBRACE constructor RBRACE
    '''
    p[0] = f'class {p[2]} ' + '{' + p[4] + '}'

def p_constructor(p):
    '''
    constructor : CONSTRUCTOR LPAREN params RPAREN LBRACE statements RBRACE
    '''
    p[0] = f'constructor {p[3]} ' + '{' + p[6] + '}'

def p_params(p):
    '''
    params : param
           | param COMMA params
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = ', '.join(p[1:])

def p_param(p):
    '''
    param : IDENTIFIER
    '''
    p[0] = p[1]

def p_statements(p):
    '''
    statements : statement
               | statement statements
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1] + p[2]

def p_statement(p):
    '''
    statement : IDENTIFIER PERIOD IDENTIFIER ASSIGN expression SEMICOLON
    '''
    p[0] = p[1]+ '.'+ p[3]+'='+p[5] +';'

def p_expression(p):
    '''
    expression : IDENTIFIER
               | NUMBER
               | STRING
    '''
    p[0] = p[1]

def p_error(p):
    if p:
        print(f"Syntax error at line {p.lineno}, position {p.lexpos}: Unexpected token '{p.value}'")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()

while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    if result is None:
        print("\033[91mThis isn't valid syntax\033[0m")  
    else:
        print("\033[93mValid statement\033[0m")  

