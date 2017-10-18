def encrypt(data, key):
    data = data.upper()
    result = ""

    for char in data:
        char_possition = ord(char)
        char_new_possition = char_possition + key

        if char_new_possition > 90:
            char_new_possition -= 26

        result += chr(char_new_possition)

    return result


def decrypt(data, key):
    data = data.upper()
    result = ""

    for char in data:
        char_possition = ord(char)
        char_new_possition = char_possition - key

        if char_new_possition < 65:
            char_new_possition += 26

        result += chr(char_new_possition)

    return result


def crack(data, alphabet_size):
    results = []

    for key in range(alphabet_size):
        results.append(decrypt(data, key))

    return results
