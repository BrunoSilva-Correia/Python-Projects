import random
import time


class DicesSimulator:
    def __init__(self):
        self.max_value = 6
        self.min_value = 1
        self.dices_quantity = 0
        self.counter = 0
        self.start_message = "Would you like to roll how many dices? "
        self.restart_message = "Would you like to change quantity of dices or reroll?(Y/N) "

    def Initialize(self):
        try: 
            answer = input(self.start_message)
            if(answer):
                self.dices_quantity = int(answer)
                self.GenerateValues()
            else: " Thanks for testing!See ya, baby."
        except:
            print("Please enter a integer number!")
            DicesSimulator.Initialize(self)

    def Restart(self):
        answer = input(self.restart_message)
        if(answer == "N" or not answer):
            print("See your next time! Thanks.")
            time.sleep(5)
        elif(answer == "Y"):
            DicesSimulator.Initialize(self)
        else:
            DicesSimulator.Restart(self)

    def GenerateValues(self):
        print("Generating random values...")
        print("================================")
        for quantity in range(self.dices_quantity):
            # print((quantity + 1) + "°" + random.randint(self.min_value, self.max_value))
            print(f'{(quantity + 1)}° dice: {random.randint(self.min_value, self.max_value)}')
        print("================================")
        self.Restart()


simulation = DicesSimulator()
simulation.Initialize()
