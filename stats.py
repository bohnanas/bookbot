# function to count the number of words in a string
def word_counter(string):
    words = string.split()

    return len(words)

# function that counts the number of times each character appears in a string
def char_counter(string):
    # create empty dictionary for each char
    chars = {}

    # iterate over each char in the string
    for char in string:
        # if uppercase char, make it lowercase
        if char.isupper():
            char = char.lower()
        # check to see if char matches in dictionary
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

    return chars

# function that sorts the char dictionary from greatest to least count (TO DO)
def sorter(dict):
    # turn the dictionary into a list of dictionaries
    list = []
    for char, count in dict.items():
        list.append({char: count})

    # sort the list of dictionaries by their values
    list.sort(reverse=True, key=sorter_helper)

    return list

# gets the value from the key even though we don't know what the key will be at the time
def sorter_helper(dict):
    return list(dict.values())[0]