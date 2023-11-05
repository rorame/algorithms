import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather.sort_values(by='recordDate', inplace=True)
    return weather[
        (weather.temperature.diff() > 0)
      & (weather.recordDate.diff().dt.days == 1)
    ][['id']]

# SQL:
# SELECT w1.id
# FROM Weather w1
# JOIN Weather w2
# ON w1.recordDate = w2.recordDate + INTERVAL '1' DAY
# WHERE w1.temperature > w2.temperature