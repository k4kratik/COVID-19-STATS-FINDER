from selenium import webdriver
from india_stat import get_india_stat
from state_wise_data import output, get_state_data
from selenium.webdriver.chrome.options import Options
import pandas as pd

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)

driver.minimize_window()

# it prints the data
get_india_stat(driver)

print("--------------------------------------------------------------------------------------------------------------")
print("\nCollecting State Wise Real time Data - Be Patient ! It will just take few seconds \n")

retrieved_data = get_state_data(driver)

driver.quit()

print("\n We have Collected Data for the following states and UTs - \n")
c = 1
for ele in retrieved_data[0].keys():
    print(f"{c}. {ele}")
    c += 1

# For Debugging
# print(retrieved_data)
your_state = int(input("\nEnter Your State ID to check current COVID-19 Condition OR you can enter 0 (zero) to print "
                       "data of all states:\t"))

if your_state not in range(len(retrieved_data[0])+1):
    print("Please Enter A Valid Integer according to your State.")
elif your_state == 0:
    # OLD
    # for i in range(1, len(retrieved_data[0])+1):
    #     output(retrieved_data[1], retrieved_data[0], i)
    df = pd.DataFrame(list(retrieved_data[0].values()), columns = ['CONFIRMED', 'ACTIVE', 'RECOVERED', 'DEATHS'],index=list(retrieved_data[0].keys()))
    print(df.to_markdown())      
else:
    output(retrieved_data[1], retrieved_data[0], your_state)

print("\n\nThanks for using This piece of code")
print("Written by - Kratik Jain")
print("Be Safe!!!")

# df = pd.DataFrame(list(data[0].values()), columns = ['CONFIRMED', 'ACTIVE', 'RECOVERED', 'DEATHS'],index=list(data[0].keys()))
