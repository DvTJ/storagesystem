import GenerateQRCode as gqrc

# Hauptprogramm Version 0.0.1d
# Konsolenabfrage, rechner an inventarbestand und eingabe in eine Textdatei

print("Willkommen bei der Inventursoftware. Wie kann ich Ihnen helfen?\n"
      "Optionen:\n"
      "1: Neues Produkt hinzufügen\n"
      "2: Bestand bei einem Produkt aktualisieren\n"
      "3: Produkt löschen\n"
      "4: Beenden")

def createNewProduct():
    # Logik zum Hinzufügen eines neuen Produkts
    print("Sie fügen ein neues Produkt zum Lager hinzu!"
          "Name des Produkts:")
    name = input()
    invNr = 1 # Wird noch durch eine laufende Nummer ersetzt!
    print("\nSehr gut! Die Inventarnummer zu dem Produkt '" + name + " ' ist: " + invNr)


