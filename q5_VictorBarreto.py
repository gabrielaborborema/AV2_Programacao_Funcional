import os
from flask import Flask, request, render_template
app = Flask(__name__, template_folder='templates_folder')

arquivo_usuarios = "usuarios_flask.txt"

cadastrar_usuario = lambda arquivo, login, senha: open(arquivo, 'a').writelines(f"{login},{senha}\n") or "USUARIO CADASTRADO!!"

fazer_login = lambda user, login, senha: "SUCESSO" if (login, senha) in user else "FRACASSO"

ler_arquivo_usuarios = lambda arquivo : [tuple(line.strip().split(',')) for line in open(arquivo, 'r')] if os.path.exists(arquivo) else open(arquivo, 'w+')

reqresp_login = lambda : fazer_login (ler_arquivo_usuarios(arquivo_usuarios), f'{request.form["username"]}', f'{request.form["password"]}') if request.method == 'POST' else render_template('login.html')

reqresp_register = lambda : cadastrar_usuario (arquivo_usuarios, f'{request.form["username"]}', f'{request.form["password"]}') if request.method == 'POST' else render_template('register.html')

app.add_url_rule('/login/', 'login', reqresp_login, methods=['GET', 'POST'])
app.add_url_rule('/register/', 'register', reqresp_register, methods=['GET', 'POST'])
app.run(host='0.0.0.0', port=8080)