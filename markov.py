from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    with open(file_path) as source_text:
        read_text = source_text.read()
        text = read_text.split()
    return text


def make_chains(text_string):
    """Takes input text as string; returns dictionary of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}

    for index in range(len(text_string)-2):
        current_key = (text_string[index], text_string[index+1])
        value_to_add = text_string[index + 2]
        
        if current_key in chains:
            chains[current_key].append(value_to_add)
        else:
            chains[current_key] = [value_to_add]
    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    first_key = choice(chains.keys())
    text = first_key[0] + " " + first_key[1]
    new_key = first_key

    while new_key in chains:
        next_word = choice(chains[new_key])
        text = text + " " + next_word
        new_key = (new_key[1], next_word)

    print text


input_path = "gettysburg.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
