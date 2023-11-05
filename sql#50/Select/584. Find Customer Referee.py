import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    customer["referee_id"] = customer["referee_id"].fillna(0)
    result = customer[customer["referee_id"] != 2]
    return pd.DataFrame(result["name"])

data = [[1, 'Will', None], [2, 'Jane', None], [3, 'Alex', 2], [4, 'Bill', None], [5, 'Zack', 1], [6, 'Mark', 2]]
customer = pd.DataFrame(data, columns=['id', 'name', 'referee_id']).astype({'id':'Int64', 'name':'object', 'referee_id':'Int64'})

# SQL:
# SELECT name
# FROM Customer
# WHERE referee_id <> 2 or referee_id is NULL