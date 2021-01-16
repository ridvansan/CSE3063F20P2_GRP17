from xlwt import Workbook


class PollReportWriter:

    def __init__(self, pollList, studentList):
        self.pollList = pollList
        self.studentList = studentList

    def poll_report(self):
        i = 1
        while i < len(self.pollList):
            wb = Workbook()
            sheet1 = wb.add_sheet(self.pollList[i].name)
            m = 1
            numofQuestionsColumn = m
            sheet1.write(0, m, 'Number Of Questions')
            m += 1
            successRateColumn = m
            sheet1.write(0, m, 'Success Rate')
            m += 1
            successPercentageColumn = m
            sheet1.write(0, m, 'Success Percentage')

            j = 1
            while j < len(self.studentList):
                sheet1.write(j, numofQuestionsColumn, self.number_of_questions(self.pollList[i]))
                j += 1

            j = 1
            while j < len(self.studentList):
                sheet1.write(j, successRateColumn, self.success_rate())
                j += 1

            j = 1
            while j < len(self.studentList):
                sheet1.write(j, successPercentageColumn, self.success_percentage())
                j += 1
            filename = "CSE3063_" + self.pollList.name + ".xlsx"
            wb.save(filename)

    def number_of_questions(self, poll):
        numberOfQuestions = 0
        i = 0
        while i < len(poll.questionlist):
            numberOfQuestions += 1
        return numberOfQuestions

    def success_rate(self):
        return 0

    def success_percentage(self):
        return 0
