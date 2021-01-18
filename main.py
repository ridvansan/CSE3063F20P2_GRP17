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

pollReader.setPollsOfStudents()

for key, value in pollReader.pollsOfStudents.items():
    currentStudentID = key.studentID
    absencePollListOfCurrentStudent = pollReader.Diff(polls, value)

    if len(absencePollListOfCurrentStudent) > 0:
        print(f"student id: {currentStudentID} ")
        for absencePoll in absencePollListOfCurrentStudent:
            print(f"poll names: {absencePoll.name}")
        print("\n")
        print(f"number of absences of that student: {len(absencePollListOfCurrentStudent)}")

pollReportWriter = PollReportWriter(studentList, polls)
pollReportWriter.quizReport()

studentAttendanceReportWriter = StudentAttendanceReportWriter(studentList, polls)
studentAttendanceReportWriter.write_output_to_file()

for poll in polls:
    if not isinstance(poll, AttendancePoll):
        poll.makeHistogram()
