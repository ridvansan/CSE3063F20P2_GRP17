import pandas as pd

class KeyMaker:

    def __init__(self,filename):
        self.filename = filename

    def makeKeys(self):
        keys = pd.read_csv("keys.csv")
        return 0
