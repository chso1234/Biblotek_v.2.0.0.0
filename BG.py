import tkinter as tk
import mysql.connector

#koble til databasen
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql",
    database="mydb" 
    )
cursor = db.cursor()

# min valgte font 
font = ("Georgia", 27)

#lager funksjoner
def legg_til():
    tittel = tittel_entry.get()
    forfatternavn = forfatter_entry.get()    
    sjanger = sjanger_entry.get()
    utgivelseår = utgivelsesår_entry.get()
    utlånsstatus= utlånsstatus_entry.get()

    sql = "INSERT INTO Bok_ID (Tittel, Forfatter, Sjanger, Utgivelsesår, Utlånsstatus) VALUES (%s, %s, %s, %s, %s)"
    val = (tittel, forfatternavn, sjanger, utgivelseår, utlånsstatus)
    cursor.execute(sql, val)
    db.commit()

def slett():
    tittel = tittel_entry.get()

    sql = f"DELETE FROM Bok_ID WHERE Tittel = '{tittel}'"
    cursor.execute(sql)
    db.commit()

def oppdater():
    tittel = tittel_entry.get()
    forfatternavn = forfatter_entry.get()
    sjanger = sjanger_entry.get()
    utgivelseår = utgivelsesår_entry.get()
    utlånsstatus = utlånsstatus_entry.get()

    sql = "UPDATE Bok_ID SET Forfatter = %s, Sjanger = %s, Utgivelsesår = %s, Utlånsstatus = %s WHERE Tittel = %s"
    val = (forfatternavn, sjanger, utgivelseår, utlånsstatus, tittel)
    cursor.execute(sql, val)
    db.commit()

def søk():
    tittel = tittel_entry.get()

    sql = "SELECT * FROM Bok_ID WHERE Tittel = %s"
    val = (tittel,)
    cursor.execute(sql, val)
    result = cursor.fetchall()

    if result:
        # Håndterer resultatet av søket
        for row in result:
            print(row)  # Her kan du tilpasse hvordan du ønsker å håndtere resultatet
    else:
        print("Ingen resultater funnet for angitt tittel.")    



#lager vinduet 
root = tk.Tk()



#lager labels 
tittel_label = tk.Label(root, font = font, text = "Tittel")

forfatter_label = tk.Label(root, font = font, text = "Forfatter")

sjanger_label = tk.Label(root, font = font, text = "Sjanger")

utgivelsesår_label = tk.Label(root, font = font, text = "Utgivelsesår")

utlånsstatus_label = tk.Label(root, font = font, text = "Utlånsstatus")


#plassering_label
tittel_label.grid(row = 2, column = 0)

forfatter_label.grid(row = 3, column = 0)

sjanger_label.grid(row = 4, column = 0)

utgivelsesår_label.grid(row = 5, column = 0)

utlånsstatus_label.grid(row = 6, column = 0)

#lager entrys
tittel_entry = tk.Entry(root, font = font)

forfatter_entry = tk.Entry(root, font = font)

sjanger_entry = tk.Entry(root, font = font)

utgivelsesår_entry = tk.Entry(root, font = font)

utlånsstatus_entry = tk.Entry(root, font = font)


#plassering_entry
tittel_entry.grid(row = 2, column = 1)

forfatter_entry.grid(row = 3, column= 1)

sjanger_entry.grid(row = 4, column = 1)

utgivelsesår_entry.grid(row = 5, column = 1)

utlånsstatus_entry.grid(row = 6, column = 1)

#lager knaper 
legg_til_button = tk.Button(root, text = "Legg til bok", font = font, command = legg_til)
legg_til_button.grid(row = 9, column = 1, sticky= "we")

søk_til_button = tk.Button(root, text = "Søk", font = font, command = søk)
søk_til_button.grid(row = 10, column = 1, sticky= "we")

oppdater_button = tk.Button(root, text = "Oppdater", font = font, command = oppdater)
oppdater_button.grid(row = 12, column = 1, sticky= "we") 

slett_button = tk.Button(root, text = "Slett", font = font, command = slett)
slett_button.grid(row = 13, column = 1, sticky= "we") 






root.mainloop()