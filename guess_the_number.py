import random

def random_number_generator_game():
    print("\n Welcome to Guess the Number Challenge!")
    print("All you have to do is, GUESS THE SECRET NUMBER...")
    print("Let's Start by seeing your adrenaline rush. Select your difficulty level from the following:")
    print(""" 
    1. Easy
    2. Medium
    3. Hard
    4. Legendary
    (type the number corresponding to the level)
    """)

    levels = {
        1: {"attempts":5, "range": (1,50)},
        2: {"attempts":7, "range": (1,100)}, # type: ignore
        3: {"attempts":10, "range": (1,500)},
        4: {"attempts":10, "range": (100,2000)}
    }
    try:
        level = int(input("Enter a choice (1-4):"))
    except ValueError as e:
        print(f"Invalid input! {e}")
        return
    
    config = levels.get(level)
    if not config:
        print("Please select a level within the range 1-4 only.")
        return
    
    attempts = 0

    max_attempts = config["attempts"]
    secret_number = random.randint(*config["range"])
    
    while attempts < max_attempts:
        try:
            guess = int(input("Make your guess!"))
        except ValueError:
            print("Invalid input! Please enter only a number.")
            continue

        attempts += 1

        if guess < secret_number:
            if secret_number - guess <= 5:
                print(f"Too close! You almost made it. Let's have your next guess! {max_attempts - attempts} attempts remaining!")
            else:
                print(f"Too low! Try a higher number in your next attempt. {max_attempts - attempts} attempts remaining!")
        elif guess > secret_number:
            if guess - secret_number <= 5:
                print(f"Too close! You almost made it. Let's have your next guess! {max_attempts - attempts} attempts remaining!")
            else:
                print(f"Too High! Try a lower number in your next attempt. {max_attempts - attempts} attempts remaining!")
        else:
            print(f"Hurray! You guessed it right in {attempts} attempts.")
            break
        
    else:
        print(f"You couldn't make it! The secret number was {secret_number}. Better Luck next time...")


while True:
    random_number_generator_game()
    again = input("Do you want to play again? (yes/no)").strip().lower()
    if not again.startswith("y"):
        print("Thanks for playing")
        break
    else:
        print("\n Restarting the game \n")