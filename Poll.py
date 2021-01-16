
class Poll:

    def __init__(self, name, datetime):

        self.name = name
        self.datetime = datetime
        self.questionlist = []

    def addToQuestionList(self, question):
        self.questionlist.append(question)
