
class Student:

    def __init__(self,studentID,name,surname,desc):
        self.studentID = studentID
        self.name = name
        self.surname = surname
        self.desc = desc


    def __str__(self):
        return f'<{self.name} {self.surname} >'
