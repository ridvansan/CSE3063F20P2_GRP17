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

pollReader = PollReader("assets/pollReports")
pollReader.readAnswersAtDirectory(studentList, polls)
pollReader.readQuestionFrequencies("assets/pollReports/CSE3063_20201123_Mon_zoom_PollReport.csv", polls)
for poll in polls:
 if not isinstance(poll, AttendancePoll):
    poll.makeHistogram()



pollReader.setPollsOfStudents()

for key, value in pollReader.pollsOfStudents.items():
    currentStudentID = key.studentID
    absencePollListOfCurrentStudent = pollReader.Diff(polls, value)

a = PollReportWriter(studentList, polls)
a.quizReport()
