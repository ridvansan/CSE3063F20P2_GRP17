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
            polls.extend(self.makeKeys(key))
        return polls

    def makeKeys(self, filename):
        file = pd.read_excel(self.directory + "/" + filename, index_col=None, header=None)
        i = -1
        polls = []
        for row in range(0, file.shape[0]):
            if pd.isnull(file.iat[row, 1]):
                polls.append(Poll(file.iat[row, 0], []))
                i += 1
            else:
                question = Question(file.iat[row, 0])
                key = Key(file.iat[row, 1])
                question.keys.append(key)
                polls[i].questionlist.append(question)

        return polls


