# ClassName: StudentInputReader
# Number of Methods: 2
# LOC: 18

import pandas as pd
from models.Student import Student


class StudentInputReader:

    def __init__(self, filename):
        self.filename = filename

    def getStudentList(self):
        file = pd.read_excel(self.filename, sheet_name='rptSinifListesi', usecols=[2, 4, 7, 10])
        file = file.dropna(how='all')
        file = file.drop_duplicates()
        file = file.reset_index(drop=True)
        file = file.drop([0])
        file = file.rename(columns={'Unnamed: 2': 'StudentID', 'Unnamed: 4': 'Name', 'Unnamed: 7': 'Surname',
                                    'Unnamed: 10': 'Description'})
        studentList = []
        ids = file.StudentID
        names = file.Name
        surnames = file.Surname
        desc = file.Description
        for i in range(1, len(file)):
            studentList.append(Student(ids[i], names[i], surnames[i], desc[i]))
        return studentList
