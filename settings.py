import os

env = os.environ

credencias = {
	'login': env["LOGIN_EMAIL"],
	'password': env["PASSWORD_EMAIL"],
}

server = {
	'smtp' : 'smtp.gmail.com',
	'port' : '587',
}
