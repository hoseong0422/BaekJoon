import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    temp =  views.loc[views['author_id'] == views['viewer_id'], ['author_id']]
    return temp.drop_duplicates(inplace=True).rename(columns={'author_id': 'id',}).sort_values(by=['id'])
