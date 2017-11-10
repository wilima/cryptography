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


def split_to_words(string):
    """Clever code from https://stackoverflow.com/questions/8870261/how-to-split-text-without-spaces-into-list-of-words"""
    from math import log

    # Build a cost dictionary, assuming Zipf's law and cost = -math.log(probability).
    words = open("english_words_by_freq.txt").read().split()
    wordcost = dict((k, log((i+1)*log(len(words)))) for i,k in enumerate(words))
    maxword = max(len(x) for x in words)

    def infer_spaces(s):
        """Uses dynamic programming to infer the location of spaces in a string
        without spaces."""

        # Find the best match for the i first characters, assuming cost has
        # been built for the i-1 first characters.
        # Returns a pair (match_cost, match_length).
        def best_match(i):
            candidates = enumerate(reversed(cost[max(0, i-maxword):i]))
            return min(
                (c + wordcost.get(
                    s[i-k-1:i], 9e999), k+1) for k,c in candidates)

        # Build the cost array.
        cost = [0]
        for i in range(1,len(s)+1):
            c,k = best_match(i)
            cost.append(c)

        # Backtrack to recover the minimal-cost string.
        out = []
        i = len(s)
        while i>0:
            c,k = best_match(i)
            assert c == cost[i]
            out.append(s[i-k:i])
            i -= k

        return " ".join(reversed(out))

    return infer_spaces(string)


