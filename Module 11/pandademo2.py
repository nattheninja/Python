import pandas as pd
nba = pd.read_csv("nba_all_elo.csv")
import numpy as np
# print(type(nba))

# print(len(nba))

# print(nba.shape)

# print(nba["fran_id"].value_counts())


print(nba.loc[nba["fran_id"] == "Lakers", "team_id"].value_counts())
print(nba.loc[nba["team_id"] == "BOS", "pts"].sum())
print(nba.index)

# ary = np.array([[1,2,3], [4, 5, 6], [7, 8, 9]])
print(ary[1:, :2])