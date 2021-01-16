import pandas as pd

from models.Key import Key
from models.Poll import Poll
from models.Question import Question

class KeyMaker:

    def __init__(self,filename):
        self.filename = filename

    def makeKeys(self):
        file = pd.read_excel(self.filename, index_col=None, header=None)
        i= -1
        polls = []
        for row in range(0,file.shape[0]):
            if pd.isnull(file.iat[row,1]):
                polls.append(Poll(file.iat[row,0],[]))
                i += 1
            else:
                question = Question(file.iat[row,0])
                key = Key(file.iat[row,1])
                question.keys.append(key)
                polls[i].questionlist.append(question)

        return polls


