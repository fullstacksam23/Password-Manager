from cryptography.fernet import Fernet
import os

def set_key():
    if os.path.exists("pass_key.key"):
        print("key already exists")
    else:            
        key = Fernet.generate_key()
        with open("pass_key.key", "wb") as file:
            file.write(key)
        

if __name__ == "__main__":
    set_key()