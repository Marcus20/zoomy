from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os

# Clear the console
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cls()

zoomBrand = """
########::'#######:::'#######::'##::::'##:'########:'########::
..... ##::'##.... ##:'##.... ##: ###::'###: ##.....:: ##.... ##:
:::: ##::: ##:::: ##: ##:::: ##: ####'####: ##::::::: ##:::: ##:
::: ##:::: ##:::: ##: ##:::: ##: ## ### ##: ######::: ##:::: ##:
:: ##::::: ##:::: ##: ##:::: ##: ##. #: ##: ##...:::: ##:::: ##:
: ##:::::: ##:::: ##: ##:::: ##: ##:.:: ##: ##::::::: ##:::: ##:
 ########:. #######::. #######:: ##:::: ##: ########: ########::
........:::.......::::.......:::..:::::..::........::........:::
"""
print(zoomBrand)
print("Looks like you have a meeting scheduled soon! Lets get you joined.\n\n")

get_id = str(input("What is the zoom ID for the meeting: "))

def valid_id(get_id):
    valid = range(9, 12)
    id_is_valid = True

    while id_is_valid:
        if(len(get_id) in valid):
            meeting_url = "https://asurion.zoom.us/j/" + str(get_id)

            browser = webdriver.Chrome()
            browser.get((meeting_url))
            if(browser.find_elements_by_xpath("//*[contains(text(), 'Invalid meeting ID')]")):
                print("The meeting ID that you entered was invalid. Please enter a valid meeting ID")
                get_id = str(input("What is the zoom ID for the meeting: "))

            else:
                print("Enjoy your meeting and STAY AWAKE :)")
                id_is_valid = False
        else:
            print("The meeting ID you have entered did not meet the length requirements. The length must be between 9 and 11 characters in length")
            get_id = str(input("What is the zoom ID for the meeting: "))

# Verify meeting validity!
valid_id(get_id)

