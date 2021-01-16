import pandas as pd


class PollReader:

    def __init__(self,filename):
        self.filename = filename

    def returnPoll(self):
        file = pd.read_csv(self.filename)
