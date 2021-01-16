
class PollAnswers:
    def __init__(self, poll):
        self.poll = poll
        self.studentAnswers = []

    def addToStudentAnswers(self, studentAnswer):
        self.studentAnswers.append(studentAnswer)