from segundo_curso_POO.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
restaurante_japones = Restaurante('Japa', 'Japonesa')
restaurante_praca.receber_avaliacao('Emy', 2)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()