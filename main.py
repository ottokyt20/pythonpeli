
Tavoite: Tutki Härmälää, kerää esineitä ja pisteitä,
löydä mystinen laatikko ja vanha avain, ja avaa laatikko
saadaksesi kultaisen aarteen. Vie aarre rantaravintolaan voittaaksesi!
"""

from paikat import paikat
from pelaaja import Pelaaja
from komennot import (
    liiku, kerää_esine
)

# Pääohjelma
def main():
    print("="*60)
    print("    HÄRMÄLÄN SEIKKAILU - Tekstiseikkailupeli")
    print("="*60)
    print("\nTervetuloa Härmälään!")
    print("Olet tutkimassa Härmälän aluetta.")
    print("Tavoitteesi on löytää mystinen aarre!")
    print("\nKirjoita 'apua' nähdäksesi komennot.\n")
    
    # Luo pelaaja
    pelaaja = Pelaaja()
    pelaaja.merkitse_paikka(pelaaja.sijainti)
    
    peli_käynnissä = True
    
    # Näytä aloituspaikka
    nykyinen_paikka = paikat[pelaaja.sijainti]
    print(f"\n{nykyinen_paikka['nimi']}")
    print(nykyinen_paikka['kuvaus'])
    
    while peli_käynnissä == True:
        syöte = input("\n> ").lower()
        
        if syöte == "":
            print("Et antanut komentoa. Yritä uudelleen.")
            continue
        
        # Jaa komento osiin
        osat = syöte.split()
        komento = osat[0]
        
        if komento == "apua" or komento == "help":
            print("\nKomennot:")
            print("  pohjoinen/etelä/itä/länsi - Liiku valittuun suuntaan")
            print("  ota - Kerää esine paikasta")
            print("  inv/inventaario - Näytä inventaario")
            print("  katso - Katso ympärillesi")
            print("  tilastot - Näytä tilastot")
            print("  lopeta - Lopeta peli")
            
        elif komento in ["pohjoinen", "etelä", "itä", "länsi", "p", "e", "i", "l"]:
            # Muunna lyhenteet täysiksi
            suuntamap = {"p": "pohjoinen", "e": "etelä", "i": "itä", "l": "länsi"}
            suunta = suuntamap.get(komento, komento)
            
            uusi_sijainti = liiku(pelaaja.sijainti, suunta)
            if uusi_sijainti:
                pelaaja.sijainti = uusi_sijainti
                uusi_paikka = paikat[pelaaja.sijainti]
                
                # Tarkista onko uusi paikka
                if pelaaja.merkitse_paikka(pelaaja.sijainti):
                    print(f"\n{uusi_paikka['nimi']}")
                    print(uusi_paikka['pitkä_kuvaus'])
                else:
                    print(f"\n{uusi_paikka['nimi']}")
                    print(uusi_paikka['kuvaus'])
                
                # Näytä esineet
                if uusi_paikka['esineet']:
                    print("Näet täällä: ")
                    for esine in uusi_paikka['esineet']:
                        if ensimmainen:
                            ensimmainen = False
                        else:
                            print(", ", end="")
                        print(esine, end="")
                    print()
                    
        elif komento == "ota":
            if osat[1:] == []:
                print("Mitä haluat ottaa?")
            else:
                esine = osat[1]
                kerää_esine(pelaaja.sijainti, esine, pelaaja.inventaario)
                    
        elif komento in ["inv", "inventaario"]:
            if pelaaja.inventaario:
                print("\nInventaariossasi: ", end="")
                
                # Käy läpi jokainen esine inventaariossa
                ensimmainen_esine = True
                for esine in pelaaja.inventaario:
                    # Jos ei ole ensimmäinen esine, tulosta pilkku
                    if ensimmainen_esine:
                        ensimmainen_esine = False
                    else:
                        print(", ", end="")
                    
                    # Tulosta esineen nimi
                    print(esine, end="")
                
                # Rivinvaihto lopuksi
                print()
            else:
                # Jos inventaario on tyhjä
                print()
                print("Inventaariosi on tyhjä.")
                
        elif komento == "katso":
            paikka = paikat[pelaaja.sijainti]
            
            # Tulosta paikan nimi ja pitkä kuvaus
            print(f"\n{paikka['nimi']}")
            print(paikka['pitkä_kuvaus'])
            
            # Tarkista onko paikalla esineitä
            if len(paikka['esineet']) > 0:
                # Tulosta esinelistan otsikko
                print("Näet täällä: ", end="")
                
                # Käy läpi jokainen esine paikalla
                ensimmainen_esine = True
                for esine in paikka['esineet']:
                    # Jos ei ole ensimmäinen esine, tulosta pilkku erottimeksi
                    if ensimmainen_esine:
                        ensimmainen_esine = False
                    else:
                        print(", ", end="")
                    
                    # Tulosta esineen nimi
                    print(esine, end="")
                
                # Rivinvaihto lopuksi
                print()
            else:
                # Jos paikalla ei ole esineitä
                print("Täällä ei ole esineitä.")
                
        elif komento == "tilastot":
            pelaaja.nayta_tilastot()
            print(f"Vaihe: {pelaaja.vaihe}/3")
            
        elif komento == "lopeta" or komento == "quit":
            print("\nKiitos pelaamisesta!")
            peli_käynnissä = False
            
        else:
            print("En ymmärrä komentoa. Kirjoita 'apua' nähdäksesi komennot.")


if __name__ == "__main__":
    main()