from tkinter import *
from sqlite3 import *

master = Tk()
master.title("Rezervacija apartmana") 
master.geometry("1200x600")

con = connect("baza_ap.db") 
c = con.cursor()

background_image = PhotoImage(file="poz.png")
background_label = Label(master, image=background_image)
background_label.place(relwidth=1, relheight=1)


frame1 = Frame(master, bg="#777777", bd="5")
frame1.place(relx=0.05, rely=0.3, relwidth=0.22, relheight=0.1)
label = Label(frame1, font=("Helvetica 13 bold"), text="Ime i prezime")
label.place(relwidth=1, relheight=0.5)
ime_i_prezime = Entry(frame1, bg="white")
ime_i_prezime.pack(side="bottom", fill="both")

frame2 = Frame(master, bg="#777777", bd="5")
frame2.place(relx=0.39, rely=0.3, relwidth=0.22, relheight=0.1)
mjesto = StringVar(frame2)
mjesto.set("Odaberite mjesto") 

mjesto1 = OptionMenu(frame2, mjesto, "Crikvenica", "Zadar", "Makarska", "Dubrovnik",)
mjesto1.config(font=("Helvetica 13 bold"))
mjesto1.pack(fill="both", expand="1")

frame3 = Frame(master, bg="#777777", bd="5")
frame3.place(relx=0.73, rely=0.3, relwidth=0.22, relheight=0.1)
naziv_apartmana = StringVar(frame3)
naziv_apartmana.set("Odaberite apartman") 

naziv_apartmana1 = OptionMenu(frame3, naziv_apartmana, "Crikvenica (KIM)", "Crikvenica (BEACH CENTER)", "Crikvenica (PROMENADA)", "Zadar (RIMANIC)", "Zadar (NOA)", "Zadar (LA LUNA)", "Makarska (VILLA 43)", "Makarska (TALIJA)", "Makarska (Podaca)", "Dubrovnik (PARADIS)", "Dubrovnik (GLORIET)", "Dubrovnik (BONBON)")
naziv_apartmana1.config(font=("Helvetica 13 bold"))
naziv_apartmana1.pack(fill="both", expand="1")


frame4 = Frame(master, bg="#777777", bd="5")
frame4.place(relx=0.2, rely=0.7, relwidth=0.22, relheight=0.1)
datum_boravka = StringVar(frame4)
datum_boravka.set("Odaberite datum boravka od//do") 

datum_boravka1 = OptionMenu(frame4, datum_boravka, "01.07.19//07.07.19", "08.07.19//14.07.19", "15.07.19//21.07.19", "22.07.19//28.07.19", "29.07.19//04.08.19", "05.08.19//11.08.19", "12.08.19//18.08.19", "19.08.19//25.08.19", "26.08.19//01.09.19")
datum_boravka1.config(font=("Helvetica 10 bold"))
datum_boravka1.pack(fill="both", expand="1")


frame5 = Frame(master, bg="#777777", bd="5")
frame5.place(relx=0.6, rely=0.7, relwidth=0.22, relheight=0.1)
broj_osoba = StringVar(frame5)
broj_osoba.set("Odaberite broj osoba")

broj_osoba1 = OptionMenu(frame5, broj_osoba, "1", "2", "3", "4", "5", "6")
broj_osoba1.config(font=("Helvetica 13 bold"))
broj_osoba1.pack(fill="both", expand="1")


frame7 = Frame(master, bg="#777777")
frame7.place(relx=0.3, rely=0.03, relwidth=0.4, relheight=0.2)
label = Label(frame7, font=("Helvetica 24 bold"), text="REZERVACIJA APARTMANA", fg="red")
label.place(relwidth=1, relheight=1)

frame8 = Frame(master, bg="#777777")
frame8.place(relx=0.26, rely=0.84, relheight=0.152, relwidth=0.5195)
Lb = Listbox(frame8, height = 12, width = 86,font=("Helvetica 10 bold")) 
Lb.pack(side = "left", fill = Y)
scroll = Scrollbar(frame8, orient = VERTICAL)
scroll.config(command = Lb.yview)
scroll.pack(side = "right", fill = Y)
Lb.config(yscrollcommand = scroll.set)            
Lb.insert(0,"Rezervirao apartman: (Ime i prezime, Mjesto, Naziv apartmana, Datum boravka, Broj osoba)")

frame = Frame(master, bg="#777777", bd="5")
frame.place(relx=0.3, rely=0.5, relwidth=0.4, relheight=0.1)


def rezerviraj_ap():
        print("Rezervirali ste apartman")

        c.execute('INSERT INTO tabla (ime_i_prezime , mjesto, naziv_apartmana, datum_boravka, broj_osoba) VALUES (?, ?, ?, ?, ?)',
                  (ime_i_prezime.get(), mjesto.get(), naziv_apartmana.get(), datum_boravka.get(), broj_osoba.get()))
        con.commit()

        ime_i_prezime.delete(0, END)
        mjesto.delete(0, END)
        naziv_apartmana.delete(0, END)
        datum_boravka.delete(0, END)
        broj_osoba.delete(0, END)

def ispis():
        print("Ispisali ste podatke iz baze podataka")
        c.execute('SELECT * FROM tabla')
        podaci = c.fetchall()
            
        for row in podaci:
                Lb.insert(1,row)         

        con.commit()

def izbrisati():
        print ("Izbrisali ste rezervaciju")
        c.execute("DELETE FROM tabla WHERE ime_i_prezime = '" + ime_i_prezime.get() + "'")
        con.commit()

        ime_i_prezime.delete(0, END)
        mjesto.delete(0, END)
        naziv_apartmana.delete(0, END)
        datum_boravka.delete(0, END)
        broj_osoba.delete(0, END)
        
button1 = Button(frame, text="Rezerviraj!!",command=rezerviraj_ap, font=("Helvetica 20 bold"), fg="red")
button1.place(relx=0.25, rely=0.18, relheight=0.7, relwidth=0.5)    

button2 = Button(master, text="Prikaži rezervacije",command=ispis, font=("Helvetica 12 bold"), fg="red")
button2.place(relx=0.78, rely=0.84, relheight=0.074, relwidth=0.15)

button3 = Button(master, text="Izbrišite rezervaciju", command=izbrisati, font=("Helvetica 12 bold"), fg="red")
button3.place(relx=0.78, rely=0.92, relheight=0.074, relwidth=0.15)

            
master.mainloop()
c.close()
con.close()
