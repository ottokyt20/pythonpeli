"""
Härmälän seikkailupelin paikat
"""

paikat = {
    "bussipysäkki": {
        "nimi": "Bussipysäkki",
        "kuvaus": "Seisot Härmälän bussipysäkillä. Bussikatos suojaa sateelta. Voit mennä pohjoiseen kampukselle tai etelään kauppakeskukseen.",
        "pitkä_kuvaus": "Olet Härmälän bussipysäkillä Sammonkadun varrella. Bussikatos on vanha mutta toimiva. Aikatauluista näet että seuraava bussi tulee 15 minuutin päästä. Pohjoinen vie TAMK:in kampukselle ja etelä johtaa kauppakeskukseen.",
        "yhteydet": {"pohjoinen": "kampuksen_piha", "etelä": "kauppakeskus"},
        "esineet": ["bussilippu", "kolikko"],
    },

    "kauppakeskus": {
        "nimi": "Kauppakeskus",
        "kuvaus": "Olet Härmälän kauppakeskuksessa. Hyllyt ovat täynnä erilaisia tuotteita. Voit mennä pohjoiseen takaisin bussipysäkille.",
        "pitkä_kuvaus": "Olet Härmälän kauppakeskuksessa, joka palvelee paikallisia asukkaita. Hyllyt ovat täynnä erilaisia tuotteita, kuten ruokaa, juomia ja muita tarvikkeita. Kaupan kassa hymyilee sinulle ystävällisesti. Voit mennä pohjoiseen takaisin bussipysäkille.",
        "yhteydet": {"pohjoinen": "bussipysäkki"},
        "esineet": ["vesipullo", "eväsleipä"],
    },

    "kampuksen_piha": {
        "nimi": "Kampuksen piha",
        "kuvaus": "Olet TAMK:in kampuksen pihalla. Opiskelijat kulkevat kiireisinä luennoille.",
        "pitkä_kuvaus": "TAMK:in kampuksen piha on täynnä opiskelijoita ja vilkasta elämää. Opiskelijat keskustelevat ja juovat kahvia ulkona olevissa pöydissä.",
        "yhteydet": {"etelä": "bussipysäkki"},
        "esineet": ["muistivihko"],
    }, 

}

