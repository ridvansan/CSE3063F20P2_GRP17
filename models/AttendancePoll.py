from models.Poll import Poll


class AttendancePoll(Poll):

    def __init__(self, name, date, questionList):
        super().__init__(name, questionList)
        self.date = date

    def analyze(self):
        pass
