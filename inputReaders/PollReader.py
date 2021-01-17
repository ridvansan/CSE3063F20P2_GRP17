import csv

from NameComparator import NameComparator
from models.PollAnswer import PollAnswer
from models.AttendancePoll import AttendancePoll
from models.Question import Question
from models.StudentAnswer import StudentAnswer


class PollReader:

    def __init__(self, filename):
        self.filename = filename
        self.studentList = []
        self.anomalies = []


    def getAnomalies(self):
        return self.anomalies


    def readAnswers(self, studentList, polls):
        self.studentList = studentList
        nameComparator = NameComparator()
        with open(self.filename, encoding="utf-8") as file:
            lines = csv.reader(file, delimiter=',')

            currentStudentListForPoll = []

            for line in lines:
                if line[1] == "User Name":
                    continue
                s = None

                for student in studentList:
                    fullName = student.name + " " + student.surname
                    userName = ''.join(i for i in str(line[1]) if not i.isdigit())
                    if nameComparator.isSameName(fullName, userName):
                        s = student
                        currentStudentListForPoll.append(s)
                        # print(s.name)
                        break

                if s is None:
                    print("Anomaly: ", line[1], ' | ', line[2], " on poll list skipping")
                    self.anomalies.append({
                        'name': line[1],
                        'email': line[2]
                    })
                    continue
                s.email = line[2]
                questionList = []
                self.getQandA(4, 'Q', questionList, line)
                questionList.pop()

                ## date: [Nov 23], [2020 10:41:25]
                date = line[3].split(',')
                date = date[0]  # date = 'Nov 23'
                poll = None
                if questionList[0] == "Are you attending this lecture?":
                    # this is attendance poll
                    questions = [Question(questionList[0])]
                    attendancePoll = AttendancePoll("attendance", date, questions)
                    if attendancePoll not in polls:
                        polls.append(attendancePoll)
                    poll = attendancePoll
                else:
                    for p in polls:
                        # questionList is a String list.
                        if p.getQuestionNames() == questionList:
                            poll = p
                            break
                if poll is None:
                    print("Poll is none for questions: ", questionList)
                    continue

                answerList = []  # Students answer not the answer key.
                self.getQandA(5, 'A', answerList, line)

                pollAnswer = PollAnswer(poll, date)
                for ans in answerList:
                    pollAnswer.addToStudentAnswers(StudentAnswer(ans))
                s.addToPollAnswers(pollAnswer)

        file.close()

    def readQuestionFrequencies(self, polls):
        with open(self.filename, encoding="utf8") as file:
            lines = csv.reader(file, delimiter=',')
            for line in lines:
                # get question names:
                questionNames = []
                # store questionNames:
                for i in range(4, len(line), 2):
                    questionNames.append(line[i])
                questionNames.pop()
                for poll in polls:
                    pollQuestions = poll.getQuestionNames()

                    if pollQuestions == questionNames:
                        for j in range(5, len(line), 2):
                            poll.insertAnswer(line[j])
        file.close()

    def getCorrespondingPoll(self, questionList, date, polls):
        poll = None
        if questionList[0] == "Are you attending this lecture?":
            # this is attendance poll
            question = Question(questionList[0])
            attendancePoll = AttendancePoll("attendance", date, [question])

            if attendancePoll not in polls:
                polls.append(attendancePoll)
            poll = attendancePoll

        else:
            for p in polls:
                if p.getQuestionNames().__eq__(questionList):
                    # print(p.name)
                    poll = p
                    break
        return poll

    def getQandA(self, startIndex, QorA, List, line):
        if QorA == 'Q':
            for i in range(startIndex, len(line), 2):
                List.append(line[i])
        else:
            for i in range(startIndex, len(line), 2):
                List.append(line[i])
