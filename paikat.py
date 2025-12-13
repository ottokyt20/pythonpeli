"""
Härmälän seikkailupelin paikat
"""

paikat = {
    "bussipysäkki": {
        "nimi": "Bussipysäkki",
        "kuvaus": "Seisot Härmälän bussipysäkillä. Bussikatos suojaa sateelta. Voit mennä pohjoiseen kampukselle tai etelään kauppakeskukseen.",
        "yhteydet": {"pohjoinen": "kampuksen_piha", "etelä": "kauppakeskus"},
        "esineet": ["bussilippu", "kolikko"],
    },

    "kauppakeskus": {
        "nimi": "Kauppakeskus",
        "kuvaus": "Olet Härmälän kauppakeskuksessa. Hyllyt ovat täynnä erilaisia tuotteita. Voit mennä pohjoiseen takaisin bussipysäkille.",
        "yhteydet": {"pohjoinen": "bussipysäkki"},
        "esineet": ["vesipullo", "eväsleipä"],
    },

    "kampuksen_piha": {
        "nimi": "Kampuksen piha",
        "kuvaus": "Olet TAMK:in kampuksen pihalla. Opiskelijat kulkevat kiireisinä luennoille.",
        "yhteydet": {"etelä": "bussipysäkki"},
        "esineet": ["muistivihko"],
    }, 

}

