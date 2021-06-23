"""
Reverse:
The user is presented with a sequence of numbers from 1 to 9, the aim of 
the game is to arrange the numbers in 123456789 sequence 
in as short moves as possible.
 
@author Sukhbinder
"""
import random

class Reversi():
    def __init__(self):
        self.x = list(range(1,10))
        self.b = list(range(1,10)) 

    def _intro(self):
        print() 
        print("Welcome to Reverse:")
        print("The user is presented with a sequence of numbers ")
        print("from 1 to 9, the aim of the game is to arrange ")
        print("the numbers in 123456789 sequence in as short moves")
        print("as possible.")
        print()
    
    
    def ch(self, n):
        self.x[:n] = self.x[n-10::-1]

    def level(self,stage):
        for i in range(stage+3):
            j = random.randrange(1,10)
            self.ch(j)
 
    def run(self):
        self._intro()
        ans=1
        stage=1
        while (ans == 1):
            turns=0
            self.level(stage)
            print("Level:",stage,"Min. Turns:",stage+3)
            while (self.x != self.b):
                print(self.b, "\a")
                print(self.x , " <= ")
                try:
                    num= eval(input('Enter num:'))
                except NameError:
                    print ("Not a valid number")
                    return True
                self.ch(num)
                turns +=1
            print("S O L V E D !")
            print(self.x)
            print("You took ",turns,"turns")
            stage +=1
            try:
                ans = eval(input('Press 1 to Play Next Level: '))
            except NameError:
                print("Exiting...")

def main():
    game = Reversi()
    game.run()


if __name__ == "__main__":
    main()