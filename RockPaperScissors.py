"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random
moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:

    def __init__(self):
        self.my_move = ""
        self.their_move = ""

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move

# creates a random player as your opponents and determines it's moves


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

# is responsible for taking the users input(moves)


class HumanPlayer(Player):
    def move(self):
        while True:
            response = input(f"Rock, paper, scissors? > ").lower()
            if response not in moves:
                print("illegal move, pls choose again")
            else:
                return response

# creates an opponent with the ability to choose based on the user's last
# move


class ReflectPlayer(Player):
    def move(self):
        if self.their_move != '':
            return self.their_move
        else:
            return random.choice(moves)

# creates an opponent with an ability to choose based on it's own last move


class CyclePlayer(Player):
    def move(self):
        if self.my_move == 'rock':
            return 'paper'
        elif self.my_move == 'paper':
            return 'scissors'
        elif self.my_move == 'scissors':
            return 'rock'
        else:
            return random.choice(moves)


Opponents = [CyclePlayer(), ReflectPlayer(), RandomPlayer()]

""" The beats function is used to decide when a player has won or lost"""


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    # sets the blueprint for the player and their scores to be created
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1score = 0
        self.p2score = 0

# this function is responsible for updating the scores for each round
# it compares the moves for the player and the opponent, determines whether it
# was a win, draw or loss for them and updates the scores for each round
# it also stores both players moves for each round and makes the reflect
# and cycle player options possible

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if beats(move1, move2):
            print(f"Player one wins")
            self.p1score += 1
        elif beats(move2, move1):
            print(f"Player two wins")
            self.p2score += 1
        else:
            print("It was a draw")
        print(f"Score: Player one {self.p1score},"
              f" Player Two {self.p2score}")

# this function is responsible for starting the game, determining
# the duration of the game and ending the game

    def play_game(self):
        try:
            rounds = int(input("How many rounds? (1-5) > "))
            if rounds in range(1, 5):
                print("Game start!")
                for round in range(rounds):
                    print(f"Round {round}:")
                    self.play_round()
                if self.p1score > self.p2score:
                    print("Congratulations! You Won!\n")
                elif self.p2score > self.p1score:
                    print("Sorry you lost... "
                          "better luck next time!\n")
                else:
                    print(f"The game was a tie!\n")
                    print(f"FINAL SCORE:"
                          f" Player One {self.p1score}\n"
                          f"Player Two {self.p2score}\n")
                endOfGame = input("Input Yes to play again\n").lower()
                if endOfGame == "y" or endOfGame == "yes":
                    self.p1score = 0
                    self.p2score = 0
                    self.play_game()
                elif endOfGame != "y" or endOfGame != "yes":
                    print("Goodbye, Thanks for playing")
                    exit()
            else:
                print("Invalid input: enter a number between 1 and 5")
                self.play_game()

        except ValueError:
            print("Invalid input: enter a number between 1 and 5")
            self.play_game()


if __name__ == '__main__':
    game = Game(HumanPlayer(), random.choice(Opponents))
    game.play_game()
