from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Minha primeira API Flask!"

@app.route("/dados")
def dados():
    # Aqui você pode adicionar a lógica para ler os dados da planilha em JSON
    data = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
