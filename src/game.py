import random


class Rockpaperscissors:
    def __init__(self, name):
        self.choices = ['rock', 'paper', 'scissors']
        self.name = name

    def get_player_choices(self):
        user_choices = input(f'Enter your choice: ({self.choices})')
        if user_choices.lower() in self.choices:
            return user_choices


        print(f'Invalid choice, you must select from {self.choices}')
        return self.get_player_choices()


    def get_computer_choices(self):
        return random.choice(self.choices )

    def decide_winner(self, user_choices, camputer_choices):
        if user_choices == camputer_choices:
            return "it's Tie!"

        win_combinations = [('rock', 'scissors'),('paper', 'rock'), ('scissors', 'paper')]
        for win_comb in win_combinations:
            if (user_choices == win_comb[0]) and (camputer_choices == win_comb[1]):
                return 'Players win!'


        return 'oh no! the camputer won'



    def play(self):
        user_choices = self.get_player_choices()
        computer_choices = self.get_computer_choices()
        print(f'Computer choice: {computer_choices}')
        print(self.decide_winner(user_choices, computer_choices))


if __name__ == '__main__':
    game = Rockpaperscissors('hirad')

    while True:
        game.play()

        continue_game = input('Do you want play again? (enter any key to paly again, enter q to exit!')
        if continue_game.lower() == 'q':
            break
