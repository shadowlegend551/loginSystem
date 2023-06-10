from tkinter import Tk, Text, Button, Label, messagebox, END
from hashlib import sha256

SYSTEMNAME = 'Loginsys2000'
BGCOLOUR = 'light grey'

def getsaved():
    table = {}
    contents = []

    with open('shadow.txt', 'r') as file:  # Password file.
        for line in file:
            contents.append(line.rstrip('\n').split())
    for sublist in contents:
        table[sublist[0]] = sublist[1]
    return table


class LogInScreen:
    def __init__(self):
        self.table = getsaved()
        
        self.root = Tk()
        self.root.configure(bg=BGCOLOUR)
        self.root.geometry('250x175')

        self.title = Label(self.root, bg=BGCOLOUR, text='Log-in system 2000', font=('Arial', 16))
        self.ulabel = Label(self.root, bg=BGCOLOUR, text='Username:')
        self.pwlabel = Label(self.root, bg=BGCOLOUR, text='Password:')

        self.usernamebox = Text(self.root, height=1, width=25)
        self.passwordbox = Text(self.root, height=1, width=25)

        self.signinbutton = Button(self.root, width=7, bg=BGCOLOUR, text='Sign In',
                                    command=lambda: signin(self, self.usernamebox.get('1.0', END), self.passwordbox.get('1.0', END)))

        self.loginbutton = Button(self.root, width=7, bg=BGCOLOUR, text='Log In', 
                                    command=lambda: login(self, self.usernamebox.get('1.0', END), self.passwordbox.get('1.0', END)))

        self.title.pack()
        self.ulabel.pack()
        self.usernamebox.pack()
        self.pwlabel.pack()
        self.passwordbox.pack()
        self.signinbutton.pack(pady=2)
        self.loginbutton.pack()


        def login(object, username, password):
            displayusername = username
            username = sha256(username.encode(encoding='utf-8')).hexdigest()  # Converts the username into a sha256-encoded string.
            password = sha256(password.encode(encoding='utf-8')).hexdigest()  # Converts the password into a sha256-encoded string.

            if username in object.table and object.table[username] == password:
                messagebox.showinfo(SYSTEMNAME, f'You have been logged in as "{displayusername}"')
            else:
                messagebox.showerror(SYSTEMNAME, f'User "{displayusername}" does not exist.')


        def signin(object, username, password):
            displayusername = username
            username = sha256(username.encode(encoding='utf-8')).hexdigest()
            if username in object.table:
                messagebox.showerror(SYSTEMNAME, f'Username "{displayusername}" already taken!')
                return
                
            password = sha256(password.encode(encoding='utf-8')).hexdigest()
            with open('shadow.txt', 'a') as file:
                file.write(f'{username} {password}\n')
            object.table[username] = password
            messagebox.showinfo(SYSTEMNAME, f'You have been signed in as "{displayusername}"')
