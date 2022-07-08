from flask import Flask, redirect, request
import send_mail

app = Flask(__name__)


@app.route("/form", methods=["POST", "GET"])
def form_email():
    if request.method == "POST":
        nome = request.form["nome"]
        e_mail = request.form["email"]
        assunto = request.form["assunto"]
        mensagem = request.form["mensagem"]
        to_mail = request.args.get("mail")

        send_mail.send_email(to_mail, nome, e_mail, assunto, mensagem)

        return f"""<h1>Enviado</h1>"""
    else:
        return "<h1>O que faz por aqui forasteiro?</h1>"


if __name__ == "__main__":
    app.run(debug=False)
