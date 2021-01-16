import pandas as pd
from openpyxl import Workbook,load_workbook

class StudentReportWriter:
    wb = Workbook()
    ws = wb.active
    ws.title = "Student Report"
    wb.save("CSE3063_studentReport.xlsx")

    def __init__(self):
        pass

    def students(self):
        df = pd.read_excel (r'assets/CES3063_Fall2020_rptSinifListesi.XLS')
        return df

    def number_of_attendance_polls(self):


    def attendance_rate(self):


    def attendance_percentage(self):


