"""
Combine all the prediction csvs into 1 single file.
"""

import pandas as pd

# --- READ EACH FILE INTO ITS OWN DATAFRAME --- #
# --- LINEAR AND RANDOM REGRESSION SEPERATELY --- #
defs_1 = pd.read_csv("Linear DEF PerApp 4GWs Prediction.csv")
mids_1 = pd.read_csv("Linear MID PerApp 5GWs Prediction.csv")
fwds_1 = pd.read_csv("Linear FWD PerApp 6GWs Prediction.csv")

defs_2 = pd.read_csv("Random DEF PerApp 4GWs Prediction.csv")
mids_2 = pd.read_csv("Random MID PerApp 5GWs Prediction.csv")
fwds_2 = pd.read_csv("Random FWD PerApp 6GWs Prediction.csv")

# --- CONCAT THE DIFFERENT DATAFRAMES INTO 1 --- #
# --- ADD THE NEW COLUMN NAMES TO THE DATAFRAME --- #
combined_players_1 = pd.concat([defs_1, mids_1, fwds_1], ignore_index=True)
combined_players_1.columns = ["Name", "Position", "Team Name", "Price", "Predict1", "Predict3GW1"]
combined_players_1 = combined_players_1.sort_values(by="Name", ignore_index=True)

# --- CONCAT THE DIFFERENT DATAFRAMES INTO 1 --- #
# --- ADD THE NEW COLUMN NAMES TO THE DATAFRAME --- #
combined_players_2 = pd.concat([defs_2, mids_2, fwds_2], ignore_index=True)
combined_players_2.columns = ["Name2", "Position2", "Team Name2", "Price2", "Predict2", "Predict3GW2"]
combined_players_2 = combined_players_2.sort_values(by="Name2", ignore_index=True)

final = pd.concat([combined_players_1, combined_players_2], axis=1)

# --- CREATE THE NEW COLUMNS FOR COMBINED LINEAR AND RANDOM REGRESSION MODEL PREDICTIONS --- #
final["Predict"] = (final["Predict1"] + final["Predict2"]) / 2
final["Predict3GW"] = (final["Predict3GW1"] + final["Predict3GW2"]) / 2

# --- DROP UNNEEDED COLUMNS --- #
final.drop(["Name2", "Position2", "Team Name2", "Price2", "Predict1", "Predict3GW1", "Predict2", "Predict3GW2"], axis=1, inplace=True)

# --- EXPORT CONCATED DATAFRAME TO A NEW CSV --- #
final.to_csv("Niyi Predictions.csv", index=False)
print(final)