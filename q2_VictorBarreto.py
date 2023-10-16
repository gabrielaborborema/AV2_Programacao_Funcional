import os

arquivo_usuarios = "usuarios.txt"

cadastrar_usuario = lambda arquivo, login, senha: open(arquivo, 'a').writelines(f"{login},{senha}\n")

fazer_login = lambda user, login, senha: "\nSUCESSO\n" if (login, senha) in user else "\nFRACASSO\n"

ler_arquivo_usuarios = lambda arquivo: [tuple(line.strip().split(',')) for line in open(arquivo, 'r')] if os.path.exists(arquivo) else open(arquivo, 'w+')

menu = lambda: input("1 - Cadastrar Usuario\n2 - Fazer Login\n3 - Sair\nEscolha uma opcao: ")

programa = lambda opcao: (
    lambda: print("\nUSUÁRIO CADASTRADO\n") if cadastrar_usuario(arquivo_usuarios, input("Digite o login a ser cadastrado: "), input("Digite a senha a ser cadastrado: ")) is None else print("\nERROR\n"),
    lambda: print(fazer_login(ler_arquivo_usuarios(arquivo_usuarios), input("Digite o login: "), input("Digite a senha: "))),
    lambda: 1
)[int(opcao) - 1]

recursivo = lambda: recursivo() if programa(menu())() is None else None

recursivo()
