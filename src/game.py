import random


class Rockpaperscissors:
    """Main calss for Rock paper scissors game."""
    def __init__(self, name: str):
        self.choices = ['rock', 'paper', 'scissors']
        self.name = name

    def get_player_choices(self):
        user_choices: str = input(f'Enter your choice: ({self.choices})')
        if user_choices.lower() in self.choices:
            return user_choices


        print(f'Invalid choice, you must select from {self.choices}')
        return self.get_player_choices()


    def get_computer_choices(self):
        """Get computer choice randomly from choices: Rock, Paper, Scissors"""
        return random.choice(self.choices )

    def decide_winner(self, user_choices:str, camputer_choices: str)-> str:
        """Decide the winner of the game based on user and computer choices.
        :param user_chisecs: The choice of the user.
        :param computer_choice: The choice of the computer.
        :return: The result of the game. (who won!)
        """
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
