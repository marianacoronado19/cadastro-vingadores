class Heroi:

    contador_id = 0
    lista_de_herois = []

    def __init__(self, nome, real, categoria, poderes, poder_principal, fraquezas, forca):
        self.nome = nome
        self.real = real
        self.categoria = categoria
        self.poderes = poderes
        self.poder_principal = poder_principal
        self.fraquezas = fraquezas
        self.forca = forca
        
        Heroi.lista_de_herois.append(self)
        self.id =  Heroi.contador_id + 1
        Heroi.contador_id += 1

    def imprimir_cabecalho():
        print(f'{'Nome de Herói'.ljust(20)} | {'Nome Real'.ljust(20)} | {'Categoria'.ljust(12)} | {'Poderes'.ljust(30)} | {'Poder Principal'.ljust(20)} | {'Fraquezas'.ljust(20)} | {'Nível de Força'.ljust(15)}')

    @classmethod
    def listar_vingadores(cls):
        Heroi.imprimir_cabecalho()
        for vingador in Heroi.lista_de_herois:
            print(f'{str(vingador.nome).ljust(20)} | {str(vingador.real).ljust(20)} | {str(vingador.categoria).ljust(12)} | {str(vingador.poderes).ljust(30)} | {str(vingador.poder_principal).ljust(20)} | {str(vingador.fraquezas).ljust(20)} | {str(vingador.forca).ljust(15)}')

    def __str__(self):
        return f'{str(self.nome).ljust(20)} | {str(self.real).ljust(20)} | {str(self.categoria).ljust(12)} | {str(self.poderes).ljust(30)} | {str(self.poder_principal).ljust(20)} | {str(self.fraquezas).ljust(20)} | {str(self.forca).ljust(15)}'

    def lista_resumo():
        print(f'{'ID'} | {'Nome de Herói'.ljust(20)}')
        for vingador in Heroi.lista_de_herois:
            print(f'{vingador.id} | {str(vingador.nome).ljust(20)}')

    def lista_tornozeleira():
        print(f'{'Nome de Herói'.ljust(20)} | {'Nome Real'.ljust(20)} | {'Tornozeleira'.ljust(10)} | {'Localizador'.ljust(10)}')