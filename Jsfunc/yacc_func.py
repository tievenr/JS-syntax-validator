import ply.yacc as yacc
from lexer_func import tokens
def p_function(p):
    '''
    function : FUNCTION IDENTIFIER LPAREN parameters RPAREN LBRACE statements RBRACE
            | FUNCTION IDENTIFIER LPAREN RPAREN LBRACE statements RBRACE
    '''
    if p[4]== 'parameters':
        p[0] = p[1]+ p[2] + '(' + p[4] + ')' + '{' + p[7] + '}'
    else:
        p[0] = p[1] + p[2] + '('+')' + '{' + p[6] + '}'

def p_parameters(p):
    '''parameters : parameter
                  | parameter COMMA parameters'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1] + ',' + p[3]

def p_parameter(p):
    '''parameter : IDENTIFIER'''
    p[0] = p[1] 

def p_statements(p):
    '''statements : statement
                  | statement statements'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1] + p[2]

def p_statement(p):
    '''statement : assignment_statement
                 | print_statement
                 | return'''
    p[0] = p[1]

def p_return(p):
    '''return : RETURN expression SEMICOLON'''
    p[0] = p[1] + p[2] + p[3]

def p_assignment_statement(p):
    '''
    assignment_statement : IDENTIFIER ASSIGN expression SEMICOLON
                         | IDENTIFIER SEMICOLON
    '''
    if len(p) == 5:
        p[0] = p[1] + '=' + p[3] + ';'
    else:
        p[0] = p[1] + ';' if len(p) == 3 else p[1] + p[2] + '=' + p[4] + ';'

def p_print_statement(p):
    '''print_statement : PRINT LPAREN expression RPAREN SEMICOLON'''
    p[0] = 'console.log(' + p[3] + ');'

def p_expression(p):
    '''expression : IDENTIFIER
                  | NUMBER
                  | expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | DQUOTE sentences DQUOTE'''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        if p[1] == '"':
            p[0] = '"' + p[2] + '"'
        else:
            p[0] = p[1] + p[2] + p[3]

def p_sentences(p):
    '''sentences : sentence
                 | sentence sentences'''
    if len(p)==2:
        p[0] = p[1]
    else:
        p[0] = p[1] + p[2]

def p_sentence(p):
    '''sentence :  IDENTIFIER
                  | NUMBER
                  | sentence PLUS
                  | sentence MINUS
                  | sentence PLUS sentence
                  | sentence MINUS sentence
                  | sentence TIMES sentence
                  | sentence DIVIDE sentence'''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1] + p[2] + p[3]

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
        print("Error")
    else:
        print("Valid statement")
#actual commit