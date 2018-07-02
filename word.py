import json
from difflib import get_close_matches

data = json.load(open("dictionary.json"))

def translate(word):
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes or N if no: " % get_close_matches(word,data.keys())[0])
        if yn == 'Y' or yn == 'y':
            return data[get_close_matches(word,data.keys())[0]]
        elif yn == 'N' or yn == 'n':
            return "Word doesn't exist!"
        else:
            return "We didn't understand your query!"
    else:
        return "Word doesn't exist!"
req = 'Y'
while(req == 'Y'):
    word = input("Enter a word to find:")
    output = translate(word.lower())
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)

    req = input("Care to try one more time? Y for Yes or N for No: ")
print("Goodbye then!!!")