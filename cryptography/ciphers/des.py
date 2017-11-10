from bitstring import BitArray

PC1 = [
        57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4
    ]

PC2 = [
    14, 17, 11, 24, 1, 5,
    3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8,
    16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
]


def swap_in_bin(bin_data, from_index, to_index):
    tmp = bin_data[from_index]
    bin_data[from_index] = bin_data[to_index]
    bin_data[to_index] = tmp

    return bin_data


def permutation_based_on_table(bin_data, table):
    key = BitArray(len(table))

    for i in range(len(table)):
        key[i] = bin_data[table[i] - 1]

    return key


def generate_halves(key_pc1_permutation):
    c0 = key_pc1_permutation[:int(len(key_pc1_permutation.bin) / 2)]
    d0 = key_pc1_permutation[int(len(key_pc1_permutation.bin) / 2):]

    c = [c0]
    d = [d0]

    for i in range(1, 17):
        ci = BitArray(c[i - 1])
        di = BitArray(d[i - 1])

        if i in [1, 2, 9, 16]:
            number_of_shifts = 1
        else:
            number_of_shifts = 2

        ci.rol(number_of_shifts)
        di.rol(number_of_shifts)
        c.append(ci)
        d.append(di)

    return c, d


def generate_keys(c, d):
    keys = []

    for i in range(16):
        joined = c[i + 1] + d[i + 1]

        key = permutation_based_on_table(joined, PC2)

        keys.append(key)

    return keys


key_string = "133457799BBCDFF1"

key = BitArray(hex=key_string)

print("Original key:")
print(key.bin)

key_pc1_permutation = permutation_based_on_table(key, PC1)

c, d = generate_halves(key_pc1_permutation)

keys = generate_keys(c, d)


print("KEYS:")
for key in keys:
    print(key.bin)
