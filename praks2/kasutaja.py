class Kasutaja():
    eesnimi = ""
    perenimi = ""
    kodakonsus = ""
    elukoht = ""
    def kirjelda_kasutaja(self):
        print("Kasutaja andmed: ")
        print("eesnimi: " + str(self.eesnimi))
        print("perenimi: " + str(self.perenimi))
        print("kodakonsus: " + str(self.kodakonsus))
        print("elukoht: " + str(self.elukoht))

    def tervita_kasutaja(self):
        #print("Tere, " + str(self.eesnimi) + " " + str(self.perenimi))
        print("Tere, {0} {1}".format(self.eesnimi, self.perenimi))