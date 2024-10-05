#Password Manager

from cryptography.fernet import Fernet
import base64
import hashlib


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


pwd = input("What is the master password?")

key = load_key()
fer = Fernet(key)

#key + password + text to encrypt = random text
#random text + key + password = text to encrypt

'''def write_key():
    key = Fernet.generate_key()
    with open ("key.key", "wb") as key_file:
        key_file.write(key)
'''


if pwd == "test":

    def view():
        with open('password.text', 'r') as f:
            for line in f.readlines():
                data = line.rstrip()
                user, passw = data.split("|")
                print("User: ", user, ", Password:", fer.decrypt(passw.encode()))
            
    def add():
        name = input("Account Name: ")
        pwd = input("Password: ")
        
        with open('password.text', 'a') as f:
            f.write(name + "|" + fer.encrypt(pwd.encode()).decode()+ "\n")
            
        
    add()
    while True:
        mode = input("Would you like to add a new password or view existing ones(view, add) or type 'q' for quit:  ").lower()
        if mode == "q":
            break
        
        elif mode == "view":
            view()
        elif mode == "add":
            add()
        else:
            print("Invalid mode. ")
            continue
else:
    quit()