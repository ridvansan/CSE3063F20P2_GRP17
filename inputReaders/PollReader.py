import csv

from models.PollAnswer import PollAnswer
from models.StudentAnswer import StudentAnswer
from models.Poll import Poll

#YAZ BURAYA AKIL
"""
    IF QUESTIONS[0] == 'Attending Lecture':
        #CONSTRUCT ATTANDENCE OBJECT
    ELSE
        CEVAPLARI LİSTELE POLLARDAN SORU LİSTELERİNİ AL VE KARŞILAŞTIR
        UYGUN POLL U BUL
        BU POLL U POLLANSWERSA AT
        ANSWERLARI LİSTELE POLLANSWERSA AT
    
"""



class PollReader:

    def __init__(self, filename):
        self.filename = filename

    studentList = []

    def readAnswers(self, studentList, polls):
        self.studentList = studentList
        with open(self.filename, encoding="utf8") as file:
            lines = csv.reader(file, delimiter= ',')

            for line in lines:
                if line[1] == "User Name":
                    continue
                s = None
                for student in studentList:
                    fullName = str(student.name + " " + student.surname).lower()
                    userName = ''.join(i for i in str(line[1]).lower() if not i.isdigit())
                    if fullName == userName:
                        s = student
                        print(s.name)
                        break

                questionList = []
                for i in range(4, len(line), 2):
                    questionList.append(i)
                poll = None
                for poll in polls:
                    if poll.getQuestionNames == questionList:
                        poll = poll

                answerList = []
                for i in range(5, len(line), 2):
                    answerList.append(i)

                dateTime = line[3]
                pollAnswer = PollAnswer(poll, dateTime)
                for ans in answerList:
                    pollAnswer.addToStudentAnswers(StudentAnswer(ans))
                s.addToPollAnswers(pollAnswer)

        file.close()


    def readQuestionFrequencies(self, polls):

        with open(self.filename, encoding="utf8") as file:
            lines = csv.reader(file, delimiter =',')
            for line in lines:
                #get question names:
                questionNames = []
                #store questionNames:
                for i in range(4, len(line), 2):
                    questionNames.append(line[i])
                questionNames.pop()
                for poll in polls:
                    pollQuestions = poll.getQuestionNames()

                    if pollQuestions == questionNames:
                        for j in range(5, len(line), 2):
                            poll.insertAnswer(line[j])
        file.close()