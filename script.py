from selenium import webdriver

import os


# Clear the console
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


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
    valid_char_length = range(9, 12)

    while True:
        if len(get_id) in valid_char_length:
            meeting_url = "https://asurion.zoom.us/j/" + str(get_id)

            browser = webdriver.Chrome()
            browser.get(meeting_url)
            if browser.find_elements_by_xpath("//*[contains(text(), 'Invalid meeting ID')]"):
                print("The meeting ID that you entered was invalid. Please enter a valid meeting ID")
                get_id = str(input("What is the zoom ID for the meeting: "))

            else:
                print("Enjoy your meeting and STAY AWAKE :)")
                break
        else:
            print(
                "The meeting ID length must be between 9 and 11 characters in length")
            get_id = str(input("What is the zoom ID for the meeting: "))


# Verify meeting validity!
valid_id(get_id)
