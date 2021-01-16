import csv

from models.PollAnswer import PollAnswer
from models.StudentAnswer import StudentAnswer

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

                    fullName = str(student.name + " " + student.surname).lower()
                    pollName = ''.join(i for i in str(line[1]).lower() if not i.isdigit())

                    if fullName == pollName:
                        pollAnswer = PollAnswer(self.filename, line[3])

                        for i in range(5, len(line), 2):
                            pollAnswer.addToStudentAnswers(StudentAnswer(line[i]))

                        student.addToPollAnswers(pollAnswer)
                        break

        file.close()


    def readQuestionFrequencies(self, polls):

        with open(self.filename, encoding="utf8") as file:
            lines = csv.reader(file, delimiter =',')
            for line in lines:
                #get question names:
                questionNames = []
                #store questionNames:
                for i in range(4, len(line), 2):
                    questionNames.append(line[i])

                for poll in polls:
                    pollQuestions = poll.getQuestionNames()
                    if pollQuestions == questionNames:
                        for j in range(5, len(line), 2):
                            poll.insertAnswer(line[j])
        file.close()