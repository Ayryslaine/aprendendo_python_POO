import os 

restaurantes = [{'nome': 'Bobs', 'categoria': 'Fast-food', 'ativo':False},
{"nome":"Subway","categoria":"Fast-food", "ativo":True},
{"nome":"Jhons Grill", "categoria":"italiano", "ativo":False}]

def exibir_nome_programa():
    print("""𝕾𝖎𝖘𝖙𝖊𝖒𝖆""")

def mostrar_opcoes():
      print("""\n1. Cadastrar restaurante
2. Listar restaurantes
3. Altenar estado do restaurante
4. Sair do sistema
      """)

def opcao_invalida():
     print("\nOpção inválida!\n")
     voltar_ao_menu()

def cadastrar_restaurante():
     mostrar_subtitulo("""🅒🅐🅓🅐🅢🅣🅡🅐🅡 🅝🅞🅥🅞🅢 🅡🅔🅢🅣🅐🅤🅡🅐🅝🅣🅔🅢""")
     adicionar_restaurante = input("\nQual restaurante você gostaria de cadastrar?: ")
     categoria_restaurante = input(f"\nQual a categoria do restaurante {adicionar_restaurante}?: ")
     dados_restaurantes = {'nome': adicionar_restaurante, 'categoria': categoria_restaurante, 'ativo':False}
     restaurantes.append(dados_restaurantes)
     print(f'\nO restaurante {adicionar_restaurante} foi cadastrado com sucesso!\n')
     voltar_ao_menu()

def listar_restaurantes():
     mostrar_subtitulo("""🅛🅘🅢🅣🅐🅡 🅡🅔🅢🅣🅐🅤🅡🅐🅝🅣🅔🅢""")
     for i in restaurantes:
          nome_restaurante = i["nome"]
          categoria_restaurante = i["categoria"]
          situacao_restaurante = "Ativado" if i["ativo"] else "Desativado" 
          print(f"-{nome_restaurante} | {categoria_restaurante} | {situacao_restaurante}")
     voltar_ao_menu()

def alternar_estado_restaurante():
     mostrar_subtitulo("🅐🅛🅣🅔🅡🅝🅐🅝🅓🅞 🅔🅢🅣🅐🅓🅞 🅡🅔🅢🅣🅐🅤🅡🅐🅝🅣🅔")
     nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
     restaurante_encontrado = False
     for i in restaurantes:
        if nome_restaurante == i['nome']:
            restaurante_encontrado = True
            i['ativo'] = not i['ativo']
            mensagem = f'\nO restaurante {nome_restaurante} foi ativado com sucesso' if i['ativo'] else f'\nO restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    
     if not restaurante_encontrado:
      print('O restaurante não foi encontrado.')
     voltar_ao_menu()

def voltar_ao_menu():
     input("\nDigite qualquer tecla para voltar ao menu: ")
     main()

def mostrar_subtitulo(texto):
     os.system("cls")
     print(texto)
     print()

def escolher_opcoes():
      try:
            escolha = int(input("Escolha uma opção: "))

            if escolha == 1:
                  cadastrar_restaurante()
            elif escolha == 2:
                  listar_restaurantes()
            elif escolha == 3:
                  alternar_estado_restaurante()
            elif escolha == 4:
                  fechar_app() 
            else:
                  opcao_invalida()
      except:
           opcao_invalida()

def fechar_app():
    mostrar_subtitulo("""🅕🅔🅒🅗🅐🅝🅓🅞 🅐🅟🅛🅘🅒🅐🅣🅘🅥🅞\n""")

def main():
    os.system("cls") #win
    #os.system("clear") #mac
    exibir_nome_programa()
    mostrar_opcoes()
    escolher_opcoes()

if __name__ == "__main__":
     main()


