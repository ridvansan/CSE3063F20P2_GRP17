class Submit:

    def __init__(self):
        self.studentQuestions = []
        self.date = None

    def getQuestionNames(self):
        questionNames = []
        for question in self.studentQuestions:
            questionNames.append(question.name)
        return questionNames
