import json
from difflib import get_close_matches as gcm
data=json.load(open('076 data.json','r'))

def translate(word):
    if word.lower() in data:
        return data[word]
    elif len(gcm(word, data.keys())) > 0:
        yn=input("Did you mean {} instead? Enter Y if yes, N if no: ".format(gcm(word, data.keys())[0])).upper()
        if yn=="Y":
            return data[gcm(word, data.keys())[0]]
        elif yn=="N":
            return "The word doesn't exist. Please double check it."
        else:
            return "Invalid Input"
    else:
        return "The word doesn't exist. Please double check it."

new_word= input("Enter word: ")

output=translate(new_word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
