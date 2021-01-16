import csv

from models.PollAnswer import PollAnswer
from models.StudentAnswer import StudentAnswer
from models.Poll import Poll

class PollReader:

    def __init__(self, filename):
        self.filename = filename

    studentList = []

    def readAnswers(self, studentList):
        self.studentList = studentList
        with open(self.filename, encoding="utf8") as file:
            lines = csv.reader(file, delimiter= ',')

            for line in lines:
                for student in studentList:
                    #Is comparison OK????????????????????
                    fullName = str(student.name + " " + student.surname).lower()
                    #remove numbers in the string
                    #poll name represents student names in the polls.
                    pollName = ''.join(i for i in str(line[1]).lower() if not i.isdigit())
                    # if lowercased student name is in the studentList
                    if fullName == pollName:
                        print("aaa")
                        #create pollAnswers
                        pollAnswers = PollAnswer(self.filename, line[3])

                        #questionlist = []
                        #for i in range(4, len(line), 2):
                        #   questionlist.append(line[i])

                        for i in range(5, len(line), 2):
                            #add answers to PollAnswers
                            pollAnswers.addToStudentAnswers(StudentAnswer(line[i]))
                        #add answersList to the corresponding Student
                        student.addToPollAnswers(pollAnswers)
                        break

        file.close()


    def readQuestionFrequencies(self):

        with open(self.filename, encoding="utf8") as file:
            lines = csv.reader(file, delimiter =',')

