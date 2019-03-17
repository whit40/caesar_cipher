#Lab #4
#Due Date: 02/01/2019, 11:59PM
########################################
#                                      
# Name: Jason C. Nucciarone
# Collaboration Statement:
# I worked on this lab alone, but I referred to these urls
# 1.https://www.programiz.com/python-programming/methods/built-in/chr
########################################

def encrypt(message, key):
    """
        >>> encrypt("Hello world",12)
        'Tqxxa iadxp'
        >>> encrypt("We are Penn State!!!",6)
        'Ck gxk Vktt Yzgzk!!!'
        >>> encrypt("We are Penn State!!!",5)
        'Bj fwj Ujss Xyfyj!!!'
        >>> encrypt(5.6,3)
        'error'
        >>> encrypt('Hello',3.5)
        'error'
        >>> encrypt(5.6,3.15)
        'error'
        >>> encrypt("The weather is nice right now", 28)
        'Vjg ygcvjgt ku pkeg tkijv pqy'
    """
    # --- YOUR CODE STARTS HERE
    if isinstance(message, str) and isinstance(key, int):
        encrypt_message = str()  # Construct an empty string for encrypted characters
        
        if key > 26:
            key = key % 26

        for character in message:
            # If character is not in alphabet, it is just appended to encrypt_message
            if character.isalpha():
                unicode_num = ord(character)  # [1] Convert character into unicode number
                unicode_num += key

                # Use 26 because there is only 26 characters in alphabet
                if character.islower():  # The character is lowercase
                    if unicode_num < ord("a"):
                        unicode_num += 26
                    elif unicode_num > ord("z"):
                        unicode_num -= 26

                if character.isupper():  # The character is uppercase
                    if unicode_num < ord("A"):
                        unicode_num += 26
                    elif unicode_num > ord("Z"):
                        unicode_num -= 26

                encrypt_message += chr(unicode_num)  # [1]

            else:
                encrypt_message += character

        return encrypt_message
        
    else:
        return 'error'


def decrypt(message, key):
    """
        >>> decrypt("Tqxxa iadxp",12)
        'Hello world'
        >>> decrypt("Ck gxk Vktt Yzgzk!!!",6)
        'We are Penn State!!!'
        >>> decrypt("Bj fwj Ujss Xyfyj!!!",5)
        'We are Penn State!!!'
        >>> decrypt(5.6,3)
        'error'
        >>> decrypt('Hello',3.5)
        'error'
        >>> decrypt(5.6,3.15)
        'error'
        >>> decrypt("Jason", ["Hello", "World"])
        'error'
        >>> decrypt("Vjg ygcvjgt ku pkeg tkijv pqy", 28)
        'The weather is nice right now'
    """
    # --- YOUR CODE STARTS HERE
    if isinstance(message, str) and isinstance(key, int):
        decrypt_message = str()  # Construct an empty string for decrypted characters
        
        if key > 26:
            key = key % 26

        for character in message:
            # If not in alphabet, just append to decrypt_message
            if character.isalpha():
                unicode_num = ord(character)  # [1]
                # To decrypt the message, take the inverse of the provided key
                unicode_num += -1*key

                # Use 26 because there is only 26 characters in alphabet
                if character.islower():  # The character is lowercase
                    if unicode_num < ord("a"):
                        unicode_num += 26
                    elif unicode_num > ord("z"):
                        unicode_num -= 26

                if character.isupper():  # The character is uppercase
                    if unicode_num < ord("A"):
                        unicode_num += 26
                    elif unicode_num > ord("Z"):
                        unicode_num -= 26

                decrypt_message += chr(unicode_num)  # [1]
                
            else:
                decrypt_message += character
                
        return decrypt_message

    else:
        return 'error'
