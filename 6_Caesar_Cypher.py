from sys import exit

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main():
    while True:
        print('Do you want to (e)ncrypt, (d)ecrypt or (q)uit?')
        answer = input('>   ')
        if answer.lower() == 'e':
            encryption()
        elif answer.lower() == 'd':
            decryption()
        elif answer.lower() == 'q':
            exit()
        else:
            print("Try again, please")

def encryption():
    key = int(input("Enter a key (1 to 26) to use:\n>   "))
    message = input("Enter the message to encrypt:\n>   ")
    cypher = ''
    for letter in message:
        index = LETTERS.find(letter.upper())
        if index != -1:
            newIndex = (index + key) if (index + key) < 26 else (index + key) % 26
            cypher += LETTERS[newIndex]
        else:
            cypher += ' '
    print(cypher)



def decryption():
    key = int(input("Enter a key (1 to 26) to use:\n>   "))
    cypher = input("Enter the message to decrypt:\n>   ")
    message = ''
    for letter in cypher:
        index = LETTERS.find(letter.upper())
        if index != -1:
            newIndex = (index - key) if (index - key) > -1 else (index - key) % 26
            message += LETTERS[newIndex]
        else:
            message += ' '
    print(message)
    


if __name__ == '__main__':
    main()