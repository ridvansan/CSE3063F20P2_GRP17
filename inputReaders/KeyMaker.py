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
        polls = []
        keys = os.listdir(self.directory)
        for key in keys:
            self.makeKeys(key)
        return polls

    def makeKeys(self, filename):
        file = open(self.directory + "/" + filename, "r")
        lines = file.readlines()
        lineIndex = 0
        pollCount = lines[lineIndex]
        lineIndex += 1
        title = lines[lineIndex]
        lineIndex += 1
        polls = []
        while lineIndex < len(lines):
            if lines[lineIndex] == "\n":
                lineIndex += 1
                continue
            elif lines[lineIndex][1:5] == "Poll":
                pollLine = lines[lineIndex].split(":")[1]
                pollName = pollLine.split("\t")[0]
                pollQuestionCount = pollLine.split("\t")[1]
                yesNo = pollLine.split("\t")[2]
                lineIndex += 1
                questions = []
                while True:

                    if lines[lineIndex] == "\n":
                        lineIndex += 1
                        continue

                    if lines[lineIndex][0].isdigit():
                        questionName = lines[lineIndex][3:]
                        lineIndex += 1
                        keys = []
                        while True:

                            if lines[lineIndex] == "\n":
                                lineIndex += 1
                                continue
                            elif lines[lineIndex][0:6] == "Answer":

                                keys.append(Key(lines[lineIndex][10:]))
                                lineIndex += 1
                            else:
                                question = Question(questionName)
                                question.keys = keys
                                questions.append(question)
                                break

                    else:
                        polls.append(Poll(pollName, questions))
                        break


