class restoraan():

    def __init__(self, rn, st):
        self.nimi = rn
        self.tuup = st
        nimi = 'Vogaal' #restorani nimi
        tuup = 'Praetud' #soogi tyyp
        def  kirjelda_restoraan():
            print("Restoraani nimi: " + str(self.nimi))
            print("Soogi tuup: " + str(self.tuup))
        def ava_restoraan():
            print("Restoraan" + str(self.restoraani_nimi) + 'on avatud.')
input()
