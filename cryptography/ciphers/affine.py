from cryptography import euler, modular_multiplicative_inverse


def encrypt(data, key):
    data = data.upper()
    result = ""
    a, b = key

    for char in data:
        char_possition = ord(char) - 65
        char_new_possition = (a * char_possition + b) % 26 + 65

        result += chr(char_new_possition)

    return result


def decrypt(data, key):
    data = data.upper()
    result = ""
    a, b = key
    inversion_a = modular_multiplicative_inverse.inverse(a, 26)

    for char in data:
        char_possition = ord(char) - 65
        char_new_possition = (char_possition - b) * inversion_a % 26 + 65

        result += chr(char_new_possition)

    return result


def crack(data, alphabet_size):
    results = []

    for a in range(euler.euler_function(alphabet_size)):
        for b in range(alphabet_size):
            results.append(decrypt(data, (a, b)))

    return results
