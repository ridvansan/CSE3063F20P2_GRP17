from inputReaders.StudentInputReader import StudentInputReader
from inputReaders.PollReader import PollReader
from models.PollAnswers import PollAnswers
from inputReaders.KeyMaker import KeyMaker

studentInputReader = StudentInputReader("assets/CES3063_Fall2020_rptSinifListesi.XLS")
studentList = studentInputReader.getStudentList()
pollReader = PollReader("assets/CSE3063_20201123_Mon_zoom_PollReport.csv")
pollReader.readPolls(studentList)
studentList = pollReader.studentList

for student in studentList:
    print(student.name + " " + student.surname)
    for answer in student.getPollAnswers():
        for studentAnswer in answer.studentAnswers:
            print(studentAnswer.answertext + ", ")
    print("\n")


#k = KeyMaker('assets/answer_monday.xls')
#k.makeKeys()
#print(k)
#input = InputHandler("poll.csv")
#keys = KeyMaker("Keys.csv")

#StudentReport = StudentReportWriter(students,input,keys)
#PollReport = PollReportWriter(students,input,keys)

#StudentReport.writeto("studentreport.xlsx")
#PollReport.writeto("pollreport.xlsx")

