# This program plays a game of Rock, Paper, Scissors between two Players,
# and reports both Player's scores each round.

import random

moves = ['rock', 'paper', 'scissors']


class Player:

    my_move = None
    their_move = None

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = their_move
        self.their_move = their_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        while True:
            choice = input("Your move? ").lower()
            if choice == 'rock':
                break
            elif choice == 'scissors':
                break
            elif choice == 'paper':
                break
            else:
                print("""Invalid choice, please choose rock, paper,
                or scissors.""")
        return choice


class ReflectPlayer(Player):
    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        elif self.their_move in moves:
            return self.their_move


class CyclePlayer(Player):
    def move(self):
        if self.my_move is None:
            return random.choice(moves)
        elif self.my_move == moves[0]:
            return moves[1]
        elif self.my_move == moves[1]:
            return moves[2]
        elif self.my_move == moves[2]:
            return moves[0]


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

        if beats(move1, move2):
            self.p1_score += 1
            print("Player One wins!")
        elif beats(move2, move1):
            self.p2_score += 1
            print("Player Two wins!")
        elif move1 == move2:
            print("You tied!")
        print(f"""The score is Player One: {self.p1_score}\t
             Player Two: {self.p2_score}""")

    def play_game(self):
        print("Game start!")
        round_count = 0
        while True:
            if self.p1_score - self.p2_score == 2:
                print("\nPlayer one has won the game!\n")
                print(f"""Final Score\nPlayer 1: {self.p1_score}
Player 2: {self.p2_score}""")
                break
            elif self.p2_score - self.p1_score == 2:
                print("\nPlayer two has won the game!\n")
                print(f"""Final Score\nPlayer 2: {self.p2_score}
Player 1: {self.p1_score}""")
                break
            else:
                print(f"Round {round_count}:")
                round_count += 1
                self.play_round()
        print("\nGame over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
