import random

class WordGuessingGame:
    def __init__(self, words):
        self.words = words
        self.word_to_guess = ""
        self.attempts = 0
        self.max_attempts = 5
        self.score = 0

    def choose_random_word(self):
        return random.choice(self.words)

    def start_game(self):
        print("Welcome to the Advanced Word Guessing Game!")
        while True:
            self.word_to_guess = self.choose_random_word()
            self.attempts = 0
            print(f"You have {self.max_attempts} attempts to guess the word. Let's begin!")
            while self.attempts < self.max_attempts:
                guess = input("Guess the word: ").lower()
                self.attempts += 1
                if guess == self.word_to_guess:
                    print("Congratulations! You guessed the word correctly.")
                    self.score += 1
                    break
                else:
                    print("Incorrect guess. Try again!")

            if self.attempts == self.max_attempts:
                print(f"Out of attempts. The word was '{self.word_to_guess}'.")

            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != 'yes':
                print(f"Your final score: {self.score}")
                break

if __name__ == "__main__":
    words_to_use = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
    game = WordGuessingGame(words_to_use)
    game.start_game()

