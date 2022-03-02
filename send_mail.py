import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import settings

def send_email(to_email, nome, sobrenome, e_mail, assunto, mensagem): 

    body_email = f"""
    <p><b>Nome:</b> {nome} {sobrenome}</p>
    <p><b>E-mail:</b> {e_mail}</p>
    <p>Assunto: {assunto}</p>
    <p>Mensagem:</p>
    <p>{mensagem}</p>
    """

    mensagem = MIMEMultipart()
    mensagem['From'] = settings.credencias["login"]
    mensagem['To'] = to_email
    mensagem['Subject'] = assunto
    mensagem.attach(MIMEText(body_email, "html"))


    server = smtplib.SMTP(settings.server["smtp"], settings.server["port"])
    server.starttls()
    server.login(mensagem['From'], settings.credecias["password"])
    server.sendmail(mensagem['From'], [mensagem['To']], mensagem.as_string().encode('utf-8'))
    server.quit()