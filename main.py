from StudentInputReader import StudentInputReader

students = StudentInputReader("assets/CES3063_Fall2020_rptSinifListesi.XLS")
students.getStudentList()
print(students)
#input = InputHandler("poll.csv")
#keys = KeyMaker("Keys.csv")

#StudentReport = StudentReportWriter(students,input,keys)
#PollReport = PollReportWriter(students,input,keys)

#StudentReport.writeto("studentreport.xlsx")
#PollReport.writeto("pollreport.xlsx")

