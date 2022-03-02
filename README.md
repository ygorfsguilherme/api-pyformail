### O que pyformail?
É uma api para enviar formulário de contato para um email.

### Tecnologia utilizado
Na construção da aplicação foi utilizado o python como linguagem de programação,
framework flask para implementar a comunicação.

### Como utilizar?

Existe duas formas, utilizando API pronta e configurada no servidor do heroku ou você mesmo fazendo deploy da aplicação.

#### Método 1
Necessário criar um formulário com a seguinte estrutura básica.
<br>
**OBS: E preciso que o campos name sejam exatamente da forma descrita.**

```html
<form action="http://api-pyformail.herokuapp.com/formulario" methods="post">
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

#### Método 2

