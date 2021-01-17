from xlwt import Workbook

class StudentAttendanceReportWriter:

    def __init__(self,studentList,pollList):
        self.studentList = studentList
        self.pollList = pollList

    def write_output_to_file(self):
        wb = Workbook()
        sheet1 = wb.add_sheet('Student Attendance Report')

        sheet1.write(0, 0, 'Student ID')
        sheet1.write(0, 1, 'First Name')
        sheet1.write(0, 2, 'Last Name')
        sheet1.write(0, 3, 'Number of attendance polls')
        sheet1.write(0, 4, 'Attendance Percantage')



        wb.save("output/CSE3063_studentReport.xls")