import os 
import ply.yacc as yacc
from lexer_var import tokens

def p_variables(p):
    '''
    variables : KEYWORD IDENTIFIER ASSIGN STRING SEMICOLON 
              | KEYWORD IDENTIFIER ASSIGN NUMBER SEMICOLON
              | KEYWORD IDENTIFIER SEMICOLON
    '''
    if len(p) == 6 :
        p[0] = f'{p[1]} {p[2]} = {p[4]};'
    else :
        p[0] = f'{p[1]} {p[2]};'
        
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
    
    if s.lower() == 'exit':
        break
    
    if not s: 
        continue
    
    result = parser.parse(s)
    
    if result is None:
        print("\033[91mThis isn't valid syntax\033[0m")  
    else:
        print("\033[93mValid statement\033[0m")  


# Perform the clear and print statements after the loop exits
os.system('clear')
print("\033[95mHappy\033[0m \033[94mparsing\033[0m \033[97m:-)\033[0m")
