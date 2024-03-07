import simplecrypt as sc

with open("2.2.2\passwords.txt", "r") as file:
    passwords = file.read().split()
with open("2.2.2\encrypted.bin", "rb") as file:
    encrypted = file.read()

for pswrd in passwords:
    try:
        print(sc.decrypt(pswrd, encrypted))
        print("The Password is:", pswrd)
        break
    except sc.DecryptionException:
        print("Bad password")