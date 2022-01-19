class Ristkülik:
    def __init__(self, laius, korgus,symbol):
        self.laius =int (laius)
        self.korgus = int (korgus)
        self.symbol = str(symbol)
    def __str__ (self):
        ruut = []
        for i in range(self.korgus):
            ruut.append(self.symbol * self.laius)
        ruut = "\n".join(ruut)
        return ruut

kujund1 = Ristkülik(1, 2, "*")
print (kujund1)
kujund2 = Ristkülik(2, 4, "z")
kujund1.__add__(kujund2)
print (kujund2)

input()
