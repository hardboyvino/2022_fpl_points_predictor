"""
Other functions required for the final prediction setup.
"""
import os
import shutil
import pickle
from pandas import read_csv

import constants


def main():
    """Main function."""


def move_scraped_files(sources, targets_folders):
    """Move the scraped files from GW Files folder to all folders requiring it for prediction."""
    # --- DEFINING SOURCE AND DESTINATION PATHS --- #
    source = sources
    targets = targets_folders

    files = os.listdir(source)

    # --- ITERATING OVER THE FILES IN THE SOURCE DIRECTORY --- #
    for target in targets:
        for fname in files:
            shutil.copy2(os.path.join(source, fname), target)


def delete_files_after_use(source_folder, targets_folders):
    """Remove all the files in target directory matching files in the source directory."""
    targets = targets_folders
    source = source_folder
    for target in targets:
        files = os.listdir(source)
        for fname in files:
            path = os.path.join(target, fname)
            os.remove(path)


def single_predict(pickling, file):
    """Add Points Prediction for the next GWs."""
    pickle_in = open(pickling, "rb")
    rf = pickle.load(pickle_in)

    data_predict = read_csv(file)
    data = read_csv(file)

    # Rename the Cost column
    data_predict = data_predict.rename(columns=constants.NEW_COLUMN_NAMES)
    data = data.rename(columns=constants.NEW_COLUMN_NAMES)

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
    data_predict = data_predict.rename(columns=constants.NEW_COLUMN_NAMES)
    data = data.rename(columns=constants.NEW_COLUMN_NAMES)

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
