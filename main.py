from ReportWriter.PollReportWriter import PollReportWriter
from inputReaders.PollReader import PollReader
from inputReaders.StudentInputReader import StudentInputReader
from inputReaders.KeyMaker import KeyMaker
from models.AttendancePoll import AttendancePoll
from ReportWriter.StudentAttendanceReportWriter import StudentAttendanceReportWriter

studentInputReader = StudentInputReader("assets/CES3063_Fall2020_rptSinifListesi.XLS")
studentList = studentInputReader.getStudentList()

keyMaker = KeyMaker('assets/keys')
polls = keyMaker.makeKeysinDirectory()

pollReader = PollReader(studentList)
pollReader.readAnswersAtDirectory(polls, "assets/pollReports")


studentAttendanceReportWriter = StudentAttendanceReportWriter(studentList, polls)
studentAttendanceReportWriter.write_output_to_file(pollReader.pollDates)

pollReportWriter = PollReportWriter(studentList, polls)
pollReportWriter.quizReport()