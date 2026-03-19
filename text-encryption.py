def encrypt(text):
    encrypted_text=""
    for i in range(len(text)):
        char=text[i]
        if char.isupper():
            encrypted_text+=chr((ord(char)+4-65)%26+65)
        elif char.islower():
            encrypted_text+=chr((ord(char)+4-97)%26+97)
        else:
            encrypted_text+=char

    print(encrypted_text)
    return

def decrypt(text):
    decrypted_text=""
    for i in range(len(text)):
        char=text[i]
        if char.isupper():
            decrypted_text+=chr((ord(char)-4-65)%26+65)
        elif char.islower():
            decrypted_text+=chr((ord(char)-4-97)%26+97)
        else:
            decrypted_text+=char
    print(decrypted_text)
    return

text=input("Enter the text:")
print("1.Encrypt" \
        "\n2.Decrypt")
choice=int(input("Choice:"))
if choice==1:
    encrypt(text)
elif choice==2:
    decrypt(text)