from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_symbols + password_numbers + password_letters
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    email = email_entry.get()
    website = website_entry.get()
    user_password = password_entry.get()

    if len(website) == 0 or len(user_password) == 0:
        messagebox.showerror(title="Error", message="Don't leave any empty fields")
    else:

        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\n{email}\n{user_password}"
                               f"\nIs it okay to save?")

        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website}, {email}, {user_password}\n")

            website_entry.delete(0, 'end')
            password_entry.delete(0, 'end')

        website_entry.focus()
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website = Label(text="Website:")
website.grid(row=1, column=0)
website = Label(text="Email/Username:")
website.grid(row=2, column=0)
website = Label(text="Password:")
website.grid(row=3, column=0)

#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
website_entry.focus()

email_entry = Entry(width=35)
email_entry.insert(0, "andrewch2817@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="EW")

#Buttons
add_button = Button(width=36, text="Add", command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

generate_button = Button(text="Generate Password", command=generate)
generate_button.grid(row=3, column=2, sticky="EW")
window.mainloop()