def guess_number_game():
    import random
    while True:
        try:
            low = int(input("Enter the lower bound of the range:"))
            high = int(input("Enter the upper bound of the range:"))
            if low >= high:
                print("Invalid range. The lower bound must be less than the upper bound.")
                continue
            break
        except ValueError:
               print("Invalid input. Please enter valid integers.")
               continue
    number = random.randint(low, high)
    attempts = (high - low) // 10 + 3
    player_attempts = 0
    while True:
        try:
            guess = int(input(f"Guess a number between {low} and {high}, you have {attempts} attempts: "))
            if guess < low or guess > high:
                print(f"Invalid guess. Please enter a number between {low} and {high}.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue
        player_attempts += 1
        attempts -= 1
        if attempts == 0:
            print(f"You have used all your attempts. The number was {number}.")
            break
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Congratulations! You guessed the number {number} in {player_attempts} attempts.")
            break
while True:
    print("Welcome to the Guess the Number Game!")
    guess_number_game()
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    while play_again not in ['yes', 'no']:
        play_again = input("Invalid input. Please enter 'yes' or 'no': ").strip().lower()
    if play_again == 'no':
        print("Thank you for playing! Goodbye!")
        break
    else:
        print("Great! Let's play again.")

    
