def encrypt(input_string, shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    output_string = []
    # Check for cases where shift is 0 or larger than alphabet length
    if shift >= 26:
        shift = shift % 26
    if shift == 0:
        return input_string
      
    # Iterate through the input string by character, using the index of the letter in the alphabet and the shift to
    # find the char to put in the output string. Deals with cases such as uppercase letters and non letter
    # characters, as well as if the shift goes past the end of the alphabet.
    for char in input_string:
        uppercase = False
        if (char == "z") or (char == "Z"):
            if (char == "Z"):
                output_string.append(alphabet[shift-1].upper)
            else:
                output_string.append(alphabet[shift-1])
            continue

        if (char not in alphabet) and (char.lower() not in alphabet):
            output_string.append(char)
            continue
        if char == char.upper():
            char = char.lower
            uppercase = True
        char_index = alphabet.find(char)
        char_index+= shift
        encrypt_char = alphabet[char_index]
        if uppercase:
            encrypt_char = encrypt_char.upper()
        output_string.append(encrypt_char)
        
    # Take the output string, which was created as a list, and join it into a proper string.
    output_string = ''.join(output_string)
    return output_string
