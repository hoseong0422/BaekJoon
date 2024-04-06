import pandas as pd

def get_fixed_name(x):
    return x[0].upper()+x[1:].lower()

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].apply(get_fixed_name)
    users.sort_values(by='user_id', inplace=True)
    return users
