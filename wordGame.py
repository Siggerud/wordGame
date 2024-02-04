import psycopg2
import random
from dotenv import load_dotenv
import os

def get_connection():

    load_dotenv()
    # Login details for database user
    host = os.getenv("host")
    dbname = os.getenv("dbname")
    user = os.getenv("user")
    port = os.getenv("port")
    pwd = os.getenv("pwd")

    # Gather all connection info into one string
    connection = \
        "host='" + host + "' " + \
        "dbname='" + dbname + "' " + \
        "user='" + user + "' " + \
        "port='" + port + "' " + \
        "password='" + pwd + "'"
        
    conn = psycopg2.connect(connection) # Create a connection
    
    return conn
                  

def get_all_words():
    conn = get_connection()

    cur = conn.cursor()

    # get all words where length is 3 or more
    cur.execute("SELECT word FROM words WHERE LENGTH(word) >= 3")

    # get all results from query
    rows = cur.fetchall() 

    return rows
  
  
def get_word(words):
    return random.choice(words)[0]
   
   
def get_censored_word(word):
    lengthOfWord = len(word)

    censoredWord = ""
    for i in  range(lengthOfWord):
        censoredWord += "-"
        
    return censoredWord
   
   
def present_word(word):
    print(f"Your word has {len(word)} letters")
    print(f"Enter q to generate new word, enter e to exit")
    
    
def add_indices_for_matching_characters(userInput, chosenWord):
    for i in range(len(userInput)):
        char1 = userInput[i]
        for j in range(len(chosenWord)):
            char2 = chosenWord.lower()[j]
            if char1 == char2:
                indices.append(j)


def get_new_censored_word(censoredWord, chosenWord):
    newCensoredWord = ""
    for k in range(len(censoredWord)):
        if k in indices:
            newCensoredWord += chosenWord[k]
        else:
            newCensoredWord += "-"
    
    return newCensoredWord


words = get_all_words()

chosenWord = get_word(words)
print(chosenWord)
censoredWord = get_censored_word(chosenWord)

present_word(chosenWord)

indices = []
tryCount = 0
treshold = 8
userInput = ""
while True:
    if censoredWord == chosenWord or tryCount == treshold:
        if censoredWord == chosenWord:
            print(f"Congratulations, you correctly guessed the word '{chosenWord}'")
        elif tryCount == treshold:
            print(f"You've used max number of tries. The word is '{chosenWord}'")
                
        userInput = ""
        while userInput != "q" and userInput != "e":
            print(f"Enter q to generate new word, enter e to exit") 
            userInput = input("Input: ")
            
        if userInput == "e":
            break
        else:
            indices = []
            tryCount = 0
            chosenWord = get_word(words)
            censoredWord = get_censored_word(chosenWord)
            
            present_word(chosenWord)

    print(f"Word: {censoredWord}")
    userInput = input("Guess the word: ").lower()

    if userInput == "e":
        break
    elif userInput == "q":
        indices = []
        tryCount = 0
        chosenWord = get_word(words)
        censoredWord = get_censored_word(chosenWord)
        
        present_word(chosenWord)
        continue
    
    add_indices_for_matching_characters(userInput, chosenWord)
    
    indices = list(dict.fromkeys(indices)) # remove duplicates from indices
    
    censoredWord = get_new_censored_word(censoredWord, chosenWord)

    tryCount += 1
    
    if censoredWord != chosenWord and tryCount != treshold:
        numberOfTriesLeft = treshold - tryCount
        print(f"You have {numberOfTriesLeft} tries left\n")
        
