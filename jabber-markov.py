from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns entire text as one list of words.

    Takes a string that is a file path, opens the file, and turns
    the file's contents into a list of words.
    """

    with open(file_path) as source_text: # opens file as a whole, not line by line
        read_text = source_text.read()
        text = read_text.split()
    return text


def make_chains(text_list):
    """Takes input text as list; returns dictionary of markov chains.

    A chain will be a key that consists of a single word (type string)
    and the value would be a list of the word(s) that follow that
    word in the input list.

    For example:

        >>> make_chains("hi mary, hi juanita")
        {'hi': ['mary', 'juanita'], ('mary,': ['hi']}
    """

    chains = {}

    for index in range(len(text_list) - 1): #doesn't use last word as a key because no value exists
        current_key = text_list[index]
        value_to_add = text_list[index + 1] #each word's value is the word that immediately follows
        
        if current_key in chains:
            chains[current_key].append(value_to_add)
        else:
            chains[current_key] = [value_to_add] #adds value in list so that more values can be added
    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    #randomly chooses first word from all keys, adds to text, and sets as the key to use
    first_key = choice(chains.keys()) #choose first key from list of keys
    text = first_key
    new_key = first_key

    #uses chains dictionary to select next word, then uses next word as key to choose next word
    while new_key in chains: #will stop when reaches last word because it is not a key
        next_word = choice(chains[new_key]) #randomly selects from all possible values at key
        text = text + " " + next_word
        new_key = next_word #last word in text becomes key

    print text


input_path = "jabberwocky.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
