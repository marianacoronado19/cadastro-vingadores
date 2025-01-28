from flask import Flask, render_template

app = Flask(__name__) #__name__ = variavel que representa o nome da classe

@app.route("/") 
def home():
    return render_template("home.html")

@app.route("/ola")
def pagina_inicial():
    return "<p>Olá, mundo!</p>"


# from model.interface import Interface

# def main():
#     Interface()

# if __name__ == '__main__': # Sempre no final do arquivo contendo a definição da função principal
#     main()