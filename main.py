import GenerateQRCode as gqrc
import product as p
import os
import dbhandle as db

# Hauptprogramm Version 0.0.1d
# Konsolenabfrage, rechner an inventarbestand und eingabe in eine Textdatei

print("Willkommen bei der Inventursoftware. Wie kann ich Ihnen helfen?\n"
      "Optionen:\n"
      "1: Neues Produkt hinzufügen\n"
      "2: Bestand bei einem Produkt aktualisieren\n"
      "3: Produkt löschen\n"
      "4: Beenden")

c_input = input("Eingabe: ")

if c_input == '1':
    p_name = input("Name: ")
    p_desc = input("Beschreibung: ")
    p_quantity = input("Anzahl: ")

    p_location = "b4"  # implement in a later stage that the server says where to store it

    p_invnr = db.requestInvNr() + 1

    #newProduct = p.Product(p_name, p_desc, p_invnr, p_location)
    #print(p_invnr)
    db.addNewItem(p_name, p_desc, p_location, p_quantity)

