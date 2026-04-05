import random  # random module for selecting a word

# Step 1: Predefined list of words
words = ["python", "apple", "chair", "table", "mouse"]

# Step 2: Randomly select a word
word = random.choice(words)

# Step 3: Create blank spaces for each letter
guessed_letters = ["_"] * len(word)

# Step 4: Set number of attempts
attempts = 6

print(" Welcome to Hangman Game!")

# Step 5: Main game loop
while attempts > 0 and "_" in guessed_letters:
    
    # Display current word status
    print("\nWord:", " ".join(guessed_letters))
    print("Attempts left:", attempts)
    
    # Take user input
    guess = input("Enter a letter: ").lower()
    
    # Check if input is valid (only one letter)
    if not guess.isalpha() or len(guess) != 1:
        print(" Please enter a single valid letter!")
        continue
    
    # Check if guessed letter is in the word
    if guess in word:
        print("✅ Correct guess!")
        
        # Update guessed letters
        for i in range(len(word)):
            if word[i] == guess:
                guessed_letters[i] = guess
    else:
        print("❌ Wrong guess!")
        attempts -= 1  # decrease attempts

# Step 6: Final result
if "_" not in guessed_letters:
    print("\n🎉 You won! The word was:", word)
else:
    print("\n💀 Game Over! The word was:", word)