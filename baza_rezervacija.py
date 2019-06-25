from sqlite3 import *

kon = connect("baza_ap.db")

c = kon.cursor()

c.execute("CREATE TABLE tabla (ime_i_prezime TEXT, str(self.mjesto) TEXT, str(self.naziv_apartmana) TEXT, datum_boravka TEXT, broj_osoba INTEGER)")

kon.close()
