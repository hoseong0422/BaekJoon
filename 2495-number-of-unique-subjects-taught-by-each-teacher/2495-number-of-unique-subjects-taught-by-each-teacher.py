import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
  temp = teacher.groupby('teacher_id').nunique().reset_index()
  return temp.rename(columns={'subject_id':'cnt'})[['teacher_id', 'cnt']]
