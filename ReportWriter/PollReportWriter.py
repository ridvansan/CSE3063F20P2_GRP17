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
            if isinstance(poll,AttendancePoll):
                continue
            index = ["studentID", "name", "surname", "email"]
            data = []
            for question in poll.getQuestionNames():
                index.append(question)
            index.append("Sucess Rate")
            index.append("Sucess Percentage")
            for student in self.studentList:
                status = student.getStatus(poll)
                if len(status) > 0:
                    data.append(status)


            frame = pd.DataFrame(data, columns=index)
            frame.to_excel("output/"+poll.name + "_report.xlsx")

    def writeQuizDetailedReportsForEachStudent(self):
        for student in self.studentList:

            pollNumber = 0
            for poll in self.pollList:
                for pollAnswer in student.pollAnswers:
                    if pollAnswer.poll.getQuestionNames() == poll.getQuestionNames():
                        date = '2020'
                        date = date.replace(" ", "_")
                        pollname = poll.name.replace(" ", "_")
                        studentName = student.name.replace(" ", "_")
                        excelName = pollname + '_' + date + '_' + studentName + "_" + student.studentID
                        index = ["Question Text", "Given Answer", "Correct Answer"]
                        studentAnswers = []
                        keys = []
                        data = []
                        answerCorrectnessList = []
                        for question in poll.questionlist:
                            keys.append(question.keys)

                        for answer in pollAnswer.studentAnswers:
                            studentAnswers.append(answer.answertext)

                        for i in range(len(keys)):
                            keyTexts= []
                            for k in keys:
                                for l in k:
                                    keyTexts.append(l.answertext)

                            studentTexts = []
                            for studentAnswer in studentAnswers:
                                studentTexts.append(studentAnswer)
                            if keyTexts[i] == studentTexts[i]:
                                answerCorrectnessList.append(1)

                            else:
                                answerCorrectnessList.append(0)
                        for i in range(len(poll.questionlist)):
                            row = []
                            row.append(keys[0])
                            row.append(studentAnswers[0])
                            row.append(answerCorrectnessList[0])
                            data.append(row)
                        print("")
                        try:
                            frame = pd.DataFrame(data, columns=index)
                            frame.to_excel("output/"+ "Poll" + '_' + str(pollNumber) + '_' + excelName + ".xlsx")
                        except:
                            continue


            pollNumber += 1
