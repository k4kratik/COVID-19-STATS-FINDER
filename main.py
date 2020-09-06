from selenium import webdriver
from india_stat import get_india_stat
from state_wise_data import get_state_data
from selenium.webdriver.chrome.options import Options
import pandas as pd
from output import output
import sys

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)

driver.minimize_window()

# it prints the data
try:
    get_india_stat(driver)
except:
    print("An Error Occurred!. Try Again and Check your internet connection.")
    sys.exit(1)
print("--------------------------------------------------------------------------------------------------------------")
print("\nCollecting State Wise Real time Data - Be Patient ! It will just take few seconds \n")

retrieved_data = get_state_data(driver)

driver.quit()

print("\n\nWe have Collected Data for the following states and UTs - \n")
c = 1
for ele in retrieved_data[0].keys():
    print(f"{c}. {ele}")
    c += 1

# For Debugging
# print(retrieved_data)

your_state = 'initial_flag'
try:
    output(retrieved_data,your_state)
    print("\n\nThanks for using This piece of code")
    print("Written by - Kratik Jain")
    print("Be Safe!!!")

except:
    print('')
    print("Please enter a valid input!")
