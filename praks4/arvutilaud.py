from praks4.kirjutuslaud import Kirjutuslaud

class Arvutilaud(Kirjutuslaud):
    def pindala(self, arvuti):
        return super.pindala(self) - arvuti #self.pikkus * self.laius - arvuti