import csv

from models.PollAnswer import PollAnswer
from models.AttendancePoll import AttendancePoll
from models.StudentAnswer import StudentAnswer
from models.Poll import Poll


class PollReader:

    def __init__(self, filename):
        self.filename = filename

    studentList = []

    def readAnswers(self, studentList, polls):
        self.studentList = studentList
        with open(self.filename, encoding="utf-8") as file:
            lines = csv.reader(file, delimiter=',')

            for line in lines:
                if line[1] == "User Name":
                    continue
                s = None
                for student in studentList:
                    fullName = student.name + " " + student.surname
                    userName = ''.join(i for i in str(line[1]) if not i.isdigit())
                    if fullName.casefold() == userName.casefold():
                        s = student
                        #print(s.name)
                        break

                if s == None:
                    print("Didnt found",line[1],"on poll list skipping")
                    continue

                questionList = []
                self.getQandA(4, 'Q', questionList, line)
                questionList.pop()

                ## date: [Nov 23], [2020 10:41:25]
                date = line[3].split(',')
                date = date[0]  # date = 'Nov 23'
                poll = None
                if questionList[0] == "Are you attending this lecture?":
                    # this is attendance poll
                    attendancePoll = AttendancePoll("attendance", date, questionList)
                    if attendancePoll not in polls:
                        polls.append(attendancePoll)
                    poll = attendancePoll
                else:
                    for p in polls:
                        if p.getQuestionNames().__eq__(questionList):
                            poll = p
                            break

                answerList = []
                for i in range(5, len(line), 2):
                    answerList.append(line[i])

                pollAnswer = PollAnswer(poll, date)
                for ans in answerList:
                    pollAnswer.addToStudentAnswers(StudentAnswer(ans))
                s.addToPollAnswers(pollAnswer)

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
                questionNames.pop()
                for poll in polls:
                    pollQuestions = poll.getQuestionNames()

                    if pollQuestions == questionNames:
                        for j in range(5, len(line), 2):
                            poll.insertAnswer(line[j])
        file.close()