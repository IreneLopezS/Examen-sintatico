from flask import Flask, render_template, request
from lexer import Lexer
from parser import Parser

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    tokens_details = []
    token_counts = {}
    is_valid = True
    error_message = ""
    
    if request.method == 'POST':
        code = request.form['code']
        lexer = Lexer()
        tokens = lexer.tokenize(code)
        tokens_details, token_counts = lexer.get_token_details(tokens)  # Aquí obtenemos los detalles y conteo
        
        parser = Parser()
        try:
            is_valid = parser.validate(code)  # Validamos la estructura
        except ValueError as e:
            is_valid = False
            error_message = str(e)

    return render_template('index.html', tokens_details=tokens_details, token_counts=token_counts, is_valid=is_valid, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
