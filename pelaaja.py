"""
Pelaajan tilanhallinta
Pelaaja spawnataan bussipysäkille, ja hänellä on inventaario esineitä varten sekä pisteet.
"""

class Pelaaja:
    def __init__(self):
        self.sijainti = 'bussipysäkki'  # Aloituspaikka
        self.inventaario = []
        self.pisteet = 0
        self.avattu_laatikko = False
        self.kaytyja_paikkoja = set()
        self.vaihe = 1
        
    def lisaa_inventaarioon(self, esine):
        """Lisää esineen inventaarioon"""
        self.inventaario.append(esine)
        
    def poista_inventaariosta(self, esine):
        """Poistaa esineen inventaariosta"""
        loydetty = False
        tavara = ''
        for tavara in self.inventaario:
            if tavara == esine:
                loydetty = True
                break
        if loydetty:
            self.inventaario.remove(esine)
            
    def onko_inventaariossa(self, esine):
        """Tarkistaa onko esine inventaariossa"""
        tavara = ''
        for tavara in self.inventaario:
            if tavara == esine:
                return True
        return False
        
    def merkitse_paikka(self, paikka):
        """Merkitsee paikan vierailluksi"""
        loydetty = False
        for kayty_paikka in self.kaytyja_paikkoja:
            if kayty_paikka == paikka:
                loydetty = True
                break
        if loydetty:
            print(f"Olet jo käynyt täällä: {paikka}")
            return False  # Käyty jo
        else:
            self.kaytyja_paikkoja.add(paikka)
            return True  # Uusi paikka
        
    def nayta_tilastot(self):
        """Näyttää pelaajan tilastot"""
        print(f"\n=== TILASTOSI ===")
        print(f"Käytyjä paikkoja: {(self.kaytyja_paikkoja)}")
        print(f"Esineitä mukana: {(self.inventaario)}")
