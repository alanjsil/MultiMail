__AUTHOR__	= "Getsu"
__DATE__	= "28/05/2017"
__VERSION__	= "1.0"
__GITHUB__	= "https://github.com/alanjsil/MultiMail"
__LICENÇA__ = "GNU General Public License v3.0"

import banner
import os
import smtplib
import time

def limpa():
    os.system('cls' if os.name == 'nt' else 'clear')

def interromper():
    RED = '\33[91m'
    YELLOW = '\33[93m'

    limpa()
    banner.banners.banner2()
    print(RED+"[!]"+YELLOW+" VOCE CANCELOU!!!")
    exit()

def gmail():
    RED = '\33[91m'
    YELLOW = '\33[93m'
    END = '\033[0m'

    print("USANDO GMAIL")
    # Entrada de email
    email = input("Seu E-mail: ")
    while "@gmail.com" not in email:
        print("E-mail invalido")
        print("Voce escolheu usar " + RED + "GMAIL" + END + ".")
        print("(reiniciando em 3 segundos)")
        time.sleep(3)
        limpa()
        banner.banners.banner1()
        print(YELLOW + "USANDO GMAIL" + END)
        email = input("Seu E-mail: ")
        limpa()
        banner.banners.banner1()

    # Entrada de senha
    nome = (email[:len(email) - 10])
    senha = input("Senha de " + nome + ": ")
    limpa()
    try:
        banner.banners.banner2()
        print(YELLOW + """
                TENTANDO LOGIN...
                POR FAVOR AGUARDE, ESTE PROCESSO PODE DEMORARAR DEPENDENDO DA SUA CONEXÃO
                 """ + END)
        print("CTRL+C para sair")
        smtp = smtplib.SMTP("smtp.gmail.com", 587)
        smtp.starttls()
        # Logando
        smtp.login(email, senha)
    except Exception as erro:
        limpa()
        banner.banners.banner2()
        print("Erro na senha/e-mail")
        errou = input("Tentar novamente? S/N\n>>> ")
        if errou == "S" or errou == "s":
            gmail()
        else:
            interromper()
    # email alvo
    limpa()
    banner.banners.banner1()
    print("""
    LOGADO COM SUCESSO
    CONTA {0}{1}{2}
    """.format(RED, nome, END))
    para = input("E-mail Alvo: ")
    destino = para.split()

    if "@" not in para:
        print("Faltando Parametros.\n Insira um e-mail valido")
        exit()

    x = 0
    msg = input("Mensagem:\n")
    vezes = int(input("Quantidade Vezes: "))
    print('\n')
    limpa()
    banner.banners.banner2()
    print(RED + "INICIANDO O ENVIO DE E-MAILS" + END)
    while x < vezes:
        x += 1
        smtp.sendmail(email, destino, msg)
        print('Enviando o %d ° e-mail.' % (x))
    try:
        banner.banners.conteudo(email, destino, msg)
    except:
        banner.banners.banner2()
        print('Houve um erro tente novamente')
    exit()

def outlook():
    RED = '\33[91m'
    YELLOW = '\33[93m'
    END = '\033[0m'

    print("USANDO OUTLOOK")
    # Entrada de email
    email = input("Seu E-mail: ")
    while "@outlook.com" not in email:
        print("E-mail invalido")
        print("Voce escolheu usar " + RED + "OUTLOOK" + END + ".")
        print("(reiniciando em 3 segundos)")
        time.sleep(3)
        limpa()
        banner.banners.banner1()
        print(YELLOW + "USANDO OUTLOOK" + END)
        email = input("Seu E-mail: ")
        limpa()
        banner.banners.banner1()

    # Entrada de senha
    nome = (email[:len(email) - 12])
    senha = input("Senha de " + nome + ": ")
    limpa()
    try:
        banner.banners.banner2()
        print(YELLOW + """
                TENTANDO LOGIN...
                POR FAVOR AGUARDE, ESTE PROCESSO PODE DEMORARAR DEPENDENDO DA SUA CONEXÃO
                 """ + END)
        print("CTRL+C para sair")
        smtp = smtplib.SMTP("smtp.live.com", 587)
        smtp.starttls()
        # Logando
        smtp.login(email, senha)
    except Exception as erro:
        limpa()
        banner.banners.banner2()
        print("Erro na senha/e-mail")
        errou = input("Tentar novamente? S/N\n>>> ")
        if errou == "S" or errou == "s":
            outlook()
        else:
            interromper()
    # email alvo
    limpa()
    banner.banners.banner1()
    print("""
    LOGADO COM SUCESSO
    CONTA {0}{1}{2}
    """.format(RED, nome, END))
    para = input("E-mail Alvo: ")
    destino = para.split()

    if "@" not in para:
        print("Faltando Parametros.\n Insira um e-mail valido")
        exit()

    x = 0
    msg = input("Mensagem:\n")
    vezes = int(input("Quantidade Vezes: "))
    print('\n')
    limpa()
    banner.banners.banner2()
    print(RED + "INICIANDO O ENVIO DE E-MAILS" + END)
    while x < vezes:
        x += 1
        smtp.sendmail(email, destino, msg)
        print('Enviando o %d ° e-mail.' % (x))
    try:
        banner.banners.conteudo(email, destino, msg)
    except:
        banner.banners.banner2()
        print('Houve um erro tente novamente')
    exit()
