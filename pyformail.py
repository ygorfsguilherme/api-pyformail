from flask import Flask, redirect, request
from flask_cors import CORS, cross_origin
import send_mail

app = Flask(__name__)

CORS(app)


@cross_origin
@app.route("/form", methods=["POST", "GET"])
def form_email():
    if request.method == "POST":
        nome_email = request.form["nome"]
        assunto = request.form["assunto"]
        e_mail = request.form["email"]
        mensagem = request.form["mensagem"]

        to_mail = request.args.get("mail")

        send_mail.send_email(to_mail, nome_email, e_mail, assunto, mensagem)

        return f"<h1>{nome_email, to_mail}</h1>"
    return f"<h1>Erro</h1>"


if __name__ == "__main__":
    app.run(debug=True)
