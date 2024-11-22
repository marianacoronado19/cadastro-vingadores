from model.heroi import Heroi
from model.interface import Interface as i

def main():
    Heroi('Homem de Ferro', 'Tony Stark', 'Humano', 'Armadura, Inteligência', 'Armadura', 'Coração', '60')
    Heroi('Capitão América', 'Steve Rogers', 'Humano', 'Força, Escudo', 'Escudo de Vibranium', 'Hydra', '55')
    Heroi('Viúva Negra', 'Natasha Romanoff', 'Humano', 'Luta, Armamento', 'Luta', 'Controle Mental', '50')
    Heroi('Hulk', 'Bruce Banner', 'Meta-Humano', 'Super-Força, Inteligência', 'Super-Força', 'Raiva', '80')
    Heroi('Gavião Arqueiro', 'Clint Barton', 'Humano', 'Arco, Luta', 'Arco e flechas', 'Loki', '40')
    Heroi('Thor', 'Thor Odinson', 'Deidade', 'Força, Raios, Martelo', 'Mjolnir', '?', '90')
    i.apresentar_menu_principal()

if __name__ == '__main__': # sempre no final do arquivo contendo a definição da função principal
    main()