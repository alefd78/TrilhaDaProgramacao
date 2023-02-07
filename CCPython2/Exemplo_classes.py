def main():
    carro1 = Carro('Brasília', 1968, 'Amarela',
                   80)  # Cria uma instância da classe Carro passando os atributos no objeto carro1
    carro2 = Carro('Fuscão', 1981, 'Preto',
                   95)  # Cria uma instância da classe Carro passando os atributos no objeto carro2

    carro1.acelere(40)
    carro2.acelere(50)
    carro1.acelere(80)
    carro1.pare()
    carro2.acelere(100)


class Carro:
    def __init__(self, m, a, c, vm):  # Função construtora, constroi o objeto baseado nos paramentros passados

        self.modelo = m
        self.ano = a
        self.cor = c
        self.vel = 0
        self.maxV = vm

    def imprima(self):  # Função recebe como referência o próprio objeto

        if self.vel == 0:
            print("%s %s %d" % (self.modelo, self.cor, self.ano))

        elif (self.vel < self.maxV):
            print("%s %s indo a %d Km/h" % (self.modelo, self.cor, self.vel))

        else:
            print("%s %s indo muito rapidoooo %d km/h" % (self.modelo, self.cor, self.vel))

    def acelere(self, v):
        self.vel = v
        if self.vel > self.maxV:
            self.vel = self.maxV
        self.imprima()

    def pare(self):
        self.vel = 0
        self.imprima()


main()