import operator


def _vigener_wrapper(data, key, operator):
    data = data.upper()
    key = key.upper()
    result = ""

    for i in range(len(data)):
        char_possition = ord(data[i]) - 65
        key_char_possition = ord(key[i % len(key)]) - 65
        char_new_possition = operator(
            char_possition, key_char_possition) % 26 + 65

        result += chr(char_new_possition)

    return result


def encrypt(data, key):
    return _vigener_wrapper(data, key, operator.add)


def decrypt(data, key):
    return _vigener_wrapper(data, key, operator.sub)
