
class Pelaaja:

    # Alustetaan pelaajan tila, self viittaa pelaajaan
    def __init__(self):
        self.sijainti = 'bussipysäkki'  # Aloituspaikka
        self.inventaario = [] # lista, inventaario esineitä varten, aluksi tyhjä
        self.pisteet = 0
        self.avattu_laatikko = False
        self.kaytyja_paikkoja = [] # lista käydyistä paikoista, aluksi tyhjä
        
    def lisaa_inventaarioon(self, esine):
        # Lisää esineen inventaarioon
        self.inventaario.append(esine)
        
    def poista_inventaariosta(self, esine):
        # Poistaa esineen inventaariosta
        if esine in self.inventaario:
            print(f"Poistetaan esine inventaariosta: {esine}")
            self.inventaario.remove(esine)
        else:
            print(f"Esine ei ole sinulla inventaariossa: {esine}")
            
    def onko_inventaariossa(self, esine):
        # Tarkistaa onko esine inventaariossa
        
        # Käy läpi inventaario, for loopilla
        for tavara in self.inventaario:
            if tavara == esine:
                return True
            else:
                return False
        
    def merkitse_paikka(self, paikka):
        # Merkitsee paikan käydyksi, palauttaa True jos paikka on uusi
        
        # Tarkista onko paikka jo käyty
        for kayty_paikka in self.kaytyja_paikkoja:
            if kayty_paikka == paikka:
                print(f"Olet jo vieraillut täällä: {paikka}")
                return False
        
        # Jos paikka on uusi, lisää se käytyjen paikkojen listaan
        self.kaytyja_paikkoja.append(paikka)
        return True  
        
    def nayta_tilastot(self):
        # Näyttää pelaajan tilastot
        print(f"\n=== TILASTOSI ===")
        print(f"Käytyjä paikkoja: {(self.kaytyja_paikkoja)}")
        print(f"Esineitä mukana: {(self.inventaario)}")
        