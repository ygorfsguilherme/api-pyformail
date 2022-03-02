### O que pyformail?
É uma api para enviar formulário de contato para um email.

### Tecnologia utilizado
Na construção da aplicação foi utilizado o python como linguagem de programação,
flask com framework para implementar a comunicação do formulario juntamento com a biblioteca smtp, para o envio de email.

### Como utilizar?

Existe duas formas, utilizando API pronta e configurada no servidor do heroku ou você mesmo fazendo deploy da aplicação.

#### Método 1 sem deploy
Necessário criar um formulário com a seguinte estrutura básica.
<br>
**OBS: E preciso que o campos name sejam exatamente da forma descrita.** <br>
*Em action no formulario substitua o SEU@EMAIL.COM por seu email e preciso colocar o e-mail que ira receber as infomações enviada.

```html
<form action="http://api-pyformail.herokuapp.com/form?mail=SEU@EMAIL.COM" methods="post">
  <label>Nome:</label>
  <input type="text" name="nome">
						
  <label>Sobrenome:</label>
  <input type="text" name="sobrenome">
						
  <label>E-mail:</label>
  <input type="email" name="email">
						
  <label>Assunto:</label>
  <input type="text" name="assunto">
						
  <label>Mensagem:</label>
  <textarea type="texto" name="mensagem"></textarea>

  <button type="submit">enviar</button>
</form>
```

### Método 2 com deploy
Consiste em utiliza de forma independende, utilizando um servidor para aplicação.
No servido e preciso definir 2 variaveis de ambiente

1 - Variaveis de ambiemte:<br>
*Será preciso utilizar um segundo email alternativo pois ele será o responsavel para envia a mensagem para seu email primario.

LOGIN_EMAIL=OUTRO@EMAIL <br>
PASSWORD_EMAIL=SENHA_DO_OUTRO_EMAIL

2 - Instalando dependecias do python:

```bash
pip3 install -r requeriments.txt
```
3 - Rodando a aplicação:
```bash
gunicorn pyformail:app
```



AVISO: É preciso que você entenda como funciona o servidor que ira roda a aplicação, sera preciso fazer pequenas alteração na aplicaçao se nescessario.<br>
DICA: Utilize o heroku como servidor, a api ja e pre-cofigurado para ele, precisando apenas adicionar as variaveis de ambiente.
