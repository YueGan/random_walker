from Tkinter import *
from scipy.stats import bernoulli
import time
import math
import datetime


class State():

    def __init__(self):
        self.CURRENT_STATE = 50
        self.TIME_ELAPSE = 1
        self.PROBABILITY = 0.5
        self.LAST_ONE_STATE = 50
        self.LAST_TWO_STATE = 50
        self.DIST_FROM_ORIGIN = 0
        self.WIN = 100
        self.LOSE = 0

    def get_states(self):

        return [self.CURRENT_STATE, self.LAST_ONE_STATE, self.LAST_TWO_STATE]

    def set_states(self, increments):

        self.LAST_TWO_STATE = self.LAST_ONE_STATE
        self.LAST_ONE_STATE = self.CURRENT_STATE
        self.CURRENT_STATE += increments
        self.DIST_FROM_ORIGIN += increments

    def get_time_elapse(self):

        return self.TIME_ELAPSE

    def set_time_elapse(self):

        self.TIME_ELAPSE += 1

    def get_probability(self):

        return self.PROBABILITY

    def set_probability(self, newprob):

        self.PROBABILITY = newprob

    def win_or_lose(self):

        return self.CURRENT_STATE == self.WIN or self.CURRENT_STATE == self.LOSE


def GUI():

    newAnimation = State()

    # blank window
    root = Tk()
    root.title("1D Random Walker")
    root.resizable(width=False, height=False)

    frameAnimation = Frame(root, height=400, width=400, bg='blue')
    frameAnimation.pack_propagate(0)
    frameText = Frame(root, height=400, width=200, bg='red')
    #Do not let children control the size of windows
    frameText.pack_propagate(0)
    frameAnimation.pack(side=LEFT, fill=BOTH)
    frameText.pack(side=RIGHT, fill=BOTH)

    labelCurState = Label(frameText)
    labelCurState.pack()
    labelPrevOneState = Label(frameText)
    labelPrevOneState.pack()
    labelPrevTwoState = Label(frameText)
    labelPrevTwoState.pack()
    labelTimeElapsed = Label(frameText)
    labelTimeElapsed.pack()
    labelProbability = Label(frameText)
    labelProbability.pack()


    canvas = Canvas(frameAnimation, height=80, width=80)
    canvas.create_oval(10, 10, 80, 80, outline="black", fill="black")
    canvas.pack(fill=BOTH, expand=True)
    canvas.place(relx=1, x=newAnimation.get_states()[0], y=1, anchor=CENTER)


    def clock():

        # Bernoulli probability
        if bernoulli.rvs(newAnimation.get_probability()):
            newAnimation.set_states(1)
        else:
            newAnimation.set_states(-1)

        newAnimation.set_time_elapse()

        # Fetch current states, time, and probability
        currentState = "Current State: " + str(newAnimation.get_states()[0])
        prevOneState = "Previous 1 State: " + str(newAnimation.get_states()[1])
        prevTwoState = "Previous 2 State: " + str(newAnimation.get_states()[2])
        timeElapsed = "Time: " + str(newAnimation.get_time_elapse())
        probability = "Probability: " + str(newAnimation.get_probability())

        # Update current states
        labelCurState.config(text=currentState)
        labelPrevOneState.config(text=prevOneState)
        labelPrevTwoState.config(text=prevTwoState)
        labelTimeElapsed.config(text=timeElapsed)
        labelProbability.config(text=probability)
        canvas.place(relx = 0.5, rely = 0.5, x=0 + newAnimation.get_states()[0], y=0, anchor=SE)

        if(newAnimation.win_or_lose() == False):
            root.after(100, clock)
        else:
            return 0

    clock()

    root.mainloop()

def main():

    GUI()

    #
    # newgame = State()
    #
    # while True:
    #     time.sleep(newgame.get_time_elapse())
    #
    #     print(newgame.get_states())
    #
    #     if bernoulli.rvs(newgame.get_probability()):
    #         newgame.set_states(1)
    #     else:
    #         newgame.set_states(-1)

    print("end.")


if __name__ == "__main__":

    main()
