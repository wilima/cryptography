import operator
import re

from cryptography import gcd


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


def find_trigram_distances(trigram, text):
    occurrences = [m.start() for m in re.finditer(trigram, text)]
    distance = []

    for j in range(len(occurrences) - 2):
        distance.append(occurrences[j + 1] - occurrences[j])

    return distance


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


def guess_key_length(encrypted):
    trigrams = sort_frequencies(calculate_frequencies_n_size(3, encrypted))

    for trigram in trigrams:
        distances = find_trigram_distances(trigram[0], encrypted)
        gcds = calculate_gcd_from_distances(distances)

        if (len(gcds) == 1) and (1 not in gcds):
            distance = list(gcds)
            break

    return distance


def calculate_gcd_from_distances(distances):
    distances = list(distances)
    gcds = set()

    for d in range(0, len(distances) - 2, 2):
        gcds.add(gcd.gcd(distances[d], distances[d + 1]))

    if (1 not in gcds) and (len(gcds) != 1) and (len(gcds) != len(distances)):
        return calculate_gcd_from_distances(gcds)
    else:
        return gcds


def create_groups_by_key_length(length, encrypted):
    group = []
    for i in range(length):
        subgroup = []
        subgroup.append(encrypted[i])

        for k in range(1, len(encrypted) - 1):
            try:
                subgroup.append(encrypted[i + length * k])
            except Exception as e:
                pass

        group.append(''.join(subgroup))

    return group


def calculate_index_of_coindience(text):
    top = 0
    for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        n = text.count(char)
        tmp = n * (n - 1)

        top += tmp

    result = top / (len(text) * (len(text) - 1))

    return result


def friedman_test(key_length, encrypted):
    groups = create_groups_by_key_length(key_length, encrypted)
    indexes_of_coindience = []

    for group in groups:
        indexes_of_coindience.append(calculate_index_of_coindience(group))

    return indexes_of_coindience


# def guess_key_length():
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

encrypted = encrypt(text, 'PES')

key_length = guess_key_length(encrypted)[0]
key_length
friedman_test(key_length, encrypted)
