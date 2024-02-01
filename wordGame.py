import random

file = open("fullformsliste.txt", "r")
lines = file.readlines()

words = [x.split("\t")[2] for x in lines if x.split("\t")[2][0] != "-"]
words.pop(0) # remove header word

chosenWord = random.choice(words)
lengthOfChosenWord = len(chosenWord)

censoredWord = ""
for i in  range(lengthOfChosenWord):
    censoredWord += "-"

print(f"Your word has {lengthOfChosenWord} letters")
print(f"Word: {censoredWord}")

userInput = ""
while userInput != chosenWord:
    userInput = input("Guess the word: ")
    
    if userInput == "0":
        break
    
    for char in userInput:
        try:
            index = chosenWord.index(char)
        except:
            continue

file.close()