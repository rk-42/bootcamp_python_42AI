import pandas as pd


def youngestfellah(df: pd.DataFrame, year: int) -> dict:
    mydict = {'f': df['Age'][(df['Sex'] == 'F') & (df['Year'] == year)].min(),
              'm': df['Age'][(df['Sex'] == 'M') & (df['Year'] == year)].min()}
    return mydict



