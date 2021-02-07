from xlwt import Workbook

from models.AttendancePoll import AttendancePoll

class StudentAttendanceReportWriter:

    def __init__(self, studentList, pollList):
        self.studentList = studentList
        self.pollList = pollList

    def getNumberOfAttendancePolls(self):
        counter = 0
        for poll in self.pollList:
            if isinstance(poll, AttendancePoll):
                counter += 1
        return counter

    def write_output_to_file(self,dates):
        wb = Workbook()
        sheet = wb.add_sheet('Student Attendance Report')

        sheet.write(0, 0, 'Student ID')
        sheet.write(0, 1, 'Name')
        sheet.write(0, 2, 'Surname')
        sheet.write(0, 3, 'Number of attendance polls')
        sheet.write(0, 4, 'Student Attendance')
        sheet.write(0, 5, 'Attendance Percantage')


        for (index, student) in enumerate(self.studentList):
            sheet.write(index + 1, 0, student.studentID)
            sheet.write(index + 1, 1, student.name)
            sheet.write(index + 1, 2, student.surname)
            sheet.write(index + 1, 3, len(dates))
            sheet.write(index + 1, 4, student.getAttendanceNew(dates))
            sheet.write(index + 1, 5, '{:.2f}%'.format(student.getAttendanceNew(dates)*100 / len(dates)))

        wb.save("output/CSE3063_studentReport.xls")
