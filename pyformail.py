from flask import Flask, redirect, request
import send_mail
app = Flask(__name__)

@app.route('/formulario', methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      nome = request.form['nome']
      sobrenome = request.form['sobrenome']
      e_mail = request.form['email']
      assunto = request.form['assunto']
      mensagem = request.form['mensagem']

      send_mail.send_email(nome, sobrenome, e_mail, assunto, mensagem)

      return redirect('https://www.google.com/')
   else:
      return "<h1>O que faz por aqui forasteiro?</h1>"

if __name__ == '__main__':
   app.run(debug = False)