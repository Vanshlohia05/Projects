from cryptography.fernet import Fernet
import base64
import hashlib

def load_key():
    try:
        with open("key.key", "rb") as file:
            key = file.read()
        return key
    except FileNotFoundError:
        print("Error: key.key file not found.")
        exit()

def generate_fernet_key(pwd):
    key = load_key()
    pwd_bytes = pwd.encode()  # Convert password to bytes
    derived_key = hashlib.sha256(key + pwd_bytes).digest()
    # Base64 encode the derived key to make it a valid Fernet key
    return base64.urlsafe_b64encode(derived_key[:32])  # Ensure it's 32 bytes

pwd = input("What is the master password?")

try:
    fer = Fernet(generate_fernet_key(pwd))
except Exception as e:
    print("Error creating Fernet object:", e)
    exit()

if pwd == "test":  # This is just for testing; you can change or remove this

    def view():
        try:
            with open('password.text', 'r') as f:
                for line in f.readlines():
                    data = line.rstrip()
                    user, passw = data.split("|")
                    try:
                        decrypted_pass = fer.decrypt(passw.encode()).decode()
                        print(f"User: {user}, Password: {decrypted_pass}")
                    except Exception as e:
                        print(f"Error decrypting password for {user}: {e}")
        except FileNotFoundError:
            print("Error: password.text file not found.")
        except Exception as e:
            print(f"Error reading password file: {e}")
            
    def add():
        name = input("Account Name: ")
        pwd = input("Password: ")
        
        try:
            encrypted_pwd = fer.encrypt(pwd.encode()).decode()
            with open('password.text', 'a') as f:
                f.write(name + "|" + encrypted_pwd + "\n")
        except Exception as e:
            print(f"Error saving password: {e}")
            
    while True:
        mode = input("Would you like to add a new password or view existing ones (view, add) or type 'q' to quit:  ").lower()
        if mode == "q":
            break
        
        elif mode == "view":
            view()
        elif mode == "add":
            add()
        else:
            print("Invalid mode.")
else:
    print("Incorrect master password. Exiting.")
    quit()
