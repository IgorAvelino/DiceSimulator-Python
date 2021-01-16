# Criando um simulador de dados
from random import randint
import PySimpleGUI as sg

# Classe
class DiceSimulator():

    sg.theme('DarkGrey13')

    def iniciar(self):

        self.valor_min = 1

        self.layout = [
            [sg.Text('DADO VIRTUAL')],
            [sg.Text('Digite quantas faces terá o dado: '), sg.Input(key='Faces')],
            [sg.Text('Rolar dado?: '), sg.Button('SIM'), sg.Button('NÃO')],
            [sg.Output()]
        ]

        self.janela = sg.Window('Dice Simulator', layout=self.layout)

        self.evento = ''
        while self.evento != "NÃO":
            self.evento, self.valores = self.janela.Read()

            self.valor_max = self.valores['Faces']

            self.dado = randint(int(self.valor_min), int(self.valor_max))

            print(f'Faces: {self.valor_max}\nValor: {self.dado}')

# Programa
dice = DiceSimulator()
dice.iniciar()
