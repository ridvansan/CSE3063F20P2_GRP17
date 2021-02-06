from models.AttendancePoll import AttendancePoll

class Student:

    def __init__(self, studentID, name, surname, desc):
        self.studentID = studentID
        self.name = name
        self.surname = surname
        self.desc = desc
        self.email = None
        self.pollAnswers = []
        self.pollsAndAnswers = {} #Poll:Answer

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'<{self.name} {self.surname} >'

    def getPollAnswers(self):
        return self.pollAnswers

    def addToPollAnswers(self, pollAnswers):
        self.pollAnswers.append(pollAnswers)

    def getAttendance(self):

        studentsAttendance = 0
        for pollAnswer in self.pollAnswers:
            if isinstance(pollAnswer.poll, AttendancePoll):
                studentsAttendance +=1

        return studentsAttendance

    def getSuccess(self, polls):
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
        return rate

    def getStatus(self, poll):
        status = []
        for pollAnswer in self.pollAnswers:
            if pollAnswer.poll.name == poll.name:
                status.append(self.studentID)
                status.append(self.name)
                status.append(self.surname)
                status.append(self.email)
                studentAnswers = []
                keys = []
                for question in poll.questionlist:
                    keys.append(question.keys)
                for answer in pollAnswer.studentAnswers:
                    studentAnswers.append(answer.answertext)
                trueCount = 0
                for i in range(len(keys)):
                    keyTexts= []
                    for k in keys:
                        for l in k:
                            keyTexts.append(l.answertext)


                    studentTexts = []
                    for studentAnswer in studentAnswers:
                        studentTexts.append(studentAnswer)
                    if keyTexts[i] == studentTexts[i]:
                        status.append(1)
                        trueCount += 1
                    else:
                        status.append(0)

                status.append(str(trueCount)+ " of " + str(len(keys)))
                status.append(trueCount/len(keys))

        return status
