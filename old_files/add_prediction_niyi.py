"""
Add prediction for next GW and next 3 GWs based on Random Forest regression
that considers all columns except price, team, position
"""
import pickle
from pandas import read_csv

NEW_COLUMN_NAMES = {"Cost (£M)":"Cost", "Points":"Points_x"}


def main():
    """Main function for Niyi's team prediction."""
    """Combine all the predictions to be done in 1 function."""
    # # --- ADD SINGLE GW PREDICTION (I.E. NEXT GW) --- #
    single_predict(pickling="Linear GK PerApp 3GWs.pkl", file="GK PerApp 3GWs.csv")
    single_predict(pickling="Linear DEF PerApp 4GWs.pkl", file="DEF PerApp 4GWs.csv")
    single_predict(pickling="Linear MID PerApp 5GWs.pkl", file="MID PerApp 5GWs.csv")
    single_predict(pickling="Linear FWD PerApp 6GWs.pkl", file="FWD PerApp 6GWs.csv")
    single_predict(pickling="Random Forest GK PerApp 5GWs.pkl", file="GK PerApp 5GWs.csv")
    single_predict(pickling="Random Forest DEF PerApp 4GWs.pkl", file="DEF PerApp 4GWs.csv")
    single_predict(pickling="Random Forest MID PerApp 5GWs.pkl", file="MID PerApp 5GWs.csv")
    single_predict(pickling="Random Forest FWD PerApp 6GWs.pkl", file="FWD PerApp 6GWs.csv")

    # # --- ADD 3 GWS PREDICTIONS --- #
    three_gw_predict(pickling="Linear 3Ahead DEF PerApp 6GWs.pkl", file="DEF PerApp 6GWs.csv")
    three_gw_predict(pickling="Linear 3Ahead MID PerApp 6GWs.pkl", file="MID PerApp 6GWs.csv")
    three_gw_predict(pickling="Linear 3Ahead FWD PerApp 5GWs.pkl", file="FWD PerApp 5GWs.csv")
    three_gw_predict(pickling="Random Forest 3Ahead DEF PerApp 6GWs.pkl", file="DEF PerApp 6GWs.csv")
    three_gw_predict(pickling="Random Forest 3Ahead MID PerApp 6GWs.pkl", file="MID PerApp 6GWs.csv")
    three_gw_predict(pickling="Random Forest 3Ahead FWD PerApp 5GWs.pkl", file="FWD PerApp 5GWs.csv")


def single_predict(pickling, file):
    """Add Points Prediction for the next GWs."""
    pickle_in = open(pickling, "rb")
    rf = pickle.load(pickle_in)

    data_predict = read_csv(file)
    data = read_csv(file)

    # Rename the Cost column
    data_predict = data_predict.rename(columns=NEW_COLUMN_NAMES)
    data = data.rename(columns=NEW_COLUMN_NAMES)

    # Drop the columns that are not going to be used in the regression
    data_predict.drop(["Name", "App.", "Fouls Made", "Exp. Clean Sheets", "Names", "Position", "Cost", "Team"], axis=1, inplace=True)

    # Setting up the values of x and y
    x = data_predict

    # Run the prediction
    prediction = rf.predict(x)
    prediction = [round(x) for x in prediction]

    header = ["Names", "Position", "Team", "Cost", "Predict1GW"]
    data_new = data.assign(Predict1GW = prediction)
    data_new.to_csv(f"{pickling[:7]}{file[:-4]} 1Ahead.csv", index=False, columns= header)


def three_gw_predict(pickling, file):
    """Add Points Prediction for the next 3 GWs."""
    pickle_in = open(pickling, "rb")
    rf = pickle.load(pickle_in)

    data_predict = read_csv(file)
    data = read_csv(file)

    # Rename the Cost column
    data_predict = data_predict.rename(columns=NEW_COLUMN_NAMES)
    data = data.rename(columns=NEW_COLUMN_NAMES)

    # Drop the columns that are not going to be used in the regression
    data_predict.drop(["Name", "App.", "Fouls Made", "Exp. Clean Sheets", "Names", "Position", "Cost", "Team"], axis=1, inplace=True)

    # Setting up the values of x and y
    x = data_predict

    # Run the prediction
    prediction = rf.predict(x)
    prediction = [round(x) for x in prediction]

    header = ["Names", "Position", "Team", "Cost", "Predict3GW"]
    data_new = data.assign(Predict3GW = prediction)
    data_new.to_csv(f"{pickling[:7]}{file[:-4]} 3Ahead.csv", index=False, columns= header)


if __name__ == "__main__":
    main()
