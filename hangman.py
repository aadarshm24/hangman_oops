import random

class Hangman:
    HANGMAN_ART = {
0: ("  +---+", 
            "  |   |", 
            "      |", 
            "      |", 
            "      |", 
            "========="),
        1: ("  +---+", 
            "  |   |", 
            "  O   |", 
            "      |", 
            "      |", 
            "========="),
        2: ("  +---+", 
            "  |   |", 
            "  O   |", 
            "  |   |", 
            "      |", 
            "========="),
        3: ("  +---+", 
            "  |   |", 
            "  O   |", 
            " /|   |", 
            "      |", 
            "========="),
        4: ("  +---+", 
            "  |   |", 
            "  O   |", 
            " /|\\  |", 
            "      |", 
            "========="),
        5: ("  +---+", 
            "  |   |", 
            "  O   |", 
            " /|\\  |", 
            " /    |", 
            "========="),
        6: ("  +---+", 
            "  |   |", 
            "  O   |", 
            " /|\\  |", 
            " / \\  |", 
            "=========")
    }

    def __init__(self, word):
        
        self.word_to_guess = word.lower() 
        self.failed_attempts = 0
        self.game_progress = ["_"] * len(self.word_to_guess)
        self.max_attempts = len(self.HANGMAN_ART) - 1
        self.guessed_letters = set()

    def find_indexes(self, letter):
        return [i for i, char in enumerate(self.word_to_guess) if char == letter]

    def is_invalid_letter(self, user_input):
        return len(user_input) != 1 or not user_input.isalpha()

    def print_game_status(self):
        print("\n**********")
        for line in self.HANGMAN_ART[self.failed_attempts]:
            print(line)
        print("**********")
        print("Word: " + " ".join(self.game_progress))
        print(f"Attempts left: {self.max_attempts - self.failed_attempts}\n")

    def update_progress(self, letter, indexes):
        for i in indexes:
            self.game_progress[i] = letter

    def get_user_input(self):
        return input("Please type a letter: ").lower().strip()

    def play(self):
        while True:
            self.print_game_status()
            guess = self.get_user_input()

            if self.is_invalid_letter(guess):
                print("Invalid input. Please enter a single letter.")
                continue

            if guess in self.guessed_letters:
                print(f"'{guess}' was already guessed.")
                continue

            self.guessed_letters.add(guess)
            indexes = self.find_indexes(guess)

            if indexes:
                self.update_progress(guess, indexes)
            else:
                self.failed_attempts += 1

            if "_" not in self.game_progress:
                self.print_game_status()
                print("Congratulations! You guessed the word!")
                break
            
            if self.failed_attempts >= self.max_attempts:
                self.print_game_status()
                print("Game Over!")
                print(f"The correct word was: {self.word_to_guess}")
                break

if __name__ == "__main__":
    words = ("apple", "banana", "coconut", "pineapple")
    game = Hangman(random.choice(words))
    game.play()