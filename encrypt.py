def encrypt(input_string, shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    #input_list = encrypt_string.split()
    output_string = []
    if shift >= 26:
        shift = shift % 26
    if shift == 0:
        return input_string
    print("SHIFT = ", shift)
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
    output_string = ''.join(output_string)
    return output_string
