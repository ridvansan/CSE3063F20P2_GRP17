import pandas as pd
from openpyxl import Workbook, load_workbook

class StudentReportWriter:
    wb = Workbook()
    ws = wb.active
    ws.title = "Student Report"
    wb.save("CSE3063_studentReport.xlsx")

    def __init__(self, studentList):
        self.studentList = studentList

    def writeOutputToFile(self):
        pass

    def number_of_attendance_polls(self):
        pass

    def attendance_rate(self):
        pass

    def attendance_percentage(self):
        pass

