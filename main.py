

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

pollReader = PollReader("assets/pollReports")
pollReader.readAnswersAtDirectory(studentList, polls)

for poll in polls:
    submit = pollReader.checkPollsAndSubmits(poll)
    if submit is not None:
        poll.date = submit.date


pollReader.polls = polls

print("test1")

#pollReader.readQuestionFrequencies("assets/pollReports/94502073867_PollReport (20).csv", polls)

pollReader.readFrequenciesAtDirectory()
print("test2")

for poll in pollReader.polls:
    if not isinstance(poll, AttendancePoll) and len(poll.answers)>0:
        poll.makeHistogram()



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


