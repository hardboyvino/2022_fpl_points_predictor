"""
Add prediction for next GW and next 3 GWs based on Random Forest regression
that considers all columns except price, team, position
"""
import pickle
import pandas as pd
import os


NEW_COLUMN_NAMES = {"Cost (£M)":"Cost", "Points":"Points_x"}

def main():
    """Main function for Joy's team prediction."""

def random_forest_regression(which_gw_are_we_on):
    """Add predicted points for 1GW and 3GWs and export to prediction folder\n
    Join the 1GW and 3GW filenames into a single filename for each position.\n
    Combine all the joined filenames for all positions into 1 csv filename exported to the main folder.\n
    Delete the prediction_folder."""
    # --- REFERENCE THE FOLDER WITH THE SCRAPED filenameS --- #
    player_data = f"GW {which_gw_are_we_on} Files"

    # --- IF PREDICTION FOLDER DOES NOT EXIST, CREATE IT --- #
    if not os.path.exists("prediction_folder"):
        os.mkdir("prediction_folder")

    # --- ADD PREDICTION TO PLAYER filenameS --- #
    single_predict(pickling=os.path.join("random_forest", "Random Forest GK PerApp 2GWs.pkl"), filename=os.path.join(player_data, "GK PerApp 2GWs.csv"))
    single_predict(pickling=os.path.join("random_forest", "Random Forest DEF PerApp 2GWs.pkl"), filename=os.path.join(player_data, "DEF PerApp 2GWs.csv"))
    single_predict(pickling=os.path.join("random_forest", "Random Forest MID PerApp 4GWs.pkl"), filename=os.path.join(player_data, "MID PerApp 4GWs.csv"))
    single_predict(pickling=os.path.join("random_forest", "Random Forest FWD PerApp 4GWs.pkl"), filename=os.path.join(player_data, "FWD PerApp 4GWs.csv"))
    three_gw_predict(pickling=os.path.join("random_forest", "Random Forest 3Ahead GK PerApp 2GWs.pkl"), filename=os.path.join(player_data, "GK PerApp 2GWs.csv"))
    three_gw_predict(pickling=os.path.join("random_forest", "Random Forest 3Ahead DEF PerApp 2GWs.pkl"), filename=os.path.join(player_data, "DEF PerApp 2GWs.csv"))
    three_gw_predict(pickling=os.path.join("random_forest", "Random Forest 3Ahead MID PerApp 5GWs.pkl"), filename=os.path.join(player_data, "MID PerApp 5GWs.csv"))
    three_gw_predict(pickling=os.path.join("random_forest", "Random Forest 3Ahead FWD PerApp 5GWs.pkl"), filename=os.path.join(player_data, "FWD PerApp 5GWs.csv"))

    # --- JOIN THE 1AHEAD AND 3AHEAD PREDICTIONS --- #
    join_predictions(os.path.join("prediction_folder", "Random GK PerApp 2GWs 1Ahead.csv"), os.path.join("prediction_folder", "Random GK PerApp 2GWs 3Ahead.csv"))
    join_predictions(os.path.join("prediction_folder", "Random DEF PerApp 2GWs 1Ahead.csv"), os.path.join("prediction_folder", "Random DEF PerApp 2GWs 3Ahead.csv"))
    join_predictions(os.path.join("prediction_folder", "Random MID PerApp 4GWs 1Ahead.csv"), os.path.join("prediction_folder", "Random MID PerApp 5GWs 3Ahead.csv"))
    join_predictions(os.path.join("prediction_folder", "Random FWD PerApp 4GWs 1Ahead.csv"), os.path.join("prediction_folder", "Random FWD PerApp 5GWs 3Ahead.csv"))

    combine_predictions(os.path.join("prediction_folder", "Random GK PerApp 2GWs Prediction.csv"), os.path.join("prediction_folder", "Random DEF PerApp 2GWs Prediction.csv"), os.path.join("prediction_folder", "Random MID PerApp 4GWs Prediction.csv"), os.path.join("prediction_folder", "Random FWD PerApp 4GWs Prediction.csv"), "Random Regression")

    delete_files_and_folders_after_prediction()


