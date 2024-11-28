import re
from collections import Counter
def count_words(text: str) -> dict:
    # remove punctuation
    new_string = re.sub(r'[^\w\s]','', text)  #r'[^\w\s]' is a regular expression
                                              #that find all non-words
    new_string = new_string.lower()

    return Counter(new_string.split())
   
    pass


def find_longest_word(text: str) -> str:
    # remove punctuation
    new_string = re.sub(r'[^\w\s]','', text)  #r'[^\w\s]' is a regular expression
                                              #that find all non-words
    # empty sentence
    if len(new_string.split()) == 0:
        return ""
    
    return max(new_string.split(), key=len)
    pass


def format_sentences(text: str) -> list:
    text = text.replace("\n","") # remove new line
    text = re.sub(r"\s\s+", " ", text) # remove multi spaces

    splittd_sentences = re.split('[.!]', text) # split by dots and !
    splittd_sentences = [el.strip().capitalize()  for el in splittd_sentences if el]
    return splittd_sentences
    pass