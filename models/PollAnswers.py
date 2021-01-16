class PollAnswers:
    def __init__(self, pollname, dateTime):
        self.poll = pollname
        self.dateTime = dateTime
        self.studentAnswers = []
        self.corrects = []

    def addToStudentAnswers(self, studentAnswer):
        self.studentAnswers.append(studentAnswer)

    def isCorrect(self):
        for count, question in enumerate(self.poll.questionlist):
            for keys in question.keys:
                if self.studentAnswers[count] == keys:
                    self.corrects.append(1)
                else:
                    self.corrects.append(0)
