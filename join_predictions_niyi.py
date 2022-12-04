"""
Combine all the predictions into 1 file.
"""
import pandas as pd


def main():
    """Combine 1GW and 3GWs prediction into 1 file."""
    # join_predictions("Linear GK PerApp 3GWs 1Ahead.csv", "Linear GK PerApp 3GWs 3Ahead.csv")
    join_predictions("Linear DEF PerApp 4GWs 1Ahead.csv", "Linear DEF PerApp 6GWs 3Ahead.csv")
    join_predictions("Linear MID PerApp 5GWs 1Ahead.csv", "Linear MID PerApp 6GWs 3Ahead.csv")
    join_predictions("Linear FWD PerApp 6GWs 1Ahead.csv", "Linear FWD PerApp 5GWs 3Ahead.csv")
    # join_predictions("Random GK PerApp 3GWs 1Ahead.csv", "Random GK PerStart 2GWs 3Ahead.csv")
    join_predictions("Random DEF PerApp 4GWs 1Ahead.csv", "Random DEF PerApp 6GWs 3Ahead.csv")
    join_predictions("Random MID PerApp 5GWs 1Ahead.csv", "Random MID PerApp 6GWs 3Ahead.csv")
    join_predictions("Random FWD PerApp 6GWs 1Ahead.csv", "Random FWD PerApp 5GWs 3Ahead.csv")


def join_predictions(gw1_csv, gw3_csv):
    """Join the 1GW and 3GW predicitions into a single prediction file"""
    # --- READ IN BOTH CSVS --- #
    prediction_1 = pd.read_csv(gw1_csv)
    prediction_3 = pd.read_csv(gw3_csv)

    # --- USE MERGE FUNCTION BY SETTING HOW TO "inner" --- #
    data = pd.merge(prediction_1, prediction_3, on="Names", how="inner")

    # --- PRINT PANDA TO A CSV USING ONLY THE DESIRED COLUMNS --- #
    data.to_csv(f"{gw1_csv[:-10]}Prediction.csv", index=False, columns=["Names", "Position_x", "Team_x", "Cost_x", "Predict1GW", "Predict3GW"])

if __name__ == "__main__":
    main()
