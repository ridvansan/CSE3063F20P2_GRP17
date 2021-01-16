import pandas as pd
from Poll import Poll

class KeyMaker:

    def __init__(self,filename):
        self.filename = filename

    def makeKeys(self):
        key = pd.read_excel(self.filename,index_col=None,header=None)
        #key = key.rename(columns={"0": "Question", "1": "Answer"})
        print(key.shape[0])

        headerRows = []
        polls = []
        for row in range(0,key.shape[0]):
            if pd.isnull(key.iat[row,1]):
                poll = Poll(key.iat[row,0])
        return 0

k = KeyMaker("assets/answer_monday.xlsx")
k.makeKeys()