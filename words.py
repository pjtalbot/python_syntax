# For a list of words, print out each word on a separate line, but in all uppercase. How can you change a word to uppercase? Ask Python for help on what you can do with strings!

# capitalize or upper?



# Turn that into a function, print_upper_words. Test it out. (Don’t forget to add a docstring to your function!)

myList = ['hi', 'you', 'there']

def print_upper_words(word_list):

    for word in word_list:
        cap = word.upper()
        print(cap)


# Change that function so that it only prints words that start with the letter ‘e’ (either upper or lowercase).

def print_only_caps(word_list):
    for word in word_list:
        if word == word.capitalize():
            print(word)


myList2 = ['Hi', 'hi', "You", "you"]

print_only_caps(myList2)

# Make your function more general: you should be able to pass in a set of letters, and it only prints words that start with one of those letters.

def print_words_starting_with(word_list, letter):
    for word in word_list:
        word
        if word.startswith(letter) or word.startswith(letter.upper()):
            print(word)

myList3 = ['Hey', 'you', 'there', 'honey']

print_words_starting_with(myList3, 'h')

