import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import settings


def send_email(to_mail, nome, e_mail, assunto, mensagem):

    body_email = f"""
    <p><b>Nome:</b> {nome}</p>
    <p><b>E-mail:</b> {e_mail}</p>
    <p>{mensagem}</p>
    """

    mensagem = MIMEMultipart()
    mensagem["From"] = settings.credencias["user"]
    mensagem["To"] = to_mail
    mensagem["Subject"] = assunto
    mensagem.attach(MIMEText(body_email, "html"))

    server = smtplib.SMTP(settings.server["smtp"], settings.server["port"])
    server.starttls()
    server.login(settings.credencias["user"], settings.credencias["password"])
    server.sendmail(
        mensagem["From"], mensagem["To"], mensagem.as_string().encode("utf-8")
    )
    server.quit()
