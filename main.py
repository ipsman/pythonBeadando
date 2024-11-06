from tkinter import *
from tkinter import messagebox, filedialog
from tkinter import ttk
from datetime import datetime, timedelta
from TagModul_AM import Tag_AM, save_data, load_data, refresh_table, users

def add_user_interface(frame, treeview):
    Label(frame, text="Új felhasználó", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=10)

    Label(frame, text="Név:").grid(row=1, column=0, padx=10, pady=5, sticky=E)
    name_entry = Entry(frame, width=30)
    name_entry.grid(row=1, column=1, padx=10, pady=5)

    Label(frame, text="Bérlet típus:").grid(row=2, column=0, padx=10, pady=5, sticky=E)
    membership_var = StringVar(value="Havi")
    membership_option = OptionMenu(frame, membership_var, "Havi", "Féléves", "Éves")
    membership_option.grid(row=2, column=1, padx=10, pady=5, sticky=W)

    Label(frame, text="Kezdet (ÉÉÉÉ-HH-NN):").grid(row=3, column=0, padx=10, pady=5, sticky=E)
    start_date_entry = Entry(frame, width=30)
    start_date_entry.grid(row=3, column=1, padx=10, pady=5)

    Label(frame, text="Lejárat:").grid(row=4, column=0, padx=10, pady=5, sticky=E)
    expiry_var = StringVar()
    expiry_entry = Entry(frame, textvariable=expiry_var, width=30, state="readonly")
    expiry_entry.grid(row=4, column=1, padx=10, pady=5)

    def update_expiry_date():
        try:
            start_date = datetime.strptime(start_date_entry.get(), "%Y-%m-%d")
            membership_type = membership_var.get()
            if membership_type == "Havi":
                expiry_date = start_date + timedelta(days=30)
            elif membership_type == "Féléves":
                expiry_date = start_date + timedelta(days=182)
            elif membership_type == "Éves":
                expiry_date = start_date + timedelta(days=365)
            expiry_var.set(expiry_date.strftime("%Y-%m-%d"))
        except ValueError:
            expiry_var.set("")

    def add_user():
        name = name_entry.get().strip()
        start_date_str = start_date_entry.get().strip()

        try:
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
            expiry_date = datetime.strptime(expiry_var.get(), "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Hiba", "Kérlek írj be egy létező dátumot (ÉÉÉÉ-HH-NN).")
            return

        membership_type = membership_var.get()

        if not name or name in users:
            messagebox.showerror("Hiba", "A névnek egyedinek kell lennie!")
            return

        new_user = Tag_AM(name, membership_type, start_date, expiry_date)
        users[name] = {"user": new_user}
        messagebox.showinfo("Siker!", f"{name} sikeresen hozzáadva!")

        name_entry.delete(0, END)
        start_date_entry.delete(0, END)
        expiry_var.set("")
        refresh_table(treeview)

    start_date_entry.bind("<FocusOut>", lambda e: update_expiry_date())
    add_button = Button(frame, text="Hozzáad", command=add_user, bg="green", fg="white")
    add_button.grid(row=5, column=0, columnspan=2, pady=20)

def main_window():
    app = Tk()
    app.title("Kondi Bérlet Nyilvántartó")
    app.geometry("800x600")

    menu = Menu(app)
    file_menu = Menu(menu, tearoff=0)
    file_menu.add_command(label="Mentés", command=save_data)
    file_menu.add_command(label="Betöltés", command=lambda: load_data(treeview))
    file_menu.add_command(label="Kilépés", command=app.destroy)
    menu.add_cascade(label="Fájl", menu=file_menu)
    app.config(menu=menu)

    add_user_frame = Frame(app)
    add_user_frame.pack(pady=20)

    treeview = ttk.Treeview(app, columns=("Név", "Bérlet típus", "Kezdet", "Lejárat"), show='headings')
    treeview.heading("Név", text="Név")
    treeview.heading("Bérlet típus", text="Bérlet típus")
    treeview.heading("Kezdet", text="Kezdet")
    treeview.heading("Lejárat", text="Lejárat")
    treeview.pack(pady=20)

    add_user_interface(add_user_frame, treeview)





def login_AM():
    def authenticate():
        if user_entry.get().strip() == "admin" and pass_entry.get().strip() == "admin":
            login_window.destroy()
            main_window()
        else:
            messagebox.showerror("Hiba", "Rossz felhasználónév vagy jelszó!")

    login_window = Tk()
    login_window.title("Login")
    login_window.geometry("300x200")

    Label(login_window, text="Felhasználónév:").pack(pady=10)
    user_entry = Entry(login_window)
    user_entry.pack(pady=5)

    Label(login_window, text="Jelszó:").pack(pady=10)
    pass_entry = Entry(login_window, show="*")
    pass_entry.pack(pady=5)

    login_button = Button(login_window, text="Belépés", command=authenticate)
    login_button.pack(pady=20)

    login_window.mainloop()

login_AM()