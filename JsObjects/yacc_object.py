import os 
import ply.yacc as yacc
from lexer_object import tokens

def p_object(p):
    'object : KEYWORD IDENTIFIER ASSIGN LBRACE instances RBRACE'
    p[0] = p[1] + p[2] + '=' + '{' + p[4] + '}'

def p_instances(p):
    '''instances : instance
             | instance COMMA instances '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_instance(p):
    'instance :  IDENTIFIER COLON value'
    p[0] = p[1]+':'+p[3]


def p_value(p):
    '''value : STRING
             | NUMBER'''
    p[0] = p[1]
def p_error(p):
    if p:
        error_position = p.lexpos
        error_token = p.type
        print(f"Syntax error at position {error_position}: Unexpected token '{error_token}'")
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




