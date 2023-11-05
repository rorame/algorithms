import pandas as pd


def article_views(views: pd.DataFrame) -> pd.DataFrame:
    id = views.query('author_id == viewer_id')['author_id'].sort_values(ascending=True).unique()
    return pd.DataFrame({'id': id})

# SQL:
# SELECT DISTINCT author_id AS id
# FROM Views
# WHERE author_id = viewer_id
# ORDER BY id
