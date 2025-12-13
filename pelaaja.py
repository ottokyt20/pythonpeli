"""
Pelaajan tilanhallinta
Pelaaja spawnataan bussipysäkille, ja hänellä on inventaario esineitä varten sekä pisteet.
"""

class Pelaaja:

    # Alustetaan pelaajan tila, self viittaa pelaajaan
    def __init__(self):
        self.sijainti = 'bussipysäkki'  # Aloituspaikka
        self.inventaario = [] # lista, inventaario esineitä varten, aluksi tyhjä
        self.pisteet = 0
        self.avattu_laatikko = False
        self.kaytyja_paikkoja = [] # tyhjä joukko
        
    def lisaa_inventaarioon(self, esine):
        # Lisää esineen inventaarioon
        self.inventaario.append(esine)
        
    def poista_inventaariosta(self, esine):
        # Poistaa esineen inventaariosta
        loydetty = False
       
       # Käy läpi inventaario, for loopilla
        for tavara in self.inventaario:
            if tavara == esine: # Jos esine löytyy, 
                loydetty = True
                break
        if loydetty:
            self.inventaario.remove(esine)
            
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
        
        # Jos ei ole käyty, lisää listaan
        self.kaytyja_paikkoja.append(paikka)
        return True  
        
    def nayta_tilastot(self):
        # Näyttää pelaajan tilastot
        print(f"\n=== TILASTOSI ===")
        print(f"Käytyjä paikkoja: {(self.kaytyja_paikkoja)}")
        print(f"Esineitä mukana: {(self.inventaario)}")