def random_forest_regression_60minutes(which_gw_are_we_on):
    """Add predicted points for 1GW and 3GWs and export to prediction folder\n
    Join the 1GW and 3GW filenames into a single filename for each position.\n
    Combine all the joined filenames for all positions into 1 csv filename exported to the main folder.\n
    Delete the prediction_folder."""
    # --- REFERENCE THE FOLDER WITH THE SCRAPED filenameS --- #
    player_data = f"GW {which_gw_are_we_on} Files"

    # --- IF PREDICTION FOLDER DOES NOT EXIST, CREATE IT --- #
    if not os.path.exists("prediction_folder"):
        os.mkdir("prediction_folder")

    # --- ADD PREDICTION TO PLAYER filenameS --- #
    single_predict(pickling=os.path.join("random_forest_60", "Random Forest DEF PerApp 2GWs.pkl"), filename=os.path.join(player_data, "DEF PerApp 2GWs.csv"))
    single_predict(pickling=os.path.join("random_forest_60", "Random Forest MID PerApp 3GWs.pkl"), filename=os.path.join(player_data, "MID PerApp 3GWs.csv"))
    single_predict(pickling=os.path.join("random_forest_60", "Random Forest FWD PerApp 2GWs.pkl"), filename=os.path.join(player_data, "FWD PerApp 2GWs.csv"))
    three_gw_predict(pickling=os.path.join("random_forest_60", "Random Forest 3Ahead DEF PerApp 2GWs.pkl"), filename=os.path.join(player_data, "DEF PerApp 2GWs.csv"))
    three_gw_predict(pickling=os.path.join("random_forest_60", "Random Forest 3Ahead MID PerApp 5GWs.pkl"), filename=os.path.join(player_data, "MID PerApp 5GWs.csv"))
    three_gw_predict(pickling=os.path.join("random_forest_60", "Random Forest 3Ahead FWD PerApp 3GWs.pkl"), filename=os.path.join(player_data, "FWD PerApp 3GWs.csv"))

    # --- JOIN THE 1AHEAD AND 3AHEAD PREDICTIONS --- #
    join_predictions(os.path.join("prediction_folder", "Random DEF PerApp 2GWs 1Ahead.csv"), os.path.join("prediction_folder", "Random DEF PerApp 2GWs 3Ahead.csv"))
    join_predictions(os.path.join("prediction_folder", "Random MID PerApp 3GWs 1Ahead.csv"), os.path.join("prediction_folder", "Random MID PerApp 5GWs 3Ahead.csv"))
    join_predictions(os.path.join("prediction_folder", "Random FWD PerApp 2GWs 1Ahead.csv"), os.path.join("prediction_folder", "Random FWD PerApp 3GWs 3Ahead.csv"))

    combine_predictions_60minutes(os.path.join("prediction_folder", "Random DEF PerApp 2GWs Prediction.csv"), os.path.join("prediction_folder", "Random MID PerApp 3GWs Prediction.csv"), os.path.join("prediction_folder", "Random FWD PerApp 2GWs Prediction.csv"), "Random Regression 60minutes")

    delete_files_and_folders_after_prediction()


