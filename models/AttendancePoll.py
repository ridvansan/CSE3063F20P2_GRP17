from models.Poll import Poll


class AttendancePoll(Poll):

    def __init__(self, name, questionList):
        super().__init__(name, questionList)

    def analyze(self):
        pass
