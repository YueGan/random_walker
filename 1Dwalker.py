from Tkinter import *
from scipy.stats import bernoulli
import time
import math


class State():

    def __init__(self):
        self.CURRENT_STATE = 0
        self.TIME_ELAPSE = 1
        self.PROBABILITY = 0.5
        self.LAST_ONE_STATE = 0
        self.LAST_TWO_STATE = 0
        self.DIST_FROM_ORIGIN = 0

    def get_states(self):

        return [self.CURRENT_STATE, self.LAST_ONE_STATE, self.LAST_TWO_STATE]

    def set_states(self, increments):

        self.LAST_TWO_STATE = self.LAST_ONE_STATE
        self.LAST_ONE_STATE = self.CURRENT_STATE
        self.CURRENT_STATE += increments
        self.DIST_FROM_ORIGIN += increments

    def get_time_elapse(self):

        return self.TIME_ELAPSE

    def set_time_elapse(self, power):

        self.TIME_ELAPSE/(math.pow(2, power))

    def get_probability(self):

        return self.PROBABILITY

    def set_probability(self, newprob):

        self.PROBABILITY = newprob





def GUI():
    # blank window
    root = Tk()

    frame = Frame(root, height=400, width=600)

    frame.pack()
    root.mainloop()

def main():

    #GUI()

    newgame = State()

    while True:
        time.sleep(newgame.get_time_elapse())

        print(newgame.get_states())

        if bernoulli.rvs(newgame.get_probability()):
            newgame.set_states(1)
        else:
            newgame.set_states(-1)

    print("end")


if __name__ == "__main__":

    main()