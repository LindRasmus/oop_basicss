from praks2.restoraan import restoraan

restoraani_nimi = ''
tuup = ''

class Restoraan():
    teenindatud_kylastajad = 0
    määra_teenindatud_kylalised = 0
    suurenda_teenindatud_kylalised = 0
    def __init__(self):
        self.nimi = restoraani_nimi
        self.tuup = tuup
        print('Restoran', str(self.nimi), 'pakub', str(self.tuup))

input()