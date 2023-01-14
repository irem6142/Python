import json
from difflib import get_close_matches as match
data=json.load(open("data.json"))
def dictionary(word):
    word=word.lower()
    if word in data:
     return data[word]
    elif (len(match(word,data.keys(),cutoff=0.8))>0):#liste dönüyor ona en yakın kelimeleri seçiyor
        answer=input("Did you mean %s ?Y/N:" % match(word,data.keys())[0])
        if(answer=="Y"):
            return data[match(word,data.keys())[0]]
        elif answer=="N":
            return "Unfortunately"
        else:
            return "Error!"
    else:
      return "The word doesn't exist"

word=input("Enter word:")
output=dictionary(word)
if type(output)==list:
    for i in output:
        print(i)
else:
    print(output)
