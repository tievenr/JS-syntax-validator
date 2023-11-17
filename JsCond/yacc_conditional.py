import os
import ply.yacc as yacc
from lexer_conditional import tokens

def p_if_else_statement(p):
    '''
    if_else_statement : IF LPAREN condition RPAREN LBRACE statements RBRACE ELSE LBRACE statements RBRACE
                      | IF LPAREN condition RPAREN LBRACE statements RBRACE
    '''
    if len(p) == 11:
        p[0] = 'if' +'(' + p[3] + ')'+'{' + p[6] + '}'+' else'+' {' + p[10] + '}'
    else:
        p[0] = 'if'+'(' + p[3] + ')'+'{' + p[6] + '}'


def p_condition(p):
    '''
    condition : expression LE expression
              | expression GE expression
              | expression LEQ expression
              | expression GEQ expression
              | expression EQ expression
              | expression NOTEQ expression
    '''
    p[0] = p[1] + p[2]  + p[3]

def p_expression(p):
    '''expression : IDENTIFIER
                  | NUMBER
                  | expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | DQUOTE sentences DQUOTE
                  | SQUOTE sentences SQUOTE'''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        if p[1] == '"' or p[1]=="'":
            p[0] = p[1] + p[2] + p[1]
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
    statement : assignment_statement
             | print_statement
    '''
    p[0] = p[1]

def p_print_statement(p):
    '''print_statement : PRINT LPAREN expression RPAREN SEMICOLON'''
    p[0] = 'console.log(' + p[3] + ');'

def p_assignment_statement(p):
    '''
    assignment_statement : IDENTIFIER ASSIGN expression SEMICOLON
                         | IDENTIFIER SEMICOLON
    '''
    if len(p) == 5:
        p[0] = p[1] + '=' + p[3] + ';'
    else:
        p[0] = p[1] + ';' if len(p) == 3 else p[1] + p[2] + '=' + p[4] + ';'

def p_error(p):
    if p:
        print(f"Syntax error at line {p.lineno}, position {p.lexpos}: Unexpected token '{p.value}'")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()

while True:
    try:
        s = input('calc > ')
        print(s)
        if s.strip() == 'exit':
            break
    except EOFError:
        break
    
    
    
    if not s: 
        continue
    
    result = parser.parse(s)
    
    if result is None:
        print("\033[91mThis isn't valid syntax\033[0m")  
    else:
        print("\033[93mValid statement\033[0m")  


os.system('clear')
print("\033[95mHappy\033[0m \033[94mparsing\033[0m \033[97m:-)\033[0m")
