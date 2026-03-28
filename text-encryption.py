def endcrypt(text:str,shift:int):
    encrypted_text=""
    for letter in text:
        if letter.isalpha():
            base=ord('A') if letter.isupper() else ord('a')
            encrypted_text+=chr((ord(letter)+shift-base)%26+base)
        else:
            encrypted_text+=letter

    return encrypted_text

text=input("Enter the text:")
print("1.Encrypt" \
        "\n2.Decrypt")
choice=int(input("choice:"))
shift=int(input("Enter the shift value:"))
if choice==1:
    encryptedText=endcrypt(text,shift)
    print(f"The encrypted text is: {encryptedText}")
elif choice==2:
    decryptedText=endcrypt(text,-shift)
    print(f"The decrypted text is: {decryptedText}")