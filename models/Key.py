from models.Answer import Answer


class Key(Answer):

    def __init__(self, text):
        super().__init__(text)
        self.text = text
