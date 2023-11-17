import ply.lex as lex
from os import system

# Tokens
tokens = (
    'IDENTIFIER',
    'NUMBER',
    'STRING',
    'SEMICOLON',
    'ASSIGN',
    'KEYWORD'
)

t_NUMBER = r'\d+(\.\d+)?'
t_STRING = r'\"([^\\\n]|(\\.))*?\"'
t_SEMICOLON = r';'
t_ASSIGN = r'='

def t_KEYWORD(t):
    r'\b(var|const|let)\b'
    return t 

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

input_text = '''
var x = 10;
'''

lexer.input(input_text)
system('clear')
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(f'\033[32m{tok.type}\033[0m -> \033[36m{tok.value}\033[0m')
