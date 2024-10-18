import re
from collections import defaultdict

class Lexer:
    def __init__(self):
        self.keywords = {'include', 'main', 'int', 'for', 'printf'}
        self.token_pattern = re.compile(r'''
            \s*(?:
                #include|              # palabra reservada
                int|                  # palabra reservada
                for|                  # palabra reservada
                printf|               # palabra reservada
                [a-zA-Z_][a-zA-Z0-9_]*| # identificador
                \d+|                  # número
                [(){};,=<>]          # símbolos
                |//.*?$|              # comentario de una línea
                /\*.*?\*/            # comentario de múltiples líneas
            )
        ''', re.MULTILINE | re.VERBOSE)

    def tokenize(self, code):
        tokens = []
        for match in self.token_pattern.finditer(code):
            token = match.group().strip()
            if token:
                tokens.append(token)
        return tokens

    def get_token_details(self, tokens):
        details = []
        counts = defaultdict(int)

        for token in tokens:
            if token in self.keywords:
                tipo = 'Palabra reservada'
            elif re.match(r'[(){};,]', token):
                tipo = 'Símbolo'
            elif re.match(r'\d+', token):
                tipo = 'Literal'
            elif re.match(r'[a-zA-Z_][a-zA-Z0-9_]*', token):
                tipo = 'Identificador' if token != 'stdio.h' else 'Identificador/Archivo'
            elif token.startswith('/*') or token.endswith('*/'):
                tipo = 'Símbolo (comentario)'
            else:
                continue

            # Almacena token, tipo y cantidad 1
            details.append((token, tipo, 1))
            # Incrementa el conteo
            counts[tipo] += 1

        return details, counts

    def get_token_counts(self, tokens):
        counts = defaultdict(int)
        for token in tokens:
            if token in self.keywords:
                counts['Palabras reservadas'] += 1
            elif re.match(r'[(){};,]', token):
                counts['Símbolos'] += 1
            elif re.match(r'\d+', token):
                counts['Literales'] += 1
            elif re.match(r'[a-zA-Z_][a-zA-Z0-9_]*', token):
                if token == 'stdio.h':
                    counts['Identificadores/Archivo'] += 1
                else:
                    counts['Identificadores'] += 1
        return counts
