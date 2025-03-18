# Perform a cross join because we want all the subjects associated with all the student IDs. Group exams
# DF based on ['student_id', 'subject_name'] and agg() the count of those exams for every student. Perform
# left join on the two tables, fill the null entries ONLY in the count col with 0, return DF with sorted 
# ['student_id', 'subject_name']

import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    df = students.merge(subjects, how='cross')
    exams = examinations.groupby(['student_id', 'subject_name']).agg(
        attended_exams = ('subject_name', 'count')
    ).reset_index()
    df = df.merge(exams, left_on = ['student_id', 'subject_name'], right_on= ['student_id', 'subject_name'], how='left')
    df['attended_exams'] = df['attended_exams'].fillna(0)
    return df.sort_values(by=['student_id', 'subject_name'])