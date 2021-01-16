
class Student:

    def __init__(self,studentID,name,surname,desc):
        self.studentID = studentID
        self.name = name
        self.surname = surname
        self.desc = desc
        self.pollAnswers = []

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'<{self.name} {self.surname} >'

    def getPollAnswers(self):
        return self.pollAnswers
    def addToPollAnswers(self, pollAnswers):
        self.pollAnswers.append(pollAnswers)