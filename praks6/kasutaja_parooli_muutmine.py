parool = "qwerty"
class Kasutaja:
    def __init__(self, nimekiri):
        self.maara_parool = Kasutaja.__teeKahekordseks(nimekiri)
    def __teeKahekordseks(naita_parooli):
        uusNimekiri = []
        for i in naita_parooli:
            naita_parooli.append(i)
            naita_parooli.append(i)
        return naita_parooli

    def __init__(self, kontrolli_parool, põhjus):
        if parool < 10 > 6:
            print("Parooli vahetamine ei õnnestunud, põhjus: ", "Parool on liiga pikk!")
        else:
            print("Parooli vahetamine  õnnestus.")
        if parool > 6:
            print("Parooli vahetamine ei õnnestunud, põhjus: ", "Parool on liiga väike!")
        else:
            print("Parooli vahetamine  õnnestus.")



parool = Kasutaja("qwerty")
print(parool.kahekordne)