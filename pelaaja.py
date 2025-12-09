"""
Pelaajan tilanhallinta
Pelaaja spawnataan bussipysäkille, ja hänellä on inventaario esineitä varten sekä pisteet.
"""

class Pelaaja:
    def __init__(self):
        self.sijainti = 'bussipysäkki'
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
        if esine in self.inventaario:
            self.inventaario.remove(esine)
            
    def onko_inventaariossa(self, esine):
        """Tarkistaa onko esine inventaariossa"""
        return esine in self.inventaario
        
    def merkitse_paikka(self, paikka):
        """Merkitsee paikan vierailluksi"""
        if paikka in self.kaytyja_paikkoja:
            return False  # Käyty jo
        else:
            self.kaytyja_paikkoja.add(paikka)
            return True  # Uusi paikka
        
    def nayta_tilastot(self):
        """Näyttää pelaajan tilastot"""
        print(f"\n=== TILASTOSI ===")
        print(f"Käytyjä paikkoja: {(self.kaytyja_paikkoja)}")
        print(f"Esineitä mukana: {(self.inventaario)}")
