from random import randint


class Ristkylik:
    def __init__(self,laius,korgus,symbol):
        self.laius =int(laius)
        self.korgus = int(korgus)
        self.symbol = str(symbol)

    def __str__(self):
        ruut = []
        for i in range(self.korgus):
            ruut.append(self.symbol * self.laius)
        ruut = "\n".join(ruut)
        return ruut

    def __add__(self, teine_ristkylik):
        self.laius = self.laius + teine_ristkylik.laius
        self.korgus = self.korgus + teine_ristkylik.korgus
        symboli_valik = randint(1, 2)
        if symboli_valik == 1:
            self.symbol = self.symbol
        else:
            self.symbol = teine_ristkylik.symbol
            return self

"midagi on valesti"