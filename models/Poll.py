import matplotlib.pyplot as plt

class Poll:

    def __init__(self, name, questionList):
        self.name = name
        self.questionlist = questionList
        self.answers = {}
        self.date = None

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
            explode = []
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
                    xAxis.append(answer)
                    explode.append(0.01)

            plt.pie(yAxis, labels=xAxis, autopct='%1.1f%%', colors=color, explode=explode)
            title = 'q' + str(upperIndex)
            plt.title(title)
            plt.axis('equal')

            png = "output/q" + str(upperIndex) + ".png"
            plt.show()
            #plt.savefig(png)




