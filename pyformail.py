from flask import Flask, jsonify, redirect, request
from flask_cors import CORS, cross_origin
import send_mail


app = Flask(__name__)
CORS(app)


@cross_origin
@app.route("/form", methods=["POST", "GET", "OPTIONS"])
def form_email():
    if request.method == "POST":
        nome = request.get_json()["nome"]
        assunto = request.get_json()["assunto"]
        e_mail = request.get_json()["email"]
        mensagem = request.get_json()["mensagem"]
        to_mail = request.args.get("mail")

        send_mail.send_email(to_mail, nome, e_mail, assunto, mensagem)

        return jsonify("200")
    return jsonify("404")


if __name__ == "__main__":
    app.run(debug=True)
