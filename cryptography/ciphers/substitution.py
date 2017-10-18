def encrypt(data, key):
    original_alphabet = key[0].upper()
    new_alphabet = key[1].upper()
    data = data.upper()
    result = ""

    for char in data:
        index = original_alphabet.index(char)
        result += new_alphabet[index]

    return result


def decrypt(data, key):
    return encrypt(data, (key[1], key[0]))
