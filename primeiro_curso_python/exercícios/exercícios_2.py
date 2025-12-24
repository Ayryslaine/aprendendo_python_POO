"""2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

Criança: 0 a 12 anos;
Adolescente: 13 a 18 anos;
Adulto: acima de 18 anos."""

idade = int(input("Digite sua idade: "))

def classificar():
    if 0 <= idade <= 12:
        print(f"Você tem {idade} anos, logo você é CRIANÇA")
    elif 12 < idade < 18:
        print(f"Você tem {idade} anos, logo você é ADOLESCENTE")
    elif idade >= 18:
        print(f"Você tem {idade} anos, logo você é ADULTO")
    else:
        print("Valor inválido")

classificar()