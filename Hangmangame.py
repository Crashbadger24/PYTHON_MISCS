import random
with open('words_list.txt','r') as f:
    words= f.readlines()
word=random.choice(words)[:-1]
allowed_errors=7

guessed_letters=[]
done=False

while not done:
    for letter in word:
       if letter.lower() in guessed_letters:
            print(letter.upper(),end=" ")
       else:
           print("_",end=" ")
    print("")
    

    guess = input(f"Allowed Errors left {allowed_errors},Next Guess: ")
    guessed_letters.append(guess.lower())
    if guess.lower() not in word.lower():
        allowed_errors-=1
        if allowed_errors==0:
            break

    done=True 
    for letter in word:
        if letter.lower() not in guessed_letters:
            done=False    
if done:
    print(f"Congrats .\n The word was {word.upper()}")
else :
    print(f"You failed. The word was  {word.upper()} ")