def linear_regression(which_gw_are_we_on):
    """Add predicted points for 1GW and 3GWs and export to prediction folder\n
    Join the 1GW and 3GW filenames into a single filename for each position.\n
    Combine all the joined filenames for all positions into 1 csv filename exported to the main folder.\n
    Delete the prediction_folder."""
    # --- REFERENCE THE FOLDER WITH THE SCRAPED filenameS --- #
    player_data = f"GW {which_gw_are_we_on} Files"

    # --- IF PREDICTION FOLDER DOES NOT EXIST, CREATE IT --- #
    if not os.path.exists("prediction_folder"):
        os.mkdir("prediction_folder")

    # --- ADD PREDICTION TO PLAYER filenameS --- #
    single_predict(pickling=os.path.join("linear_regress", "Linear GK PerApp 3GWs.pkl"), filename=os.path.join(player_data, "GK PerApp 3GWs.csv"))
    single_predict(pickling=os.path.join("linear_regress", "Linear DEF PerApp 2GWs.pkl"), filename=os.path.join(player_data, "DEF PerApp 2GWs.csv"))
    single_predict(pickling=os.path.join("linear_regress", "Linear MID PerApp 4GWs.pkl"), filename=os.path.join(player_data, "MID PerApp 4GWs.csv"))
    single_predict(pickling=os.path.join("linear_regress", "Linear FWD PerApp 3GWs.pkl"), filename=os.path.join(player_data, "FWD PerApp 3GWs.csv"))
    three_gw_predict(pickling=os.path.join("linear_regress", "Linear 3Ahead GK PerApp 3GWs.pkl"), filename=os.path.join(player_data, "GK PerApp 3GWs.csv"))
    three_gw_predict(pickling=os.path.join("linear_regress", "Linear 3Ahead DEF PerApp 2GWs.pkl"), filename=os.path.join(player_data, "DEF PerApp 2GWs.csv"))
    three_gw_predict(pickling=os.path.join("linear_regress", "Linear 3Ahead MID PerApp 2GWs.pkl"), filename=os.path.join(player_data, "MID PerApp 2GWs.csv"))
    three_gw_predict(pickling=os.path.join("linear_regress", "Linear 3Ahead FWD PerApp 5GWs.pkl"), filename=os.path.join(player_data, "FWD PerApp 5GWs.csv"))

    # --- JOIN THE 1AHEAD AND 3AHEAD PREDICTIONS --- #
    join_predictions(os.path.join("prediction_folder", "Linear GK PerApp 3GWs 1Ahead.csv"), os.path.join("prediction_folder", "Linear GK PerApp 3GWs 3Ahead.csv"))
    join_predictions(os.path.join("prediction_folder", "Linear DEF PerApp 2GWs 1Ahead.csv"), os.path.join("prediction_folder", "Linear DEF PerApp 2GWs 3Ahead.csv"))
    join_predictions(os.path.join("prediction_folder", "Linear MID PerApp 4GWs 1Ahead.csv"), os.path.join("prediction_folder", "Linear MID PerApp 2GWs 3Ahead.csv"))
    join_predictions(os.path.join("prediction_folder", "Linear FWD PerApp 3GWs 1Ahead.csv"), os.path.join("prediction_folder", "Linear FWD PerApp 5GWs 3Ahead.csv"))

    combine_predictions(os.path.join("prediction_folder", "Linear GK PerApp 3GWs Prediction.csv"), os.path.join("prediction_folder", "Linear DEF PerApp 2GWs Prediction.csv"), os.path.join("prediction_folder", "Linear MID PerApp 4GWs Prediction.csv"), os.path.join("prediction_folder", "Linear FWD PerApp 3GWs Prediction.csv"), "Linear Regression")

    delete_files_and_folders_after_prediction()


