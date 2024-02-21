from ply import lex

tokens = (
    'NUMERO',
    'SUMA',
    'RESTA',
    'MULTIPLICACION',
    'DIVISION',
)


# Definir las reglas para los tokens
t_SUMA = r'\+'
t_RESTA = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'


def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t


t_ignore = ' \n'


def t_error(t):
    print(f"ese caracter aun no esta definido: '{t.value[0]}'")
    t.lexer.skip(1)


lexer = lex.lex()

datos = '3 + 1 * 3 - 2 / 9'
lexer.input(datos)

while True:
    token = lexer.token()
    if not token:
        break
    print(token)

