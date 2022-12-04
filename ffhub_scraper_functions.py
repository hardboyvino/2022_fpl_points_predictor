"""
Functions required for scraping of data from FFHUB website.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
from time import sleep
import os

import constants


def main():
    """Main function."""


def open_ffhub_opta():
    """Open the LocalHost Chrome browser.\n
    Then open FFHUB website Opta with all details logged in.\n
    Maximize the browser window."""
    chrome_open_command = r'cmd /c start chrome.exe --remote-debugging-port=1991 --user-data-dir="C:\Users\Adeniyi Babalola\Desktop\PythonPrograms\chromedata"'
    os.system(chrome_open_command)

    driver = chrome_options_driver_only()

    driver.get("https://www.fantasyfootballhub.co.uk/opta")
    driver.maximize_window()
    short_sleep()


def chrome_options_driver_only():
    """Get the chromedriver, get local host browser address and create webdriver variable only."""
    chrome_options = ChromeOptions()
    chrome_options.add_experimental_option("debuggerAddress", "localhost:1991")
    driver = webdriver.Chrome(options=chrome_options)
    return driver


def chrome_options_driver_wait():
    """Get the chromedriver, get local host browser address and return tuple (webdriver variable, wait variable)."""
    chrome_options = ChromeOptions()
    chrome_options.add_experimental_option("debuggerAddress", "localhost:1991")
    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 10)
    return driver,wait


def move_sliders_and_scrape_new_season(driver, which_gw_are_we_on, filename, gws_to_consider):
    """Move the sliders for scraping and get data for the specific gameweek."""
    # --- GAMEWEEK FILES DIRECTORY --- #
    # --- CHECK IF THE DIRECTORY FOR THIS GW EXISTS, IF NOT, CREATE IT
    if not os.path.exists(f"GW {which_gw_are_we_on} Files"):
        os.mkdir(f"GW {which_gw_are_we_on} Files")

    directory = f"GW {which_gw_are_we_on} Files"
    file_path = os.path.join(directory, filename)

    # --- SLIDER WIDTH MEASURED IN PIXELS WITH CHROME EXTENSION RULER --- #
    # constants.SLIDER_WIDTH = 569

    # --- FIND THE SLIDER ELEMENTS AND STORE EACH AS ITS OWN VARIABLE --- #
    slider_1 = driver.find_element(By.XPATH, "(//span[@aria-label='range-slider'])[3]")
    slider_2 = driver.find_element(By.XPATH, "(//span[@aria-label='range-slider'])[4]")

    # --- DIVIDE SLIDER WIDTH BY 1 LESS OF WHICHEVER GAMEWEEK THE GAME IS ON --- #
    pixels_per_gw = f"{constants.SLIDER_WIDTH / (which_gw_are_we_on - 1):.14f}"
    print(pixels_per_gw)

    # --- MOVE THE UPPER SLIDER BACK BY 1 GW. THIS IS BECAUSE OF HOW FFHUB WEBSITE RESPONDS CURRENTLY --- #
    ActionChains(driver).drag_and_drop_by_offset(slider_2, -(float(pixels_per_gw)), 0).perform()
    short_sleep()

    # ---- MOVE THE UPPER SLIDER BACK TO ITS ORIGINAL POSITION --- #
    ActionChains(driver).drag_and_drop_by_offset(slider_2, (float(pixels_per_gw)), 0).perform()
    short_sleep()

    # --- MOVE THE LOWER SLIDER TO THE CURRENT GAMEWEEK --- #
    ActionChains(driver).drag_and_drop_by_offset(slider_1, constants.SLIDER_WIDTH, 0).perform()
    short_sleep()

    # --- MOVE THE LOWER SLIDER TO THE REQUIRED GAMEWEEK --- #
    ActionChains(driver).drag_and_drop_by_offset(slider_1, -((gws_to_consider - 1) * float(pixels_per_gw)), 0).perform()
    random_sleeps()

    # --- SCRAPE PLAYER DATA AND PRINT A MESSAGE TO LET THE USER KNOW THE PROGRAM HAS REACHED THIS STAGE --- #
    data = scrape_players(driver)
    print("Getting the main player data...")
    short_sleep()

    # --- EXPORT THE DATA TO A CSV WITH A UNIQUE NAME DETERMINED BY KWARGS --- #
    data.to_csv(file_path, mode="w", index=False, header=True)
    short_sleep()

    # --- RESET LOWER SLIDER TO GAMEWEEK 1 --- #
    ActionChains(driver).drag_and_drop_by_offset(slider_1, -constants.SLIDER_WIDTH, 0).perform()
    short_sleep()


def scrape_players(driver):
    """
    Inspect the page and scrape all players and respective data from the page.\n
    Separate Names column to Name, Position and Team columns for dataset usability.
    """

    # --- READ THE PAGE SOURCE --- #
    html = driver.page_source

    # --- CREATE PANDAS DATAFRAME FOR ALL POSSIBLE TABLES ON THE HTML PAGE --- #
    df = pd.read_html(html)

    # --- SELECT THE DESIRED TABLE FROM LIST OF TABLES (IN THIS CASE THERE IS ONLY ONE TABLE) --- #
    data = df[0]

    # --- SPLIT THE NAMES COLUMN INTO NAME, POSITION AND TEAM --- #
    data[["Names", "Position"]] = data["Name"].str.split("(", expand=True)
    data[["Position", "Team"]] = data["Position"].str.split(")", expand=True)

    # --- REMOVE ALL INSTANCES OF % AND £ IN THE TABLE SO IT IS ONLY NUMBERS --- #
    data = data.replace(regex=["%"], value=[""])
    data = data.replace(regex=["£"], value=[""])

    return data


def which_gw_are_we_on():
    """Get the most recent gameweek from FFHUB website."""
    driver = chrome_options_driver_only()
    slider_2 = driver.find_element(By.XPATH, "(//span[@aria-label='range-slider'])[4]")
    return int(slider_2.text)


def load_all_players(driver, wait):
    """Load all possible players for the current selection."""
    # --- FIND THE DROPDOWN TO SELECT HOW MANY PLAYERS TO LOAD --- #
    driver.find_element(By.CSS_SELECTOR, "div[class='my-4'] div[class=' css-r71ql9-singleValue']").click()

    # --- SELECT ALL --- #
    load_all = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'All (slow)')]")))
    load_all.click()
    random_sleeps()


def click_per90(driver):
    """Click on Per 90 mins Fixture Filter."""
    driver.find_element(By.CSS_SELECTOR, "#per90").click()
    medium_sleep()


def click_per_start(driver):
    """Click on Per Start Fixture Filter."""
    driver.find_element(By.CSS_SELECTOR, "#perstart").click()
    medium_sleep()


def click_perapp(driver):
    """Click on Per Apperance Fixture Filter."""
    driver.find_element(By.CSS_SELECTOR, "#perapp").click()
    medium_sleep()


def stat_type_custom(driver, wait):
    """This function goes into the Stat Type option and selects Custom."""
    # --- CLICK THE DROPDOWN --- #
    driver.find_element(
        By.XPATH, value="(//div[contains(@class,'css-seq4h5-control')])[3]"
    ).click()

    short_sleep()

    # --- CLICK ON THE CUSTOM OPTION --- #
    custom = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Custom')]"))
    )
    custom.click()

    short_sleep()

    # --- CLICK THE SAVE BUTTON FOR THE CUSTOM SELECTIONS (PREFERRED DATA PRE-STORED IN ACCOUNT) --- #
    driver.find_element(By.XPATH, value="//button[normalize-space()='Save']").click()
    medium_sleep()


def unclick_positions(driver, i):
    """Find the player position element on the page and click on those specified by the function calling."""
    driver.find_element(By.XPATH, "//input[@id=" + str(i) + "]").click()


def select_mid_position(driver):
    """Select the midfielder position."""
    # REQUIRES UNCLICKING ALL OTHER POSITIONS (GK, DEF, FWD) --- #
    for i in {0, 1, 3}:
        unclick_positions(driver, i)
    medium_sleep()


def select_def_position(driver):
    """Select the defender position."""
    # REQUIRES UNCLICKING ALL OTHER POSITIONS (GK, MID, FWD) --- #
    for i in {0, 2, 3}:
        unclick_positions(driver, i)
    medium_sleep()


def select_gk_position(driver):
    """Select the goalkeepper position."""
    # --- REQUIRES UNCLICKING ALL OTHER POSITIONS (DEF, MID, FWD) --- #
    for i in range(1, 4):
        unclick_positions(driver, i)
    medium_sleep()


def select_fwd_position(driver):
    """Select the forward position."""
    # --- REQUIRES UNCLICKING ALL OTHER POSITIONS (GK, DEF, MID) --- #
    for i in {0, 1, 2}:
        unclick_positions(driver, i)
    medium_sleep()


def random_sleeps(time=15):
    """Pause the program for a long time to allow loading.\n
    Default to 15 seconds."""
    sleep(time)


def short_sleep(time=5):
    """Pause the program for a very short time to allow loading.\n
    Default to 5 seconds."""
    sleep(time)


def medium_sleep(time=10):
    """Pause the program for a not so short period of time to allow loading.\n
    Default to 10 seconds."""
    sleep(time)


if __name__ == "__main__":
    main()
