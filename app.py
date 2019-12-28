import json
from difflib import get_close_matches 

data = json.load(open("data.json"))

def WordInDictionary(term):
    if term.lower() in data:
        return data[term.lower()]
    
    elif term.upper() in data:
        return data[term.upper()]
    
    elif term.title() in data:
        return data[term.title()]

#get_close_matches returns the good enough matches based on user input, then suggests that word to the user.
    elif len(get_close_matches(term, data.keys())) > 0:
        response = input(term + " is not a word in the dictionary.  Did you mean %s instead? (Y/N): " % get_close_matches(term, data.keys())[0])
        if response == 'Yes' or response == 'Y' or response == 'yes' or response == 'y':
            return data[get_close_matches(term, data.keys())[0]]
        elif response == 'No' or response == 'N' or response == 'no' or response == 'n':
            return "The word you entered either doesn't exist in the dictionary or your spelling is incorrect."
        else:
            return "That word is not in the dictionary."
    else:
        return "That word is not in the dictionary."

prompt = input("Enter a word: ")

#To ensure that only the definitions of a word are only printed out on an induvidual line
output = WordInDictionary(prompt)
if type(output) == list:
    for iterator in output:
        print(iterator)