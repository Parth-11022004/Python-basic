import random
print("Welcome!")
listt = ['blanket', 'laptop', 'bottle', 'pillow', 'clock', 'notebook', 'water', 'orange', 'pencil', 'cup', 'keyboard', 'lamp', 'book', 'computer', 'fridge', 'paper', 'sofa', 'pen', 'apple', 'window']

word = random.choice(listt)
life = 5

blanks = list("_"*len(word))
print("".join(blanks))

guessed_letters = []

while life!=0 and list(word) != blanks:
    letter = input("Guess a letter\n").lower()
    
    if letter in guessed_letters:
        print("You have already guessed this letter")
        continue
    guessed_letters.append(letter)

    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                blanks[i] = letter
        print("Good guess:","".join(blanks))         

    else:
        life = life - 1
        print(f"Wrong guess! You have {life} lives left")
      
    if list(word) == blanks:
        print("Congrats! You win!!")  
        break

if life == 0:
    print(f"Gave over! The word was {word}")
 