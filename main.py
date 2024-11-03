from tkinter import *
from tkinter import messagebox

def belepes():
    pass




def regisztracio():

    def ok_gomb_kezelese():
        reg_ablak.destroy()

    def jelszo_gen():
        pass

    reg_ablak = Tk()
    reg_ablak.title("Regisztráció")

    f_nev_cimke = Label(reg_ablak, text="Felhasználó neve (email):")
    f_jelszo_cimke =Label(reg_ablak, text="Jelszó:")
    f_jelszo2_cimke = Label(reg_ablak, text="A jelszó ismét:")

    ok_gomb = Button(reg_ablak, text="OK", command=ok_gomb_kezelese)
    jelszo_gen_gomb = Button(reg_ablak, text="Jelszó generálása", command=jelszo_gen)

    f_nev = StringVar()
    f_nev.set("")
    f_nev_be = Entry(reg_ablak, textvariable=f_nev, width=20)
    f_jelszo = StringVar()
    f_jelszo.set("")
    f_jelszo_be = Entry(reg_ablak, textvariable=f_jelszo, width=20)
    f_jelszo2 = StringVar()
    f_jelszo2.set("")
    f_jelszo2_be = Entry(reg_ablak, textvariable=f_jelszo2, width=20)

    f_nev_cimke.pack()
    f_nev_be.pack()
    f_jelszo_cimke.pack()
    f_jelszo_be.pack()
    jelszo_gen_gomb.pack()
    f_jelszo2_cimke.pack()
    f_jelszo2_be.pack()
    ok_gomb.pack()

    reg_ablak.mainloop()

def nevjegy():
    messagebox.showinfo("Néjegy", "Készítő: Én, 2024")

def sugo():
    messagebox.showerror("Súgó", "Még nincs súgó!")

app = Tk()
app.title("Dolgozói nyilvántartás")

menulista = Menu(app)

fajl = Menu(menulista)
fajl.add_command(label="Belépés", command=belepes)
fajl.add_command(label="Regisztráció", command=regisztracio)
fajl.add_command(label="Kilépés", command=app.destroy)
menulista.add_cascade(label="Fájl", menu=fajl)

egyeb = Menu(menulista)
egyeb.add_command(label="Névjegy", command=nevjegy)
egyeb.add_command(label="Súgó", command=sugo)
menulista.add_cascade(label="Egyéb", menu=egyeb)

app.config(menu=menulista)
app.mainloop()