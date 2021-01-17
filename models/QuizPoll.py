from models.Poll import Poll


class QuizPoll(Poll):
    def __init__(self, name, questionList):
        super().__init__(name, questionList)
        self.name = name
        self.questionList = questionList

