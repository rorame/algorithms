import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    df_merge = visits.merge(transactions, how='left', on='visit_id')
    return df_merge[~df_merge['transaction_id'].notna()] \
        .groupby('customer_id', as_index=False) \
        .agg(count_no_trans = ('visit_id','nunique'))

# SQL:
# SELECT v.customer_id, COUNT(*) AS count_no_trans
# FROM Visits v
# LEFT JOIN Transactions t
# ON v.visit_id = t.visit_id
# WHERE t.visit_id IS NULL
# GROUP BY v.customer_id