"""
Combine all the prediction csvs into 1 single file.
"""

import pandas as pd

# --- READ EACH FILE INTO ITS OWN DATAFRAME --- #
gks = pd.read_csv("Random GK PerApp 3GWs Prediction.csv")
defs = pd.read_csv("Random DEF PerApp 2GWs Prediction.csv")
mids = pd.read_csv("Random MID PerApp 6GWs Prediction.csv")
fwds = pd.read_csv("Random FWD PerApp 5GWs Prediction.csv")

# --- CONCAT THE DIFFERENT DATAFRAMES INTO 1 --- #
# --- ADD THE NEW COLUMN NAMES TO THE DATAFRAME --- #
combined_players = pd.concat([gks, defs, mids, fwds], ignore_index=True)
combined_players.columns = ["Name", "Position", "Team Name", "Price", "Predict", "Predict3GW"]

# --- EXPORT CONCATED DATAFRAME TO A NEW CSV --- #
combined_players.to_csv("Joy Predictions.csv", index=False)

print(combined_players)
