import csv
from Poll import Poll

class InputHandler:
    def __init__(self, filename):
        self.filename = filename

    studentList = []

    def readPolls(self, studentList):
        self.studentList = studentList
        with open(self.filename, 'r') as file:
            lines = csv.reader(file)

            for line in lines:
              for student in studentList:
                fullName = str(student.name + " " + student.surname).lower()
                # if lowercased student name is in the studentList
                if fullName == str(line[1]).lower():
                    poll = Poll(self.filename)