import ply.lex as lex
from os import system

tokens = (
    'IDENTIFIER',
    'NUMBER',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'SEMICOLON',
    'CLASS',
    'ASSIGN',
    'CONSTRUCTOR',
    'COMMA',
    'STRING',
    'PERIOD'
)
t_STRING = r'\"([^\\\n]|(\\.))*?\"'
t_NUMBER = r'\d+(\.\d+)?'
t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMICOLON = r'\;'
t_ASSIGN = r'\='
t_COMMA = r'\,'
t_PERIOD=r'\.'

def t_CONSTRUCTOR(t):
    r'constructor'
    return t

def t_CLASS(t):
    r'class'
    return t

t_ignore = ' \t\n'

def t_error(t):
    print(f"Illegal character {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

input_text = '''
class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
}
'''

lexer.input(input_text)
system('clear')
while True:
    tok = lexer.token()
    if not tok:
        break  
    print(f'\033[32m{tok.type}\033[0m -> \033[36m{tok.value}\033[0m')
