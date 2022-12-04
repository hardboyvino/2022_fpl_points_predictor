"""
Functions specfic to the player GWs to be scrapped per position.

For GKs - PerApp 3GWs, PerApp 5GWs, PerApp 6GWs, PerStart 2GWs
For DEFs - PerApp 2GWs, PerApp 4GWs, PerApp 5GWs, PerApp 6GWs
For MIDs - PerApp 5GWs, PerApp 6GWs
For FWDs - PerApp 5GWs, PerApp 6GWs
"""
from ffhub_scraper_functions import click_perapp, move_sliders_and_scrape_new_season, select_def_position, select_fwd_position, select_gk_position, select_mid_position, click_per_start


def main():
    """Main Function."""


def player_scraper_functions(driver, which_gw_are_we_on):
    """Combined all the player scraper functions into 1 super function."""
    gk_perstart(driver, which_gw_are_we_on)
    gk_perapp(driver, which_gw_are_we_on)
    def_perapp(driver, which_gw_are_we_on)
    mid_perapp(driver, which_gw_are_we_on)
    fwd_perapp(driver, which_gw_are_we_on)


def gk_perstart(driver, which_gw_are_we_on):
    """Scrape Goalkeepers Per Start for past 2 gameweeks."""
    position = "GK"
    gws_to_consider = 2

    select_gk_position(driver)
    click_per_start(driver)
    move_sliders_and_scrape_new_season(driver, which_gw_are_we_on = which_gw_are_we_on, filename=f"{position} PerStart {gws_to_consider}GWs.csv", gws_to_consider=gws_to_consider)
    select_gk_position(driver)


def gk_perapp(driver, which_gw_are_we_on):
    """Scrape Goalkeepers Per App for past 3, 5 and 6 gameweeks."""
    position = "GK"
    gws_to_consider = [3, 5, 6]

    for gw in gws_to_consider:
        select_gk_position(driver)
        click_perapp(driver)
        move_sliders_and_scrape_new_season(driver, which_gw_are_we_on = which_gw_are_we_on, filename=f"{position} PerApp {gw}GWs.csv", gws_to_consider=gw)
        select_gk_position(driver)


def def_perapp(driver, which_gw_are_we_on):
    """Scrape Defenders Per App for past 2, 4, 5 and 6 gameweeks."""
    position = "DEF"
    gws_to_consider = [2, 4, 5, 6]

    for gw in gws_to_consider:
        select_def_position(driver)
        click_perapp(driver)
        move_sliders_and_scrape_new_season(driver, which_gw_are_we_on = which_gw_are_we_on, filename=f"{position} PerApp {gw}GWs.csv", gws_to_consider=gw)
        select_def_position(driver)


def mid_perapp(driver, which_gw_are_we_on):
    """Scrape Midfielders Per App for past 5 and 6 gameweeks."""
    position = "MID"
    gws_to_consider = [5, 6]

    for gw in gws_to_consider:
        select_mid_position(driver)
        click_perapp(driver)
        move_sliders_and_scrape_new_season(driver, which_gw_are_we_on = which_gw_are_we_on, filename=f"{position} PerApp {gw}GWs.csv", gws_to_consider=gw)
        select_mid_position(driver)


def fwd_perapp(driver, which_gw_are_we_on):
    """Scrape Forwards Per App for past 5 and 6 gameweeks."""
    position = "FWD"
    gws_to_consider = [5, 6]

    for gw in gws_to_consider:
        select_fwd_position(driver)
        click_perapp(driver)
        move_sliders_and_scrape_new_season(driver, which_gw_are_we_on = which_gw_are_we_on, filename=f"{position} PerApp {gw}GWs.csv", gws_to_consider=gw)
        select_fwd_position(driver)


if __name__ == "__main__":
    main()
