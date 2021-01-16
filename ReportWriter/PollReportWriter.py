from openpyxl import Workbook, load_workbook

class PollReportWriter:
    wb = Workbook()
    ws = wb.active
    ws.title = "Poll Report"

    wb.save("CSE3063_pollReport.xlsx")



