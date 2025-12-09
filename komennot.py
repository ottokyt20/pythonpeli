"""
Komentojen käsittely
"""

from paikat import paikat

def liiku(nykyinen_paikka, suunta):
    if nykyinen_paikka in paikat:
        paikka = paikat[nykyinen_paikka]
        
        if suunta in paikka['yhteydet']:
            uusi_paikka = paikka['yhteydet'][suunta]
            print(f"Menet {suunta}...")
            return uusi_paikka
        else:
            print(f"Et voi mennä {suunta}.")
            return None
    else:
        print(f"Virhe: Paikka '{nykyinen_paikka}' ei ole olemassa.")
        return None


def kerää_esine(nykyinen_paikka, esine, pelaajan_tavarat):
    if nykyinen_paikka in paikat:
        paikka = paikat[nykyinen_paikka]
        
        if esine in paikka['esineet']:
            paikka['esineet'].remove(esine)
            pelaajan_tavarat.append(esine)
            print(f"Otat esineen: {esine}")
            return True
        else:
            print(f"Täällä ei ole esinettä '{esine}'.")
            return False
    else:
        print(f"Virhe: Paikka '{nykyinen_paikka}' ei ole olemassa.")
        return False

