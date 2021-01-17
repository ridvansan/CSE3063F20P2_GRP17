
import numpy as np
class Poll:

    def __init__(self, name, questionList):
        self.name = name
        self.questionlist = questionList
        self.answers = {}

    def addToQuestionList(self, question):
        self.questionlist.append(question)

    def __str__(self):
        return f'{self.name} <{self.questionlist}>\n '



    def getQuestionNames(self):
        questionNames = []
        for question in self.questionlist:
            questionNames.append(question.name)
        return questionNames

    def insertAnswer(self, questionAnswers):
        for questionAnswer in questionAnswers:
            if questionAnswer in self.answers:
                self.answers[questionAnswer] += 1
            else:
                self.answers[questionAnswer] = 1

    def makeHistogram(self, poll):
            bins = range(0, len(poll.answers), 1)
            data = poll.answers.values()
            for answers in poll.answers:
                    print(str(answers) + " ")
            plt.hist(data, density=True, bins=bins)
            plt.xlabel = "answers"
            plt.ylabel = "values"
            plt.show()
            print("siadjfaskdfasdfg")


