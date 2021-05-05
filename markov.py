"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    file_string = ""

    with open(file_path) as file:
        for line in file:
            line = line.rstrip()
            file_string += line + " "

    return file_string


def make_chains(text_string, n):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]

    """

    chains = {}
    text_string_list = text_string.split()

    for i in range(len(text_string_list)-n):
        ref_tuple = ()
        for num in range(n):
            ref_tuple += (text_string_list[i+num],)
        word = text_string_list[i+n]
        
        if ref_tuple in chains:
            chains[ref_tuple].append(word)
        else:
            chains[ref_tuple] = [word]
    
    return chains


def make_text(chains, n):
    """Return text from chains."""

    words = []

    while True:
        random_key = choice(list(chains.keys()))
        if random_key[0][0].isupper() and random_key[0][0].isalpha():
            break

    for i in range(n):
        words.append(random_key[i])
    
    while True:
        initial_key = ()
        for num in range(-n, 0):
            initial_key += (words[num],)

        if initial_key in chains.keys():
            words.append(choice(chains[initial_key]))
        else:
            break

    return ' '.join(words)


input_path = input("Please enter the file path > ")

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, 3)

# Produce random text
random_text = make_text(chains, 3)

print(random_text)
