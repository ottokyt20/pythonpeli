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

            if suunta_loytyy == True:
                uusi_paikka = paikka['yhteydet'][suunta]
                print(f"Menet {suunta}...")
                return uusi_paikka
            else:
                print(f"Et voi mennä suuntaan: {suunta}.")
                return False
        else:
            print(f"Paikka '{nykyinen_paikka}' ei ole saatavilla.")
            return False
        

def keraa_esine(pelaaja, paikka, esine):
    # Kerää esineen paikasta
    if esine in paikka['esineet']:
        pelaaja.lisaa_inventaarioon(esine)
        paikka['esineet'].remove(esine)
        print(f"Otat esineen: {esine}")
    else:
        print(f"Esinettä '{esine}' ei löydy tästä paikasta.")
