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
from other_prediction_functions import delete_files_after_use, move_scraped_files, single_predict, three_gw_predict
from player_scrapper_functions import player_scraper_functions


open_ffhub_opta()

driver, wait = chrome_options_driver_wait()
which_gw_are_we_on = which_gw_are_we_on()
stat_type_custom(driver, wait)
load_all_players(driver, wait)

player_scraper_functions(driver, which_gw_are_we_on)

# --- TEMPORARILY MOVE PLAYER DATA SCRAPED FILES TO FOLDERS FOR SCRAPING --- #
move_scraped_files("GW Files", ["Joy Pickles", "Niyi Pickles", "Tosin Pickles"])

# delete_files_after_use("GW Files", ["Joy Pickles", "Niyi Pickles", "Tosin Pickles"])
