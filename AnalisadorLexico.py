# Bibliotecas
import os.path
import sys

# Regras
rules = {
    # Reservadas
    'WHILE'    : 'RESERVADAS',
    'ENQUANTO' : 'RESERVADAS',
    'IF'       : 'RESERVADAS',
    'SE'       : 'RESERVADAS',
    'FOR'      : 'RESERVADAS',
    'PARA'     : 'RESERVADAS',
    'PRINT'    : 'RESERVADAS',
    'MOSTRE'   : 'RESERVADAS',
    'INPUT'    : 'RESERVADAS',
    'LER'      : 'RESERVADAS',
    'DEFINICOES' : 'RESERVADAS',
    'ELSE' : 'RESERVADAS',
    'FIM' : 'RESERVADAS',
    # Operador Matemático
    '+' : 'MATEMATICO',
    '-' : 'MATEMATICO',
    '/' : 'MATEMATICO',
    '*' : 'MATEMATICO',
    '^' : 'MATEMATICO',
    # Operador
    ':=' : 'OPERADOR',
    '==' : 'OPERADOR',
    '<<' : 'OPERADOR',
    '<=' : 'OPERADOR',
    '>>' : 'OPERADOR',
    '&&' : 'OPERADOR',
    '||' : 'OPERADOR',
    ':' : 'OPERADOR',
    ';' : 'OPERADOR',
}

myFile = open('./programa.txt', 'r') # Abre o arquivo
output = [] # Array de saída
string = ""
processString = False

for linha in myFile:
    col = 0
    arrayLines = linha.split()
    for token in arrayLines:
        if processString: # Verificador de string
            string += " " + token
            # Verifica pela aspas de fechamento
            if '"' in token:
                output.append(['STRING', string, col])
                string = ""
                processString = False
            col += 1
            continue
        if token.startswith('"'): # Verificador de string
            if token.endswith('"') and len(token) > 1:
                output.append(['STRING', token.strip('"'), col])
            else:
                # Remove o espaço à esquerda
                string = token
                processString = True
            col += 1
            continue
        if token.isdigit(): # Verificador de número
            output.append(['NUMERO', token, col])
        elif token in rules: # Se está na regra
            output.append([rules[token], token, col])
        elif token.startswith('var') and len(token) <= 12 and any(i in token for i in ['INT','FLT','STR']): # Se começa com 'var', tamanho <=12 e tipo válido
            output.append(['IDENTIFICADOR', token, col])
        else:
            output.append(['ERRO', token, col])
        col += 1 #acrescenta mais um na posição do token

myFile.close()
print(output)

