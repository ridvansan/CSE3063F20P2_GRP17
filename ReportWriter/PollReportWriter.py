import json
import string

from xlwt import Workbook
import pandas as pd
from models.AttendancePoll import AttendancePoll

class PollReportWriter:

    def __init__(self, studentList,pollList):
        self.pollList = pollList
        self.studentList = studentList

    def quizReport(self):
        for poll in self.pollList:
            index = ["studentID", "name", "surname", "email"]
            data = []
            for question in poll.getQuestionNames():
                index.append(question)
            index.append("Sucess Rate")
            index.append("Sucess Percentage")
            for student in self.studentList:
                status = student.getStatus(poll)
                if len(status) > 6:
                    data.append(status)
            if len(data) > 0:
                frame = pd.DataFrame(data, columns=index)
                frame.to_excel("output/"+poll.name + "_report.xlsx")

    def writeQuizDetailedReportsForEachStudent(self):
        for student in self.studentList:
            for poll in student.PollsAndAnswers:
                index = ["question text", "given answer", "correct answer"]
                #fill whether the student answered the corresponding question correct or not
                dataInExcelFile = []
                for index, answer,question in zip(poll.questionlist, student.PollsAndAnswers[poll]):
                    row = []
                    row.append(question.name)
                    row.append(answer.answertext)
                    if question.keys[0].text == answer.answertext:
                        row.append(1)
                    else:
                        row.append(0)
                    dataInExcelFile.append(row)
                frame = pd.DataFrame(dataInExcelFile, columns=index)
                replaceChar = ",:- "
                pollName = poll.name
                date = poll.date
                for char in replaceChar:
                    pollName = pollName.replace(char, "_")
                for char in replaceChar:
                    date = date.replace(char, "_")
                frame.to_excel("output/SecondAnalytic/" + "Poll" + '_' + pollName + '_' + date + '_' + student.name + '_' + student.surname + '_' + student.studentID + '.xlsx')

