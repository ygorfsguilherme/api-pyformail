import os

env = os.environ

credencias = {
    "user": env["LOGIN_EMAIL"],
    "password": env["PASSWORD_EMAIL"],
}


server = {
    "smtp": "smtp.zoho.com",
    "port": "587",
}
