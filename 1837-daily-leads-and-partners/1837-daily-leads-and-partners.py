import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
  return daily_sales.groupby(by=['date_id', 'make_name']).nunique().sort_values(by=['make_name', 'date_id'], ascending=False).rename(columns={'lead_id':'unique_leads', 'partner_id':'unique_partners'}).reset_index()
