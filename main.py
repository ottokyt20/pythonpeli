

from paikat import paikat
from pelaaja import (
    Pelaaja, lisää_inventaarioon, poista_inventaariosta, onko_inventaariossa, merkitse_paikka, nayta_tilastot
)
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
        syöte = input().lower()
        
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
                    print(uusi_paikka['kuvaus'])
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
                esine = osat[1]
                kerää_esine(pelaaja.sijainti, esine, pelaaja.inventaario)
                    
        elif komento in ["inv", "inventaario"]:
            if pelaaja.inventaario:
                onko_inventaariossa = True
                print("Inventaariosi sisältää:")
                for esine in pelaaja.inventaario:
                    print(f"- {esine}")
            else:
                print("Inventaariosi on tyhjä.")
                
        elif komento == "katso":
            paikka = paikat[pelaaja.sijainti]
            
            # Tulosta paikan nimi ja pitkä kuvaus
            print(f"\n{paikka['nimi']}")
            print(paikka['pitkä_kuvaus'])
            
            # Tarkista onko paikalla esineitä
            if len(paikka['esineet']) > 0:
                # Tulosta esinelistan otsikko
                print("Näet täällä: ")
                # Käy läpi jokainen esine paikalla
                for esine in paikka['esineet']:
                    # Jos ei ole ensimmäinen esine, tulosta pilkku
                    print(f"- {esine}")
                    
    
            else:
                # Jos paikalla ei ole esineitä
                print("Täällä ei ole esineitä.")
                
        elif komento == "tilastot":
            pelaaja.nayta_tilastot()
        elif komento == "lopeta" or komento == "quit":
            print("\nKiitos pelaamisesta!")
            peli_käynnissä = False
            
        else:
            print("En ymmärrä komentoa. Kirjoita 'apua' nähdäksesi komennot.")


if __name__ == "__main__":
    main()