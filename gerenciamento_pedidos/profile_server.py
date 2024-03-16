from flask import Flask, request, jsonify 
import requests

app = Flask(__name__)

user_service_url = "[http://](http://user-service:5001/)localhost:5001"

@app.route('/perfil/<nome_usuario>', method=['GET']) 
def obter_perfil_usuario(nome_usuario):
    dados_usuario = {"nome_usuario": nome_usuario} 
    resposta = requests.post(f"{user_service_url}/registerar", json=dados_usuario)

    if resposta.status_code == 200:
        return jsonify({"Mensagem": "Perfil obtido com sucesso", "dados_usuario": dados_usuario})
    else:
        return jsonify({"Mensagem": "Falha ao obter perfil"})
    
if __name__ == "main":
    app.run(host='0.0.0.0', port=5001)