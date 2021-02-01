import json
from difflib import get_close_matches

data = json.load(open("data.json"))

# Vraca rec iz recnika (dictionary-ja) koju korisnik unese
def translate(word):
    # Da svaka uneta rec bude malim slovima (da se ne unese RAIN)
    word = word.lower()
    if word in data:
        return data[word]
    # Ukoliko imamo imena gradova npr Belgrade da ne bi to stavljao kao malo belgrade posto ga nece naci u data nego da ostane Belgrade
    elif word.title() in data:
        return data[word.title()]
    # Ukoliko imamo USA ili NATO pa da bi mogao i za takve reci da pronadje adekvatne opise
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        # Data.keys()[0] znaci da vraca samo prvu predlozenu vrednost pa ce biti: Did you mean rain instead npr
        decision = input("Did you mean %s instead? Enter Y if yes or N if no: " % get_close_matches(word, data.keys())[0])
        if decision == 'Y':
            return data[get_close_matches(word, data.keys())[0]]
        elif decision == "N":
            return "The word does not exist. Please, check it."
        # Ukoliko korisnik ne unese ni Y ni N nego neko trece slovo
        else:
            return "We did not understand your entry."
    else:
        return "The word does not exist in current data dictionary"


user_word = input("Please, enter your word: ")

output = translate(user_word)

# Ako zadata rec ima vise linija objasnjenja onda je to lista i ispis bude [dfdsf,fasdf] tako da for petljom ispisemo
# liniju po liniju iz te liste a ako je obican string tj objasnjenje ima samo jednu recenicu onda samo ispisemo string
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)


