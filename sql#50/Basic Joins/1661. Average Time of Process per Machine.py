# SQL:
# SELECT a.machine_id, ROUND(AVG(b.timestamp - a.timestamp), 3) AS processing_time
# FROM Activity a
# JOIN Activity b
# ON
#     a.machine_id = b.machine_id AND
#     a.process_id = b.process_id AND
#     a.activity_type = 'start' AND
#     b.activity_type = 'end'
# GROUP BY a.machine_id


import pandas as pd

def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    activity['timestamp'] = activity.apply(lambda x: x.timestamp * -1 if x.activity_type == 'start' else x.timestamp, axis=1)
    avg_machine = activity.groupby(['machine_id', 'process_id'], as_index=False)['timestamp'].sum()
    return avg_machine.groupby('machine_id', as_index=False)['timestamp'].mean().round(3).rename(columns={'timestamp': 'processing_time'})