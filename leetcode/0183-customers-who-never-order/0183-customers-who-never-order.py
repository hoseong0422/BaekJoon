import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
  temp = customers[~customers['id'].isin(orders['customerId'])]
  return temp.rename(columns={'name':'Customers'})[['Customers']]
