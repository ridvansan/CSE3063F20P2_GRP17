
class Question:

    def __init__(self, name):
        self.name = name
        self.keys = []

    def appendToKeys(self, key):
        self.keys.append(key)

    def putKeys(self, keys):
        self.keys = keys

    def __eq__(self,other):
        if not isinstance(other,Question):
            return False
        return self.keys == other.keys

    def __str__(self):
        return f'{self.name} <{self.keys}>'
