from models import AttendancePoll

class Student:

    def __init__(self, studentID, name, surname, desc):
        self.studentID = studentID
        self.name = name
        self.surname = surname
        self.desc = desc
        self.pollAnswers = []

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'<{self.name} {self.surname} >'

    def getPollAnswers(self):
        return self.pollAnswers

    def addToPollAnswers(self, pollAnswers):
        self.pollAnswers.append(pollAnswers)

    def getAttendance(self, polls):
        # TODO NEEDS TO BE TESTED EXPERIMENTAL CODE (especially for isinstance thing)
        attandancePollCounter = 0
        for poll in polls:
            if isinstance(poll, AttendancePoll):
                attandancePollCounter += 1

        studentsAttendance = 0
        for pollAnswer in self.pollAnswers:
            if isinstance(pollAnswer.poll, AttendancePoll):
                studentsAttendance +=1

        return '%d of %d' % (studentsAttendance, attandancePollCounter)

    def getSuccess(self, polls):
        # TODO NEEDS TO BE TESTED EXPERIMENTAL CODE (especially for isinstance thing)
        for poll in polls:
            if isinstance(poll, AttendancePoll):
                continue

            for pollanswer in self.pollAnswers:
                if pollanswer.poll.name == poll.name:
                    studentAnswers = []
                    for q in pollanswer.studentAnswers:
                        studentAnswers.append(q.answertext)
                    keyAnswers = []
                    for p in poll.questionlist:
                        for k in p.keys:
                            keyAnswers.append(k.answertext)

                    correctQuestionCount = 0
                    for i in range(len(keyAnswers)):
                        try:
                            if studentAnswers[i] == keyAnswers[i]:
                                correctQuestionCount += 1
                        except:
                            pass

                    rate = correctQuestionCount / len(keyAnswers)
                    print(self.name, self.surname, rate * 100)
                    break
        return 0
