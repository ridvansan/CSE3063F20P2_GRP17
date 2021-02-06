#ClassName:KeyMaker
#NumberofMethods:2
#NumberofDomainMehods:1
#LineOfCodes:17
#isDomain:False

import pandas as pd
from models.Key import Key
from models.Poll import Poll
from models.Question import Question
import os

class KeyMaker:

    def __init__(self, directory):
        self.directory = directory

    def makeKeysinDirectory(self):
        pollka = []
        keys = os.listdir(self.directory)
        for key in keys:
            self.makeKeys(key)
        return pollka

    def makeKeys(self, filename):
        pollName = ""
        questionName = ""
        answers = []
        polls = []
        questions = []
        question = ""
        pollID = 0
        questionID = 0
        file = open(self.directory + "/" + filename, "r")
        lines = file.readlines()

        for line in lines:
            if line == "\n":
                continue
            elif line[0:8] == "You have":
                pollCount = 15
            elif line[0:5] == "Title":
                title = line[6:]
            elif line[1:5] == "Poll":
                pollID = int(line.split(":")[0].split()[1]) - 1
                print(pollID)
                polls.append(Poll(line, []))
            elif line[0].isdigit():
                questionID = int(line.split(".")[0]) - 1
                polls[pollID].addToQuestionList(Question(line))

            elif line[0:6] == "Answer":
                polls[pollID].questionlist[questionID].appendToKeys(Key(line))




