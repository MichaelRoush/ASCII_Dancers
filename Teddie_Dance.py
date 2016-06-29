# coding=UTF-8

import os
import time

dance1 = ["  O , O  ", "  O ,O   ", "  O , O  ", "   O, O  "]
dance2 = [" ( O◡O ) ", " (  O◡O) ", " ( O◡O ) ", " (O◡O  ) "]
dance3 = ["<( |:| )>", " ( >|:|)>", "<( |:| )>", "<(|:|< ) "]
dance4 = ["  Ev     ", "  Every  ", "  Day's  ", "  Great  ", "   At    ", "  Your   ", "  Ju     ", "  Junes  "]
timeSig = [0.3, 0.3, 0.6, 0.6, 0.6, 0.6, 0.6, 1.2]

if __name__ == "__main__":
    counter = 0
    timeStep = 0
    while True:
        os.system('clear')
        print(dance1[counter])
        print(dance2[counter])
        print(dance3[counter])
        print(dance4[timeStep])
        if counter < 3:
            counter += 1
        else:
            counter = 0

        time.sleep(timeSig[timeStep])
        if timeStep < 7:
            timeStep += 1
        else:
            timeStep = 0

