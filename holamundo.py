#from flask import Flask
#
#app = Flask(__name__)
#
#@app.route('/')
#def hola_mundo():
#    return '¡Hola, Mundo!'
#
#if __name__ == '__main__':
#    app.run(debug=True)
#    # 127.0.0.1:5000

from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    contenidoHtml = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Página con Flask</title>
    </head>
    <body>
        <h1>Hola Mundo desde Flask 😎</h1>
    </body>
    </html>
    """

    return render_template_string(contenidoHtml)

if __name__ == '__main__':
    app.run(debug=True)
