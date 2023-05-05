"""
Scraper to get the data from FantasyFootballHub website and predict player points for coming gameweeks.
"""
from ffhub_scraper_functions import (
    chrome_options_driver_wait,
    load_all_players,
    open_ffhub_opta,
    stat_type_custom,
    which_gw_are_we_on,
)
from regressions import (
    random_forest_regression,
    linear_regression,
    random_forest_regression_60minutes,
    linear_regression_60minutes,
)
from player_scrapper_functions import player_scraper_functions

import pandas as pd
import os


open_ffhub_opta()

driver, wait = chrome_options_driver_wait()
which_gw_are_we_on = which_gw_are_we_on()
stat_type_custom(driver, wait)
load_all_players(driver, wait)

player_scraper_functions(driver, which_gw_are_we_on)

# # --- RUN ALGORITHMS TO GET PREDICTED POINTS FILES --- #
# random_forest_regression(which_gw_are_we_on)
# linear_regression(which_gw_are_we_on)
# random_forest_regression_60minutes(which_gw_are_we_on)
# linear_regression_60minutes(which_gw_are_we_on)

folder_path = f"GW {which_gw_are_we_on} Files"
output_file = "merged.csv"
columns_to_merge = ["Names", "Position", "Team", "Cost (£M)"]

# List all the CSVs in the folder

csv_files = [f for f in os.listdir(folder_path) if f.endswith(".csv")]

# Read and merge specific columns from each CSV file
merged_data = []
for csv_file in csv_files:
    file_path = os.path.join(folder_path, csv_file)
    data = pd.read_csv(file_path, usecols=columns_to_merge)
    merged_data.append(data)

# Combine all the data into one DataFrame and save as a new CSV file
combined_data = pd.concat(merged_data, ignore_index=True)
combined_data.to_csv(output_file, index=False)