def linear_regression_60minutes(which_gw_are_we_on):
    """Add predicted points for 1GW and 3GWs and export to prediction folder\n
    Join the 1GW and 3GW filenames into a single filename for each position.\n
    Combine all the joined filenames for all positions into 1 csv filename exported to the main folder.\n
    Delete the prediction_folder."""
    # --- REFERENCE THE FOLDER WITH THE SCRAPED filenameS --- #
    player_data = f"GW {which_gw_are_we_on} Files"

    # --- IF PREDICTION FOLDER DOES NOT EXIST, CREATE IT --- #
    if not os.path.exists("prediction_folder"):
        os.mkdir("prediction_folder")

    # --- ADD PREDICTION TO PLAYER filenameS --- #
    single_predict(pickling=os.path.join("linear_regress_60", "Linear DEF PerApp 2GWs.pkl"), filename=os.path.join(player_data, "DEF PerApp 2GWs.csv"))
    single_predict(pickling=os.path.join("linear_regress_60", "Linear MID PerApp 2GWs.pkl"), filename=os.path.join(player_data, "MID PerApp 2GWs.csv"))
    single_predict(pickling=os.path.join("linear_regress_60", "Linear FWD PerApp 5GWs.pkl"), filename=os.path.join(player_data, "FWD PerApp 5GWs.csv"))
    three_gw_predict(pickling=os.path.join("linear_regress_60", "Linear 3Ahead DEF PerApp 2GWs.pkl"), filename=os.path.join(player_data, "DEF PerApp 2GWs.csv"))
    three_gw_predict(pickling=os.path.join("linear_regress_60", "Linear 3Ahead MID PerApp 2GWs.pkl"), filename=os.path.join(player_data, "MID PerApp 2GWs.csv"))
    three_gw_predict(pickling=os.path.join("linear_regress_60", "Linear 3Ahead FWD PerApp 5GWs.pkl"), filename=os.path.join(player_data, "FWD PerApp 5GWs.csv"))

    # --- JOIN THE 1AHEAD AND 3AHEAD PREDICTIONS --- #
    join_predictions(os.path.join("prediction_folder", "Linear DEF PerApp 2GWs 1Ahead.csv"), os.path.join("prediction_folder", "Linear DEF PerApp 2GWs 3Ahead.csv"))
    join_predictions(os.path.join("prediction_folder", "Linear MID PerApp 2GWs 1Ahead.csv"), os.path.join("prediction_folder", "Linear MID PerApp 2GWs 3Ahead.csv"))
    join_predictions(os.path.join("prediction_folder", "Linear FWD PerApp 5GWs 1Ahead.csv"), os.path.join("prediction_folder", "Linear FWD PerApp 5GWs 3Ahead.csv"))

    combine_predictions_60minutes(os.path.join("prediction_folder", "Linear DEF PerApp 2GWs Prediction.csv"), os.path.join("prediction_folder", "Linear MID PerApp 2GWs Prediction.csv"), os.path.join("prediction_folder", "Linear FWD PerApp 5GWs Prediction.csv"), "Linear Regression 60minutes")

    delete_files_and_folders_after_prediction()


def single_predict(pickling, filename):
    """Add Points Prediction for the next GWs."""
    pickle_in = open(pickling, "rb")
    rf = pickle.load(pickle_in)

    data_predict = pd.read_csv(filename)
    data = pd.read_csv(filename)

    # Rename the Cost column
    data_predict = data_predict.rename(columns=NEW_COLUMN_NAMES)
    data = data.rename(columns=NEW_COLUMN_NAMES)

    # Drop the columns that are not going to be used in the regression
    data_predict.drop(["Name", "App.", "Fouls Made", "Exp. Clean Sheets", "Names", "Position", "Cost", "Team"], axis=1, inplace=True)

    # Setting up the values of x and y
    x = data_predict

    # Run the prediction
    prediction = rf.predict(x)
    prediction = [round(x * 2) / 2 for x in prediction]

    pickling = os.path.basename(pickling)
    filename = os.path.basename(filename)

    header = ["Names", "Position", "Team", "Cost", "Predict1GW"]
    data_new = data.assign(Predict1GW = prediction)
    data_new.to_csv(os.path.join("prediction_folder", f"{pickling[:7]}{filename[:-4]} 1Ahead.csv"), index=False, columns=header)


