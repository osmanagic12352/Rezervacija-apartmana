from tkinter import *

master = Tk()
master.title("Rezervacija apartmana") 
master.geometry("1200x600")

background_image = PhotoImage(file="poz.png")
background_label = Label(master, image=background_image)
background_label.place(relwidth=1, relheight=1)


frame = Frame(master, bg="#777777", bd="5")
frame.place(relx=0.3, rely=0.5, relwidth=0.4, relheight=0.1)
button = Button(frame, text="Rezerviraj!!", font=("Helvetica 20 bold"), fg="red")
button.place(relx=0.25, rely=0.18, relheight=0.7, relwidth=0.5)

frame1 = Frame(master, bg="#777777", bd="5")
frame1.place(relx=0.05, rely=0.3, relwidth=0.22, relheight=0.1)
label = Label(frame1, font=("Helvetica 13 bold"), text="Ime i prezime")
label.place(relwidth=1, relheight=0.5)
entry = Entry(frame1, bg="white")
entry.pack(side="bottom", fill="both")

frame2 = Frame(master, bg="#777777", bd="5")
frame2.place(relx=0.39, rely=0.3, relwidth=0.22, relheight=0.1)
variable = StringVar(frame2)
variable.set("Odaberite mjesto") 

w = OptionMenu(frame2, variable, "Crikvenica", "Zadar", "Makarska", "Dubrovnik",)
w.config(font=("Helvetica 13 bold"))
w.pack(fill="both", expand="1")

frame3 = Frame(master, bg="#777777", bd="5")
frame3.place(relx=0.73, rely=0.3, relwidth=0.22, relheight=0.1)
variable = StringVar(frame3)
variable.set("Odaberite apartman") 

w = OptionMenu(frame3, variable, "Crikvenica (KIM)", "Crikvenica (BEACH CENTER)", "Crikvenica (PROMENADA)", "Zadar (RIMANIC)", "Zadar (NOA)", "Zadar (LA LUNA)", "Makarska (VILLA 43)", "Makarska (TALIJA)", "Makarska (Podaca)", "Dubrovnik (PARADIS)", "Dubrovnik (GLORIET)", "Dubrovnik (BONBON)")
w.config(font=("Helvetica 13 bold"))
w.pack(fill="both", expand="1")


frame4 = Frame(master, bg="#777777", bd="5")
frame4.place(relx=0.2, rely=0.7, relwidth=0.22, relheight=0.1)
variable = StringVar(frame4)
variable.set("Odaberite datum boravka od//do") 

w = OptionMenu(frame4, variable, "01.07.19//07.07.19", "08.07.19//14.07.19", "15.07.19//21.07.19", "22.07.19//28.07.19", "29.07.19//04.08.19", "05.08.19//11.08.19", "12.08.19//18.08.19", "19.08.19//25.08.19", "26.08.19//01.09.19")
w.config(font=("Helvetica 10 bold"))
w.pack(fill="both", expand="1")


frame5 = Frame(master, bg="#777777", bd="5")
frame5.place(relx=0.6, rely=0.7, relwidth=0.22, relheight=0.1)
variable = StringVar(frame5)
variable.set("Odaberite broj osoba")

w = OptionMenu(frame5, variable, "1", "2", "3", "4", "5", "6")
w.config(font=("Helvetica 13 bold"))
w.pack(fill="both", expand="1")


frame7 = Frame(master, bg="#777777")
frame7.place(relx=0.3, rely=0.03, relwidth=0.4, relheight=0.2)
label = Label(frame7, font=("Helvetica 24 bold"), text="REZERVACIJA APARTMANA", fg="red")
label.place(relwidth=1, relheight=1)

            
master.mainloop()
