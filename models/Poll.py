import matplotlib.pyplot as plt
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

    def makeHistogram(self):
        for upperIndex, question in enumerate(self.answers.values()):
            yAxis = []
            xAxis = []
            color = []
            correctAnswer = self.questionlist[upperIndex].keys[0].text

            for index, data in enumerate(question.values()):

                val_list = list(question.values())
                key_list = list(question.keys())
                answerIndex = val_list.index(data)
                answer = key_list[answerIndex]

                if answer == correctAnswer:
                    color.append('green')
                else:
                    color.append('blue')
                if index < 6:
                    yAxis.append(data)
                    xAxis.append("a" + str(index))

                plt.bar(xAxis, yAxis, color=color)
                plt.xlabel = "answers"
                plt.ylabel = "values"

                png = "output/q" + str(upperIndex) + ".png"
                plt.savefig(png)