def three_gw_predict(pickling, filename):
    """Add Points Prediction for the next 3 GWs."""
    pickle_in = open(pickling, "rb")
    rf = pickle.load(pickle_in)

    data_predict = pd.read_csv(filename)
    data = pd.read_csv(filename)

    # Rename the Cost column
    data_predict = data_predict.rename(columns=NEW_COLUMN_NAMES)
    data = data.rename(columns=NEW_COLUMN_NAMES)

    # Drop the columns that are not going to be used in the regression
    data_predict.drop(["Name", "App.", "Fouls Made", "Exp. Clean Sheets", "Names", "Position", "Cost", "Team"], axis=1, inplace=True)

    # Setting up the values of x and y
    x = data_predict

    # Run the prediction
    prediction = rf.predict(x)
    prediction = [round(x * 2) / 2 for x in prediction]

    pickling = os.path.basename(pickling)
    filename = os.path.basename(filename)

    header = ["Names", "Position", "Team", "Cost", "Predict3GW"]
    data_new = data.assign(Predict3GW = prediction)
    data_new.to_csv(os.path.join("prediction_folder", f"{pickling[:7]}{filename[:-4]} 3Ahead.csv"), index=False, columns=header)


def join_predictions(gw1_csv, gw3_csv):
    """Join the 1GW and 3GW predicitions into a single prediction filename"""
    # --- READ IN BOTH CSVS --- #
    prediction_1 = pd.read_csv(gw1_csv)
    prediction_3 = pd.read_csv(gw3_csv)

    # --- USE MERGE FUNCTION BY SETTING HOW TO "inner" --- #
    data = pd.merge(prediction_1, prediction_3, on="Names", how="inner")

    # --- PRINT PANDA TO A CSV USING ONLY THE DESIRED COLUMNS --- #
    data.to_csv(f"{gw1_csv[:-10]}Prediction.csv", index=False, columns=["Names", "Position_x", "Team_x", "Cost_x", "Predict1GW", "Predict3GW"])


def combine_predictions(gks, defs, mids, fwds, regression):
    """Combine all the prediction csvs into 1 single file."""
    # --- READ EACH FILE INTO ITS OWN DATAFRAME --- #
    gks = pd.read_csv(gks)
    defs = pd.read_csv(defs)
    mids = pd.read_csv(mids)
    fwds = pd.read_csv(fwds)

    # --- CONCAT THE DIFFERENT DATAFRAMES INTO 1 --- #
    # --- ADD THE NEW COLUMN NAMES TO THE DATAFRAME --- #
    combined_players = pd.concat([gks, defs, mids, fwds], ignore_index=True)
    combined_players.columns = ["Name", "Position", "Team Name", "Price", "Predict", "Predict3GW"]

    # --- EXPORT CONCATED DATAFRAME TO A NEW CSV --- #
    combined_players.to_csv(f"{regression}.csv", index=False)

    print(combined_players)


def combine_predictions_60minutes(defs, mids, fwds, regression):
    """Combine all the prediction csvs into 1 single file."""
    # --- READ EACH FILE INTO ITS OWN DATAFRAME --- #
    defs = pd.read_csv(defs)
    mids = pd.read_csv(mids)
    fwds = pd.read_csv(fwds)

    # --- CONCAT THE DIFFERENT DATAFRAMES INTO 1 --- #
    # --- ADD THE NEW COLUMN NAMES TO THE DATAFRAME --- #
    combined_players = pd.concat([defs, mids, fwds], ignore_index=True)
    combined_players.columns = ["Name", "Position", "Team Name", "Price", "Predict", "Predict3GW"]

    # --- EXPORT CONCATED DATAFRAME TO A NEW CSV --- #
    combined_players.to_csv(f"{regression}.csv", index=False)

    print(combined_players)


def delete_files_and_folders_after_prediction():
    """Delete the files in Prediction Folder then delete the folder itself."""
    folder = "prediction_folder"

    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        os.unlink(file_path)

    os.rmdir("prediction_folder")


if __name__ == "__main__":
    main()
