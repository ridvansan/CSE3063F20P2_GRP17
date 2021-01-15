

students = StudentHandler("students.csv")
input = InputHandler("poll.csv")
keys = KeyMaker("Keys.csv")

StudentReport = StudentReportWriter(students,input,keys)
PollReport = PollReportWriter(students,input,keys)

StudentReport.writeto("studentreport.xlsx")
PollReport.writeto("pollreport.xlsx")

