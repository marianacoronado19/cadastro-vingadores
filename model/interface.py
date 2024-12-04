from datetime import datetime
from model.heroi import Heroi
import os
from model.database import Database

class Interface:

    convocado = False

    def __init__(self): #sempre executado
        Heroi.carregar_herois()
        self.apresentar_menu_principal()     

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
|2. Listar todos os heróis cadastrados |
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

        poderes = input('Poderes: ').split(',')        
        poder_principal = input('Poder principal do herói: ')
        fraquezas = input('Fraquezas do herói: ').split(',')

        while True: # Define o valor máximo da força
            try:
                forca = int(input('Nível de força (0 - 10000): '))
                if forca > 10000:
                    print("O limite de força é 10000. Tente novamente.")
                else:
                    break
            except ValueError:
                print("Por favor, insira um número válido para o nível de força.")

        # Salva o vingador no banco de dados
        try:
            db = Database()
            db.connect()

            query = "INSERT INTO heroi (nome_heroi, nome_real, categoria, poderes, poder_principal, fraquezas, nivel_forca) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values = (nome, real, categoria, ', '.join(poderes), poder_principal, ', '.join(fraquezas), forca)
            
            cursor = db.execute_query(query, values)
            heroi = Heroi(cursor.lastrowid, nome, real, categoria, poderes, poder_principal, fraquezas, forca)

        except Exception as e:
            print(f'Erro ao salvar vingador no banco de dados: {e}')
        finally:
            db.disconnect()

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
                motivo = input('Motivo da convocação: ')
                data_padrao = datetime.now()
                data_convocacao_input = input("Data de convocação (deixe em branco para a data de hoje): ")
                if data_convocacao_input == '':
                    data_convocacao = data_padrao
                else:
                    data_convocacao = data_convocacao_input

                data_comparecimento_input = input("Digite uma data de comparecimento (ou deixe em branco para N/A): ")
                if not data_comparecimento_input:
                    data_comparecimento = None
                else:
                    data_comparecimento = data_comparecimento_input
                
                status_convocacao = input('Status da convocação (pendente, comparecido, etc): ').capitalize()

                try:
                    db = Database()
                    db.connect()

                    query = "INSERT INTO convocacao (motivo, data_convocacao, data_comparecimento, status_convocacao) VALUES (%s, %s, %s, %s)"  # query envia um comando para o mysql
                    values = (motivo, data_convocacao, data_comparecimento, status_convocacao)
                    
                    cursor = db.execute_query(query, values)
                    idconvocacao = cursor.lastrowid

                    query_heroi_convocacao = "INSERT INTO heroi_convocacao (idheroi, idconvocacao) VALUES (%s, %s)"
                    db.execute_query(query_heroi_convocacao, (heroi_encontrado.id, idconvocacao))
                except Exception as e:
                    print(f'Erro ao salvar vingador no banco de dados: {e}')
                finally:
                    db.disconnect()

                print(f'O herói {heroi_encontrado.nome} foi convocado com sucesso!')
            else:
                print(f'Nenhum herói encontrado com o nome "{nome_escolha}". Tente novamente.')
        else:
            print('Nenhum herói cadastrado até o momento.')

    @staticmethod
    def aplicar_tornozeleira():
        '''Uma função que define se deve ser aplicada uma tornozeleira a determinado herói, faz a filtração dos nomes e define o valor da variavel como True (não é possível aplicar tornozeleira ao Thor, Hulk ou heróis com um determinado nível de força...)'''
        os.system('cls')
        Interface.imprime_titulo_tela('Aplicação de Tornozeleira.')
        Heroi.herois_convocados()

        if not Heroi.lista_de_herois:
            print("Não há heróis cadastrados no sistema.")
            return

        nome_escolha = input('Digite o nome do herói para aplicar a tornozeleira: ').strip()
        heroi_encontrado = next((h for h in Heroi.lista_de_herois if nome_escolha.strip().lower() in h.nome.strip().lower() or nome_escolha.strip().lower() in h.real.strip().lower()), None)

        if not heroi_encontrado:
            print("Nenhum herói encontrado com o nome informado.")
            return

        try:
            db = Database()
            db.connect()

            query = "SELECT condicao FROM vingadores.view_herois_convocados WHERE nome_heroi = %s"
            values = (heroi_encontrado.nome,)
            result = db.select(query, values)

            if not result:
                print(f"Não foi encontrado status de convocação para o herói {heroi_encontrado.nome}.")
                return

            condicao = result[0][0]

            if condicao != 'Comparecido':
                print(f"A tornozeleira não pode ser aplicada a {heroi_encontrado.nome} porque a condição da convocação não é 'Comparecido'.")
                return
            

        except Exception as e:
            print(f'Erro ao consultar a view de heróis convocados: {e}')
            return
        finally:
            db.disconnect()

        status = input('Status (Ativa, Inativa): ')
        data_padrao = datetime.now()

        data_ativacao_input = input("Data de ativação da tornozeleira (deixe em branco para a data de hoje): ")
        if data_ativacao_input == '':
            data_ativacao = data_padrao
        else:
            try:
                data_ativacao = data_ativacao_input
            except ValueError:
                print("Formato de data inválido! Usando a data padrão.")
                data_ativacao = data_padrao

        data_desativacao_input = input("Digite uma data de desativacao (ou deixe em branco para N/A): ")
        if not data_desativacao_input:
            data_desativacao = None
        else:
            try:
                data_desativacao = data_desativacao_input
            except ValueError:
                os.system('cls')
                print("Formato de data inválido! Usando 'N/A' para desativação.")
                data_desativacao = None

        heroi_encontrado.forca = int(heroi_encontrado.forca)

        if not heroi_encontrado.convocado:
            os.system('cls')
            print(f"O herói {heroi_encontrado.nome} precisa ser convocado primeiro.")
            return

        if not heroi_encontrado.status_tornozeleira:  
            if heroi_encontrado.nome.lower() == 'thor':
                os.system('cls')
                print('"O Deus do Trovão não se submeterá a tal dispositivo mundano!" - Não foi possível aplicar uma tornozeleira a Thor')
            elif heroi_encontrado.nome.lower() == 'hulk':
                os.system('cls')
                print('"ARGH! HULK ESMAGA ESSE TROÇO!!!" - Não foi possível aplicar uma tornozeleira a Hulk')
            else:
                if heroi_encontrado.forca < 5000:
                    heroi_encontrado.status_tornozeleira = True
                    try:
                        db = Database()
                        db.connect()

                        query = "INSERT INTO tornozeleira (status_tornozeleira, data_ativacao, data_desativacao) VALUES (%s, %s, %s)"
                        values = (status, data_ativacao, data_desativacao)

                        cursor = db.execute_query(query, values)
                        idtornozeleira = cursor.lastrowid

                        query_heroi_convocacao = "INSERT INTO heroi_tornozeleira (idheroi, idtornozeleira) VALUES (%s, %s)"
                        db.execute_query(query_heroi_convocacao, (heroi_encontrado.id, idtornozeleira))

                    except Exception as e:
                        os.system('cls')
                        print(f'Erro ao salvar vingador no banco de dados: {e}')
                    finally:
                        db.disconnect()
                        os.system('cls')
                        Heroi.status_t = True
                        print(f"Uma tornozeleira foi aplicada ao herói {heroi_encontrado.nome}.")
                else:
                    os.system('cls')
                    print(f"Não é possível aplicar uma tornozeleira a {heroi_encontrado.nome} devido ao seu alto nível de força ({heroi_encontrado.forca}).")
        else:
            os.system('cls')
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