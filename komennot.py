"""
Komentojen käsittely
"""

from paikat import paikat

def liiku(nykyinen_paikka, suunta):
    # Tarkista onko paikka olemassa
    paikka_loytyy = False
    for paikka_avain in paikat:
        if paikka_avain == nykyinen_paikka:
            paikka_loytyy = True
            break
    
    if paikka_loytyy:
        paikka = paikat[nykyinen_paikka]
        
        # Tarkista onko suunta mahdollinen
        suunta_loytyy = False
        for yhteys in paikka['yhteydet']:
            if yhteys == suunta:
                suunta_loytyy = True
                break
        
        if suunta_loytyy:
            uusi_paikka = paikka['yhteydet'][suunta]
            print(f"Menet {suunta}...")
            return uusi_paikka
        else:
            print(f"Et voi mennä {suunta}.")
            return False
    else:
        print(f"Paikka '{nykyinen_paikka}' ei ole saatavilla.")
        return False


# Kerää esine paikasta
def kerää_esine(nykyinen_paikka, esine, pelaajan_tavarat):
    # Tarkista onko paikka olemassa
    paikka_loytyy = False
    for paikka_avain in paikat:
        if paikka_avain == nykyinen_paikka:
            paikka_loytyy = True
            break
    
    if paikka_loytyy:
        paikka = paikat[nykyinen_paikka]
        
        # Tarkista onko esine paikalla
        esine_loytyy = False
        for paikan_esine in paikka['esineet']:
            if paikan_esine == esine:
                esine_loytyy = True
                break
        
        if esine_loytyy:
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

