
# Pääohjelma tekstiseikkailupeliin, Härmälän seikkailu

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
    print("Olet TAMK:in opiskelija tutkimassa Härmälän aluetta.")
    print("Tavoitteesi on kerätä pisteitä, löytää mystinen laatikko")
    print("ja avata se. Onko sinulla mitä tarvitaan?")
    print("\nKirjoita 'apua' nähdäksesi komennot.\n")
    
    # Luo pelaaja
    pelaaja = Pelaaja()
    pelaaja.merkitse_paikka(pelaaja.sijainti)
    
    
    
    peli_käynnissä = True
    
    # Näytä aloituspaikka
    nykyinen_paikka = paikat[pelaaja.sijainti]
    print(f"\n{nykyinen_paikka['nimi']}")
    print(nykyinen_paikka['kuvaus'])
    
    while peli_käynnissä:
        syöte = input("\n> ").lower()
        
        if syöte == "":
            print("Et antanut komentoa. Yritä uudelleen.")
            continue
        
        komento = syöte.split()[0] # Ensimmäinen sana on komento, käyttäjän syötteestä
        
        if komento == "apua" or komento == "help":
            print("\nKomennot:")
            print("  pohjoinen/etelä/itä/länsi - Liiku suuntaan")
            print("  ota [esine] - Ota esine")
            print("  inv/inventaario - Näytä inventaario")
            print("  katso - Katso ympärillesi")
            print("  tilastot - Näytä tilastot")
            print("  lopeta - Lopeta peli")
            
        elif komento == "pohjoinen" or komento == "etelä" or komento == "itä" or komento == "länsi":
            suunta = komento 
            
            uusi_paikka = liiku(pelaaja.sijainti, suunta)


            
            if uusi_paikka:
                pelaaja.merkitse_paikka(uusi_paikka)
                pelaaja.sijainti = uusi_paikka
                uusi_paikka = paikat[pelaaja.sijainti]

                print(f"\n{uusi_paikka['nimi']}")
                print(uusi_paikka['kuvaus'])
                # Tarkista onko paikalla esineitä
                if uusi_paikka['esineet']:
                    print("Näet täällä: ")
                    for esine in uusi_paikka['esineet']:
                        print(f" - {esine}")
                    


        # Kerää esine
        elif komento == "ota":
            if len(syöte.split()) < 2:
                print("Mitä haluat ottaa?")
            else:
                esine = syöte.split()[1]
                kerää_esine(pelaaja.sijainti, esine, pelaaja.inventaario)
                    
        elif komento == "inv" or komento == "inventaario":
            # Tarkista onko inventaariossa esineitä
            if len(pelaaja.inventaario) > 0:
                # Tulosta inventaarion otsikko
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
            # Hae nykyisen paikan tiedot
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
                

        # Näytä pelaajan tilastot
        elif komento == "tilastot":
            pelaaja.nayta_tilastot()
            print(f"Sijaintisi: {pelaaja.sijainti}")

        # Lopeta peli
        elif komento == "lopeta" or komento == "quit":
            print(f"Kirjoitit komennon {komento}. Peli päättyy.")
            print("\nKiitos pelaamisesta!")
            peli_käynnissä = False
            
        else:
            print("En ymmärrä komentoa. Kirjoita 'apua' nähdäksesi komennot.")


if __name__ == "__main__":
    main()