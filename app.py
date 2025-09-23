import os

restaurantes = [{'nome': 'praça', 'categoria': 'japonesa', 'ativo': False},
                {'nome': 'pizza suprema', 'categoria': 'pizza', 'ativo': True}]


def exibir_nome_do_programa():
    print('Sabor Express \n')


def exibir_opcoes():
    print('1.Cadastrar restaurante')
    print('2.Listar restaurante')
    print('3.Ativar restaurante')
    print('4.Sair \n')


def finalizar_app():
    exibir_subtitulo('Encerrando o programa\n')


def voltar_ao_menu_principal():
    input('Digite uma tecla para voltar ao menu principal')
    main()


def opcao_invalida():
    print('opção inválida!\n')
    voltar_ao_menu_principal()


def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()


def cadastrar_novo_restaurante():
    exibir_subtitulo('cadastro de novos restaurantes')
    nome_do_restaurante = input('digite o nome do restaurante:')
    categoria = input(
        f'digite o nome da categoria do restaurante {nome_do_restaurante}:')
    dados_do_restaurante = {'nome': nome_do_restaurante,
                            'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'cadastrado .{nome_do_restaurante} com sucesso!')
    voltar_ao_menu_principal()


def listar_restaurante():
    exibir_subtitulo('Listando restaurantes \n')

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
        print(f' - {nome_restaurante} | {categoria} | {ativo}')
    voltar_ao_menu_principal()


def ativar_restaurante():
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input(
        'digite o nome do restaurante que deseja alterar o estado:')

    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurantes['nome']:
            restaurante_encontrado = True


def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção:'))
        print('Você escolheu a opção', opcao_escolhida)
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurante()
        elif opcao_escolhida == 3:
            ativar_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()
