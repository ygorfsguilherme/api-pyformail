import smtplib
import email.message
import settings

def send_email(nome, sobrenome, e_mail, assunto, mensagem): 
    From_EMAIL = settings.FROM_EMAIL
    To_EMAIL = settings.TO_EMAIL
    password =  settings.PASS_EMAIL

    body_email = f"""
        <p><strong>Nome: {nome} {sobrenome}</strong></p>
        <p><strong>E-mail:</strong> {e_mail}</p>
        <p>Assunto: {assunto}</p>
        <p>Mensagem:</p>
        <p>{mensagem}</p>
        """

    msg = email.message.Message()
    msg['Subject'] = assunto
    msg['From'] = From_EMAIL
    msg['To'] = To_EMAIL
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(body_email)

    sm = smtplib.SMTP('smtp.gmail.com: 587')
    sm.starttls()
    sm.login(msg['From'], password)
    sm.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))