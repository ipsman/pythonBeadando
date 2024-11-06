from tkinter import messagebox, filedialog
from datetime import datetime, timedelta

class Tag_AM:
    def __init__(self, name, membership_type, start_date, expiry_date):
        self.name = name
        self.membership_type = membership_type
        self.start_date = start_date
        self.expiry_date = expiry_date

    def is_membership_active(self):
        today = datetime.today()
        return self.start_date <= today <= self.expiry_date

    def get_user_data(self):
        return {
            "name": self.name,
            "membership_type": self.membership_type,
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "expiry_date": self.expiry_date.strftime("%Y-%m-%d")
        }

users = {}

def save_data():
    file_name = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_name:
        try:
            with open(file_name, "w") as file:
                for name, data in users.items():
                    user = data["user"]
                    file.write(
                        f"Név: {user.name}, Bérlet típus: {user.membership_type}, Kezdet: {user.start_date.strftime('%Y-%m-%d')}, Lejárat: {user.expiry_date.strftime('%Y-%m-%d')}\n")
            messagebox.showinfo("Mentés", "Adat sikeresen elmentve!")
        except Exception as e:
            messagebox.showerror("Hiba", f"Mentési hiba: {str(e)}")

def load_data(treeview):
    file_name = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_name:
        try:
            with open(file_name, "r") as file:
                for line in file:
                    data = line.strip().split(", ")
                    if len(data) != 4:
                        continue
                    name = data[0].split(": ")[1]
                    membership_type = data[1].split(": ")[1]
                    start_date = datetime.strptime(data[2].split(": ")[1], "%Y-%m-%d")
                    expiry_date = datetime.strptime(data[3].split(": ")[1], "%Y-%m-%d")
                    new_user = Tag_AM(name, membership_type, start_date, expiry_date)
                    users[name] = {"user": new_user}
            messagebox.showinfo("Betöltés", "Adat sikeresen betöltve!")
            refresh_table(treeview)
        except Exception as e:
            messagebox.showerror("Hiba", f"Betöltési hiba: {str(e)}")

def refresh_table(treeview):
    for item in treeview.get_children():
        treeview.delete(item)

    for name, data in users.items():
        user = data["user"]
        treeview.insert("", "end", values=(
            user.name, user.membership_type, user.start_date.strftime("%Y-%m-%d"),
            user.expiry_date.strftime("%Y-%m-%d")))