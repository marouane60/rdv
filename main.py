import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from webdriver_manager.chrome import ChromeDriverManager
#"planning1075"
def select_guichet(guichet_id, driver):
    driver.find_element(By.ID, guichet_id).click()
    time.sleep(5)
    driver.find_element(By.NAME, "nextButton").click()
    time.sleep(5)
def check_for_appointment(guichet):
    pref_link = "https://pprdv.interieur.gouv.fr/booking/create/989/1"

    ## create an object of the chrome webdriver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    ## open selenium URL in chrome browser
    driver.get(pref_link)

    select_guichet(guichet, driver)

    if (driver.page_source.find("plus de plage") < 0):
        return True
    else:
        driver.quit()
        return False

def check_all_guichets():
    for guichet in ["planning1075", "planning1076", "planning1077"]:
        if(check_for_appointment(guichet)):
            return True
    return False

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while(check_all_guichets() == False):
        check_all_guichets()

    os.system("say rendez vous rab bek")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
