from xlwt import Workbook


class StudentReportWriter:

    def __init__(self, studentList):
        self.studentList = studentList

    def write_output_to_file(self):
        wb = Workbook()
        sheet1 = wb.add_sheet('Student Report')

        i = 0
        while i < len(self.studentList):
            sheet1.write(i, 0, self.studentList[i])
            i += 1
        i = 0
        while i < len(self.studentList):
            sheet1.write(i, 1, self.number_of_attendance_polls())
            i += 1
        i = 0
        while i < len(self.studentList):
            sheet1.write(i, 2, self.attendance_rate())
            i += 1
        i = 0
        while i < len(self.studentList):
            sheet1.write(i, 3, self.attendance_percentage())
            i += 1
        i = 0
        wb.save("CSE3063_studentReport.xlsx")

    def number_of_attendance_polls(self):
        return 0

    def attendance_rate(self):
        return 0

    def attendance_percentage(self):
        return 0
