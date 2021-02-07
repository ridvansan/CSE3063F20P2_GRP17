from models.AttendancePoll import AttendancePoll

class Student:

    def __init__(self, studentID, name, surname, desc):
        self.studentID = studentID
        self.name = name
        self.surname = surname
        self.desc = desc
        self.email = None
        self.pollAnswers = []
        self.PollsAndAnswers = {} #Poll:Answers
        self.attendances = set()

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

    def getAttendanceDates(self):
        dates = set()
        for attendance in self.attendances:
            dates.add(attendance.date)
        return dates

    def isAttended(self,date):
        if date in self.getAttendanceDates():
            return True
        else:
            for poll, stAnswer in self.PollsAndAnswers.items():
                if stAnswer.date == date:
                    return True
        return False

    def getAttendanceNew(self,dates):
        daysAttended = 0
        for date in dates:
            if self.isAttended(date):
                daysAttended += 1
        return daysAttended

    def getQuestionsTrueFalse(self, poll):
        pollQuestions = []
        for i in range(len(poll.questionlist)):
            a = sorted(poll.questionlist,key = lambda x:x.name)[i].getKeys()
            b = self.PollsAndAnswers.get(poll)
            if b == None:
                continue
            b = sorted(self.PollsAndAnswers.get(poll).studentQuestions,key=lambda x:x.name)[i].getKeys()
            if a == b:
                pollQuestions.append(1)
            else:
                pollQuestions.append(0)
        return pollQuestions



    def getSuccessNew(self):
        correctAnswersByPoll= []
        for poll, submit in self.PollsAndAnswers.items():
            pollQuestions = []
            list = sorted(submit.studentQuestions, key=lambda x: x.name, reverse=True)
            for i in range(len(poll.questionlist)):
                a = poll.questionlist[i].getKeys()
                b = list[i].getKeys()
                if a == b:
                    pollQuestions.append(1)
                else:
                    pollQuestions.append(0)
            correctAnswersByPoll.append(pollQuestions)
        return correctAnswersByPoll


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
        status.append(self.studentID)
        status.append(self.name)
        status.append(self.surname)
        status.append(self.email)
        sucess = self.getQuestionsTrueFalse(poll)
        counter = 0
        for i in sucess:
            status.append(i)
            counter += i
        rate = f"{counter} / {len(poll.questionlist)}"
        percentage = counter*100/len(poll.questionlist)
        status.append(rate)
        status.append(percentage)
        return status
