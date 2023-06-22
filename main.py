import json
import random
from testtracker import TestTracker


MAX_LIVES = 3
MORSE_DICT_DIR = "data.json"
ENGLISH_DICT_DIR = "english_dictionary.csv"


def getDict():
	with open(MORSE_DICT_DIR) as f:
		return json.load(f)


def getWords():
	with open(ENGLISH_DICT_DIR) as f:
		return f.read().splitlines()


if __name__ == "__main__":
	morseDict = getDict()
	words = getWords()
	resultTracker = TestTracker(0)
 
	try:
		while True:
			randomWord = random.choice(words)
			morseWord  = ' '.join([morseDict[c] if c.isalnum() else '' for c in randomWord.lower()])
			userGuess  = ""
			tries = MAX_LIVES
			print(f"Type this word in morse: {randomWord}")
	
			while tries > 0 and userGuess != morseWord:
				#print(morseWord)
				userGuess = input(f"({tries} left)\n")
				tries -= 1
					
			if tries > 0:
				resultTracker.incCount(1)
				print(TestTracker.wrapColor("Correct", "OKGREEN"))
			else:
				resultTracker.incCount(0)
				print(TestTracker.wrapColor("Incorrect. ", "ERRORRED") + f"\nThe awnser was: {morseWord}")
	
			print(resultTracker.getResults() + '\n')
	except:
		print("Closing...")