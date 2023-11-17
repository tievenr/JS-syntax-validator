import ply.lex as lex
from os import system
# Tokens
tokens = (
    'LE',
    'GE',
    'GEQ',
    'LEQ',
    'EQ',
    'NOTEQ',
    'PRINT',
    'DQUOTE',
    'IDENTIFIER',
    'NUMBER',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'ASSIGN',
    'IF',
    'ELSE',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'SQUOTE',
    'SEMICOLON'
)
t_LEQ = r'<='  
t_GEQ = r'>='  
t_LE = r'<'    
t_GE = r'>'    
t_EQ = r'=='   
t_NOTEQ = r'!='  
t_NUMBER = r'\d+(\.\d+)?'
t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_DQUOTE = r'"'
t_SQUOTE=r'\''
t_ASSIGN = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_SEMICOLON = r';'

# Ignored characters (spaces and tabs)
t_ignore = ' \t'

def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_PRINT(t):
    r'console.log'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

input_text = '''
if(a >= 10){
    console.log('Hello lmao')}
else
{
    a += 10;
    console.log('You suck')
}
'''

lexer.input(input_text)
system('clear')
while True:
    tok = lexer.token()
    if not tok:
        break
    print(f'\033[32m{tok.type}\033[0m -> \033[36m{tok.value}\033[0m')

