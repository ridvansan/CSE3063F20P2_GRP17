from models.Poll import Poll


class AttendancePoll(Poll):

    def __init__(self, name, date, questionList):
        super().__init__(name, questionList)
        self.date = date

    def analyze(self):
        pass

    def __eq__(self, other):
        if isinstance(other, AttendancePoll):
            return self.date == other.date
