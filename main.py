from ReportWriter.PollReportWriter import PollReportWriter
from inputReaders.PollReader import PollReader
from inputReaders.StudentInputReader import StudentInputReader
from inputReaders.KeyMaker import KeyMaker
from ReportWriter.StudentAttendanceReportWriter import StudentAttendanceReportWriter

studentInputReader = StudentInputReader("assets/CES3063_Fall2020_rptSinifListesi.XLS")
studentList = studentInputReader.getStudentList()

keyMaker = KeyMaker('assets/keys')
polls = keyMaker.makeKeysinDirectory()


pollReader = PollReader("assets/pollReports")
pollReader.readAnswersAtDirectory(studentList, polls)
#pollReader.readQuestionFrequencies(polls)

#attendanceReportWriter = StudentAttendanceReportWriter(studentList, polls)
#attendanceReportWriter.write_output_to_file()

#


a = PollReportWriter(studentList,polls)
a.quizReport()
