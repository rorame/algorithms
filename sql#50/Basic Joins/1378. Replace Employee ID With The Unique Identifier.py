import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    return employees.merge(employee_uni, how='left', on='id')[['unique_id', 'name']]

# SQL:
# SELECT u.unique_id, e.name
# FROM Employees e
# LEFT JOIN EmployeeUNI u
# ON e.id = u.id