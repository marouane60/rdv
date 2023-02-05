import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time




def check_for_appointment():
    pref_link = "https://www.hauts-de-seine.gouv.fr/booking/create/8485/0"

    ## create an object of the chrome webdriver
    driver = webdriver.Chrome(executable_path=r'./chromedriver')
    ## open selenium URL in chrome browser
    driver.get(pref_link)

    driver.find_element(By.ID, "condition").click()
    time.sleep(5)
    driver.find_element(By.NAME, "nextButton").click()
    time.sleep(5)

    if(driver.page_source.find("plus de plage") < 0):
        os.system("say rendez vous rab bek")
    else:
        check_for_appointment()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    check_for_appointment()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
