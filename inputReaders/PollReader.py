import csv
import os

from NameComparator import NameComparator
from models.Anomaly import Anomaly
from models.PollAnswer import PollAnswer
from models.AttendancePoll import AttendancePoll
from models.Question import Question
from models.StudentAnswer import StudentAnswer
from models.Submit import Submit

from difflib import SequenceMatcher


class PollReader:

    def __init__(self, directory):
        self.directory = directory
        self.studentList = []
        self.anomalies = []
        self.pollsOfStudents = {}  # dictionary key: student value: Poll Array
        self.absences = {}  # dictionary key: poll values: numbers of absences (int)
        self.submits = []

    def getNumOfAbsenceForThatPoll(self, poll, pollStudentList):
        return len(self.studentList) - len(pollStudentList)

    def setPollsOfStudents(self):
        for student in self.studentList:
            currentStudentPolls = []
            for pollAnswer in student.getPollAnswers():
                currentStudentPolls.append(pollAnswer.poll)
                self.pollsOfStudents[student] = currentStudentPolls

    def Diff(self, li1, li2):
        li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
        return li_dif

    def getAnomalies(self):
        return self.anomalies

    def readAnswersAtDirectory(self, studentList, polls):
        reports = os.listdir(self.directory)
        for report in reports:
            self.readAnswers(studentList, polls, report)

    def readAnswers(self, studentList, polls, filename):
        self.studentList = studentList

        with open(self.directory + "/" + filename, encoding="utf-8") as file:
            file.readline()
            file.readline()
            file.readline()
            file.readline()
            file.readline()
            file.readline()
            lines = csv.reader(file, delimiter=',')

            x = ['x']
            for line in lines:
                if line[1] == "User Name":
                    continue
                s = self.getStudent(line, studentList)
                line.pop()
                if s is None:
                    continue

                submit = self.createSubmit(line, x)
                if submit is not None:
                    self.submits.append(submit)
                x = line

            # getPoll = self.getPollOfSubmit(polls, submit)

            # s.PollsAndAnswers[getPoll] = submit

        file.close()

    def readQuestionFrequencies(self, fileName, polls):
        with open(fileName, encoding="utf8") as file:
            lines = csv.reader(file, delimiter=',')
            for line in lines:
                # get question names:
                questionNames = []
                # store questionNames:
                for i in range(4, len(line), 2):
                    questionNames.append(line[i])
                questionNames.pop()
                for poll in polls:
                    if not isinstance(poll, AttendancePoll):
                        pollQuestions = poll.getQuestionNames()

                        if pollQuestions == questionNames:
                            questionAnswers = []
                            for j in range(5, len(line), 2):
                                questionAnswers.append(line[j])
                            for index, answer in enumerate(questionAnswers):
                                if poll.answers[questionNames[index]] == None:
                                    answersForSpecificQuestion = {}
                                    answersForSpecificQuestion[answer] = 1
                                    poll.answers[questionNames[index]] = answersForSpecificQuestion
                                else:
                                    if poll.answers[questionNames[index]].get(answer) != None:
                                        poll.answers[questionNames[index]][answer] += 1
                                    else:
                                        poll.answers[questionNames[index]].update({answer: 1})

        file.close()

    def getCorrespondingPoll(self, questionList, date, polls):
        poll = None
        if questionList[0] == "Are you attending this lecture?":
            # this is attendance poll
            question = Question(questionList[0])
            attendancePoll = AttendancePoll("attendance", date, [question])

            if attendancePoll not in polls:
                polls.append(attendancePoll)
            poll = attendancePoll

        else:
            for p in polls:
                if p.getQuestionNames().__eq__(questionList):
                    # print(p.name)
                    poll = p
                    break
        return poll

    def getQandA(self, startIndex, List, line):
        for i in range(startIndex, len(line), 2):
            List.append(line[i])

    def createSubmit(self, line, x):
        length = len(line)
        submit = Submit()
        questions = []
        submit.date = line[3]
        for i in range(4, length, 2):
            question = Question(line[i])
            if len(x) > i and line[i] == x[i]:
                return None
            keyStrings = line[i + 1].split(";")
            for keyString in keyStrings:
                question.keys.append(StudentAnswer(keyString))
            questions.append(question)
        submit.studentQuestions = questions
        return submit

    def getPollOfSubmit(self, polls, submit):
        for poll in polls:
            if len(poll.questionlist) == len(submit.studentQuestions):
                a = sorted(poll.getQuestionNames())
                b = sorted(submit.getQuestionNames())

                for i in range(0, len(poll.questionlist)):
                    percentage = SequenceMatcher(None, a[i], b[i]).ratio()
                    if percentage > 0.6:
                        print("buldum")
                        return poll
        return None

    def checkPollsAndSubmits(self, poll):
        a = sorted(poll.getQuestionNames())
        for submit in self.submits:
            if len(poll.questionlist) >= len(submit.studentQuestions):
                b = sorted(submit.getQuestionNames())

                percentage = SequenceMatcher(None, a[0], b[0]).ratio()
                if percentage > 0.6:
                    print("buldum")
                    return submit
        return None

    def getStudent(self, line, studentList):
        nameComparator = NameComparator()
        for student in studentList:
            fullName = student.name + " " + student.surname
            userName = ''.join(i for i in str(line[1]) if not i.isdigit())
            if nameComparator.isSameName(fullName, userName):
                s = student
                s.email = line[2]
                return s
        # Add anomaly to here
        print("Anomaly: ", line[1], ' | ', line[2], " on poll list skipping")
        anomaly = Anomaly(
            line[1],
            line[2]
        )
        self.anomalies.append(anomaly)
        return None
