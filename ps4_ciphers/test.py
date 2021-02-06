import string
### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###
shift = 1
lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)
encryption_dict = {}
for i in range(len(lower)):
    encryption_dict[lower[i]] = lower[i+shift-26]
for i in range(len(upper)):
    encryption_dict[upper[i]] = upper[i+shift-26]
#return encryption_dict
message_text_encrypted="hello"
message_text_encrypted2=""
#encryption_dict = {}
#encryption_dict = build_shift_dict(shift)
for char in message_text_encrypted:
    if str.isalpha(char) is True:
        message_text_encrypted2 = message_text_encrypted2 + encryption_dict.get(char)
    else:
        message_text_encrypted2 = message_text_encrypted2 + char
print(message_text_encrypted)
print(message_text_encrypted2)

