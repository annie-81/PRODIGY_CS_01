import sys
while(1):
    n=input("Enter an option: E for encryption or D for decryption or S for exit:")
    if n=="E" or n=="e":
        text= input("Enter your text/message: ")
        key = int(input("Specify the shift length (0 to 25): "))
        result = ""
        for character in text:
            if character.isalpha():
                shifted_char = chr((ord(character.lower()) - 97 + key) % 26 + 97)
                result += shifted_char if character.islower() else shifted_char.upper()
            else:
                result += character
        print(f"{text} has been encrypted as {result}") 
    elif n=="D" or n=="d":
        de_message = input("Enter the message to be decrypted: ")
        k = int(input("Enter the key to decrypt (0 to 25): "))
        decrypted_message = ""
        for ch in de_message:
            if ch.isalpha():
                shifted_char = chr((ord(ch.lower()) - 97 - k) % 26 + 97)
                decrypted_message += shifted_char if ch.islower() else shifted_char.upper()
            else:
                decrypted_message += ch
        print("Your decrypted message is:",decrypted_message)
    elif n=="S" or n=="s":
        sys.exit()
    else:
        print("!!Enter E or D or S only!!")
