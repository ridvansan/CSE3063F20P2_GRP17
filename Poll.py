
class Poll:

    def __init__(self, name):

        self.name = name
        self.questionlist = []

    def addToQuestionList(self, question):
        self.questionlist.append(question)
