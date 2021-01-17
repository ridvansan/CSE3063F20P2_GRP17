from inputReaders.PollReader import PollReader
from inputReaders.StudentInputReader import StudentInputReader
from inputReaders.KeyMaker import KeyMaker
from models.AttendancePoll import AttendancePoll
from ReportWriter.PollReportWriter import PollReportWriter


studentInputReader = StudentInputReader("assets/CES3063_Fall2020_rptSinifListesi.XLS")
studentList = studentInputReader.getStudentList()

k = KeyMaker('assets/answer_monday.xls')
polls = k.makeKeys()


pollReader = PollReader("assets/CSE3063_20201123_Mon_zoom_PollReport.csv")
pollReader.readAnswers(studentList, polls)

#studentListWithAnswers = pollReader.studentList

#pollReader.readQuestionFrequencies(polls)


#a = PollReportWriter(studentList,polls)
#a.success_rate()
