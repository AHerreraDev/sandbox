#Simple dictionary like APP
##
import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("data.json"))

word = raw_input("Enter word:")

#Return the meaning of the word that the user submited
def result(w):
	w = w.lower()
	if w in data:
		return data[w]
	elif w not in data:
		closest = get_close_matches(w, data.keys())[0]
		response = raw_input("Did you mean {} instead? If so, type \'y\' to continue: ".format(closest)) 
		if response.lower() == "y":
			output = data[closest]
			if type(output) == list:
				for item in output:
					return item
		elif response.lower() == "n":
			return "Word does not exists"
	else:
		return "Word does not exists"


print result(word)