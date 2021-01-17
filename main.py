from inputReaders.PollReader import PollReader
from inputReaders.StudentInputReader import StudentInputReader
from inputReaders.KeyMaker import KeyMaker
from ReportWriter.PollReportWriter import PollReportWriter

studentInputReader = StudentInputReader("assets/CES3063_Fall2020_rptSinifListesi.XLS")
studentList = studentInputReader.getStudentList()

k = KeyMaker('assets/answer_monday.xls')
polls = k.makeKeys()

pollReader = PollReader("assets/CSE3063_20201123_Mon_zoom_PollReport.csv")
pollReader.readAnswers(studentList, polls)
studentListWithAnswers = pollReader.studentList




pollReader.readQuestionFrequencies(polls)

for poll in polls:
    poll.makeHistogram()

for s in studentList:
    print(s.name, s.getAttendance(polls))

a = PollReportWriter(polls,studentList)
a.success_rate()
#print(k)
#input = InputHandler("poll.csv")
#keys = KeyMaker("Keys.csv")

#StudentReport = StudentReportWriter(students,input,keys)
#PollReport = PollReportWriter(students,input,keys)

#StudentReport.writeto("studentreport.xlsx")
#PollReport.writeto("pollreport.xlsx")

