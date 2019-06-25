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

frame = Frame(master, bg="#efd5a8", bd="5")
frame.place(relx=0.722, rely=0.6, relwidth=0.25, relheight=0.15)

frame1 = Frame(master, bg="#efd5a8", bd="5")
frame1.place(relx=0.03, rely=0.3, relwidth=0.25, relheight=0.15)
label = Label(frame1, bg="#efd5a8", font=("Helvetica 14 bold"), text="Ime i prezime")
label.place(relwidth=1, relheight=0.4)
ime_i_prezime = Entry(frame1, font=("Helvetica 14"), bg="white")
ime_i_prezime.place(relx=0, rely=0.4, relwidth=1, relheight=0.6)

frame2 = Frame(master, bg="#efd5a8", bd="5")
frame2.place(relx=0.35, rely=0.3, relwidth=0.3, relheight=0.1)
label2 = Label(frame2, bg="#efd5a8", font=("Helvetica 16 bold"), text="Odaberite mjesto boravka,\nzatim odaberite apartman")
label2.place(relwidth=1, relheight=1)



class App(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        

        self.dict = {"Crikvenica": ["Crikvenica (KIM)", "Crikvenica (BEACH CENTER)", "Crikvenica (PROMENADA)"],
                     "Zadar": ["Zadar (RIMANIC)", "Zadar (NOA)", "Zadar (LA LUNA)"],
                     "Makarska": ["Makarska (VILLA 43)", "Makarska (TALIJA)", "Makarska (Podaca)"],
                     "Dubrovnik": ["Dubrovnik (PARADIS)", "Dubrovnik (GLORIET)", "Dubrovnik (BONBON)"]
                     }
       

        self.mjesto = StringVar(self)
        self.naziv_apartmana = StringVar(self)

        self.mjesto.trace('w', self.update_options)

        self.optionmenu_a = OptionMenu(self, self.mjesto, *self.dict.keys())
        self.optionmenu_b = OptionMenu(self, self.naziv_apartmana, '')

        self.mjesto.set("Crikvenica")

        self.optionmenu_a.config(font=("Helvetica 24 bold"))
        self.optionmenu_b.config(font=("Helvetica 16 bold"))

        self.optionmenu_a.place(relx=0, rely=0, relwidth=1, relheight=0.5)
        self.optionmenu_b.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)
        self.place(relx=0.35, rely=0.4, relwidth=0.3, relheight=0.4)


    def update_options(self, *args):
        grad = self.dict[self.mjesto.get()]
        self.naziv_apartmana.set(grad[0])

        menu = self.optionmenu_b['menu']
        menu.delete(0, 'end')

        for mjesto_ap in grad:
            menu.add_command(label=mjesto_ap, command=lambda apartman=mjesto_ap: self.naziv_apartmana.set(apartman))


frame4 = Frame(master, bg="#efd5a8", bd="5")
frame4.place(relx=0.03, rely=0.6, relwidth=0.25, relheight=0.15)
datum_boravka = StringVar(frame4)
datum_boravka.set("Odaberite datum boravka od//do") 

datum_boravka1 = OptionMenu(frame4, datum_boravka, "01.07.19//07.07.19", "08.07.19//14.07.19", "15.07.19//21.07.19", "22.07.19//28.07.19", "29.07.19//04.08.19", "05.08.19//11.08.19", "12.08.19//18.08.19", "19.08.19//25.08.19", "26.08.19//01.09.19")
datum_boravka1.config(font=("Helvetica 12 bold"))
datum_boravka1.pack(fill="both", expand="1")


frame5 = Frame(master, bg="#efd5a8", bd="5")
frame5.place(relx=0.72, rely=0.3, relwidth=0.25, relheight=0.15)
broj_osoba = StringVar(frame5)
broj_osoba.set("Odaberite broj osoba")

broj_osoba1 = OptionMenu(frame5, broj_osoba, "1", "2", "3", "4", "5", "6")
broj_osoba1.config(font=("Helvetica 13 bold"))
broj_osoba1.pack(fill="both", expand="1")


frame7 = Frame(master, bg="#eac2a3")
frame7.place(relx=0.3, rely=0.03, relwidth=0.4, relheight=0.2)
label = Label(frame7, font=("Helvetica 24 bold"), text="REZERVACIJA APARTMANA", fg="white", bg="#efd5a8")
label.place(relwidth=1, relheight=1)

frame8 = Frame(master, bg="#efd5a8")
frame8.place(relx=0.17, rely=0.84, relheight=0.152, relwidth=0.5195)
Lb = Listbox(frame8, height = 12, width = 86,font=("Helvetica 10 bold")) 
Lb.pack(side = "left", fill = Y)
scroll = Scrollbar(frame8, orient = VERTICAL)
scroll.config(command = Lb.yview)
scroll.pack(side = "right", fill = Y)
Lb.config(yscrollcommand = scroll.set)            
Lb.insert(0,"Rezervirao apartman: (Ime i prezime, Mjesto, Naziv apartmana, Datum boravka, Broj osoba)")




def rezerviraj_ap():
        print("Rezervirali ste apartman")

        c.execute('INSERT INTO tabla (ime_i_prezime , self.mjesto, self.naziv_apartmana, datum_boravka, broj_osoba) VALUES (?, ?, ?, ?, ?)',
                  (ime_i_prezime.get(), self.mjesto.get(), self.naziv_apartmana.get(), datum_boravka.get(), broj_osoba.get()))
        con.commit()

        ime_i_prezime.delete(0, END)
       

def ispis():
        print("Ispisali ste podatke iz baze podataka")
        c.execute('SELECT * FROM tabla')
        podaci = c.fetchall()
            
        for row in podaci:
                Lb.insert(1,row)         

        con.commit()

def izbrisati():
        print ("Izbrisali ste rezervaciju")
        c.execute("DELETE FROM tabla WHERE ime_i_prezime = '" + self.ime_i_prezime.get() + "'")
        con.commit()

        ime_i_prezime.delete(0, END)
        
        
button1 = Button(frame, text="Završi rezervaciju!",command=rezerviraj_ap, font=("Helvetica 23 bold"), fg="red")
button1.place(relx=0, rely=0, relheight=1, relwidth=1)    

button2 = Button(master, text="Prikaži rezervacije",command=ispis, font=("Helvetica 12 bold"), fg="red")
button2.place(relx=0.69, rely=0.84, relheight=0.074, relwidth=0.15)

button3 = Button(master, text="Izbrišite rezervaciju", command=izbrisati, font=("Helvetica 12 bold"), fg="red")
button3.place(relx=0.69, rely=0.92, relheight=0.074, relwidth=0.15)

if __name__ == "__main__":
    
    app = App(master)
    app.mainloop()
            
master.mainloop()
c.close()
con.close()
