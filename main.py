class Calculadora:
    def __init__(self, number1, number2):
        self.numero1 = number1
        self.numero2 = number2
        self.add()
        self.subtract()

    def sumar(self):
        print(f'{self.numero1 + self.numero2}')

    def restar(self):
        print(f'{self.numero1 - self.numero2}')
    
    def multiplicar(self):
        print(f'{self.numero1 * self.numero2}')
    
    def dividir(self):
        print(f'{self.numero1 / self.numero2}')


operaciones = Calculadora(20, 5)
