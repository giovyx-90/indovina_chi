import random
import string

# Lista personaggi del gioco

anna = {"nome": "Anna", "genere": "femmina", "colore_occhi": "azzurri", "tipo_capelli": "ricci", "colore_capelli": "castani", "occhiali": False, "barba/baffi": False, "lentiggini": True}
bruno = {"nome": "Bruno", "genere": "maschio", "colore_occhi": "verdi", "tipo_capelli": "lisci", "colore_capelli": "biondi", "occhiali": True, "barba/baffi": True, "lentiggini": False}
carla = {"nome": "Carla", "genere": "femmina", "colore_occhi": "marroni", "tipo_capelli": "lisci", "colore_capelli": "rossi", "occhiali": False, "barba/baffi": False, "lentiggini": False}
davide = {"nome": "Davide", "genere": "maschio", "colore_occhi": "grigi", "tipo_capelli": "calvo", "colore_capelli": "grigi", "occhiali": False, "barba/baffi": False, "lentiggini": True}
elena = {"nome": "Elena", "genere": "femmina", "colore_occhi": "azzurri", "tipo_capelli": "mossi", "colore_capelli": "neri", "occhiali": True, "barba/baffi": False, "lentiggini": False}
fabio = {"nome": "Fabio", "genere": "maschio", "colore_occhi": "marroni", "tipo_capelli": "ricci", "colore_capelli": "castani", "occhiali": False, "barba/baffi": True, "lentiggini": False}
giulia= {"nome": "Giulia","genere": "femmina",  "colore_occhi": "verdi", "tipo_capelli": "lisci", "colore_capelli": "biondi", "occhiali": False, "barba/baffi": False, "lentiggini": True}
hugo = {"nome": "Hugo", "genere": "maschio", "colore_occhi": "marroni", "tipo_capelli": "mossi", "colore_capelli": "grigi", "occhiali": True, "barba/baffi": False, "lentiggini": False}
irene = {"nome": "Irene", "genere": "femmina", "colore_occhi": "azzurri", "tipo_capelli": "lisci", "colore_capelli": "rossi", "occhiali": False, "barba/baffi": False, "lentiggini": False}
luca = {"nome": "Luca","genere": "maschio", "colore_occhi": "grigi", "tipo_capelli": "biondi", "colore_capelli": "biondi", "occhiali": False, "barba/baffi": True, "lentiggini": False}
marco = {"nome": "Marco", "genere": "maschio", "colore_occhi": "azzurri", "tipo_capelli": "lisci", "colore_capelli": "biondi", "occhiali": True, "barba/baffi": False, "lentiggini": False}
lucia = {"nome": "Lucia", "genere": "femmina", "colore_occhi": "verdi", "tipo_capelli": "ricci", "colore_capelli": "castani", "occhiali": False, "barba/baffi": False, "lentiggini": True}
michele = {"nome": "Michele", "genere": "maschio", "colore_occhi": "grigi", "tipo_capelli": "mossi", "colore_capelli": "rossi", "occhiali": False, "barba/baffi": True, "lentiggini": False}
rosa = {"nome": "Rosa", "genere": "femmina", "colore_occhi": "marroni", "tipo_capelli": "lisci", "colore_capelli": "neri", "occhiali": True, "barba/baffi": False, "lentiggini": False}
matteo = {"nome": "Matteo", "genere": "maschio", "colore_occhi": "azzurri", "tipo_capelli": "calvo", "colore_capelli": "biondi", "occhiali": False, "barba/baffi": False, "lentiggini": True}
francesca = {"nome": "Francesca", "genere": "femmina", "colore_occhi": "grigi", "tipo_capelli": "mossi", "colore_capelli": "biondi", "occhiali": True, "barba/baffi": False, "lentiggini": False}
leo = {"nome": "Leo", "genere": "maschio", "colore_occhi": "marroni", "tipo_capelli": "ricci", "colore_capelli": "neri", "occhiali": False, "barba/baffi": True, "lentiggini": False}
gianluca = {"nome": "Gianluca", "genere": "maschio", "colore_occhi": "grigi", "tipo_capelli": "lisci", "colore_capelli": "grigi", "occhiali": True, "barba/baffi": False, "lentiggini": False}
sonia = {"nome": "Sonia", "genere": "femmina", "colore_occhi": "azzurri", "tipo_capelli": "ricci", "colore_capelli": "castani", "occhiali": True, "barba/baffi": False, "lentiggini": False}

lista_personaggi = [anna, bruno, carla, davide, elena, fabio, giulia, hugo, irene, luca, marco, lucia, rosa, matteo, francesca, leo, gianluca, sonia]

# Re-definisco pesi_domande

pesi_domande = {
    "genere": 15,
    "colore_occhi": 10,
    "tipo_capelli": 8,
    "colore_capelli": 7,
    "occhiali": 5,
    "barba/baffi": 5,
    "lentiggini": 5
}

# Dizionari per le difficoltà

