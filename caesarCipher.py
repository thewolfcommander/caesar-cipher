input("Input Reqeuired... ")
#program for caesar cipher algorithm
def encrypt(text,s):
    result = " "
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + s - 65)%26 + 65)

        else:
            result += chr((ord(char) + s - 97)%26 + 97)

    return result
encrypt(text=input("Enter the Text... "), s=input("enter the key"))
