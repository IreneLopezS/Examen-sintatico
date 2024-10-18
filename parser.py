import re

class Parser:
    def __init__(self):
        self.expected_structure = re.compile(r'''
            ^\s*#include\s+<stdio\.h>\s*            # Línea de inclusión
            main\(\)\s*                             # Declaración de la función main
            /\*.*?\*/\s*                             # Comentario
            \{\s*                                    # Apertura de llave
            int\s+([a-zA-Z_][a-zA-Z0-9_]*),\s*([a-zA-Z_][a-zA-Z0-9_]*)=\d+;\s*  # Declaración de variables
            for\s*\(\s*\2=\d+;\s*\2<=\d+;\s*\2\+\+\)\s*  # Bucle for usando la variable
            \{\s*                                    # Apertura de llave del bucle
            printf\("%d ",\s*\1\);\s*               # Llamada a printf con la otra variable
            \2\+\+;\s*                               # Incremento de la variable
            \}\s*                                    # Cierre de llave del bucle
            \}\s*                                    # Cierre de llave de main
            $                                        # Fin de la cadena
        ''', re.MULTILINE | re.VERBOSE)

    def validate(self, code):
        if self.expected_structure.match(code):
            return True
        else:
            raise ValueError("Estructura incorrecta")
