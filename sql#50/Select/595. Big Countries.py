import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    return world.query('area >= 3000000 | population >= 25000000')[['name', 'population', 'area']]

# SQL:
# SELECT name, population, area
# FROM World
# WHERE area >= 3000000 OR population >= 25000000