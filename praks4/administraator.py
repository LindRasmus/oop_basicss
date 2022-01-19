from praks3.Kasutaja import Kasutaja

class Admin(Kasutaja):
    privileegid = ("lubatud_lisada_kasutajad", "lubatud_eemaldada_kasutajad", "lubatud_blokeerida_kasutajad", "lubatud_muuta_faile", "lubatud_kustutada_faile")

    def naita_privileegid(self):
        print('Kasutaja andmed: \n', self.privileegid)