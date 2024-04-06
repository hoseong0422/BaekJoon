import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
  temp = store[store['amount'] > 500][['customer_id']].nunique()
  return pd.DataFrame(temp, columns=['rich_count']).reset_index(drop=True)
