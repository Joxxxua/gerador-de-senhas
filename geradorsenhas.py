import random
caracteres = "1234567890abcdefghijklnmopqstwxyzABCDEFGHIJKLNMOPQSTWXYZ!@#$%&¨*"
quant_senhas = int(input("Qual a quantidade de senhas que você deseja criar? "))
comprimento = int(input("Quantos números você quer que sua senha tenha? "))
for pwd in range(quant_senhas):
    senha = ""
    for c in range(comprimento):
        senha += random.choice(caracteres)
    print(senha)
