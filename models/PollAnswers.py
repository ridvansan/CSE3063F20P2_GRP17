
class PollAnswers:
    def __init__(self, pollname, dateTime):
        self.poll = pollname
        self.dateTime = dateTime
        self.studentAnswers = []

    def addToStudentAnswers(self, studentAnswer):
        self.studentAnswers.append(studentAnswer)