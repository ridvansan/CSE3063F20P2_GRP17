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
            frame.to_excel(poll.name + ".xlsx")

