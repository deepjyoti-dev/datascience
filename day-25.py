
import pandas as p

import numpy as n

j_df = p.read_json("bitly.json", lines=True)

print(type(j_df))

j_df.isnull().any(axis = 0) 

j_df = j_df.replace([n.nan, "Missing"], [" ", "Unknown"])

j_df_col1 = j_df['tz'].value_counts().head(10)

tz_count = j_df['tz'].value_counts()

j_df_col1.plot.bar()

t_df = j_df['a'].str.split(n = 1, expand = True).add_prefix("Token_")

tokens_frequency = t_df['Token_0'].value_counts()

tokens_frequency.head().plot.bar()

t_df = t_df.replace(n.nan, 'Missing')

t_df["os"] = 'Not Windows'
t_df["os"][t_df["Token_1"].str.find("Windows") != -1] = "Windows"



