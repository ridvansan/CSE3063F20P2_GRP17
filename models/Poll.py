from abc import abstractmethod
import matplotlib.pyplot as plt

class Poll:

    def __init__(self, name, questionList):
        self.name = name
        self.questionlist = questionList
        self.answers = {}

    def addToQuestionList(self, question):
        self.questionlist.append(question)

    def __str__(self):
        return f'{self.name} <{self.questionlist}>\n '

    @abstractmethod
    def analyze(self):
        pass

    def getQuestionNames(self):
        questionNames = []
        for question in self.questionlist:
            questionNames.append(question.name)
        return questionNames

    def insertAnswer(self, answer):
        if answer in self.answers:
            self.answers[answer] += 1
        else:
            self.answers[answer] = 1

    def makeHistogram(self):
            plt.xlabel = self.answers.keys()
            plt.ylabel = self.answers.values()
            plt.hist()
            plt.show()

