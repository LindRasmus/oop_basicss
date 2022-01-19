from praks4.sodurid import Inimene

class Sodur(Inimene):
    def __init__(self, armee_nr):
        super(Sodur, self).__init__()
        self.armee_nr = armee_nr

    def info(self):
        ("id = {0}". format(self.id))