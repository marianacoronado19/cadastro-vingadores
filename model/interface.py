from ast import Attribute
from model.heroi import Heroi
import os

class Interface:

    convocado = False
 
    def imprimir_titulo_app():
        '''Uma função que imprime o título do app'''
        print('''

                                ░█████╗░░█████╗░██████╗░░█████╗░░██████╗████████╗██████╗░░█████╗░  ██████╗░░█████╗░░██████╗
                                ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔══██╗  ██╔══██╗██╔══██╗██╔════╝
                                ██║░░╚═╝███████║██║░░██║███████║╚█████╗░░░░██║░░░██████╔╝██║░░██║  ██║░░██║██║░░██║╚█████╗░
                                ██║░░██╗██╔══██║██║░░██║██╔══██║░╚═══██╗░░░██║░░░██╔══██╗██║░░██║  ██║░░██║██║░░██║░╚═══██╗
                                ╚█████╔╝██║░░██║██████╔╝██║░░██║██████╔╝░░░██║░░░██║░░██║╚█████╔╝  ██████╔╝╚█████╔╝██████╔╝
                                ░╚════╝░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░  ╚═════╝░░╚════╝░╚═════╝░

                                        ██╗░░░██╗██╗███╗░░██╗░██████╗░░█████╗░██████╗░░█████╗░██████╗░███████╗░██████╗
                                        ██║░░░██║██║████╗░██║██╔════╝░██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝
                                        ╚██╗░██╔╝██║██╔██╗██║██║░░██╗░███████║██║░░██║██║░░██║██████╔╝█████╗░░╚█████╗░
                                        ░╚████╔╝░██║██║╚████║██║░░╚██╗██╔══██║██║░░██║██║░░██║██╔══██╗██╔══╝░░░╚═══██╗
                                        ░░╚██╔╝░░██║██║░╚███║╚██████╔╝██║░░██║██████╔╝╚█████╔╝██║░░██║███████╗██████╔╝
                                        ░░░╚═╝░░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░
''')
 
    @staticmethod
    def apresentar_menu_principal():
        '''Uma função que apresenta o menu principal e as funções na qual o usuário pode escolher'''
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
        '''Função com um pequeno título para cada uma das "guias" escolhidas'''
        os.system('cls')
        Interface.imprimir_titulo_app
        print(f'{str(titulo).upper()}')
        print('*' * 25)
        print()

    @staticmethod
    def cadastrar_heroi():
        '''Função que recolhe as informações e atributos de cada herói'''
        Interface.imprime_titulo_tela('Cadastrando novo herói')
        nome = input('Nome de herói: ')
        real = input('Nome real: ')

        while True: # Define os possíveis valores de categoria
            try:
                categoria = input('Categoria (humano, meta-humano, androide, alienígena, deidade): ')
                if categoria.lower() not in ['humano', 'meta-humano', 'alienigena', 'deidade', 'androide']:
                    print('\nEsta categoria não é válida, tente algo como: Humano, Meta-Humano, Androide, Alienigena ou Deidade')
                else:
                    break
            except AttributeError:
                print("Por favor, insira um valor válido.")

        poderes = input('Poderes: ')
        if len(poderes) > 100:
            print('Os poderes não podem exceder 100 caracteres. Tente novamente.')
            return
        
        poder_principal = input('Poder principal do herói: ')
        fraquezas = input('Fraquezas do herói: ')

        while True:
            try:
                forca = int(input('Nível de força (0 - 10000): '))
                if forca > 10000:
                    print("O limite de força é 10000. Tente novamente.")
                else:
                    break
            except ValueError:
                print("Por favor, insira um número válido para o nível de força.")

        heroi = Heroi(nome, real, categoria, poderes, poder_principal, fraquezas, forca)
        print(f'O Herói foi cadastrado: \n{heroi}')

    @staticmethod
    def formar_time():
        '''Uma função que seleciona vários heróis pelo nome e forma um time, mostrando informações dos mesmos'''
        os.system('cls')
        Interface.imprime_titulo_tela('Formando um time!')
        Heroi.lista_resumo()
    
        if Heroi.lista_de_herois:
            try:
                nome_escolha = input('Digite o nome dos heróis para formar uma equipe (separados por vírgula ou espaço): ').strip().lower()
                nomes = [nome.strip() for nome in nome_escolha.replace(',', ' ').split()]

                time = []  # Lista para armazenar os heróis selecionados

                for nome_str in nomes:
                    herois_encontrados = next((h for h in Heroi.lista_de_herois if nome_str in h.nome.lower() or nome_str in h.real.lower()), None)
                    if herois_encontrados:
                        time.append(herois_encontrados)
                    else:
                        print(f'Herói com nome "{nome_str}" não encontrado.')

                    if time:
                        Interface.imprime_titulo_tela('Equipe formada com sucesso!')
                        Heroi.imprimir_cabecalho()
                        for heroi in time:
                            print(heroi)
                    else:
                        print('Nenhum herói foi selecionado ou todos os nomes fornecidos foram inválidos.')
            except ValueError:
                print("Houve um erro na entrada. Por favor, tente novamente.")    

    @staticmethod
    def convocar_heroi():
        '''Uma função que filtra o nome do heroi e depois o convoca'''
        os.system('cls')
        Interface.imprime_titulo_tela('Convocando Herói!')
        if Heroi.lista_de_herois: 
            nome_escolha = input('Digite o nome do herói que deseja convocar: ').strip().lower()

            heroi_encontrado = next((h for h in Heroi.lista_de_herois if nome_escolha.strip().lower() in h.nome.strip().lower() or nome_escolha.strip().lower() in h.real.strip().lower()), None)

            if heroi_encontrado:
                heroi_encontrado.convocado = True
                print(f'O herói {heroi_encontrado.nome} foi convocado com sucesso!')
            else:
                print(f'Nenhum herói encontrado com o nome "{nome_escolha}". Tente novamente.')
        else:
            print('Nenhum herói cadastrado até o momento.')

    @staticmethod
    def aplicar_tornozeleira():
        '''Uma função que define se deve ser aplicada uma tornozeleira a determinado herói, faz a filtração dos nomes e define o valor da variavel como True (não é possível aplicar tornozeleira ao Thor, Hulk ou heróis com um dererminado nível de força...)'''
        os.system('cls')
        Interface.imprime_titulo_tela('Aplicação de Tornozeleira.')
        
        if not Heroi.lista_de_herois:
            print("Não há heróis cadastrados no sistema.")
            return
        
        nome_escolha = input('Digite o nome do herói para aplicar a tornozeleira: ').strip()
        heroi_encontrado = next((h for h in Heroi.lista_de_herois if nome_escolha.strip().lower() in h.nome.strip().lower() or nome_escolha.strip().lower() in h.real.strip().lower()), None)

        heroi_encontrado.forca = int(heroi_encontrado.forca)

        if heroi_encontrado is None:
            print("Nenhum herói encontrado com o nome informado.")
            return
        if not heroi_encontrado.convocado:
            print(f"O herói {heroi_encontrado.nome} precisa ser convocado primeiro.")
            return
        
        if not heroi_encontrado.status_tornozeleira: # se já não estiver com tornozeleira
            if heroi_encontrado.nome.lower() == 'thor':
                print('"O Deus do Trovão não se submeterá a tal dispositivo mundano!" - Não foi possível aplicar uma tornozeleira a Thor')
            elif heroi_encontrado.nome.lower() == 'hulk':
                print('"ARGH! HULK ESMAGA ESSE TROÇO!!!" - Não foi possível aplicar uma tornozeleira a Hulk')
            else:
                if heroi_encontrado.forca < 5000:
                    heroi_encontrado.status_tornozeleira = True
                    print(f"Uma tornozeleira foi aplicada ao herói {heroi_encontrado.nome}.")
                else:
                    print(f"Não é possível aplicar uma tornozeleira a {heroi_encontrado.nome} devido ao seu alto nível de força ({heroi_encontrado.forca}).")
        else: 
                print(f'O herói {heroi_encontrado.nome} já está usando uma tornozeleira.')   

    @staticmethod
    def aplicar_gps():
        '''Uma função que define se deve ser aplicado um GPS a determinado herói, faz a filtração dos nomes e define o valor da variavel como True'''
        os.system('cls')
        Interface.imprime_titulo_tela('Aplicação de Localizador.')
        
        if not Heroi.lista_de_herois:
            print("Não há heróis cadastrados no sistema.")
            return
        
        nome_escolha = input('Digite o nome do herói para aplicar o GPS: ').strip()
        heroi_encontrado = next((h for h in Heroi.lista_de_herois if nome_escolha.strip().lower() in h.nome.strip().lower() or nome_escolha.strip().lower() in h.real.strip().lower()), None)
        if heroi_encontrado is None:
            print("Nenhum herói encontrado com o nome informado.")
            return
        if not heroi_encontrado.status_tornozeleira:
            print(f"O herói {heroi_encontrado.nome} precisa estar usando uma tornozeleira primeiro.")
            return
        else:
            if not heroi_encontrado.status_gps:
                heroi_encontrado.status_gps = True
                print(f'O GPS da tornozeleira do herói {heroi_encontrado.nome} foi ligado.')
            else:
                print(f'O herói {heroi_encontrado.nome} já está sendo rastreado.')

    @staticmethod
    def emitir_mandado():
        '''Emite um mandado para um heróis especifico'''
        os.system('cls')
        Interface.imprime_titulo_tela('Emissão do mandado de prisão.')

        nome_escolha = input('Digite o nome do herói para emitir um mandado de prisão: ').strip()
        heroi_encontrado = next((h for h in Heroi.lista_de_herois if nome_escolha.strip().lower() in h.nome.strip().lower() or nome_escolha.strip().lower() in h.real.strip().lower()), None)

        print(f'Um mandado de prisão foi emitido para {heroi_encontrado.nome}.')

    @staticmethod
    def info():
        '''Mostra todas as informações de um vingador'''
        os.system('cls')
        Interface.imprime_titulo_tela('Emissão do mandado de prisão.')

        nome_escolha = input('Digite o nome do herói para obter suas informações: ').strip()
        heroi_encontrado = next((h for h in Heroi.lista_de_herois if nome_escolha.strip().lower() in h.nome.strip().lower() or nome_escolha.strip().lower() in h.real.strip().lower()), None)
        print(f'''
Nome do herói: {heroi_encontrado.nome}
Nome real: {heroi_encontrado.real}
Categoria: {heroi_encontrado.categoria}
Poderes: {heroi_encontrado.poderes}
Poder principal: {heroi_encontrado.poder_principal}
Fraquezas: {heroi_encontrado.forca}
Nível de força: {heroi_encontrado.forca}
Status de convocação: {heroi_encontrado.convocado}
Status da tornozeleira: {heroi_encontrado.status_tornozeleira}
Status do chip GPS: {heroi_encontrado.status_gps}
''')
        
    def ler_opcao_usuario():
        '''Uma função que lê a opção do usuário na tela inicial'''
        try:
            opcao = int(input('O que deseja fazer?: '))
            if opcao == 1:
                Interface.imprimir_titulo_app()
                Interface.cadastrar_heroi()
            elif opcao == 2:
                Interface.imprimir_titulo_app()
                Interface.imprime_titulo_tela('Listando Vingadores')
                Heroi.lista_tornozeleira()
            elif opcao == 3:
                Interface.imprimir_titulo_app()
                Interface.imprime_titulo_tela('Formando um time!')
                print('Escolha Heróis para formar um time: ')
                Interface.formar_time()
            elif opcao == 4:
                Interface.imprimir_titulo_app()
                Interface.imprime_titulo_tela('Convocando Herói!')
                Interface.convocar_heroi()
            elif opcao == 5:
                Interface.imprimir_titulo_app()
                Interface.imprime_titulo_tela('Aplicando Tornozeleira!')
                Interface.aplicar_tornozeleira()
            elif opcao == 6:
                Interface.imprimir_titulo_app()
                Interface.imprime_titulo_tela('Aplicando Localizador!')
                Interface.aplicar_gps()
            elif opcao == 7:
                Interface.imprimir_titulo_app()
                Interface.imprime_titulo_tela('Emitindo mandado de prisão!')
                Interface.emitir_mandado()
            elif opcao == 8:
                Interface.imprimir_titulo_app()
                Interface.imprime_titulo_tela('Informações sobre o Herói!')
                Interface.info()
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