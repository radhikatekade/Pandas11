# Perform a left join on employees table and employees unique ID table. Although we want result as the 
# [unique_id, name], we are performing left join such that we get [name, unique_id] because we also want
# NULL unique_id values which we'll only be able to retain with keeping all the names.

import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    df = employees.merge(employee_uni, left_on= 'id', right_on='id', how='left')
    return df[['unique_id', 'name']]