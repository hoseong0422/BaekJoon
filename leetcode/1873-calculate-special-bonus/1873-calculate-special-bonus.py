import pandas as pd

def get_target(x):
    data = x.split('/')
    if int(data[0]) % 2 != 0 and 'M' not in data[1]:
        return "a"
    else:
        return "b"
def get_str_value(x):
    return str(x)

def get_bonus(x):
    data = x.split('/')
    if data[1] == 'a':
        return int(data[0])
    else:
        return 0

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['temp_id'] = employees['employee_id'].apply(get_str_value)
    employees['temp'] = employees['temp_id'] + '/' + employees['name']
    employees['target'] = employees['temp'].apply(get_target)
    employees['temp_salary'] = employees['salary'].apply(get_str_value)
    employees['temp_bonus'] = employees['temp_salary'] + '/' + employees['target']
    employees['bonus'] = employees['temp_bonus'].apply(get_bonus)
    employees.sort_values(by='employee_id', inplace=True)
    
    return employees[['employee_id', 'bonus']]
