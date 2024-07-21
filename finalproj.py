import requests
import sys
import json

def hangman():
    guess(genranword())


def genranword():
    try:
        api_url = 'https://random-word-api.herokuapp.com/word'
        response = requests.get(api_url).json()[0]
        return response

    except:
        sys.exit("Could not generate a word")


def guess(guessword):
        
    userguess=""
    
    tries=6

    for _ in guessword:
        userguess+="-"


    while(tries>0):
        
        if (userguess == guessword):
            sys.exit(f"\nYOU GUESSED THE WORD!\nTHE WORD WAS : {guessword}")

        user=input(f"YOUR GUESSED WORD: {userguess}\nTRIES LEFT: {tries}\nTURN:")[0]
        
        if(userguess.find(user)>=0):
            print("\nCHARACTER ALREADY GUESSED :(. TRY AGAIN.\n")
            tries-=1
            continue

        if(guessword.find(user)>=0):
            
            indexes=[i for i, x in enumerate(guessword) if x == user]

            user_list = list(userguess)

            for index in indexes:
                user_list[index]=user

            userguess = "".join(user_list)
        
        else:
            print("NOPE! GUESS AGAIN\n")
            tries-=1
            continue
    
    sys.exit(f"\nYOU LOST\nTHE WORD WAS : {guessword}")
    

hangman()