def crack(data):

    def sort_frequencies(dictionary):
        import operator
        sorted_frequencies = sorted(dictionary.items(), key=operator.itemgetter(1))
        sorted_frequencies.reverse()
        return sorted_frequencies

    def calculate_frequencies_n_size(n, data):
        frequencies = {}

        for i in range(len(data) - (n - 1)):
            n_gram = ""

            for j in range(n):
                n_gram += data[i + j]

            if len(n_gram) != 1 and len(''.join(set(n_gram))) == 1:
                continue

            if frequencies.get(n_gram) is None:
                frequencies[n_gram] = 0
            else:
                frequencies[n_gram] += 1

        for n_gram, frequency in frequencies.items():
            frequencies[n_gram] = frequency / len(data)

        return frequencies

    english_letter_frequencies = {'A': 8.167,
                                  'B': 1.492,
                                  'C': 2.782,
                                  'D': 4.253,
                                  'E': 12.702,
                                  'F': 2.228,
                                  'G': 2.015,
                                  'H': 6.094,
                                  'I': 6.966,
                                  'J': 0.153,
                                  'K': 0.772,
                                  'L': 4.025,
                                  'M': 2.406,
                                  'N': 6.749,
                                  'O': 7.507,
                                  'P': 1.929,
                                  'Q': 0.095,
                                  'R': 5.987,
                                  'S': 6.327,
                                  'T': 9.056,
                                  'U': 2.758,
                                  'V': 0.978,
                                  'W': 2.360,
                                  'X': 0.150,
                                  'Y': 1.974,
                                  'Z': 0.074}

    english_bigrams_frequencies = {'TH': 2.71,
                                    'EN': 1.13,
                                    'NG': 0.89,
                                    'HE': 2.33,
                                    'AT': 1.12,
                                    'AL': 0.88,
                                    'IN': 2.03,
                                    'ED': 1.08,
                                    'IT': 0.88,
                                    'ER': 1.78,
                                    'ND': 1.07,
                                    'AS': 0.87,
                                    'AN': 1.61,
                                    'TO': 1.07,
                                    'IS': 0.86,
                                    'RE': 1.41,
                                    'OR': 1.06,
                                    'HA': 0.83,
                                    'ES': 1.32,
                                    'EA': 1.00,
                                    'ET': 0.76,
                                    'ON': 1.32,
                                    'TI': 0.99,
                                    'SE': 0.73,
                                    'ST': 1.25,
                                    'AR': 0.98,
                                    'OU': 0.72,
                                    'NT': 1.17,
                                    'TE': 0.98,
                                    'OF': 0.71}

    english_trigrams_frequencies = {'THE': 1.81,
                                    'ERE': 0.31,
                                    'HES': 0.24,
                                    'AND': 0.73,
                                    'TIO': 0.31,
                                    'VER': 0.24,
                                    'ING': 0.72,
                                    'TER': 0.30,
                                    'HIS': 0.24,
                                    'ENT': 0.42,
                                    'EST': 0.28,
                                    'OFT': 0.22,
                                    'ION': 0.42,
                                    'ERS': 0.28,
                                    'ITH': 0.21,
                                    'HER': 0.36,
                                    'ATI': 0.26,
                                    'FTH': 0.21,
                                    'FOR': 0.34,
                                    'HAT': 0.26,
                                    'STH': 0.21,
                                    'THA': 0.33,
                                    'ATE': 0.25,
                                    'OTH': 0.21,
                                    'NTH': 0.33,
                                    'ALL': 0.25,
                                    'RES': 0.21,
                                    'INT': 0.32,
                                    'ETH': 0.24,
                                    'ONT': 0.20}

    english_quadgrams_frequencies = {'TION': 0.31,
                                    'OTHE': 0.16,
                                    'THEM': 0.12,
                                    'NTHE': 0.27,
                                    'TTHE': 0.16,
                                    'RTHE': 0.12,
                                    'THER': 0.24,
                                    'DTHE': 0.15,
                                    'THEP': 0.11,
                                    'THAT': 0.21,
                                    'INGT': 0.15,
                                    'FROM': 0.10,
                                    'OFTH': 0.19,
                                    'ETHE': 0.15,
                                    'THIS': 0.10,
                                    'FTHE': 0.19,
                                    'SAND': 0.14,
                                    'TING': 0.10,
                                    'THES': 0.18,
                                    'STHE': 0.14,
                                    'THEI': 0.10,
                                    'WITH': 0.18,
                                    'HERE': 0.13,
                                    'NGTH': 0.10,
                                    'INTH': 0.17,
                                    'THEC': 0.13,
                                    'IONS': 0.10,
                                    'ATIO': 0.17,
                                    'MENT': 0.12,
                                    'ANDT': 0.10}

    sorted_english_frequencies = sort_frequencies(english_letter_frequencies)
    sorted_english_bigrams_frequencies = sort_frequencies(english_bigrams_frequencies)
    sorted_english_trigrams_frequencies = sort_frequencies(english_trigrams_frequencies)
    sorted_english_quadgrams_frequencies = sort_frequencies(english_quadgrams_frequencies)

    data = data.upper()

    sorted_frequencies = sort_frequencies(calculate_frequencies_n_size(1, data))
    sorted_bigrams_frequencies = sort_frequencies(calculate_frequencies_n_size(2, data))
    sorted_trigrams_frequencies = sort_frequencies(calculate_frequencies_n_size(3, data))
    sorted_quadgrams_frequencies = sort_frequencies(calculate_frequencies_n_size(4, data))

    alphabet = {}

    for i in range(26):
        new_char = sorted_frequencies[i][0]
        original_char = sorted_english_frequencies[i][0]

        alphabet[new_char] = original_char


    def create_alphabet_from_n_grams(n_grams, n_grams_original):
        alphabet = {}

        for i in range(len(n_grams[:20])):
            new_bigram = n_grams[i][0]
            original_bigram = n_grams_original[i][0]

            for char, original_char in zip(new_bigram, original_bigram):
                if alphabet.get(char) is None:
                    alphabet[char] = original_char
                else:
                    break

        return alphabet

    alphabet_bigrams = create_alphabet_from_n_grams(sorted_bigrams_frequencies, sorted_english_bigrams_frequencies)

    alphabet_trigrams = create_alphabet_from_n_grams(sorted_trigrams_frequencies, sorted_english_trigrams_frequencies)

    alphabet_quadgrams = create_alphabet_from_n_grams(sorted_quadgrams_frequencies, sorted_english_quadgrams_frequencies)

    alphabets = [alphabet, alphabet_bigrams, alphabet_trigrams]

    alphabet = {}

    for i in range(26):
        char = chr(i + ord('A'))
        alphabet_chars = set()

        for alphabet in alphabets:
            if alphabet.get(char) is not None:
                alphabet_chars.add(alphabet.get(char))

        alphabet[char] = alphabet_chars

    while True:
        for char in alphabet:
            print(char + ' : ' + str(alphabet.get(char)))

        output = ""

        for char in data:
            if len(alphabet.get(char)) == 1:
                output += list(alphabet.get(char))[0]
            else:
                output += char.lower()

        print()
        print('Priority: EARIOTNSLCUDPMHGBFYWKVXZJQ')
        print()
        print('original: ' + data[:100].lower())
        print('result: ' + output[:100])
        print()
        print(split_to_words(output.lower()[:100]))
        print()

        user_input = input('Enter modification\n')
        user_input = user_input.upper()

        if user_input == 'stop':
            break
        else:
            chars = user_input.split('=')

            for key, value in alphabet.items():
                if chars[1].upper() in value:
                    if len(alphabet[key]) == 1:
                        alphabet[key].remove(chars[1])
                        alphabet[key] = set(alphabet[chars[0]])

            alphabet[chars[0]] = set(chars[1])


