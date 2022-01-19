from praks2.restoraan import restoraan

class JaatiseKiosk(restoraan):
    jaatise_valik = ["Maasikajäätis", "Shokolaadijäätis", "vanillijäätis", "Erimaitseline", "Laktoosivaba"]

    def naita_jaatise_valik(self):
        for jk in range(1, len(self.jaatise_valik) + 1):
            print("{0}. {1}", "Saadaval olevad  jäätise valikud:".format(jk, self.jaatise_valik[jk-1]))

     #setter
    def maara_jaatise_valik(self, valik):
        print('Lisa jaatise variandid: ')
        while(True):
            valik = input("sisesta: ")
            if valik (valik == ''):
                break
            self.jaatise_valik.append(valik)