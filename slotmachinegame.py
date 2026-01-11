import random      # modulo per numeri casuali
import math        # modulo per calcoli matematici

crediti = 100      # crediti iniziali del giocatore

print("🎰 SLOT MACHINE 🎰")
print("REGOLE DEL GIOCO:")
print("- Inizi con 100 crediti")
print("- Inserisci una puntata ad ogni turno")
print("- Escono 3 numeri casuali da 1 a 5")
print("- 3 numeri uguali: vinci 3 volte la puntata")
print("- 2 numeri uguali: vinci 1.5 volte la puntata")
print("- Nessuna coppia: perdi la puntata")
print("- Scrivi 'esci' per uscire")
print("- Se i crediti arrivano a 0 perdi\n")

# il gioco continua finché ci sono crediti
while crediti > 0:
    puntata = input("Inserisci la puntata: ")

    # se l'utente scrive 'esci' il gioco termina
    if puntata == "esci":
        break

    # controllo che l'input sia un numero
    if puntata():
        puntata = int(puntata)

        # controllo che la puntata sia valida
        if puntata <= 0:
            print("La puntata deve essere positiva\n")
        elif puntata > crediti:
            print("Non hai abbastanza crediti\n")
        else:
            # sottraggo la puntata dai crediti
            crediti = crediti - puntata

            # genero tre numeri casuali da 1 a 5
            r1 = random.randint(1, 5)
            r2 = random.randint(1, 5)
            r3 = random.randint(1, 5)

            print("Risultato:", r1, r2, r3)

            # controllo vincite
            if r1 == r2 and r2 == r3:
                # jackpot: vincita tripla
                vincita = math.floor(puntata * 3)
                crediti = crediti + vincita
                print("JACKPOT! Hai vinto", vincita)
            elif r1 == r2 or r2 == r3 or r1 == r3:
                # coppia: vincita 1.5 volte la puntata
                vincita = math.floor(puntata * 1.5)
                crediti = crediti + vincita
                print("Coppia! Hai vinto", vincita)
            else:
                # nessuna vincita
                print("Nessuna vincita")

            # mostro i crediti rimasti
            print("Crediti rimasti:", crediti, "\n")
    else:
        # input non numerico
        print("Errore: inserisci un numero valido\n")

# fine del gioco
if crediti == 0:
    print("Sei andato in bancarotta!")
else:

    print("Gioco terminato con", crediti, "crediti")
