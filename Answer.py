#CAN BE SEPERATED WITH IMPORTS



class Answer:

    def __init__(self,text):
        self.answertext = text


class StudentAnswer(Answer):

    def __init__(self, text):
        super().__init__(text)


class Key(Answer):

    def __init__(self, text):
        super().__init__(text)
