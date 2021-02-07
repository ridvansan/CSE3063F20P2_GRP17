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


for st in studentList:
    st.getAttendanceNew(pollReader.pollDates)

for st in studentList:
    st.getSuccessNew()


studentAttendanceReportWriter = StudentAttendanceReportWriter(studentList, polls)
studentAttendanceReportWriter.write_output_to_file(pollReader.pollDates)

pollReportWriter = PollReportWriter(studentList, polls)
pollReportWriter.quizReport()

"""
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



for poll in polls:
    if not isinstance(poll, AttendancePoll):
        poll.makeHistogram()
"""