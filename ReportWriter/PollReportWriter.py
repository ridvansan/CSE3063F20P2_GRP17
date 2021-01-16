from xlwt import Workbook


class PollReportWriter:

    def __init__(self, pollList, studentList):
        self.pollList = pollList
        self.studentList = studentList

    def poll_report(self):
        pollName = "ayse" #TODO we get pollName from pollList by using loop
        wb = Workbook()
        sheet1 = wb.add_sheet(pollName)

        i = 1
        while i < len(self.pollList):
            sheet1.write(0, i, pollName)
            i += 1
        numofQuestionsColumn = i
        sheet1.write(0, i, 'Number Of Questions')
        i += 1
        successRateColumn = i
        sheet1.write(0, i, 'Success Rate')
        i += 1
        successPercentageColumn = i
        sheet1.write(0, i, 'Success Percentage')

        k = 0
        while k < len(self.pollList):
            j = 1
            while j < len(self.studentList):
                sheet1.write(j, numofQuestionsColumn, self.number_of_questions(self.pollList[k]))
                j += 1
            k += 1

        j = 1
        while j < len(self.studentList):
            sheet1.write(j, successRateColumn, self.success_rate())
            j += 1

        j = 1
        while j < len(self.studentList):
            sheet1.write(j, successPercentageColumn, self.success_percentage())
            j += 1

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
