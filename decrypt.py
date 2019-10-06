from simplecrypt import decrypt

with open("encrypted.bin", "rb") as input_file:
    encrypted = input_file.read()
    with open("passwords.txt", "r") as passwords:
        for password in passwords:
            try:
                decrypted = decrypt(password.strip(), encrypted)
                print(decrypted)
            except:
                print('Wrong password')