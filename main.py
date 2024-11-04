from tkinter import *
from tkinter import messagebox, filedialog
from tkinter import ttk
from datetime import datetime, timedelta


# User class to manage user information
class User:
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


# Dictionary to store user data
users = {}


# Function to save users to a TXT file
def save_data():
    file_name = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_name:
        try:
            with open(file_name, "w") as file:
                for name, data in users.items():
                    user = data["user"]
                    file.write(
                        f"Name: {user.name}, Membership Type: {user.membership_type}, Start Date: {user.start_date.strftime('%Y-%m-%d')}, Expiry Date: {user.expiry_date.strftime('%Y-%m-%d')}\n")
            messagebox.showinfo("Save", "Data saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Saving error: {str(e)}")


# Function to load users from a TXT file
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
                    new_user = User(name, membership_type, start_date, expiry_date)
                    users[name] = {"user": new_user}
            messagebox.showinfo("Load", "Data loaded successfully!")
            refresh_table(treeview)
        except Exception as e:
            messagebox.showerror("Error", f"Loading error: {str(e)}")


# Function to create the user interface for adding new users
def add_user_interface(frame, treeview):
    Label(frame, text="Add New User", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=10)

    # Name input
    Label(frame, text="Name:").grid(row=1, column=0, padx=10, pady=5, sticky=E)
    name_entry = Entry(frame, width=30)
    name_entry.grid(row=1, column=1, padx=10, pady=5)

    # Membership type input
    Label(frame, text="Membership Type:").grid(row=2, column=0, padx=10, pady=5, sticky=E)
    membership_var = StringVar(value="Monthly")
    membership_option = OptionMenu(frame, membership_var, "Monthly", "Semi-Annual", "Annual")
    membership_option.grid(row=2, column=1, padx=10, pady=5, sticky=W)

    # Start date input
    Label(frame, text="Start Date (YYYY-MM-DD):").grid(row=3, column=0, padx=10, pady=5, sticky=E)
    start_date_entry = Entry(frame, width=30)
    start_date_entry.grid(row=3, column=1, padx=10, pady=5)

    # Expiry date input (read-only)
    Label(frame, text="Expiry Date:").grid(row=4, column=0, padx=10, pady=5, sticky=E)
    expiry_var = StringVar()
    expiry_entry = Entry(frame, textvariable=expiry_var, width=30, state="readonly")
    expiry_entry.grid(row=4, column=1, padx=10, pady=5)

    # Update expiry date based on membership type
    def update_expiry_date():
        try:
            start_date = datetime.strptime(start_date_entry.get(), "%Y-%m-%d")
            membership_type = membership_var.get()
            if membership_type == "Monthly":
                expiry_date = start_date + timedelta(days=30)
            elif membership_type == "Semi-Annual":
                expiry_date = start_date + timedelta(days=182)
            elif membership_type == "Annual":
                expiry_date = start_date + timedelta(days=365)
            expiry_var.set(expiry_date.strftime("%Y-%m-%d"))
        except ValueError:
            expiry_var.set("")  # Clear if the date is invalid

    # Add user button functionality
    def add_user():
        name = name_entry.get().strip()
        start_date_str = start_date_entry.get().strip()

        try:
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
            expiry_date = datetime.strptime(expiry_var.get(), "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid start date (YYYY-MM-DD).")
            return

        membership_type = membership_var.get()

        if not name or name in users:
            messagebox.showerror("Error", "Name is required and must be unique!")
            return

        new_user = User(name, membership_type, start_date, expiry_date)
        users[name] = {"user": new_user}
        messagebox.showinfo("Success", f"{name} added successfully!")

        # Clear input fields
        name_entry.delete(0, END)
        start_date_entry.delete(0, END)
        expiry_var.set("")
        refresh_table(treeview)

    # Bindings
    start_date_entry.bind("<FocusOut>", lambda e: update_expiry_date())

    # Add button
    add_button = Button(frame, text="Add", command=add_user, bg="green", fg="white")
    add_button.grid(row=5, column=0, columnspan=2, pady=20)


# Function to refresh the Treeview table
def refresh_table(treeview):
    for item in treeview.get_children():
        treeview.delete(item)  # Clear existing data in the treeview

    for name, data in users.items():
        user = data["user"]
        treeview.insert("", "end", values=(
            user.name, user.membership_type, user.start_date.strftime("%Y-%m-%d"),
            user.expiry_date.strftime("%Y-%m-%d")))


# Main window function
def main_window():
    app = Tk()
    app.title("Gym Membership Management")
    app.geometry("800x600")

    menu = Menu(app)
    file_menu = Menu(menu, tearoff=0)
    file_menu.add_command(label="Save", command=save_data)
    file_menu.add_command(label="Load", command=lambda: load_data(treeview))
    file_menu.add_command(label="Exit", command=app.destroy)
    menu.add_cascade(label="File", menu=file_menu)
    app.config(menu=menu)

    add_user_frame = Frame(app)
    add_user_frame.pack(pady=20)

    # Create Treeview to display user data
    treeview = ttk.Treeview(app, columns=("Name", "Membership Type", "Start Date", "Expiry Date"), show='headings')
    treeview.heading("Name", text="Name")
    treeview.heading("Membership Type", text="Membership Type")
    treeview.heading("Start Date", text="Start Date")
    treeview.heading("Expiry Date", text="Expiry Date")
    treeview.pack(pady=20)

    add_user_interface(add_user_frame, treeview)

    app.mainloop()


# Login screen function
def login():
    def authenticate():
        if user_entry.get().strip() == "admin" and pass_entry.get().strip() == "admin":
            login_window.destroy()
            main_window()
        else:
            messagebox.showerror("Error", "Invalid username or password!")

    login_window = Tk()
    login_window.title("Login")
    login_window.geometry("300x200")

    Label(login_window, text="Username:").pack(pady=10)
    user_entry = Entry(login_window)
    user_entry.pack(pady=5)

    Label(login_window, text="Password:").pack(pady=10)
    pass_entry = Entry(login_window, show="*")
    pass_entry.pack(pady=5)

    login_button = Button(login_window, text="Login", command=authenticate)
    login_button.pack(pady=20)

    login_window.mainloop()


# Run the program
login()
