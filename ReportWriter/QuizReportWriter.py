import pandas as pd
from pyexcel_ods import save_data
from collections import OrderedDict

class QuizReportWriter:
    def __init__(self,studentList,pollList):
        self.studentList = studentList
        self.pollList = pollList
    #number of questions
    #number of correctly answered questions
    #number of wrongly answered questions
    #number of empty questions
    #rate of correctly answered questions(/total number of questions)
    #accuracy percentage(rate of correctly answered questions*100)

    def quiz_report(self):
        pass

    def save_ods_from_excel(excel_file, target_ods_file):
        # First read into dataframe
        df = pd.read_excel(excel_file)
        # Change everything to string since we're just writing
        df = df.astype(str)
        # Initiliaze data to be written as an empty list, as pyods needs a list to write
        whole_data_list = []
        # Initiliaze the empty dict() for the data
        d = OrderedDict()
        # Write the columns first to be the first entries
        whole_data_list.append(list(df.columns))
        # loop through data frame and update the data list
        for index, row in df.iterrows():
            whole_data_list.append(list(row.values))
        # Populate dict() with updated data list
        d.update({"Moved sheet": whole_data_list})
        # Finally call save_data() from pyods to store the ods file
        save_data(target_ods_file, d)