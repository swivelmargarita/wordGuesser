import random
from pathlib import Path


class WordGuessGame:
    def __init__(self):
        pass

    def get_words(self, path=Path("/usr/share/dict/american-english"), length=5) -> list:
        words_with_length_n = []
        with open(path) as f:
            for line in f:
                word = str(line).strip().lower()
                if len(word) == length and word.isalpha():
                    words_with_length_n.append(word)
        return words_with_length_n

    def get_random_word(self, words) -> str:
        rand_i = random.randint(0, len(words))
        return words[rand_i]

    def game_loop(self, random_word: str):
        curr_word = ['_'] * len(random_word)
        found_word = False
        attempts = 0
        attempted_words = set()
        while not found_word:
            player_guess = input("Enter your guess:\n")
            attempted_words.add(player_guess)
            if len(player_guess) != 1:
                print("Enter only one character")
                continue
            for i, c in enumerate(random_word):
                if random_word[i] == player_guess:
                    curr_word[i] = player_guess

            attempts += 1
            curr_word_str = ''.join(str(c) for c in curr_word)
            print(curr_word_str, f"Attempts:{attempts}", f"attemted words: {attempted_words}")
            if  curr_word_str == random_word:
                found_word = True





def main():
    game = WordGuessGame()
    random_word = game.get_random_word(game.get_words())
    game.game_loop(random_word)


if __name__ == '__main__':
    main()
