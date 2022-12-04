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
from regressions import random_forest_regression, linear_regression
from player_scrapper_functions import player_scraper_functions


open_ffhub_opta()

driver, wait = chrome_options_driver_wait()
which_gw_are_we_on = which_gw_are_we_on()
stat_type_custom(driver, wait)
load_all_players(driver, wait)

player_scraper_functions(driver, which_gw_are_we_on)

# --- RUN ALGORITHMS TO GET PREDICTED POINTS FILES --- #
random_forest_regression(which_gw_are_we_on)
linear_regression(which_gw_are_we_on)