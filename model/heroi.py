from model.database import Database

class Heroi:

    lista_de_herois = []

    def __init__(self, id, nome, real, categoria, poderes, poder_principal, fraquezas, forca, convocado = False, status_t = False, status_g = False):
        self.id = id
        self.nome = nome
        self.real = real
        self.categoria = categoria
        self.poderes = poderes
        self.poder_principal = poder_principal
        self.fraquezas = fraquezas
        self.forca = forca
        self.convocado = convocado
        self.status_t = status_t
        self.status_g = status_g
        
        Heroi.lista_de_herois.append(self)

    def tornozeleira_formatada(self):
        return "Sim" if self.status_t else "Não"

    def gps_formatado(self):
        return "Sim" if self.status_g else "Não"

    def imprimir_cabecalho():
        print(f'| {'Nome de Herói'.ljust(20)} | {'Nome Real'.ljust(20)} | {'Categoria'.ljust(12)} | {'Poderes'.ljust(30)} | {'Poder Principal'.ljust(20)} | {'Fraquezas'.ljust(20)} | {'Nível de Força'.ljust(15)} |')

    @classmethod
    def listar_vingadores(cls):
        Heroi.imprimir_cabecalho()
        for vingador in Heroi.lista_de_herois:
            print(f'| {str(vingador.nome).ljust(20)} | {str(vingador.real).ljust(20)} | {str(vingador.categoria).ljust(12)} | {str(vingador.poderes).ljust(30)} | {str(vingador.poder_principal).ljust(20)} | {str(vingador.fraquezas).ljust(20)} | {int(vingador.forca)}{' '*11} |')

    def __str__(self):
        return f'| {str(self.nome).ljust(20)} | {str(self.real).ljust(20)} | {str(self.categoria).ljust(12)} | {str(self.poderes).ljust(30)} | {str(self.poder_principal).ljust(20)} | {str(self.fraquezas).ljust(20)} | {int(self.forca)}{' '*11} |'

    def lista_resumo():
        print(f'| {'Nome de Herói'.ljust(20)} |')
        print(f'+{'-'*22}+')
        for vingador in Heroi.lista_de_herois:
            print(f'| {str(vingador.nome).ljust(20)} |')
        print(f'+{'-'*22}+')

    def lista_tornozeleira():
        print(f"| {'Nome de Herói'.ljust(20)} | {'Nome Real'.ljust(20)} | {'Categoria'.ljust(15)} | {'Tornozeleira'.ljust(12)} | {'Localizador'.ljust(12)} |")
        print(f"+{'-'*22}|{'-'*22}|{'-'*17}|{'-'*14}|{'-'*14}+")
        for heroi in Heroi.lista_de_herois:
            print(f"| {str(heroi.nome).ljust(20)} | {str(heroi.real).ljust(20)} | {str(heroi.categoria).ljust(15)} | {str(heroi.tornozeleira_formatada()).ljust(12)} | {str(heroi.gps_formatado()).ljust(12)} |")
        print(f"+{'-'*22}|{'-'*22}|{'-'*17}|{'-'*14}|{'-'*14}+")

    @staticmethod
    def carregar_herois():
        try:
            db = Database()
            db.connect()

            query = 'SELECT idheroi, nome_heroi, nome_real, categoria, poderes, poder_principal, fraquezas, nivel_forca FROM heroi'
            herois = db.select(query) # retorna uma lista de tuplas
            for heroi in herois:
                Heroi(*heroi)
        except Exception as e:
            print(f'Erro: {e}')
        finally:
            db.disconnect() # precisa terminar a conexão !!

    def herois_convocados():
        try:
            db = Database()
            db.connect()

            query = 'SELECT nome_heroi, data_convocacao, condicao FROM vingadores.view_herois_convocados'
            herois = db.select(query) # retorna uma lista de tuplas

            if not herois:
                print('Nenhum herói convocado.')
                return

            print(f"| {'Nome de Herói'.ljust(20)} | {'Data de Convocação'.ljust(19)} | {'Status de Convocação'.ljust(20)} |")
            print(f"+{'-'*22}|{'-'*21}|{'-'*22}+")

            for heroi in herois:
                nome_heroi = heroi[0]
                data_convocacao = heroi[1]
                status_convocacao = heroi[2]
                print(f"| {nome_heroi.ljust(20)} | {data_convocacao} | {status_convocacao.ljust(20)} |")
            print(f"+{'-'*22}|{'-'*21}|{'-'*22}+\n")
        except Exception as e:
            print(f'Erro: {e}')
        finally:
            db.disconnect()