
class Student:

    def __init__(self,studentID,name,surname,desc):
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

    def getAttendance(self,polls):
        pollCount = len(polls)
        studentPollCount = len(self.pollAnswers)
        return '%d of %d' % (studentPollCount, pollCount)

    def getSuccess(self,polls):
        for poll in polls:
            for pollanswer in self.pollAnswers:
                if pollanswer.poll.name == poll.name:
                    stAnswers = []
                    for q in pollanswer.studentAnswers:
                        stAnswers.append(q.answertext)
                    keyAnswers = []
                    for p in poll.questionlist:
                        for k in p.keys:
                            keyAnswers.append(k.answertext)

                    t = 0
                    for i in range(len(keyAnswers)):
                        try:
                            if stAnswers[i] == keyAnswers[i]:
                                t += 1
                        except:
                            pass

                    rate = t/len(keyAnswers)
                    print(self.name,self.surname, rate*100)
                    break
        return 0
