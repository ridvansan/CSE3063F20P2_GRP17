from ReportWriter.PollReportWriter import PollReportWriter
from ReportWriter.StudentAttendanceReportWriter import StudentAttendanceReportWriter
from inputReaders.KeyMaker import KeyMaker
from inputReaders.PollReader import PollReader
from inputReaders.StudentInputReader import StudentInputReader
from models.AttendancePoll import AttendancePoll

studentInputReader = StudentInputReader("assets/CES3063_Fall2020_rptSinifListesi.XLS")
studentList = studentInputReader.getStudentList()

keyMaker = KeyMaker('assets/keys')
polls = keyMaker.makeKeysinDirectory()

pollReader = PollReader(studentList)
pollReader.readAnswersAtDirectory(polls, "assets/pollReports")

pollReader.polls = polls

pollReader.readFrequenciesAtDirectory("assets/pollReports")


for poll in pollReader.polls:
    if not isinstance(poll, AttendancePoll) and len(poll.answers) > 0:
        poll.makeHistogram()

studentAttendanceReportWriter = StudentAttendanceReportWriter(studentList, polls)
studentAttendanceReportWriter.write_output_to_file(pollReader.pollDates)

pollReportWriter = PollReportWriter(studentList, polls)
pollReportWriter.quizReport()