difficoltà = {
    "casual": {
        "domande": 7,
        "punteggio_iniziale": 80,
        "pesi_domande": {
            "genere": 10,
            "colore_occhi": 7,
            "tipo_capelli": 6,
            "colore_capelli": 6,
            "occhiali": 4,
            "barba/baffi": 4,
            "lentiggini": 4
        },
        "numero_personaggi": 20
    },
    "normale": {
        "domande": 6,
        "punteggio_iniziale": 60,
        "pesi_domande": pesi_domande,  # Utilizza il peso delle domande già definito
        "numero_personaggi": 30
    },
    "difficile": {
        "domande": 5,
        "punteggio_iniziale": 60,
        "pesi_domande": {
            "genere": 20,
            "colore_occhi": 15,
            "tipo_capelli": 12,
            "colore_capelli": 10,
            "occhiali": 8,
            "barba/baffi": 8,
            "lentiggini": 8
        },
        "numero_personaggi": 30
    },
    "detective": {
        "domande": 5,
        "punteggio_iniziale": 50,
        "pesi_domande": {
            "genere": 25,
            "colore_occhi": 20,
            "tipo_capelli": 15,
            "colore_capelli": 12,
            "occhiali": 10,
            "barba/baffi": 10,
            "lentiggini": 10
        },
        "numero_personaggi": 30
    }
}

difficoltà



# Sceglie un personaggio del gioco
personaggi_compatibili = lista_personaggi.copy()
personaggio_scelto = random.choice(lista_personaggi)

def aggiorna_personaggi_compatibili(domanda,risposta):
    global personaggi_compatibili

    nuovi_personaggi_compatibili = []
    for personaggio in personaggi_compatibili:
        if verifica_domanda(domanda, personaggio)[0] == risposta:
            nuovi_personaggi_compatibili.append(personaggio)
    personaggi_compatibili = nuovi_personaggi_compatibili  

    print("""\nPersonaggi rimanenti:""")
    for personaggio in personaggi_compatibili:
        print(personaggio["nome"])
    
    

def messaggio_di_benvenuto(numero_domande):
    print(f"""
🎉 **Benvenuto a INDOVINA CHI - Python Edition!** 🎉

In questo gioco, devi indovinare il personaggio misterioso che ho scelto tra una lista di candidati. Ogni personaggio ha diverse caratteristiche, come il colore degli occhi, il tipo di capelli e altro ancora.

Ecco come funziona:
1. All'inizio di ogni turno, sceglierò un personaggio misterioso.
2. Avrai un totale di {numero_domande} domande per cercare di indovinare chi sia questo personaggio basandoti sulle sue caratteristiche.
3. Puoi fare domande come "Ha gli occhiali?" o "Ha i capelli ricci?" e io risponderò con "sì" o "no".
4. Dopo ogni domanda, ti mostrerò i personaggi che rimangono compatibili con le tue domande.
5. Se pensi di sapere chi sia il personaggio misterioso prima di esaurire le tue domande, puoi fare un tentativo dicendo "indovina" e poi inserendo il nome del personaggio.
6. Se indovini, vinci! Altrimenti, perdi punti.

Ricorda di usare le tue domande con saggezza e cerca di indovinare il personaggio il più velocemente possibile per ottenere il punteggio più alto.

Buona fortuna e divertiti!
""")


def lista_caratteristiche_personaggi():
    print("\nEcco la lista dei personaggi con le loro caratteristiche:")
    for personaggio in lista_personaggi:
        print("\n" + personaggio["nome"])
        print("- Genere:", personaggio["genere"])
        print("- Colore degli occhi:", personaggio["colore_occhi"])
        print("- Tipo di capelli:", personaggio["tipo_capelli"])
        print("- Colore dei capelli:", personaggio["colore_capelli"])
        print("- Occhiali:", "Sì" if personaggio["occhiali"] else "No")
        print("- Barba/baffi:", "Sì" if personaggio["barba/baffi"] else "No")
        print("- Lentiggini:", "Sì" if personaggio["lentiggini"] else "No")

def verifica_domanda(domanda, personaggio):
    caratteristica = None
    risposta = "non so"
    # Verifica per il genere
    if "maschio" in domanda:
        caratteristica = "genere"
        risposta = "sì" if personaggio["genere"] == "maschio" else "no"
    elif "femmina" in domanda:
        caratteristica = "genere"
        risposta = "sì" if personaggio["genere"] == "femmina" else "no"
    
    # Verifica per il colore degli occhi
    for colore in ["azzurri", "verdi", "marroni", "grigi"]:
        if colore in domanda:
            caratteristica = "colore_occhi"
            risposta = "sì" if personaggio["colore_occhi"] == colore else "no"
    
    # Verifica per il tipo di capelli
    for tipo in ["ricci", "lisci", "mossi", "calvo"]:
        if tipo in domanda:
            caratteristica = "tipo_capelli"
            risposta = "sì" if personaggio["tipo_capelli"] == tipo else "no"
    
    # Verifica per il colore dei capelli
    for colore in ["castani", "biondi", "rossi", "neri", "grigi"]:
        if colore in domanda:
            caratteristica = "colore_capelli"
            risposta = "sì" if personaggio["colore_capelli"] == colore else "no"
    
    # Verifica per gli occhiali
    if "occhiali" in domanda:
        caratteristica = "occhiali"
        risposta = "sì" if personaggio["occhiali"] else "no"
    
    # Verifica per la barba/baffi
    if "barba" in domanda or "baffi" in domanda:
        caratteristica = "barba/baffi"
        risposta = "sì" if personaggio["barba/baffi"] else "no"
    
    # Verifica per le lentiggini
    if "lentiggini" in domanda:
        caratteristica = "lentiggini"
        risposta = "sì" if personaggio["lentiggini"] else "no"
    
    return risposta, caratteristica

