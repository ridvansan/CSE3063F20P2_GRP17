
class Student:

    def __init__(self,studentID,name,surname,desc):
        self.studentID = studentID
        self.name = name
        self.surname = surname
        self.desc = desc
        self.polls = []

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'<{self.name} {self.surname} >'

    def addToPolls(self, poll):
        self.polls.append(poll)