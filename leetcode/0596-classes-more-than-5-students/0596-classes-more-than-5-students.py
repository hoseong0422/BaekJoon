import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
  temp = courses.groupby('class').count().reset_index()
  return temp.loc[temp['student'] >= 5][['class']]
