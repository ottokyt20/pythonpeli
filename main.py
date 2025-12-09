"""
HÄRMÄLÄN SEIKKAILU - Tekstiseikkailupeli
Pelin pääohjelma

Tavoite: Tutki Härmälää, kerää esineitä ja pisteitä,
löydä mystinen aarre ja vie se rantaravintolaan voittaaksesi!
"""

from paikat import paikat
from pelaaja import Pelaaja
from komennot import (
    liiku, kerää_esine
)

def main():
    """Pelin pääsilmukka"""
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
        
        if syöte == "apua" or syöte == "help":
            print("\nKomennot:")
            print("  pohjoinen/etelä/itä/länsi - Liiku valittuun suuntaan")
            print("  ota - Kerää esine paikasta")
            print("  inv/inventaario - Näytä inventaario")
            print("  katso - Katso ympärillesi")
            print("  tilastot - Näytä tilastot")
            print("  lopeta - Lopeta peli")
            
        elif syöte in ["pohjoinen", "etelä", "itä", "länsi"]:
            suuntamap = { "pohjoinen": "north", "etelä": "south", "itä": "east", "länsi": "west" }
            suunta = suuntamap.get(syöte, syöte)
            
            uusi_sijainti = liiku(pelaaja.sijainti, suunta)
            if uusi_sijainti:
                pelaaja.sijainti = uusi_sijainti
                uusi_paikka = paikat[pelaaja.sijainti]
                
                if pelaaja.merkitse_paikka(pelaaja.sijainti):
                    print(f"\n{uusi_paikka['nimi']}")
                    print(uusi_paikka['pitkä_kuvaus'])
                else:
                    print(f"\n{uusi_paikka['nimi']}")
                    print(uusi_paikka['kuvaus'])
                
                if uusi_paikka['esineet']:
                    print("Näet täällä: ", end="")
                    ensimmainen = True
                    for esine in uusi_paikka['esineet']:
                        if ensimmainen:
                            ensimmainen = False
                        else:
                            print(", ", end="")
                        print(esine, end="")
                    print()
                    
        elif syöte == "ota":
            if "aarre" in paikat[pelaaja.sijainti]['esineet']:
                pelaaja.lisaa_inventaarioon("aarre")
                paikat[pelaaja.sijainti]['esineet'].remove("aarre")
                print("Otit aarteen!")
                print("\n" + "="*60)
                print("VOITIT PELIN!")
                print("Löysit mystisen aarteen!")
                print("="*60)
                peli_käynnissä = False
            else:
                print("Aaretta ei ole täällä.")
                pelaaja.lisaa_inventaarioon(paikat[pelaaja.sijainti]['esineet'])
                print("Otit esineen! Löysit esineen: ", paikat[pelaaja.sijainti]['esineet'])
                    
        elif syöte in ["inv", "inventaario"]:
            if pelaaja.inventaario:
                print("\nInventaariossasi: ", end="")
                ensimmainen = True
                for esine in pelaaja.inventaario:
                    if ensimmainen:
                        ensimmainen = False
                    else:
                        print(", ", end="")
                    print(esine, end="")
                print()
            else:
                print("\nInventaariosi on tyhjä.")
                
        elif syöte == "katso":
            paikka = paikat[pelaaja.sijainti]
            print(f"\n{paikka['nimi']}")
            print(paikka['pitkä_kuvaus'])
            if paikka['esineet']:
                print("Näet täällä: ", end="")
                ensimmainen = True
                for esine in paikka['esineet']:
                    if ensimmainen:
                        ensimmainen = False
                    else:
                        print(", ", end="")
                    print(esine, end="")
                print()
            else:
                print("Täällä ei ole esineitä.")
                
        elif syöte == "tilastot":
            pelaaja.nayta_tilastot()
            print(f"Vaihe: {pelaaja.vaihe}/3")
            
        elif syöte == "lopeta" or syöte == "quit":
            print("\nKiitos pelaamisesta!")
            peli_käynnissä = False
            
        else:
            print("En ymmärrä komentoa. Kirjoita 'apua' nähdäksesi komennot.")


if __name__ == "__main__":
    main()