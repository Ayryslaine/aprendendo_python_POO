"""1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura 
if else para determinar se o número é par ou ímpar."""

escolher = int(input("Escolha um número: "))

def par_impar():
    if escolher % 2 == 0:
        print(f"O número {escolher} é par")
    else:
        print(f"O número {escolher} é ímpar")

par_impar()
