import random
from nwords import shapes, randoms,animals,birds,colors,city


def get_word_animal():
    word = random.choice(animals)
    return word.upper()
def get_word_birds():
    word = random.choice(birds)
    return word.upper()
def get_word_colors():
    word = random.choice(colors)
    return word.upper()
def get_word_city():
    word = random.choice(city)
    return word.upper()
def get_word_shapes():
    word = random.choice(shapes)
    return word.upper()
def get_word_random():
    word = random.choice(randoms)
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hangman! You are provided with 6 tries to guess the word!!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: \n").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter\n", guess)
            elif guess not in word:
                print(guess, "is not in the word.\n")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("**********Good job,", guess, "is in the word!**********")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word\n", guess)
            elif guess != word:
                print(guess, "is not the word.\n")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.\n")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("**********Congrats, you guessed the word! You win!**********")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!\n")


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def main():
    print("----------HANGMAN----------\n")
    play_again="Y"
    while(play_again == "y" or  play_again=="Y"):
        print("Choose any topic\n 1.animals\n 2.birds\n 3.colors\n 4.city\n 5.shapes\n 6.Any random word\n")
        ch = int(input())
        if ch==1:
             word = get_word_animal()
             play(word)
        elif ch ==2:
            word = get_word_birds()
            play(word)
        elif ch ==3:
            word = get_word_colors()
            play(word)
        elif ch ==4:
            word = get_word_city()
            play(word)
        elif ch ==5:
            word = get_word_shapes()
            play(word)
        elif ch==6:
            word = get_word_random()
            play(word)
        else:
            print("Invalid option\n")
        play_again=input("Play Again? (Y/N) ")


if __name__ == "__main__":
    main()
