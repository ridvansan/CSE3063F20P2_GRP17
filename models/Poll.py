class Poll:

    def __init__(self, name, questionList):
        self.name = name
        self.questionlist = questionList

    def addToQuestionList(self, question):
        self.questionlist.append(question)

    def __str__(self):
        return f'{self.name} <{self.questionlist}>\n '
