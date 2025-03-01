from tkinter import *
from tkinter import messagebox
import random
import json
import string
import encryption
# password generator
def generate():
    letters = string.ascii_letters
    numbers = [str(i) for i in range(0, 10)]
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    password_letters = [random.choice(letters) for i in range(nr_letters)]
    password_symbols = [random.choice(symbols) for i in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for i in range(nr_numbers)]
    password_list = password_letters+password_symbols+password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.delete(0, END)
    password_input.insert(0, password)
    

def save_pass():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="No field can be left blank!")
        return
    is_ok = messagebox.askokcancel(title=website, message=f"Check Details:\nWebsite: {website}\nEmail: {email}\nPassword: {password}\nConfirm Save?")
    password = encryption.pass_encrypt(password)
    if is_ok:
        new_dict = {
            website: {
                "email": email,
                "password": password,
            }
        }
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
                data.update(new_dict)
        except FileNotFoundError:
            data = new_dict
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)
        

        website_input.delete(0, END)
        password_input.delete(0, END)
    
# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search():
    website = website_input.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No passwords saved")
    else:
        try:
            ans = data[website]
        except KeyError:
            messagebox.showerror(title="Error", message=f"No passwords saved under {website}")
        else:
            encrypted_pass = ans["password"]
            decrypted_pass = encryption.pass_decrypt(encrypted_pass)
            messagebox.showinfo(title="Show Password", message=f"email: {ans['email']}\npassword: {decrypted_pass}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("MyPass")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)

website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=1)
website_input.focus()

search_button = Button(text="Search", width=15, command=search)
search_button.grid(row=1, column=2)

email_label = Label(text="Email/Username: ")
email_label.grid(row=2, column = 0)

email_input = Entry(width=35)
email_input.insert(0, "sam@gmail.com")
email_input.grid(row=2, column=1)


password_label = Label(text = "Password: ")
password_label.grid(row=3, column= 0)

password_input = Entry(width = 35)
password_input.grid(row=3, column=1)

generate_pass = Button(text="Generate Password", command=generate)
generate_pass.grid(row=3, column=2)

add_button = Button(text = "Add", width=36, command=save_pass)
add_button.grid(row=4, column=1, columnspan=2)
window.mainloop()