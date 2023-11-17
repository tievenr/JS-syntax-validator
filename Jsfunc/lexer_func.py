import ply.lex as lex
from os import system
# Tokens
tokens = (
    'PRINT',
    'DQUOTE',
    'IDENTIFIER',
    'NUMBER',
    'LPAREN',
    'RPAREN',
    'FUNCTION',
    'LBRACE',
    'RBRACE',
    'COMMA',
    'ASSIGN',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'SEMICOLON',
    'RETURN'
)

t_NUMBER = r'\d+(\.\d+)?'
t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r','
t_DQUOTE = r'"'
t_ASSIGN = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_SEMICOLON = r';'

# Ignored characters (spaces and tabs)
t_ignore = ' \t'

def t_FUNCTION(t):
    r'function'
    return t

def t_RETURN(t):
    r'return'
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
   function addNumbers(a, b) {
    a=5;
}

'''

lexer.input(input_text)
system('clear')
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(f'\033[32m{tok.type}\033[0m -> \033[36m{tok.value}\033[0m')

