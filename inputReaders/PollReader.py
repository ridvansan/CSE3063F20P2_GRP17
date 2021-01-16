import csv

from Answer import StudentAnswer
from PollAnswers import PollAnswers

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

                    #Is comparison OK????????????????????
                    fullName = str(student.name + " " + student.surname).lower()
                    #remove numbers in the string
                    pollName = ''.join(i for i in str(line[1]).lower() if not i.isdigit())
                    # if lowercased student name is in the studentList
                    if fullName == pollName:
                        #create pollAnswers
                        pollAnswers = PollAnswers(self.filename, line[3])

                        for i in range(5, len(line), 2):
                            #add answers to PollAnswers
                            pollAnswers.addToStudentAnswers(StudentAnswer(line[i]))
                        #add answersList to the corresponding Student
                        student.addToPollAnswers(pollAnswers)
                        break


