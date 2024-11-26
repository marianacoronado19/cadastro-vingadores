from ast import Attribute
from model.heroi import Heroi
import os

class Interface:

    # herois_convocados = []
    convocado = False
 
    def imprimir_titulo_app():
        print('''
▒█▀▀█ █▀▀█ █▀▀▄ █▀▀█ █▀▀ ▀▀█▀▀ █▀▀█ █▀▀█ 　 █▀▀▄ █▀▀ 　 ▒█░▒█ █▀▀ █▀▀█ █▀▀█ ░▀░ █▀▀
▒█░░░ █▄▄█ █░░█ █▄▄█ ▀▀█ ░░█░░ █▄▄▀ █░░█ 　 █░░█ █▀▀ 　 ▒█▀▀█ █▀▀ █▄▄▀ █░░█ ▀█▀ ▀▀█
▒█▄▄█ ▀░░▀ ▀▀▀░ ▀░░▀ ▀▀▀ ░░▀░░ ▀░▀▀ ▀▀▀▀ 　 ▀▀▀░ ▀▀▀ 　 ▒█░▒█ ▀▀▀ ▀░▀▀ ▀▀▀▀ ▀▀▀ ▀▀▀
            ''')
 
    @staticmethod
    def apresentar_menu_principal():
        os.system('cls')
        Interface.imprimir_titulo_app()
        print('''        
+--------------------------------------+
|Menu Principal                        |
|1. Cadastrar um novo herói            |
|2. Listar todos os carros cadastrados |
|3. Formar equipe de Heróis            |
|4. Convocar heróis                    |
|5. Aplicar tornozeleira               |
|6. Aplicar GPS                        |
|7. Emitir mandado de prisão           |
|8. Informações do herói               |
|0. Sair                               |
+--------------------------------------+      
              ''')
        Interface.ler_opcao_usuario()

    @staticmethod
    def imprime_titulo_tela(titulo):
        os.system('cls')
        Interface.imprimir_titulo_app
        print(f'{str(titulo).upper()}')
        print('*' * 25)
        print()

    def cadastrar_heroi():
        Interface.imprime_titulo_tela('Cadastrando novo herói')
        nome = input('Nome de herói: ')
        real = input('Nome real: ')
        categoria = input('Categoria (humano, meta-humano, alienígena, deus): ')
        poderes = input('Poderes: ')
        poder_principal = input('Poder principal do herói: ')
        fraquezas = input('Fraquezas do herói: ')
        forca = int(input('Nível de força (números inteiros): '))
        heroi = Heroi(nome, real, categoria, poderes, poder_principal, fraquezas, forca)
 
        print(f'O Herói foi cadastrado: \n{heroi}')

    def formar_time():
        '''Uma função que seleciona vários heróis e forma um time, mostrando informações dos mesmos'''
        os.system('cls')
        Interface.imprime_titulo_tela('Formando um time!')
        Heroi.lista_resumo()
        if Heroi.lista_de_herois:
            try:
                id_escolhido = input('Escolha os IDs dos Heróis desejados (separando por vírgula ou espaço): ')
                # Separa os IDs inseridos
                id_escolhido = [id.strip() for id in id_escolhido.replace(',', ' ').split()]

                time = []

                for id_str in id_escolhido: # Verifica cada ID inserido
                    try:
                        id_escolhido = int(id_str) # Encontra o herói pelo ID
                        heroi_encontrado = next((h for h in Heroi.lista_de_herois if h.id == id_escolhido), None)

                        if heroi_encontrado:
                            time.append(heroi_encontrado)
                        else:
                            print(f'Herói com ID {id_escolhido} não encontrado.')

                    except ValueError:
                        print(f'O ID {id_str} é inválido. Por favor, insira números válidos!')

                if time:
                    Interface.imprime_titulo_tela('Equipe formada com sucesso!')
                    Heroi.imprimir_cabecalho()
                    for heroi in time:
                        print(heroi)
                else:
                    print('Nenhum herói foi selecionado ou todos os IDs fornecidos foram inválidos.')

            except ValueError:
                print("Por favor, insira um número válido para o ID.")
                Interface.formar_time()

    def convocar_heroi():
        '''Uma função que filtra o nome do heroi e depois o convoca'''
        os.system('cls')
        Interface.imprime_titulo_tela('Convocando Herói!')
        if Heroi.lista_de_herois: 
            nome_escolha = input('Digite o nome do herói que deseja convocar: ').strip().lower()

            heroi_encontrado = next((h for h in Heroi.lista_de_herois if nome_escolha.strip().lower() in h.nome.strip().lower()), None)

            if heroi_encontrado:
                heroi_encontrado.convocado = True
                print(f'O herói {heroi_encontrado.nome} foi convocado com sucesso!')
            else:
                print(f'Nenhum herói encontrado com o nome "{nome_escolha}". Tente novamente.')
        else:
            print('Nenhum herói cadastrado até o momento.')

    def aplicar_tornozeleira():
        os.system('cls')
        Interface.imprime_titulo_tela('Aplicação de Tornozeleira.')
        nome_escolha = input('Digite o nome do herói para aplicar a tornozeleira: ').strip()
        heroi_encontrado = next((h for h in Heroi.lista_de_herois if nome_escolha.lower() in h.nome.lower()), None)

        if heroi_encontrado is None:
            print("Nenhum herói encontrado com o nome informado.")
            return
        if heroi_encontrado.convocado and heroi_encontrado.forca <= 500:
            print(f"Uma tornozeleira foi aplicada ao herói {heroi_encontrado.nome}.")
        elif heroi_encontrado.convocado and heroi_encontrado.forca > 500:
            print(f"Não é possível aplicar uma tornozeleira a este herói por conta de seu nível de força ({heroi_encontrado.forca}).")
        else:
            print("O herói precisa ser convocado primeiro.")

        # id_heroi = input('Digite o nome do herói para aplicar a tornozeleira: ').strip().lower()

        # heroi_encontrado = next((h for h in Heroi.lista_de_herois if str(h.id) == id_heroi), None)

        # if heroi_encontrado:
        #     if heroi_encontrado.convocado:
        #         print(f'A tornozeleira foi aplicada ao herói {heroi_encontrado.nome}.')
        #     else:
        #         print(f'O herói {heroi_encontrado.nome} não foi convocado. Não é possível aplicar a tornozeleira.')
        # else:
        #     print(f'Nenhum herói encontrado com o nome {id_heroi}.')

    def ler_opcao_usuario():
        '''Uma função que lê a opção do usuário na tela inicial'''
        try:
            opcao = int(input('O que deseja fazer?: '))
            if opcao == 1:
                Interface.cadastrar_heroi()
            elif opcao == 2:
                Interface.imprime_titulo_tela('Listando Vingadores')
                Heroi.lista_tornozeleira()
            elif opcao == 3:
                Interface.imprime_titulo_tela('Formando um time!')
                print('Escolha Heróis para formar um time: ')
                Interface.formar_time()
            elif opcao == 4:
                Interface.imprime_titulo_tela('Convocando Herói!')
                Interface.convocar_heroi()
            elif opcao == 5:
                Interface.imprime_titulo_tela('Aplicando Tornozeleira!')
                Interface.aplicar_tornozeleira()
            elif opcao == 0:
                print('Encerrando programa')
                exit()
            else:
                print('\nEsta opção não é válida.')
                print('Volte e insira um valor válido:')
 
        except ValueError:
            print('Você deve digitar um número inteiro.')

        Interface.voltar_ao_menu_principal()
 
    @staticmethod
    def voltar_ao_menu_principal():
        '''Volta ao menu principal'''
        print()
        input('Precione ENTER para voltar ao menu')
        os.system('cls')
        Interface.apresentar_menu_principal()