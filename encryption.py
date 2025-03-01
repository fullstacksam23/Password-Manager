from cryptography.fernet import Fernet

def pass_encrypt(password):
    key = ""
    with open("key_generator/pass_key.key", "rb") as file:
        key = file.read()
    f = Fernet(key)
    return f.encrypt(password.encode()).decode()

def pass_decrypt(password):
    key = ""
    with open("key_generator/pass_key.key", "rb") as file:
        key = file.read()
    f = Fernet(key)
    return f.decrypt(password).decode()

# e = pass_encrypt("abc")
# print(pass_decrypt(e))
    
