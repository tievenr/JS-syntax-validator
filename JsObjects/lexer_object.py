import ply.lex as lex
from os import system

tokens = (
    'IDENTIFIER',
    'LBRACE',
    'RBRACE',
    'COLON',
    'ASSIGN',
    'COMMA',
    'DQUOTE',
    'NUMBER',
    'STRING',
    'KEYWORD'

)
t_STRING = r'\"([^\\\n]|(\\.))*?\"'
t_NUMBER = r'\d+(\.\d+)?'
t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COLON = r':'
t_COMMA = r','
t_DQUOTE = r'"'
t_ASSIGN=r'='

t_ignore = ' \t'

def t_KEYWORD(t):
    r'\b(var|const|let)\b'
    return t 

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

input_text = '''let x={
    "name": "John",
    "age": 30,
    "city": "New York"
}
'''

lexer.input(input_text)
system('clear')
while True:
    tok = lexer.token()
    if not tok:
        break  
    print(f'\033[32m{tok.type}\033[0m -> \033[36m{tok.value}\033[0m')