text = """The second most useful app I have on my phone is Sleep Cycle. I turn it on when I am about to fall asleep, and it tracks the duration and quality of my rest. Modern technology — what a world! Of all the aspects of the quantified self I engage in, analyzing my sleep patterns is by far my favorite. In the same way a food tracker forces you to look at what you put into your body, tracking your sleep makes you realize you are probably not getting nearly as much sleep as you should. Of course, you can always go low-tech and keep a sleep diary — and to help you out, here is the handy NYT sleep diary you can print for all your tracking needs. Domestically, Prince Mohammed has sought to consolidate control over the energy sector. He has brought in Wall Street bankers to organize an initial public offering of the national oil company, Saudi Aramco, which is likely to value the enterprise at hundreds of billions of dollars. And he has replaced the country longtime oil minister, replacing him with a more pliant hand who has become crucial to fulfilling the prince plans. With the kingdom  economy suffering from weakened oil markets, Saudi Arabia, with the prince backing, has been a leading force behind the effort by the Organization of the Petroleum Exporting Countries to bolster prices by limiting production. It is a complicated task with prices continuing to fall, as American shale oil producers and Libya add to the glut of supplies. Domestically, Prince Mohammed has sought to consolidate control over the energy sector. He has brought in Wall Street bankers to organize an initial public offering of the national oil company, Saudi Aramco, which is likely to value the enterprise at hundreds of billions of dollars. And he has replaced the country longtime oil minister, replacing him with a more pliant hand who has become crucial to fulfilling the prince plans. So far, those cuts are credited with bolstering prices and supporting the revenues of producer countries. But falling prices could push Prince Mohammed to once again consider whether output constraints serve Saudi interests. They are relying on what looks like a watertight scholarly analysis to support their call: the work of a prominent energy systems engineer from Stanford University, Mark Z. Jacobson. With three co-authors, he published a widely heralded article two years ago asserting that it would be eminently feasible to power the American economy by midcentury almost entirely with energy from the wind, the sun and water. What is more, it would be cheaper than running it on fossil fuels. The experts are not opposed to aggressive investments in renewable energy. But they argue, as does most of the scientific community represented on the Intergovernmental Panel on Climate Change, that other energy sources — atomic power, say, or natural gas coupled with technologies to remove carbon from the atmosphere — are likely to prove indispensable in the global effort to combat climate change. Ignoring them risks derailing the effort to combat climate change. The weakness of energy systems powered by the sun and the wind is their intermittency. Where will the energy come from when the sun is not shining and the wind isn not blowing? Professor Jacobson addresses this in two ways, vastly increasing the nation peak hydroelectricity capacity and deploying energy storage at a vast scale."""

text = text.replace(' ', '')
text = text.replace(',', '')
text = text.replace('—', '')
text = text.replace('-', '')
text = text.replace('.', '')
text = text.replace('!', '')
text = text.replace('?', '')
text = text.replace(':', '')
text = text.replace('\n', '')

text = text.upper()
text

output = encrypt(text, ('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'ZEBRASCDFGHIJKLMNOPQTUVWXY'))

crack(output)