def gioca(difficoltà, personaggi_selezionati):
    continua_gioco = True
    domande_rimanenti = difficoltà["domande"]
    punteggio = difficoltà["punteggio_iniziale"]  
    messaggio_di_benvenuto(domande_rimanenti) 

    while continua_gioco:
        domanda = input("""
        \nFai la tua domanda (o scrivi 'indovina' per tentare una risposta): digita 'lista_personaggi' per la lista totale dei personaggi e le loro caratteristiche. """).lower()
        
        if "indovina" in domanda:
            risposta = input("\nChi pensi sia il personaggio misterioso? (scrivi solo il nome): ").lower()
            if risposta == personaggio_scelto["nome"].lower():
                print(f"\nComplimenti! Hai indovinato! Il tuo punteggio finale è: {punteggio} in difficoltà {scelta_difficoltà}.")
                continua_gioco = False
            else:
                print(f"\nMi dispiace, ma {risposta} non è corretto.")
                punteggio -= 20  # Sottrai 20 punti per un tentativo errato
                domande_rimanenti -= 1
                print(f"Punteggio attuale: {punteggio}")  # Mostra il punteggio dopo ogni azione
                print(f"Domande rimanenti: {domande_rimanenti}")


        elif 'lista_personaggi' in domanda:
            lista_caratteristiche_personaggi()
        
        else:
            risposta, caratteristica = verifica_domanda(domanda, personaggio_scelto)
            if risposta == "non so":
                print("\nNon ho capito la tua domanda. Riprova.")
            elif caratteristica in difficoltà['pesi_domande']:
                aggiorna_personaggi_compatibili(domanda, risposta)
                print("\n" + risposta.capitalize() + ".")
                punteggio -= difficoltà['pesi_domande'][caratteristica]
                domande_rimanenti -= 1
            

            print(f"Punteggio attuale: {punteggio}")  # Mostra il punteggio dopo ogni azione
            print(f"Domande rimanenti: {domande_rimanenti}")
  
        if domande_rimanenti == 0:
            print(f"\nHai esaurito le tue domande! Il personaggio era {personaggio_scelto['nome']}.")
            print(f"Il tuo punteggio finale è: {punteggio}")
            continua_gioco = False
        
        if punteggio <= 0:
            print(f"Non puoi avere punteggio negativo, quindi il gioco è finito. Il personaggio misterioso era {personaggio_scelto['nome']}.")
            continua_gioco = False
        

        

# Il gioco intero
try:
    while True:
        scelta = input("""
        \nINDOVINA CHI --- Python Edition [Creato da Giovyx90]
        Premi 'INVIO' per giocare o digita 'esci' per uscire: """)

        if scelta == "":  # Se l'utente ha premuto solo INVIO
            print("""
            Scegli una difficoltà:
            - Casual: 7 domande, 50 punti, 20 personaggi su 30, meno penalità per domanda.
            - Normale: 6 domande, 50 punti, tutti i personaggi.
            - Difficile: 5 domande, 50 punti, tutti i personaggi con più penalità per domanda.
            - Detective: 5 domande, 40 punti, tutti i personaggi con ancora più penalità per domanda.
            """)
            
            
            scelta_difficoltà = input("Seleziona la difficoltà (casual, normale, difficile, detective): ").lower()   
            if scelta_difficoltà not in difficoltà:
                print("Scelta non valida. Riprova.")
                
                continue
                
            # Seleziona un sottoinsieme di personaggi se necessario
            if difficoltà[scelta_difficoltà]["numero_personaggi"] < len(lista_personaggi):
                personaggi_selezionati = random.sample(lista_personaggi, difficoltà[scelta_difficoltà]["numero_personaggi"])
            else:
                personaggi_selezionati = lista_personaggi

            gioca(difficoltà[scelta_difficoltà], personaggi_selezionati) 
        elif scelta == "esci":
            print("Grazie per aver giocato! Alla prossima!")
            break
        else: 
            print("Scelta non valida. Riprova.")
except KeyboardInterrupt:
        print("\nHai premuto CTRL+C. Uscita forzata dal gioco.")
    