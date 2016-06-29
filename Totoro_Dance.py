# coding=UTF-8

import os
import time

dance1 = ["  (\ /)  ", "  (\/)   ", "  (\ /)  ", "   (\/)  "]
dance2 = [" (=0-0=) ", " ( =0-0) ", " (=0-0=) ", " (0-0= ) "]
dance3 = ["<((^^^))>", " ( >(^^)>", "<((^^^))>", "<(^^)< ) "]
dance4 = [" To      ", "   to    ", "     ro  ", " To      ", " Toto    ", " Totoro  "]
timeSig = [0.5, 0.3, 0.5, 0.5, 0.5, 1.7]

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
        
        if timeStep < 5:
            timeStep += 1
        else:
            timeStep = 0
